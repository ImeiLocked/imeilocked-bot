import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ContextTypes, ConversationHandler
)
from config import *
from services import SERVICES
from texts import TEXTS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LANG, COMPANY, SUBCATEGORY, SERVICE, IMEI, EMAIL, PAYMENT, CONFIRM, WAITING = range(9)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    keyboard = [
        [InlineKeyboardButton("🇪🇸 Español", callback_data="lang_es"),
         InlineKeyboardButton("🇺🇸 English", callback_data="lang_en")]
    ]
    await update.message.reply_text(
        f"👋 Welcome / Bienvenido\n\n*{BOT_NAME}*\n\nChoose your language / Elige tu idioma:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return LANG

async def set_language(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    ctx.user_data["lang"] = lang
    t = TEXTS[lang]
    keyboard = []
    for company in SERVICES.keys():
        keyboard.append([InlineKeyboardButton(company, callback_data=f"company_{company}")])
    keyboard.append([InlineKeyboardButton(t["btn_cancel"], callback_data="cancel")])
    await query.edit_message_text(
        t["welcome"].format(name=BOT_NAME),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return COMPANY

async def select_company(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    company = query.data.replace("company_", "")
    ctx.user_data["company"] = company
    subcategories = SERVICES[company]
    keyboard = []
    for subcat in subcategories.keys():
        keyboard.append([InlineKeyboardButton(subcat, callback_data=f"subcat_{subcat}")])
    keyboard.append([InlineKeyboardButton(t["btn_back"], callback_data="back_companies")])
    if lang == "es":
        msg = f"📂 {company}\n\nSelecciona una subcategoria:"
    else:
        msg = f"📂 {company}\n\nSelect a subcategory:"
    await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))
    return SUBCATEGORY

async def select_subcategory(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    subcat = query.data.replace("subcat_", "")
    ctx.user_data["subcategory"] = subcat
    company = ctx.user_data["company"]
    services_list = SERVICES[company][subcat]
    ctx.user_data["current_services"] = services_list

    if lang == "es":
        msg = f"📂 {company}\n➡️ {subcat}\n\nElige el numero del servicio que deseas:\n\n"
        for i, svc in enumerate(services_list, 1):
            msg += f"{i}. {svc['name']['es']}\n💰 ${svc['price']:.2f} | ⏱ {svc['time']}\n\n"
        msg += "✏️ Escribe el numero del servicio:"
    else:
        msg = f"📂 {company}\n➡️ {subcat}\n\nChoose the number of the service you want:\n\n"
        for i, svc in enumerate(services_list, 1):
            msg += f"{i}. {svc['name']['en']}\n💰 ${svc['price']:.2f} | ⏱ {svc['time']}\n\n"
        msg += "✏️ Type the service number:"

    keyboard = [[InlineKeyboardButton(t["btn_back"], callback_data="back_subcategories")]]
    await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))
    return SERVICE

async def select_service(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lang = ctx.user_data.get("lang", "en")
    services_list = ctx.user_data.get("current_services", [])
    try:
        num = int(update.message.text.strip())
        if num < 1 or num > len(services_list):
            raise ValueError
    except ValueError:
        if lang == "es":
            await update.message.reply_text(f"❌ Por favor escribe un numero entre 1 y {len(services_list)}.")
        else:
            await update.message.reply_text(f"❌ Please type a number between 1 and {len(services_list)}.")
        return SERVICE

    selected = services_list[num - 1]
    ctx.user_data["service"] = selected
    ctx.user_data["service_name"] = selected["name"][lang]
    ctx.user_data["service_price"] = selected["price"]

    if lang == "es":
        msg = (
            f"✅ Servicio seleccionado:\n"
            f"📱 {selected['name']['es']}\n"
            f"💰 Precio: ${selected['price']:.2f}\n"
            f"⏱ Tiempo estimado: {selected['time']}\n\n"
            f"🔢 Por favor, ingresa el IMEI del dispositivo:\n"
            f"(Marca *#06#* en el telefono para obtenerlo)"
        )
    else:
        msg = (
            f"✅ Service selected:\n"
            f"📱 {selected['name']['en']}\n"
            f"💰 Price: ${selected['price']:.2f}\n"
            f"⏱ Estimated time: {selected['time']}\n\n"
            f"🔢 Please enter the device IMEI:\n"
            f"(Dial *#06#* on the phone to get it)"
        )
    await update.message.reply_text(msg)
    return IMEI

async def get_imei(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    imei = update.message.text.strip()
    if not imei.isdigit() or len(imei) not in [15, 16]:
        await update.message.reply_text(t["invalid_imei"])
        return IMEI
    ctx.user_data["imei"] = imei
    if lang == "es":
        await update.message.reply_text(
            "✅ IMEI recibido.\n\n📧 Ahora ingresa tu correo electronico\n(Aqui te enviaremos el resultado del servicio)"
        )
    else:
        await update.message.reply_text(
            "✅ IMEI received.\n\n📧 Now enter your email address\n(We'll send the service result here)"
        )
    return EMAIL

async def get_email(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    email = update.message.text.strip()
    if "@" not in email or "." not in email:
        await update.message.reply_text(t["invalid_email"])
        return EMAIL
    ctx.user_data["email"] = email
    keyboard = []
    for method in PAYMENT_METHODS:
        cid = method.get("crypto_id")
        if cid:
            wallet_info = CRYPTO_WALLETS.get(cid, {})
            if not wallet_info.get("address"):
                continue
        else:
            if not method.get("address") and method["id"] not in ["zelle", "paypal"]:
                continue
        keyboard.append([InlineKeyboardButton(method["label"], callback_data=f"pay_{method['id']}")])
    keyboard.append([InlineKeyboardButton(t["btn_cancel"], callback_data="cancel")])
    if lang == "es":
        await update.message.reply_text("💳 Selecciona el metodo de pago:", reply_markup=InlineKeyboardMarkup(keyboard))
    else:
        await update.message.reply_text("💳 Select payment method:", reply_markup=InlineKeyboardMarkup(keyboard))
    return PAYMENT

async def select_payment(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    pay_id = query.data.replace("pay_", "")
    selected_pay = None
    for method in PAYMENT_METHODS:
        if method["id"] == pay_id:
            selected_pay = method
            break
    ctx.user_data["payment_method"] = selected_pay["label"]
    ctx.user_data["payment_id"] = pay_id
    base_price = ctx.user_data["service_price"]
    if pay_id == "zelle":
        surcharge = base_price * (ZELLE_SURCHARGE_PERCENT / 100)
        final_price = base_price + surcharge
        ctx.user_data["final_price"] = final_price
        if lang == "es":
            price_note = f"💰 Precio base: ${base_price:.2f}\n➕ Recargo Zelle ({ZELLE_SURCHARGE_PERCENT}%): +${surcharge:.2f}\n💵 Total: ${final_price:.2f}"
        else:
            price_note = f"💰 Base price: ${base_price:.2f}\n➕ Zelle surcharge ({ZELLE_SURCHARGE_PERCENT}%): +${surcharge:.2f}\n💵 Total: ${final_price:.2f}"
    else:
        ctx.user_data["final_price"] = base_price
        price_note = f"💰 ${base_price:.2f}"

    keyboard = [
        [InlineKeyboardButton(t["btn_confirm"], callback_data="confirm_order")],
        [InlineKeyboardButton(t["btn_cancel"], callback_data="cancel")]
    ]

    if lang == "es":
        summary = (
            f"📋 RESUMEN DE TU PEDIDO\n"
            f"──────────────────────────────\n"
            f"📱 Servicio: {ctx.user_data['service_name']}\n"
            f"🔢 IMEI: {ctx.user_data['imei']}\n"
            f"📧 Email: {ctx.user_data['email']}\n"
            f"💳 Pago: {selected_pay['label']}\n"
            f"{price_note}\n"
            f"⏱ Tiempo estimado: {ctx.user_data['service']['time']}\n"
            f"──────────────────────────────\n\n"
            f"Confirmas tu pedido?"
        )
    else:
        summary = (
            f"📋 ORDER SUMMARY\n"
            f"──────────────────────────────\n"
            f"📱 Service: {ctx.user_data['service_name']}\n"
            f"🔢 IMEI: {ctx.user_data['imei']}\n"
            f"📧 Email: {ctx.user_data['email']}\n"
            f"💳 Payment: {selected_pay['label']}\n"
            f"{price_note}\n"
            f"⏱ Estimated time: {ctx.user_data['service']['time']}\n"
            f"──────────────────────────────\n\n"
            f"Do you confirm your order?"
        )
    await query.edit_message_text(summary, reply_markup=InlineKeyboardMarkup(keyboard))
    return CONFIRM

async def confirm_order(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    user = query.from_user
    data = ctx.user_data

    admin_msg = (
        f"🔔 NEW ORDER / NUEVO PEDIDO\n"
        f"{'─'*35}\n"
        f"👤 Client: {user.full_name}\n"
        f"🆔 Telegram: @{user.username or 'N/A'} ({user.id})\n"
        f"📱 Service: {data['service_name']}\n"
        f"🔢 IMEI: {data['imei']}\n"
        f"📧 Email: {data['email']}\n"
        f"💳 Payment: {data['payment_method']}\n"
        f"💰 Amount: ${data['final_price']:.2f}\n"
        f"⏱ ETA: {data['service']['time']}\n"
        f"{'─'*35}\n"
        f"Reply: /pay {user.id} to send instructions."
    )
    await ctx.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_msg)

    pay_id = data.get("payment_id", "")
    crypto_ids = ["usdt_trc20", "usdt_erc20", "btc"]

    if pay_id in crypto_ids:
        wallet_info = CRYPTO_WALLETS.get(pay_id)
        if wallet_info and wallet_info.get("address"):
            if lang == "es":
                wallet_msg = (
                    f"💳 Instrucciones de Pago\n\n"
                    f"{'─'*30}\n"
                    f"🔗 Red: {wallet_info['label']}\n"
                    f"📋 Direccion:\n{wallet_info['address']}\n\n"
                    f"{wallet_info['network_note']}\n"
                    f"{'─'*30}\n\n"
                    f"📸 Escanea el QR o copia la direccion de arriba.\n"
                    f"Envia exactamente el monto indicado y luego enviame el comprobante de pago aqui."
                )
            else:
                wallet_msg = (
                    f"💳 Payment Instructions\n\n"
                    f"{'─'*30}\n"
                    f"🔗 Network: {wallet_info['label']}\n"
                    f"📋 Address:\n{wallet_info['address']}\n\n"
                    f"{wallet_info['network_note']}\n"
                    f"{'─'*30}\n\n"
                    f"📸 Scan the QR or copy the address above.\n"
                    f"Send exactly the amount quoted and then send me the payment receipt here."
                )
            await query.message.reply_text(wallet_msg)
            qr_file = wallet_info.get("qr_image", "")
            if qr_file and os.path.exists(qr_file):
                with open(qr_file, "rb") as f:
                    await ctx.bot.send_photo(chat_id=user.id, photo=f)

    elif pay_id == "zelle":
        if lang == "es":
            zelle_msg = (
                f"🏦 Pago por Zelle\n\n"
                f"Para completar tu pago por Zelle, contacta directamente "
                f"a nuestro agente quien te proporcionara el numero de Zelle.\n\n"
                f"👉 Escribenos aqui: https://t.me/ImeiLocked\n\n"
                f"Por favor menciona al contactarnos:\n"
                f"📱 Servicio: {data['service_name']}\n"
                f"💰 Monto a pagar: ${data['final_price']:.2f}\n"
                f"(Ya incluye el recargo del {ZELLE_SURCHARGE_PERCENT}%)"
            )
        else:
            zelle_msg = (
                f"🏦 Zelle Payment\n\n"
                f"To complete your Zelle payment, contact our agent directly. "
                f"They will provide you with the Zelle number.\n\n"
                f"👉 Contact us here: https://t.me/ImeiLocked\n\n"
                f"Please mention when contacting us:\n"
                f"📱 Service: {data['service_name']}\n"
                f"💰 Amount to pay: ${data['final_price']:.2f}\n"
                f"(Already includes the {ZELLE_SURCHARGE_PERCENT}% surcharge)"
            )
        await query.message.reply_text(zelle_msg)

    elif pay_id == "paypal":
        if lang == "es":
            paypal_msg = (
                f"🔵 Pago por PayPal\n\n"
                f"Para completar tu pago por PayPal, contacta directamente "
                f"a nuestro agente quien te proporcionara los datos de pago.\n\n"
                f"👉 Escribenos aqui: https://t.me/ImeiLocked\n\n"
                f"Por favor menciona al contactarnos:\n"
                f"📱 Servicio: {data['service_name']}\n"
                f"💰 Monto a pagar: ${data['final_price']:.2f}"
            )
        else:
            paypal_msg = (
                f"🔵 PayPal Payment\n\n"
                f"To complete your PayPal payment, contact our agent directly. "
                f"They will provide you with the payment details.\n\n"
                f"👉 Contact us here: https://t.me/ImeiLocked\n\n"
                f"Please mention when contacting us:\n"
                f"📱 Service: {data['service_name']}\n"
                f"💰 Amount to pay: ${data['final_price']:.2f}"
            )
        await query.message.reply_text(paypal_msg)

    if lang == "es":
        client_msg = (
            f"🎉 Pedido recibido!\n\n"
            f"📱 Servicio: {data['service_name']}\n"
            f"🔢 IMEI: {data['imei']}\n"
            f"💰 Total: ${data['final_price']:.2f}\n"
            f"⏱ Tiempo estimado: {data['service']['time']}\n\n"
            f"✅ Una vez que realices el pago, envia el comprobante aqui mismo.\n"
            f"Nuestro agente lo revisara y procesara tu pedido."
        )
    else:
        client_msg = (
            f"🎉 Order received!\n\n"
            f"📱 Service: {data['service_name']}\n"
            f"🔢 IMEI: {data['imei']}\n"
            f"💰 Total: ${data['final_price']:.2f}\n"
            f"⏱ Estimated time: {data['service']['time']}\n\n"
            f"✅ Once you make the payment, send the receipt here.\n"
            f"Our agent will review and process your order."
        )
    await query.edit_message_text(client_msg)

    ctx.user_data["client_id"] = user.id
    ctx.user_data["client_name"] = user.full_name
    ctx.user_data["client_username"] = user.username or "N/A"

    return WAITING

async def forward_to_admin(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    client_name = ctx.user_data.get("client_name", user.full_name)
    client_username = ctx.user_data.get("client_username", user.username or "N/A")
    service_name = ctx.user_data.get("service_name", "N/A")

    header = (
        f"📨 MENSAJE DE CLIENTE\n"
        f"👤 {client_name} (@{client_username})\n"
        f"🆔 ID: {user.id}\n"
        f"📱 Servicio: {service_name}\n"
        f"{'─'*30}\n"
    )

    if update.message.photo:
        photo = update.message.photo[-1]
        caption = update.message.caption or ""
        await ctx.bot.send_photo(
            chat_id=ADMIN_CHAT_ID,
            photo=photo.file_id,
            caption=f"{header}{caption}"
        )
        lang = ctx.user_data.get("lang", "en")
        if lang == "es":
            await update.message.reply_text("✅ Comprobante recibido. Nuestro agente lo revisara pronto.")
        else:
            await update.message.reply_text("✅ Receipt received. Our agent will review it shortly.")

    elif update.message.document:
        await ctx.bot.send_document(
            chat_id=ADMIN_CHAT_ID,
            document=update.message.document.file_id,
            caption=f"{header}{update.message.caption or ''}"
        )
        lang = ctx.user_data.get("lang", "en")
        if lang == "es":
            await update.message.reply_text("✅ Archivo recibido. Nuestro agente lo revisara pronto.")
        else:
            await update.message.reply_text("✅ File received. Our agent will review it shortly.")

    elif update.message.text:
        await ctx.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"{header}{update.message.text}"
        )

    return WAITING

async def cmd_pay(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != str(ADMIN_CHAT_ID):
        return
    args = ctx.args
    if not args:
        await update.message.reply_text(
            "Usage:\n/pay <user_id> → next message forwarded to client\n"
            "/paycrypto <user_id> <crypto_id> → sends wallet + QR\n\n"
            "Crypto IDs: usdt_trc20 | usdt_erc20 | btc"
        )
        return
    ctx.user_data["pending_pay_user"] = args[0]
    await update.message.reply_text(
        f"✅ Ready. Your next message will be sent to user {args[0]}.\nWrite the payment instructions now."
    )

async def cmd_paycrypto(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != str(ADMIN_CHAT_ID):
        return
    args = ctx.args
    if len(args) < 2:
        await update.message.reply_text("Usage: /paycrypto <user_id> <crypto_id>\nExample: /paycrypto 123456789 usdt_trc20")
        return
    target_id = args[0]
    crypto_id = args[1]
    wallet_info = CRYPTO_WALLETS.get(crypto_id)
    if not wallet_info or not wallet_info.get("address"):
        await update.message.reply_text(f"❌ Wallet '{crypto_id}' not configured.")
        return
    msg = (
        f"💳 Payment Instructions / Instrucciones de Pago\n\n"
        f"{'─'*30}\n"
        f"🔗 Network / Red: {wallet_info['label']}\n"
        f"📋 Address / Direccion:\n{wallet_info['address']}\n\n"
        f"{wallet_info['network_note']}\n"
        f"{'─'*30}\n\n"
        f"📸 Scan QR / Escanea el QR:"
    )
    await ctx.bot.send_message(chat_id=target_id, text=msg)
    qr_file = wallet_info.get("qr_image", "")
    if qr_file and os.path.exists(qr_file):
        with open(qr_file, "rb") as f:
            await ctx.bot.send_photo(chat_id=target_id, photo=f)
    await update.message.reply_text(f"✅ Wallet + QR sent to user {target_id}.")

async def forward_payment(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != str(ADMIN_CHAT_ID):
        return
    target = ctx.user_data.get("pending_pay_user")
    if not target:
        return
    await ctx.bot.send_message(
        chat_id=target,
        text=f"💳 Payment Instructions / Instrucciones de Pago:\n\n{update.message.text}"
    )
    await update.message.reply_text(f"✅ Message sent to user {target}.")
    ctx.user_data.pop("pending_pay_user", None)

async def back_companies(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    keyboard = []
    for company in SERVICES.keys():
        keyboard.append([InlineKeyboardButton(company, callback_data=f"company_{company}")])
    keyboard.append([InlineKeyboardButton(t["btn_cancel"], callback_data="cancel")])
    await query.edit_message_text(
        t["welcome"].format(name=BOT_NAME),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return COMPANY

async def back_subcategories(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    company = ctx.user_data.get("company", "")
    subcategories = SERVICES[company]
    keyboard = []
    for subcat in subcategories.keys():
        keyboard.append([InlineKeyboardButton(subcat, callback_data=f"subcat_{subcat}")])
    keyboard.append([InlineKeyboardButton(t["btn_back"], callback_data="back_companies")])
    if lang == "es":
        msg = f"📂 {company}\n\nSelecciona una subcategoria:"
    else:
        msg = f"📂 {company}\n\nSelect a subcategory:"
    await query.edit_message_text(msg, reply_markup=InlineKeyboardMarkup(keyboard))
    return SUBCATEGORY

async def cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    await query.answer()
    await query.edit_message_text(t["cancelled"])
    ctx.user_data.clear()
    return ConversationHandler.END

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANG: [CallbackQueryHandler(set_language, pattern="^lang_")],
            COMPANY: [
                CallbackQueryHandler(select_company, pattern="^company_"),
                CallbackQueryHandler(cancel, pattern="^cancel$"),
            ],
            SUBCATEGORY: [
                CallbackQueryHandler(select_subcategory, pattern="^subcat_"),
                CallbackQueryHandler(back_companies, pattern="^back_companies$"),
                CallbackQueryHandler(cancel, pattern="^cancel$"),
            ],
            SERVICE: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, select_service),
                CallbackQueryHandler(back_subcategories, pattern="^back_subcategories$"),
            ],
            IMEI: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_imei)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
            PAYMENT: [
                CallbackQueryHandler(select_payment, pattern="^pay_"),
                CallbackQueryHandler(cancel, pattern="^cancel$"),
            ],
            CONFIRM: [
                CallbackQueryHandler(confirm_order, pattern="^confirm_order$"),
                CallbackQueryHandler(cancel, pattern="^cancel$"),
            ],
            WAITING: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_admin),
                MessageHandler(filters.PHOTO, forward_to_admin),
                MessageHandler(filters.Document.ALL, forward_to_admin),
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    app.add_handler(conv)
    app.add_handler(CommandHandler("pay", cmd_pay))
    app.add_handler(CommandHandler("paycrypto", cmd_paycrypto))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND & filters.User(int(ADMIN_CHAT_ID)),
        forward_payment
    ))
    print(f"🤖 {BOT_NAME} is running...")
    app.run_polling()
