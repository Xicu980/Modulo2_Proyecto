#IMPORTAMOS LIBRERIAS
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import warnings
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

warnings.filterwarnings('ignore')
#st.set_option('deprecation.showPyplotGlobalUse', False)

#CONFIGURACION DE LA PAGINA
st.set_page_config(
    page_title="Ayuntamiento de Barcelona",
    page_icon="r'data/webimg/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded", #opciones: collapsed, expanded NO OBLIGATORIO
)

# Título de la página
# st.title("Estudio preliminar sobre la incidencia de la Ley de Urbanización Turistica en Barcelona")

# Crear menú lateral
menu_options = ["inicio", "Barcelona en detalle", "regularización", "efectos de la ley", "herramienta"]
menu_choice = st.sidebar.selectbox("Seleccione una opción", menu_options)

# Mostrar contenido según la selección
if menu_choice == "inicio":
    st.markdown('<h1 style="text-align: center; color: blue;">Estudio preliminar sobre la incidencia de la Ley de Urbanización Turistica en Barcelona</h1>', unsafe_allow_html=True)
    #st.markdown('<div style="text-align: center;"> <img src="data/webimg/Barcelona.jpg" width="300"> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    columnas = st.columns(3)
    with columnas[1]:
        st.image("data/webimg/Barcelona.jpg", width=500)
    st.markdown('<p style="text-align: center;">Analisis de mercado de AirBnb in Barcelona. Datos de InsideAirBnb al 06/09/2024</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
elif menu_choice == "Barcelona en detalle":
    st.subheader("Algun datos sobre Barcelona:")
    st.markdown(
    """
    #### Población
    Barcelona cuenta con una población aproximadamente de **1.620.000 habitantes**. </br>
    Sin embargo, su área metropolitana cuenta con algo más de **5 millones de personas**. </br>
    Esto hace que Barcelona se consolide como una de las ciudades más grandes de Europa.
    
    #### Economía
    El Producto Interno Bruto (PIB) de Barcelona es aproximadamente de **159,8 mil millones de euros** (2020), 
    destacando sectores como el **industrial**, el **tecnológico** y los **servicios financieros**.
    
    #### Turismo
    El turismo es una de las principales fuentes de ingresos de Barcelona. </br>
    En el **2023**, la ciudad recibió cerca de **26 millones de turistas**, que generaron un impacto directo 
    de **12,418 millones de euros** (un **21% más** que en el 2022).

    #### Oferta Cultural y Rectativa
    La ciudad ofrece una amplia gama de actividades culturales, deportivas y de ocio. Sus playas, parques y eventos cultiuales la
    convertien en un lugar actractrivo tantop para residente coma para visitantes.

    Barcelona combina elementos que promueven una alta calidad de vida, como su clima, oferta cultural y servicios públicos.
    No obstante, enfrenta **retos en áreas como la vivienda asequible** y la sostenibilidad ambiental, que requieren atención continua
    para mantener y mejorar el bienestar de sus habitantes.
    """,
    unsafe_allow_html=True
)
elif menu_choice == "regularización":
    st.subheader("Las regolarizaciones en Barcelona")
    st.image("data/webimg/precio_medio_alquiler.png", width=800)
    
    st.markdown(
    """
       
    - **2021**: Barcelona prohíbe el alquiler de habitaciones privadas para estancias de menos de 31 días.
    - **Junio 2024**: El alcalde Jaume Collboni anunció un plan para eliminar los más de **10.000 pisos turísticos** para finales
    del 2028. </br> **Estudiaremos el impacto de esta medida en el sector de AirBnb**
    - **Diciembre 2024**: Se propone modificar el **Plan General Metropolitano** para regular los alquileres de temporada.
    """,
    unsafe_allow_html=True
    )
    st.image("data/webimg/vivienda_turisticas_bcn.png", width=700)
    st.caption("Datos de PEUAT Barcelona")
elif menu_choice == "efectos de la ley":
    st.subheader("Los efectos de la Ley")
    st.markdown(
    """
    Dado que la Ley del 21 de junio de 2024 es demasiado reciente para evaluar su efectividad en profundidad, hemos centrado nuestra atención en cómo esta ha incentivado a los propietarios a regularizar sus viviendas turísticas. Esto se refleja en un incremento del 2,02% en las viviendas con licencia durante el ultimo periodo que va de Junio a Septiembre del mismo año.
    Y un incremento de un 6,02% respecto a los ultimos datos del 2023
    """
    )
    st.image("data/webimg/Licencias.png", width=1000)

    st.markdown(
    """
    Esto se traduce en 557 anuncios adicionales desde junio a septiembre, y 1.161 más con respecto a 2023. 
    Al parecer, la nueva ley ha estimulado tanto la regularización como la aparición de nuevos anuncios, 
    probablemente motivados por la incertidumbre futura.

    Para enriquecer nuestro análisis, hemos examinado las estrategias aplicadas en otras ciudades:

    **París:** Exige a los propietarios registrar sus propiedades y limita el alquiler turístico a 120 días por año. 
    Además, ha multado a plataformas como Airbnb por incumplimientos, reduciendo significativamente 
    el número de viviendas turísticas ilegales.

    **Nueva York:** Prohíbe los alquileres de menos de 30 días si el anfitrión no reside en la misma vivienda. 
    No obstante, esta medida ha generado un mercado paralelo de alquileres ilegales.

    **Lisboa:** Ha ofrecido incentivos fiscales para que los propietarios conviertan sus viviendas turísticas 
    en residencias habituales. Esta estrategia ha resultado más efectiva para reincorporar inmuebles al 
    mercado residencial sin eliminar por completo la opción turística.
    """

    )

elif menu_choice == "herramienta":
    st.subheader("Herramienta de analisis de datos al 06/09/2024")
    st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiMDc2YzI5YWQtYjk4ZS00NWM0LWI3ZTYtMGQwZjAyZWRhZjJiIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9", height=900)
# Agregar un pie de página opcional
st.sidebar.markdown("---")
st.sidebar.write("© 2024 by Francesco Degl Innocenti")
st.sidebar.write("Bootcamp Hub Upgrade 2024")