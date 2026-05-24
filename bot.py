"""
╔══════════════════════════════════════════════════════════╗
║           UNLOCK SERVICES BOT - MAIN FILE                ║
║  Para cambiar nombre/marca: edita config.py              ║
║  Para cambiar servicios: edita services.py               ║
║  Para cambiar precios/pagos/wallets: edita config.py     ║
╚══════════════════════════════════════════════════════════╝
"""

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

LANG, CATEGORY, SERVICE, IMEI, EMAIL, PAYMENT, CONFIRM = range(7)

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
    for cat in SERVICES.keys():
        keyboard.append([InlineKeyboardButton(cat, callback_data=f"cat_{cat}")])
    keyboard.append([InlineKeyboardButton(t["btn_cancel"], callback_data="cancel")])
    await query.edit_message_text(
        t["welcome"].format(name=BOT_NAME),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return CATEGORY

async def select_category(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    cat = query.data.replace("cat_", "")
    ctx.user_data["category"] = cat
    keyboard = []
    for svc in SERVICES[cat]:
        label = f"{svc['name'][lang]}  💰 ${svc['price']:.2f}  ⏱ {svc['time']}"
        keyboard.append([InlineKeyboardButton(label, callback_data=f"svc_{svc['id']}")])
    keyboard.append([InlineKeyboardButton(t["btn_back"], callback_data="back_categories")])
    await query.edit_message_text(
        t["select_service"].format(category=cat),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return SERVICE

async def select_service(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    svc_id = query.data.replace("svc_", "")
    selected = None
    for cat_services in SERVICES.values():
        for svc in cat_services:
            if svc["id"] == svc_id:
                selected = svc
                break
    if not selected:
        await query.edit_message_text("❌ Service not found.")
        return ConversationHandler.END
    ctx.user_data["service"] = selected
    ctx.user_data["service_name"] = selected["name"][lang]
    ctx.user_data["service_price"] = selected["price"]
    await query.edit_message_text(
        t["enter_imei"].format(
            service=selected["name"][lang],
            price=selected["price"],
            time=selected["time"]
        ),
        parse_mode="Markdown"
    )
    return IMEI

async def get_imei(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    imei = update.message.text.strip()
    if not imei.isdigit() or len(imei) not in [15, 16]:
        await update.message.reply_text(t["invalid_imei"])
        return IMEI
    ctx.user_data["imei"] = imei
    await update.message.reply_text(t["enter_email"], parse_mode="Markdown")
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
    await update.message.reply_text(
        t["choose_payment"],
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
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
        price_note = t["zelle_surcharge"].format(
            percent=ZELLE_SURCHARGE_PERCENT,
            original=base_price,
            surcharge=surcharge,
            final=final_price
        )
    else:
        ctx.user_data["final_price"] = base_price
        price_note = f"💰 **${base_price:.2f}**"
    keyboard = [
        [InlineKeyboardButton(t["btn_confirm"], callback_data="confirm_order")],
        [InlineKeyboardButton(t["btn_cancel"], callback_data="cancel")]
    ]
    summary = t["order_summary"].format(
        service=ctx.user_data["service_name"],
        imei=ctx.user_data["imei"],
        email=ctx.user_data["email"],
        payment=selected_pay["label"],
        price_note=price_note,
        time=ctx.user_data["service"]["time"]
    )
    await query.edit_message_text(
        summary,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return CONFIRM

async def confirm_order(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    user = query.from_user
    data = ctx.user_data
    admin_msg = (
        f"🔔 *NEW ORDER / NUEVO PEDIDO*\n"
        f"{'─'*35}\n"
        f"👤 *Client:* {user.full_name}\n"
        f"🆔 *Telegram:* @{user.username or 'N/A'} (`{user.id}`)\n"
        f"📱 *Service:* {data['service_name']}\n"
        f"🔢 *IMEI:* `{data['imei']}`\n"
        f"📧 *Email:* {data['email']}\n"
        f"💳 *Payment:* {data['payment_method']}\n"
        f"💰 *Amount:* ${data['final_price']:.2f}\n"
        f"⏱ *ETA:* {data['service']['time']}\n"
        f"{'─'*35}\n"
        f"👉 Reply with: `/pay {user.id}` then send payment instructions."
    )
    await ctx.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_msg, parse_mode="Markdown")
    await query.edit_message_text(
        t["order_received"].format(
            name=BOT_NAME,
            service=data["service_name"],
            imei=data["imei"],
            price=data["final_price"],
            time=data["service"]["time"]
        ),
        parse_mode="Markdown"
    )
    return ConversationHandler.END

async def cmd_pay(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != str(ADMIN_CHAT_ID):
        return
    args = ctx.args
    if not args:
        await update.message.reply_text(
            "Usage:\n"
            "/pay <user_id>           → next message forwarded to client\n"
            "/paycrypto <user_id> <crypto_id> → sends wallet + QR automatically\n\n"
            "Crypto IDs: usdt_trc20 | usdt_erc20 | btc"
        )
        return
    ctx.user_data["pending_pay_user"] = args[0]
    await update.message.reply_text(
        f"✅ Ready. Your next message will be sent to user `{args[0]}`.\nWrite the payment instructions now.",
        parse_mode="Markdown"
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
        await update.message.reply_text(f"❌ Wallet '{crypto_id}' not configured. Edit config.py first.")
        return
    msg = (
        f"💳 *Payment Instructions / Instrucciones de Pago*\n\n"
        f"{'─'*30}\n"
        f"🔗 *Network / Red:* {wallet_info['label']}\n"
        f"📋 *Address / Dirección:*\n`{wallet_info['address']}`\n\n"
        f"{wallet_info['network_note']}\n"
        f"{'─'*30}\n\n"
        f"📸 *Scan QR below / Escanea el QR:*"
    )
    await ctx.bot.send_message(chat_id=target_id, text=msg, parse_mode="Markdown")
    qr_file = wallet_info.get("qr_image", "")
    if qr_file and os.path.exists(qr_file):
        with open(qr_file, "rb") as f:
            await ctx.bot.send_photo(
                chat_id=target_id,
                photo=f,
                caption=f"✅ Send *exactly* the amount quoted to this address.\n\n📩 Reply here once sent.",
                parse_mode="Markdown"
            )
    else:
        await ctx.bot.send_message(
            chat_id=target_id,
            text="📋 Copy the address above carefully. Once you've sent payment, reply here.",
            parse_mode="Markdown"
        )
    await update.message.reply_text(f"✅ Wallet + QR sent to user {target_id}.")

async def forward_payment(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    if str(update.effective_user.id) != str(ADMIN_CHAT_ID):
        return
    target = ctx.user_data.get("pending_pay_user")
    if not target:
        return
    await ctx.bot.send_message(
        chat_id=target,
        text=f"💳 *Payment Instructions / Instrucciones de Pago:*\n\n{update.message.text}",
        parse_mode="Markdown"
    )
    await update.message.reply_text(f"✅ Message sent to user {target}.")
    ctx.user_data.pop("pending_pay_user", None)

async def back_categories(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = ctx.user_data.get("lang", "en")
    t = TEXTS[lang]
    keyboard = []
    for cat in SERVICES.keys():
        keyboard.append([InlineKeyboardButton(cat, callback_data=f"cat_{cat}")])
    keyboard.append([InlineKeyboardButton(t["btn_cancel"], callback_data="cancel")])
    await query.edit_message_text(
        t["welcome"].format(name=BOT_NAME),
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return CATEGORY

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
            LANG:     [CallbackQueryHandler(set_language, pattern="^lang_")],
            CATEGORY: [
                CallbackQueryHandler(select_category, pattern="^cat_"),
                CallbackQueryHandler(cancel, pattern="^cancel$"),
            ],
            SERVICE:  [
                CallbackQueryHandler(select_service, pattern="^svc_"),
                CallbackQueryHandler(back_categories, pattern="^back_categories$"),
            ],
            IMEI:     [MessageHandler(filters.TEXT & ~filters.COMMAND, get_imei)],
            EMAIL:    [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
            PAYMENT:  [
                CallbackQueryHandler(select_payment, pattern="^pay_"),
                CallbackQueryHandler(cancel, pattern="^cancel$"),
            ],
            CONFIRM:  [
                CallbackQueryHandler(confirm_order, pattern="^confirm_order$"),
                CallbackQueryHandler(cancel, pattern="^cancel$"),
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
