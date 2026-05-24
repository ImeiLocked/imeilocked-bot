import os

BOT_NAME = "🔓 ImeiLocked Services"
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN_CHAT_ID = "1482942049"
ZELLE_SURCHARGE_PERCENT = 10

CRYPTO_WALLETS = {
    "usdt_trc20": {
        "label": "💚 USDT TRC20 (Tron)",
        "address": "TAXyPWxMyUyeUikVQKJ418EfeFU8DZvpAS",
        "qr_image": "qr_usdt_trc20.jpg",
        "network_note": "⚠️ Usa SOLO la red TRC20 (Tron). Enviar por otra red = pérdida de fondos.",
    },
    "usdt_erc20": {
        "label": "🔵 USDT ERC20 (Ethereum)",
        "address": "",
        "qr_image": "",
        "network_note": "⚠️ Usa SOLO la red ERC20 (Ethereum).",
    },
    "btc": {
        "label": "🟡 Bitcoin (BTC)",
        "address": "",
        "qr_image": "",
        "network_note": "⚠️ Usa SOLO la red Bitcoin.",
    },
}

PAYMENT_METHODS = [
    {
        "id": "usdt_trc20",
        "label": "💚 USDT TRC20 (Tron) — Recomendado",
        "crypto_id": "usdt_trc20",
        "auto": False,
    },
    {
        "id": "usdt_erc20",
        "label": "🔵 USDT ERC20 (Ethereum)",
        "crypto_id": "usdt_erc20",
        "auto": False,
    },
    {
        "id": "btc",
        "label": "🟡 Bitcoin (BTC)",
        "crypto_id": "btc",
        "auto": False,
    },
    {
        "id": "zelle",
        "label": f"🏦 Zelle (+{ZELLE_SURCHARGE_PERCENT}% fee)",
        "crypto_id": None,
        "auto": False,
        "address": "",
    },
    {
        "id": "paypal",
        "label": "🔵 PayPal",
        "crypto_id": None,
        "auto": False,
        "address": "",
    },
]
