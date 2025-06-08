import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Grupo VIP Droxbit", page_icon="💎", layout="centered")

# Estilos personalizados
st.markdown("""
<style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 10px;
    }
    .desc {
        font-size: 18px;
        color: #34495e;
        text-align: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Título principal estilizado
st.markdown('<div class="title">💎 Acceso al Grupo VIP de Droxbit</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Bienvenido a nuestro exclusivo <b>Grupo VIP</b> 🎉<br>Para formar parte, solo debes realizar un único pago de <b>S/ 40.00</b>.</div>', unsafe_allow_html=True)

# Beneficios
st.markdown("""
### 🔑 Con tu membresía VIP obtendrás:
- 🎮 Acceso prioritario a contenido exclusivo.
- 🤖 Recomendaciones personalizadas en tecnología y gaming.
- 🧠 Consejos avanzados sobre productividad digital.
- 🕹️ Participación en sorteos y eventos especiales.
""")

# QR y método de pago
st.markdown("### 📲 Escanea el siguiente QR para realizar el pago de **S/ 40.00** con cualquier billetera móvil:")

# Mostrar imagen QR con tamaño reducido
qr_image = Image.open("images/imagen1.png")
st.image(qr_image, caption="Escanea y paga con Yape, Plin, BBVA, BCP, Interbank, etc.", width=300)

# Confirmación de envío
st.markdown("""
---  
📩 **Una vez realizado el pago**, por favor envíanos tu comprobante al **correo** o **WhatsApp** para validar tu acceso al grupo VIP.
""")

