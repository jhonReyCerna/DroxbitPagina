import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


#config
st.set_page_config(page_title="Droxbit", page_icon="🤖", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
email_address ="emailcontact@gmail.com"

lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

with st.container():
    st.subheader("Hola, soy Droxbit 👨‍💻")
    st.title("Creamos contenido para tiktok")
    st.write(
        "👾 Tutoriales rápidos para mejorar tus habilidades. 💻 Hackea tu productividad con herramientas y apps. 🎮 Trucos y gameplays que te harán subir de nivel en tus juegos favoritos. 🤖 Novedades en IA y tecnología para estar siempre actualizado."
    )
    st.write("[Saber más >](https://www.tiktok.com/@droxbitxd?lang=es)")



# sobre nosotros
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Sobre nosotros")
        st.write(
            """
            En Droxbit, somos un equipo apasionado por la tecnología y el mundo digital. Nos especializamos en crear contenido que simplifica lo complejo, desde las últimas tendencias en gadgets y tecnología, hasta los juegos más innovadores del mercado. Nuestro objetivo es hacer que la tecnología sea accesible para todos, ofreciendo tips prácticos, tutoriales, reseñas y análisis que ayudan a nuestra comunidad a tomar decisiones informadas y optimizar su vida digital.

            Nuestra Misión
            
            Hacer que la tecnología y el gaming sean herramientas al alcance de todos, brindando contenido educativo y entretenido que te empodera para aprovechar el máximo potencial de las herramientas digitales y disfrutar de lo último en videojuegos.

            Nuestra Visión
            
            Convertirnos en la comunidad líder en tecnología y gaming, donde cada miembro pueda aprender, crecer y disfrutar de las infinitas posibilidades del mundo digital.

            Valores que nos definen:

            Innovación: Siempre explorando lo último en tecnología y gaming.
            
            Accesibilidad: Explicamos lo complejo de forma sencilla.
            
            Pasión: Somos gamers, somos techies, y eso se nota.
            
            Comunidad: Nos importa el feedback y el crecimiento de nuestra audiencia.
            
            ¡Bienvenido a Droxbit, donde la tecnología y el gaming son más que un hobby, son nuestro estilo de vida!
            """
        )
        st.write("[Más sobre nosotros>](https://www.youtube.com/watch?v=dKTFpjqiVfE)")
    with right_column:
        st_lottie(load_lottieurl(lottie_file), height=400)

# servicios
with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("En Droxbit, ofrecemos una amplia gama de servicios diseñados para los entusiastas de la tecnología y el gaming, así como para aquellos que buscan optimizar su vida digital. Nuestro enfoque es educativo, práctico y siempre actualizado con las últimas tendencias.")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/apps.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Tutoriales Personalizados")
        st.write(
            """
            Aprende a utilizar nuevas herramientas digitales y maximiza el potencial de tu tecnología favorita con nuestros tutoriales paso a paso. Cubrimos desde configuraciones básicas hasta hacks avanzados.   
            """
        )
        st.write("[Ver servicios >](https://www.youtube.com/watch?v=kO80u5yKl5Q)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/automation.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Recomendaciones de Gadgets")
        st.write(
            """
            Te ayudamos a elegir los mejores gadgets según tus necesidades y presupuesto. Realizamos análisis profundos y comparaciones para que siempre compres lo mejor.
            """
        )
        st.write("[Ver servicios >](https://www.youtube.com/watch?v=EFWwlgJg7Zg)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/visualizacion.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Reseñas de Videojuegos")
        st.write(
            """
            Exploramos lo último en el mundo de los videojuegos, con reseñas detalladas que cubren gameplay, gráficos, historia y más, para que tomes la mejor decisión antes de j
            """
        )
        st.write("[Ver servicios >](https://www.youtube.com/watch?v=JfFEWkHXq6o)")
        
with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/visualizacion.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Consultoría en Tecnología")
        st.write(
            """
            Asesoramos a empresas y personas sobre las mejores herramientas digitales para mejorar la productividad, la seguridad y la eficiencia en su vida diaria o en sus negocios.
            """
        )
        st.write("[Ver servicios >](https://www.youtube.com/watch?v=IKuwoKgHDXA)")


# contacto
with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros!")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
