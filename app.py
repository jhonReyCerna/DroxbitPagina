import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="El Contador - Grupo VIP", page_icon="📊", layout="centered")

# Estilos personalizados
st.markdown("""
<style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #1e272e;
        text-align: center;
        margin-bottom: 10px;
    }
    .desc {
        font-size: 18px;
        color: #485460;
        text-align: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Título principal estilizado
st.markdown('<div class="title">📊 Acceso VIP - El Contador</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Bienvenido al exclusivo <b>Grupo VIP de apuestas deportivas</b> 🏆<br>Accede con un único pago de <b>S/ 40.00</b> y mejora tus jugadas.</div>', unsafe_allow_html=True)

# Beneficios
st.markdown("""
### 🧠 ¿Qué obtienes con tu acceso VIP?
- 📈 Análisis diarios de partidos y estadísticas.
- 💰 Recomendaciones seguras para apuestas deportivas.
- 🏅 Acceso anticipado a pronósticos de expertos.
- 🎯 Estrategias de gestión de banca y control de riesgo.
- 🗣️ Comunidad privada con tips en tiempo real.
""")

# QR y método de pago
st.markdown("### 💵 Realiza el pago de **S/ 40.00** escaneando el siguiente código con tu billetera móvil:")

# Mostrar imagen QR
qr_image = Image.open("images/imagen1.png")
st.image(qr_image, caption="Yape, Plin, BBVA, BCP, Interbank, etc.", width=300)

# Confirmación de envío
st.markdown("""
---
📤 **Después de realizar el pago**, envía tu comprobante por **WhatsApp** o **correo electrónico** para validar tu ingreso al grupo **El Contador**.
""")
