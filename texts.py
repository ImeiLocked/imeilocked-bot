TEXTS = {
    "es": {
        "welcome": (
            "✅ *{name}*\n\n"
            "Bienvenido a nuestro servicio profesional de desbloqueo.\n\n"
            "📋 Selecciona una categoría para ver los servicios disponibles:"
        ),
        "select_service": (
            "📂 *Categoría: {category}*\n\nSelecciona el servicio que necesitas:"
        ),
        "enter_imei": (
            "✅ *Servicio seleccionado:*\n"
            "📱 {service}\n"
            "💰 Precio: *${price:.2f}*\n"
            "⏱ Tiempo estimado: *{time}*\n\n"
            "🔢 Por favor, ingresa el *IMEI* del dispositivo:\n"
            "_(Marca *#06#* en el teléfono para obtenerlo)_"
        ),
        "invalid_imei": "❌ IMEI inválido. Debe tener 15 o 16 dígitos. Por favor intenta de nuevo:",
        "enter_email": (
            "✅ IMEI recibido.\n\n"
            "📧 Ahora ingresa tu *correo electrónico*\n"
            "_(Aquí te enviaremos el resultado del servicio)_"
        ),
        "invalid_email": "❌ Correo inválido. Por favor ingresa un email válido:",
        "choose_payment": "💳 *Selecciona el método de pago:*",
        "zelle_surcharge": (
            "💰 Precio base: *${original:.2f}*\n"
            "➕ Recargo Zelle ({percent}%): *+${surcharge:.2f}*\n"
            "💵 *Total: ${final:.2f}*"
        ),
        "order_summary": (
            "📋 *RESUMEN DE TU PEDIDO*\n"
            "──────────────────────────────\n"
            "📱 *Servicio:* {service}\n"
            "🔢 *IMEI:* `{imei}`\n"
            "📧 *Email:* {email}\n"
            "💳 *Pago:* {payment}\n"
            "{price_note}\n"
            "⏱ *Tiempo estimado:* {time}\n"
            "──────────────────────────────\n\n"
            "¿Confirmas tu pedido?"
        ),
        "order_received": (
            "🎉 *¡Pedido recibido!*\n\n"
            "✅ *{name}*\n\n"
            "📱 *Servicio:* {service}\n"
            "🔢 *IMEI:* `{imei}`\n"
            "💰 *Total:* ${price:.2f}\n"
            "⏱ *Tiempo estimado:* {time}\n\n"
            "⏳ *Próximos pasos:*\n"
            "1️⃣ Recibirás las instrucciones de pago en breve.\n"
            "2️⃣ Una vez confirmado el pago, procesaremos tu pedido.\n"
            "3️⃣ El resultado se enviará a tu correo.\n\n"
            "📞 Si tienes dudas, nuestro agente te contactará pronto."
        ),
        "cancelled": "❌ Pedido cancelado. Escribe /start para comenzar de nuevo.",
        "btn_confirm": "✅ Confirmar Pedido",
        "btn_cancel": "❌ Cancelar",
        "btn_back": "⬅️ Volver",
    },

    "en": {
        "welcome": (
            "✅ *{name}*\n\n"
            "Welcome to our professional unlock service.\n\n"
            "📋 Select a category to see available services:"
        ),
        "select_service": (
            "📂 *Category: {category}*\n\nSelect the service you need:"
        ),
        "enter_imei": (
            "✅ *Service selected:*\n"
            "📱 {service}\n"
            "💰 Price: *${price:.2f}*\n"
            "⏱ Estimated time: *{time}*\n\n"
            "🔢 Please enter the device *IMEI*:\n"
            "_(Dial *#06#* on the phone to get it)_"
        ),
        "invalid_imei": "❌ Invalid IMEI. It must have 15 or 16 digits. Please try again:",
        "enter_email": (
            "✅ IMEI received.\n\n"
            "📧 Now enter your *email address*\n"
            "_(We'll send the service result here)_"
        ),
        "invalid_email": "❌ Invalid email. Please enter a valid email address:",
        "choose_payment": "💳 *Select payment method:*",
        "zelle_surcharge": (
            "💰 Base price: *${original:.2f}*\n"
            "➕ Zelle surcharge ({percent}%): *+${surcharge:.2f}*\n"
            "💵 *Total: ${final:.2f}*"
        ),
        "order_summary": (
            "📋 *ORDER SUMMARY*\n"
            "──────────────────────────────\n"
            "📱 *Service:* {service}\n"
            "🔢 *IMEI:* `{imei}`\n"
            "📧 *Email:* {email}\n"
            "💳 *Payment:* {payment}\n"
            "{price_note}\n"
            "⏱ *Estimated time:* {time}\n"
            "──────────────────────────────\n\n"
            "Do you confirm your order?"
        ),
        "order_received": (
            "🎉 *Order received!*\n\n"
            "✅ *{name}*\n\n"
            "📱 *Service:* {service}\n"
            "🔢 *IMEI:* `{imei}`\n"
            "💰 *Total:* ${price:.2f}\n"
            "⏱ *Estimated time:* {time}\n\n"
            "⏳ *Next steps:*\n"
            "1️⃣ You'll receive payment instructions shortly.\n"
            "2️⃣ Once payment is confirmed, we'll process your order.\n"
            "3️⃣ The result will be sent to your email.\n\n"
            "📞 If you have questions, our agent will contact you soon."
        ),
        "cancelled": "❌ Order cancelled. Type /start to begin again.",
        "btn_confirm": "✅ Confirm Order",
        "btn_cancel": "❌ Cancel",
        "btn_back": "⬅️ Back",
    },
}
