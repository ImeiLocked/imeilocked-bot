"""
╔══════════════════════════════════════════════════════════╗
║                    services.py                           ║
║  ✏️  EDITA ESTE ARCHIVO PARA:                            ║
║     - Agregar nuevos servicios                           ║
║     - Cambiar precios                                    ║
║     - Cambiar tiempos de entrega                         ║
║     - Agregar nuevas categorías                          ║
╚══════════════════════════════════════════════════════════╝

CÓMO AGREGAR UN SERVICIO:
──────────────────────────
{
    "id": "tmob_nuevo_01",        ← ID único (invéntalo, sin espacios)
    "name": {
        "es": "Nombre en Español",
        "en": "Name in English"
    },
    "price": 99.00,               ← Precio en dólares
    "time": "1-24 Horas",         ← Tiempo de entrega
},

CÓMO AGREGAR UNA CATEGORÍA NUEVA:
───────────────────────────────────
Agrega al final del diccionario SERVICES:
"🦗 CRICKET": [
    { ... servicio ... },
]
"""

SERVICES = {

    # ════════════════════════════════════════════════════
    #  T-MOBILE / SPRINT / METRO PCS
    # ════════════════════════════════════════════════════
    "📱 T-Mobile / Sprint / MetroPCS": [
        {
            "id": "tmob_all_models",
            "name": {
                "es": "T-Mobile | Sprint | MetroPCS — iPhone Todos los Modelos (Premium 100% / No Warranty)",
                "en": "T-Mobile | Sprint | MetroPCS — iPhone All Models (Premium 100% / No Warranty)"
            },
            "price": 95.00,
            "time": "1-12 Horas",
        },
        {
            "id": "tmob_direct_11_14",
            "name": {
                "es": "T-Mobile — iPhone 11/12/13/14 Series Premium 100% (Sin Garantía)",
                "en": "T-Mobile — iPhone 11/12/13/14 Series Premium 100% (No Warranty)"
            },
            "price": 100.00,
            "time": "1-24 Horas",
        },
        {
            "id": "tmob_direct_15",
            "name": {
                "es": "T-Mobile — iPhone 15 Series Premium 100% (Sin Garantía)",
                "en": "T-Mobile — iPhone 15 Series Premium 100% (No Warranty)"
            },
            "price": 100.00,
            "time": "1-24 Horas",
        },
        {
            "id": "tmob_direct_16",
            "name": {
                "es": "T-Mobile — iPhone 16 Series Premium 100% (Sin Garantía)",
                "en": "T-Mobile — iPhone 16 Series Premium 100% (No Warranty)"
            },
            "price": 100.00,
            "time": "1-24 Horas",
        },
        {
            "id": "tmob_direct_17",
            "name": {
                "es": "T-Mobile — iPhone 17 Series Premium 100% (Sin Garantía)",
                "en": "T-Mobile — iPhone 17 Series Premium 100% (No Warranty)"
            },
            "price": 100.00,
            "time": "1-24 Horas",
        },
        {
            "id": "tmob_slow_12",
            "name": {
                "es": "T-Mobile Eligible — iPhone hasta Serie 12 (Clean & Paid)",
                "en": "T-Mobile Eligible — iPhone up to Series 12 (Clean & Paid)"
            },
            "price": 60.00,
            "time": "1-7 Días",
        },
        {
            "id": "tmob_slow_13_14",
            "name": {
                "es": "T-Mobile Eligible — iPhone 13 & 14 Series (Clean & Paid)",
                "en": "T-Mobile Eligible — iPhone 13 & 14 Series (Clean & Paid)"
            },
            "price": 65.00,
            "time": "1-5 Días",
        },
        {
            "id": "tmob_slow_15",
            "name": {
                "es": "T-Mobile Eligible — iPhone 15 Series (Clean & Paid)",
                "en": "T-Mobile Eligible — iPhone 15 Series (Clean & Paid)"
            },
            "price": 73.00,
            "time": "1-5 Días",
        },
        {
            "id": "tmob_slow_16",
            "name": {
                "es": "T-Mobile Eligible — iPhone 16 Series (Clean & Paid)",
                "en": "T-Mobile Eligible — iPhone 16 Series (Clean & Paid)"
            },
            "price": 85.00,
            "time": "1-5 Días",
        },
        {
            "id": "tmob_slow_17",
            "name": {
                "es": "T-Mobile Eligible — iPhone 17 Series (Clean & Paid)",
                "en": "T-Mobile Eligible — iPhone 17 Series (Clean & Paid)"
            },
            "price": 85.00,
            "time": "1-5 Días",
        },
        {
            "id": "tmob_franklin",
            "name": {
                "es": "T-Mobile — Franklin Wireless T9 Router/Hotspot Unlock (Auto API)",
                "en": "T-Mobile — Franklin Wireless T9 Router/Hotspot Unlock (Auto API)"
            },
            "price": 13.00,
            "time": "Minutos",
        },
        {
            "id": "tmob_premium_unbarring",
            "name": {
                "es": "T-Mobile Premium Unbarring — iPhone & Generic (Bloqueado/Robado → Clean)",
                "en": "T-Mobile Premium Unbarring — iPhone & Generic (Blocked/Stolen → Clean)"
            },
            "price": 60.00,
            "time": "1-12 Horas",
        },
        {
            "id": "tmob_unbarring",
            "name": {
                "es": "T-Mobile Unbarring — iPhone & Generic (Cambio ESN a Clean)",
                "en": "T-Mobile Unbarring — iPhone & Generic (ESN Change to Clean)"
            },
            "price": 37.00,
            "time": "1-72 Horas",
        },
        {
            "id": "tmob_express_all_14",
            "name": {
                "es": "T-Mobile/Sprint/MetroPCS — Todos los Modelos hasta iPhone 14 Pro Max (Premium Express)",
                "en": "T-Mobile/Sprint/MetroPCS — All Models up to iPhone 14 Pro Max (Premium Express)"
            },
            "price": 146.00,
            "time": "1-12 Horas",
        },
        {
            "id": "tmob_express_15pro",
            "name": {
                "es": "T-Mobile/Sprint/MetroPCS — iPhone 15 Pro / 15 Pro Max (Premium Express)",
                "en": "T-Mobile/Sprint/MetroPCS — iPhone 15 Pro / 15 Pro Max (Premium Express)"
            },
            "price": 183.00,
            "time": "1-12 Horas",
        },
        {
            "id": "tmob_express_15",
            "name": {
                "es": "T-Mobile/Sprint/MetroPCS — iPhone 15 / 15 Plus (Premium Express)",
                "en": "T-Mobile/Sprint/MetroPCS — iPhone 15 / 15 Plus (Premium Express)"
            },
            "price": 176.00,
            "time": "1-12 Horas",
        },
        {
            "id": "tmob_express_16",
            "name": {
                "es": "T-Mobile/Sprint/MetroPCS — iPhone 16 / 16 Plus (Premium Express)",
                "en": "T-Mobile/Sprint/MetroPCS — iPhone 16 / 16 Plus (Premium Express)"
            },
            "price": 205.00,
            "time": "1-24 Horas",
        },
        {
            "id": "tmob_express_16pro",
            "name": {
                "es": "T-Mobile/MetroPCS/Sprint — iPhone 16 Pro / 16 Pro Max (Clean/Premium + Finance Express)",
                "en": "T-Mobile/MetroPCS/Sprint — iPhone 16 Pro / 16 Pro Max (Clean/Premium + Finance Express)"
            },
            "price": 218.00,
            "time": "1-12 Horas",
        },
        {
            "id": "tmob_express_17",
            "name": {
                "es": "Sprint/T-Mobile/MetroPCS — iPhone 17 / 17 Air (Premium ⚡ Sin Relock)",
                "en": "Sprint/T-Mobile/MetroPCS — iPhone 17 / 17 Air (Premium ⚡ No Relock)"
            },
            "price": 248.00,
            "time": "6-24 Horas",
        },
        {
            "id": "tmob_express_17pro",
            "name": {
                "es": "Sprint/T-Mobile/MetroPCS — iPhone 17 Pro (Premium ⚡ Sin Relock)",
                "en": "Sprint/T-Mobile/MetroPCS — iPhone 17 Pro (Premium ⚡ No Relock)"
            },
            "price": 270.00,
            "time": "6-24 Horas",
        },
        {
            "id": "tmob_express_17promax",
            "name": {
                "es": "Sprint/T-Mobile/MetroPCS — iPhone 17 Pro Max (Premium ⚡ Sin Relock)",
                "en": "Sprint/T-Mobile/MetroPCS — iPhone 17 Pro Max (Premium ⚡ No Relock)"
            },
            "price": 288.00,
            "time": "6-24 Horas",
        },
    ],

    # ════════════════════════════════════════════════════
    #  VERIZON
    # ════════════════════════════════════════════════════
    "📡 Verizon USA": [
        {
            "id": "ver_fast_16",
            "name": {
                "es": "Verizon USA — iPhone Unlock Todos los Modelos hasta Serie 16 (Fast / Eligible 60 días)",
                "en": "Verizon USA — iPhone Unlock All Models up to Series 16 (Fast / Eligible 60 Days)"
            },
            "price": 115.00,
            "time": "1-72 Horas",
        },
        {
            "id": "ver_17_unpaid",
            "name": {
                "es": "Verizon USA — iPhone Todos los Modelos hasta Serie 17 (Clean & Unpaid / 90% Éxito / Sin Relock)",
                "en": "Verizon USA — iPhone All Models up to Series 17 (Clean & Unpaid / 90% Success / No Relock)"
            },
            "price": 99.00,
            "time": "1-15 Días",
        },
        {
            "id": "ver_convert_eligible",
            "name": {
                "es": "Verizon USA — Convertir IMEI No Elegible a Elegible (iPhone & Generic)",
                "en": "Verizon USA — Convert Non Eligible IMEI to Eligible Status (iPhone & Generic)"
            },
            "price": 40.00,
            "time": "1-7 Días",
        },
        {
            "id": "ver_esn_check",
            "name": {
                "es": "Verizon USA — ESN Check (Clean / Bloqueado / Blacklist) Instant",
                "en": "Verizon USA — ESN Check (Clean / Blocked / Blacklist) Instant"
            },
            "price": 1.03,
            "time": "Minutos",
        },
        {
            "id": "ver_finder",
            "name": {
                "es": "Verizon USA — Finder: Nombre + Número del Primer Dueño",
                "en": "Verizon USA — Finder: First Owner Name + Number"
            },
            "price": 12.00,
            "time": "2-5 Días",
        },
        {
            "id": "ver_unbarring",
            "name": {
                "es": "Verizon USA — Unbarring iPhone & Generic (ESN a Clean / Sin Relock)",
                "en": "Verizon USA — Unbarring iPhone & Generic (ESN to Clean / No Relock)"
            },
            "price": 77.00,
            "time": "1-12 Días",
        },
        {
            "id": "ver_esn_block",
            "name": {
                "es": "Verizon USA — Unlock Eligibility Checker iPhone & Generic (Instant)",
                "en": "Verizon USA — Unlock Eligibility Checker iPhone & Generic (Instant)"
            },
            "price": 1.25,
            "time": "Instant",
        },
        {
            "id": "ver_android",
            "name": {
                "es": "Verizon USA — Android Unlock por IMEI Sin Código (Samsung/Pixel/Etc) Clean Only",
                "en": "Verizon USA — Android IMEI Unlock No Ask Code (Samsung/Pixel/Etc) Clean Only"
            },
            "price": 147.00,
            "time": "10-25 Días",
        },
        {
            "id": "ver_motorola",
            "name": {
                "es": "Motorola USA — Verizon Unlock Codes (Ver descripción)",
                "en": "Motorola USA — Verizon Unlock Codes (Check Description)"
            },
            "price": 11.00,
            "time": "10-20 Minutos",
        },
        {
            "id": "ver_apple_id",
            "name": {
                "es": "Verizon USA — Apple Owner ID Info Service (Servicio Rápido)",
                "en": "Verizon USA — Apple Owner ID Info Service (Fast Service)"
            },
            "price": 25.00,
            "time": "1-12 Horas",
        },
    ],

    # ════════════════════════════════════════════════════
    #  AT&T USA & AT&T MÉXICO
    # ════════════════════════════════════════════════════
    "📶 AT&T USA & México": [
        {
            "id": "att_mx_6_xs",
            "name": {
                "es": "AT&T México — iPhone 6 hasta Xs Max (99% Éxito)",
                "en": "AT&T Mexico — iPhone 6 to Xs Max (99% Success)"
            },
            "price": 34.90,
            "time": "1-24 Horas",
        },
        {
            "id": "att_mx_11_12",
            "name": {
                "es": "AT&T México — iPhone 11/12 Series (99% Éxito)",
                "en": "AT&T Mexico — iPhone 11/12 Series (99% Success)"
            },
            "price": 43.00,
            "time": "1-48 Horas",
        },
        {
            "id": "att_mx_13",
            "name": {
                "es": "AT&T México — iPhone 13 Series (99% Éxito)",
                "en": "AT&T Mexico — iPhone 13 Series (99% Success)"
            },
            "price": 68.00,
            "time": "1-24 Horas",
        },
        {
            "id": "att_mx_14",
            "name": {
                "es": "AT&T México — iPhone 14 Series (99% Éxito)",
                "en": "AT&T Mexico — iPhone 14 Series (99% Success)"
            },
            "price": 79.00,
            "time": "1-24 Horas",
        },
        {
            "id": "att_mx_15",
            "name": {
                "es": "AT&T México — iPhone 15 Series (99% Éxito)",
                "en": "AT&T Mexico — iPhone 15 Series (99% Success)"
            },
            "price": 88.00,
            "time": "1-24 Horas",
        },
        {
            "id": "att_mx_16",
            "name": {
                "es": "AT&T México — iPhone 16 Series (99% Éxito)",
                "en": "AT&T Mexico — iPhone 16 Series (99% Success)"
            },
            "price": 97.00,
            "time": "1-24 Horas",
        },
        {
            "id": "att_mx_17",
            "name": {
                "es": "AT&T México — iPhone 17 Series (99% Éxito)",
                "en": "AT&T Mexico — iPhone 17 Series (99% Success)"
            },
            "price": 108.00,
            "time": "Minutos",
        },
        {
            "id": "att_clean_refund",
            "name": {
                "es": "AT&T USA — Clean Check + Unlock (Reembolso si no se completa)",
                "en": "AT&T USA — Clean Check + Unlock (Refund if not completed)"
            },
            "price": 6.00,
            "time": "Minutos",
        },
        {
            "id": "att_clean_checker",
            "name": {
                "es": "AT&T USA — Status Check + Unlock Rápido 90% (Sin Reembolso)",
                "en": "AT&T USA — Status Check + Unlock Fast 90% (No Refund)"
            },
            "price": 1.50,
            "time": "Minutos",
        },
        {
            "id": "att_past_due_xs",
            "name": {
                "es": "AT&T USA — Past Due Payments iPhone hasta Xs Max (Alto Éxito)",
                "en": "AT&T USA — Past Due Payments iPhone up to Xs Max (High Success)"
            },
            "price": 45.00,
            "time": "7-25 Días",
        },
        {
            "id": "att_past_due_12",
            "name": {
                "es": "AT&T USA — Past Due Payments iPhone 11 hasta 12 Pro Max (Alto Éxito)",
                "en": "AT&T USA — Past Due Payments iPhone 11 to 12 Pro Max (High Success)"
            },
            "price": 55.00,
            "time": "7-25 Días",
        },
        {
            "id": "att_past_due_16",
            "name": {
                "es": "AT&T USA — Past Due Payments iPhone 13 hasta 16 Pro Max (Alto Éxito)",
                "en": "AT&T USA — Past Due Payments iPhone 13 to 16 Pro Max (High Success)"
            },
            "price": 75.00,
            "time": "1-25 Días",
        },
        {
            "id": "att_no_longer_basic",
            "name": {
                "es": "AT&T USA — Device No Longer Active / Account 2 Locked (iPhone & Generic)",
                "en": "AT&T USA — Device No Longer Active / Account 2 Locked (iPhone & Generic)"
            },
            "price": 22.80,
            "time": "1-10 Días",
        },
        {
            "id": "att_no_longer_high",
            "name": {
                "es": "AT&T USA — No Longer Active, Alto Éxito (iPhone & Generic Todos los Modelos)",
                "en": "AT&T USA — No Longer Active, High Success (iPhone & Generic All Models)"
            },
            "price": 33.00,
            "time": "1-48 Horas",
        },
        {
            "id": "att_post_60",
            "name": {
                "es": "AT&T USA — Post-Purchase 60 Days (iPhone & Generic Todos los Modelos)",
                "en": "AT&T USA — Post-Purchase 60 Days (iPhone & Generic All Models)"
            },
            "price": 9.40,
            "time": "24-72 Horas",
        },
        {
            "id": "att_android_unbarring",
            "name": {
                "es": "AT&T USA — Carrier Unbarring Android Generic (Blacklist → Clean)",
                "en": "AT&T USA — Carrier Unbarring Android Generic (Blacklist → Clean)"
            },
            "price": 120.00,
            "time": "1-25 Días",
        },
        {
            "id": "att_semi_14",
            "name": {
                "es": "AT&T USA — iPhone Semi Premium hasta Serie 14 (1-55 días hábiles)",
                "en": "AT&T USA — iPhone Semi Premium up to Series 14 (1-55 working days)"
            },
            "price": 150.00,
            "time": "1-10 Días",
        },
        {
            "id": "att_semi_15",
            "name": {
                "es": "AT&T USA — iPhone Semi Premium hasta Serie 15 (1-55 días hábiles)",
                "en": "AT&T USA — iPhone Semi Premium up to Series 15 (1-55 working days)"
            },
            "price": 245.00,
            "time": "1-10 Días",
        },
        {
            "id": "att_semi_16",
            "name": {
                "es": "AT&T USA — iPhone Semi Premium Serie 16 (1-55 días hábiles)",
                "en": "AT&T USA — iPhone Semi Premium Series 16 (1-55 working days)"
            },
            "price": 265.00,
            "time": "1-10 Días",
        },
        {
            "id": "att_unbarring_16_17",
            "name": {
                "es": "AT&T USA — Unbarring iPhone 16 & 17 (Blacklist → Clean)",
                "en": "AT&T USA — Unbarring iPhone 16 & 17 (Blacklist → Clean)"
            },
            "price": 150.00,
            "time": "10-25 Días",
        },
        {
            "id": "att_apple_id",
            "name": {
                "es": "AT&T USA — Apple Owner ID Info Service (Servicio Rápido)",
                "en": "AT&T USA — Apple Owner ID Info Service (Fast Service)"
            },
            "price": 25.00,
            "time": "6-72 Horas",
        },
    ],

    # ════════════════════════════════════════════════════
    #  CHECKS / VERIFICACIONES
    # ════════════════════════════════════════════════════
    "🔍 Checks & Verificaciones": [
        {
            "id": "chk_honor",
            "name": {
                "es": "Honor — Info Check por IMEI & Serial (Instant)",
                "en": "Honor — Info Check by IMEI & Serial (Instant)"
            },
            "price": 1.06,
            "time": "Instant",
        },
        {
            "id": "chk_tmob_esn",
            "name": {
                "es": "T-Mobile USA — ESN Pro Check por IMEI (Instant)",
                "en": "T-Mobile USA — ESN Pro Check by IMEI (Instant)"
            },
            "price": 1.05,
            "time": "Instant",
        },
        {
            "id": "chk_iphone_carrier",
            "name": {
                "es": "iPhone — Carrier / Sim Lock Status & Fecha de Compra por IMEI/SN (Instant)",
                "en": "iPhone — Carrier / Sim Lock Status & Purchase Date by IMEI/SN (Instant)"
            },
            "price": 1.03,
            "time": "Instant",
        },
        {
            "id": "chk_xiaomi_full",
            "name": {
                "es": "Xiaomi — Full Device Details Check (IMEI / Serial / Activación / Find Device)",
                "en": "Xiaomi — Full Device Details Check (IMEI / Serial / Activation / Find Device)"
            },
            "price": 1.08,
            "time": "Minutos",
        },
        {
            "id": "chk_xiaomi_country",
            "name": {
                "es": "Xiaomi — Country Check vía Lock Code (Keylock/CodeLock)",
                "en": "Xiaomi — Country Check via Lock Code (Keylock/CodeLock)"
            },
            "price": 1.60,
            "time": "1-2 Horas",
        },
        {
            "id": "chk_samsung_simlock",
            "name": {
                "es": "Samsung — Sim Lock Status Checker por IMEI (Locked/Unlocked) Instant",
                "en": "Samsung — Sim Lock Status Checker by IMEI (Locked/Unlocked) Instant"
            },
            "price": 1.10,
            "time": "Instant",
        },
        {
            "id": "chk_samsung_knox",
            "name": {
                "es": "Samsung — Knox Guard / Carrier / Warranty Status Checker (Instant)",
                "en": "Samsung — Knox Guard / Carrier / Warranty Status Checker (Instant)"
            },
            "price": 1.11,
            "time": "Instant",
        },
        {
            "id": "chk_pixel",
            "name": {
                "es": "Google Pixel — Activation Date / Warranty / Carrier Check por IMEI/SN",
                "en": "Google Pixel — Activation Date / Warranty / Carrier Check by IMEI/SN"
            },
            "price": 1.10,
            "time": "Minutos",
        },
        {
            "id": "chk_metropcs_app",
            "name": {
                "es": "MetroPCS — Device Unlock App Checker + Unlock (180 días activado / Sin Reembolso)",
                "en": "MetroPCS — Device Unlock App Checker + Unlock (180 days activated / No Refund)"
            },
            "price": 7.35,
            "time": "1-72 Horas",
        },
        {
            "id": "chk_metropcs_android",
            "name": {
                "es": "Metro PCS USA — Android APP Unlock (180 días activado / Sin Reembolso)",
                "en": "Metro PCS USA — Android APP Unlock (180 days activated / No Refund)"
            },
            "price": 8.00,
            "time": "Minutos",
        },
        {
            "id": "chk_tmob_contract",
            "name": {
                "es": "T-Mobile USA — Eligibility Checker Instant (Contract/Finance/GSMA/Sprint Data)",
                "en": "T-Mobile USA — Eligibility Checker Instant (Contract/Finance/GSMA/Sprint Data)"
            },
            "price": 1.17,
            "time": "Minutos",
        },
        {
            "id": "chk_ver_esn",
            "name": {
                "es": "Verizon USA — ESN Check Clean/Bloqueado/Blacklist (Instant)",
                "en": "Verizon USA — ESN Check Clean/Blocked/Blacklist (Instant)"
            },
            "price": 1.03,
            "time": "Minutos",
        },
        {
            "id": "chk_ver_eligibility",
            "name": {
                "es": "Verizon USA — Unlock Eligibility Checker iPhone & Generic (Instant)",
                "en": "Verizon USA — Unlock Eligibility Checker iPhone & Generic (Instant)"
            },
            "price": 1.25,
            "time": "Instant",
        },
        {
            "id": "chk_spectrum",
            "name": {
                "es": "Spectrum USA — iPhone Unlock Eligibility Checker (Instant)",
                "en": "Spectrum USA — iPhone Unlock Eligibility Checker (Instant)"
            },
            "price": 1.08,
            "time": "Instant",
        },
        {
            "id": "chk_cricket",
            "name": {
                "es": "Cricket USA — Unlock Eligibility Checker iPhone & Generic (Instant)",
                "en": "Cricket USA — Unlock Eligibility Checker iPhone & Generic (Instant)"
            },
            "price": 1.70,
            "time": "Instant",
        },
        {
            "id": "chk_lpro",
            "name": {
                "es": "LPro A12+ — Rebypass hasta iOS 18.1.1 con/sin Network",
                "en": "LPro A12+ — Rebypass up to iOS 18.1.1 with/without Network"
            },
            "price": 15.00,
            "time": "Instant",
        },
    ],

    # ════════════════════════════════════════════════════
    #  UNBARRING / ESN CLEANING
    # ════════════════════════════════════════════════════
    "🔓 Unbarring & ESN Cleaning": [
        {
            "id": "unb_tmob_premium",
            "name": {
                "es": "T-Mobile Premium Unbarring — iPhone & Generic (Bloqueado/Robado → Clean)",
                "en": "T-Mobile Premium Unbarring — iPhone & Generic (Blocked/Stolen → Clean)"
            },
            "price": 60.00,
            "time": "1-12 Horas",
        },
        {
            "id": "unb_tmob",
            "name": {
                "es": "T-Mobile Unbarring — iPhone & Generic (Cambio ESN a Clean)",
                "en": "T-Mobile Unbarring — iPhone & Generic (ESN Change to Clean)"
            },
            "price": 37.00,
            "time": "1-72 Horas",
        },
        {
            "id": "unb_att_android",
            "name": {
                "es": "AT&T USA — Carrier Unbarring Android (Blacklist → Clean)",
                "en": "AT&T USA — Carrier Unbarring Android (Blacklist → Clean)"
            },
            "price": 120.00,
            "time": "1-25 Días",
        },
        {
            "id": "unb_cricket",
            "name": {
                "es": "Cricket — Unbarring Todos los Modelos hasta iPhone 15 Pro Max (Blacklist/Robado → Clean, Fraude NO soportado)",
                "en": "Cricket — Unbarring All Models up to iPhone 15 Pro Max (Blacklist/Stolen → Clean, Fraud NOT supported)"
            },
            "price": 60.00,
            "time": "2-7 Días",
        },
        {
            "id": "unb_att_16_17",
            "name": {
                "es": "AT&T USA — Unbarring iPhone 16 & 17 (Blacklist → Clean)",
                "en": "AT&T USA — Unbarring iPhone 16 & 17 (Blacklist → Clean)"
            },
            "price": 150.00,
            "time": "10-25 Días",
        },
        {
            "id": "unb_verizon",
            "name": {
                "es": "Verizon USA — Unbarring iPhone & Generic (ESN → Clean / Sin Relock)",
                "en": "Verizon USA — Unbarring iPhone & Generic (ESN → Clean / No Relock)"
            },
            "price": 77.00,
            "time": "1-12 Días",
        },
    ],
}
