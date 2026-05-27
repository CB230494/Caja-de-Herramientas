import streamlit as st

st.set_page_config(
    page_title="Caja de Herramientas Preventiva Policial",
    page_icon="🧰",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    color: #1f2937;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #4b5563;
    margin-bottom: 30px;
}

.card {
    padding: 28px;
    border-radius: 25px;
    color: white;
    min-height: 230px;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.20);
    transition: transform 0.2s ease-in-out;
    margin-bottom: 15px;
}

.card:hover {
    transform: scale(1.03);
}

.card h2 {
    font-size: 32px;
    font-weight: 900;
    margin-bottom: 10px;
}

.card p {
    font-size: 17px;
    line-height: 1.4;
}

.great {
    background: linear-gradient(135deg, #ff7b00, #ffb703);
}

.mpas {
    background: linear-gradient(135deg, #0077b6, #00b4d8);
}

.dare {
    background: linear-gradient(135deg, #7209b7, #c77dff);
}

.pscc {
    background: linear-gradient(135deg, #06d6a0, #118ab2);
}

.vif {
    background: linear-gradient(135deg, #ef476f, #d62828);
}

.info-box {
    background: #e0f2fe;
    padding: 18px;
    border-radius: 15px;
    border-left: 6px solid #0284c7;
    margin-bottom: 25px;
    color: #1f2937;
}

.resource-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.12);
    margin-bottom: 15px;
    border-left: 8px solid #2563eb;
}

.resource-title {
    font-size: 22px;
    font-weight: 800;
    color: #1f2937;
}

.resource-type {
    font-size: 15px;
    font-weight: 700;
    color: #2563eb;
}

.resource-desc {
    color: #4b5563;
    font-size: 16px;
}

.program-header {
    padding: 35px;
    border-radius: 28px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.20);
}

.program-header h1 {
    font-size: 44px;
    font-weight: 900;
    margin-bottom: 8px;
}

.program-header p {
    font-size: 19px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# BASE DE RECURSOS
# ============================================================

RECURSOS = [
    {
        "programa": "GREAT",
        "tipo": "Juego",
        "titulo": "Página de juegos virtuales Friv",
        "descripcion": "Enlace de ejemplo hacia una página externa de juegos virtuales.",
        "url": "https://www.friv.com/"
    },
    {
        "programa": "GREAT",
        "tipo": "Video",
        "titulo": "Video educativo de apoyo",
        "descripcion": "Video de YouTube agregado como ejemplo para el programa.",
        "url": "https://www.youtube.com/watch?v=NVBf1AgIjBQ"
    },
    {
        "programa": "GREAT",
        "tipo": "PDF",
        "titulo": "Material PDF del programa GREAT",
        "descripcion": "Aquí puedes colocar el enlace de un PDF oficial o guía metodológica.",
        "url": "https://www.great-online.org/"
    },

    {
        "programa": "MPAS",
        "tipo": "Juego",
        "titulo": "Juegos virtuales de apoyo",
        "descripcion": "Recurso interactivo externo para actividades educativas.",
        "url": "https://www.friv.com/"
    },
    {
        "programa": "MPAS",
        "tipo": "Video",
        "titulo": "Video educativo MPAS",
        "descripcion": "Video de apoyo para actividades preventivas.",
        "url": "https://www.youtube.com/watch?v=NVBf1AgIjBQ"
    },
    {
        "programa": "MPAS",
        "tipo": "PDF",
        "titulo": "Material informativo MPAS",
        "descripcion": "Espacio para agregar PDF, guía o documento institucional.",
        "url": "https://www.seguridadpublica.go.cr/"
    },

    {
        "programa": "DARE",
        "tipo": "Video",
        "titulo": "Video educativo YouTube",
        "descripcion": "Video agregado como ejemplo para el programa DARE.",
        "url": "https://www.youtube.com/watch?v=NVBf1AgIjBQ"
    },
    {
        "programa": "DARE",
        "tipo": "Juego",
        "titulo": "Juegos virtuales Friv",
        "descripcion": "Página externa de juegos interactivos.",
        "url": "https://www.friv.com/"
    },
    {
        "programa": "DARE",
        "tipo": "PDF",
        "titulo": "Material PDF DARE",
        "descripcion": "Espacio para enlazar material informativo del programa.",
        "url": "https://dare.org/"
    },

    {
        "programa": "PSCC",
        "tipo": "Video",
        "titulo": "Video comunitario de prevención",
        "descripcion": "Video de ejemplo para actividades comunitarias.",
        "url": "https://www.youtube.com/watch?v=NVBf1AgIjBQ"
    },
    {
        "programa": "PSCC",
        "tipo": "Juego",
        "titulo": "Juegos virtuales comunitarios",
        "descripcion": "Página externa de juegos para actividades recreativas.",
        "url": "https://www.friv.com/"
    },
    {
        "programa": "PSCC",
        "tipo": "PDF",
        "titulo": "Material de Seguridad Comunitaria",
        "descripcion": "Enlace de referencia para material comunitario.",
        "url": "https://www.seguridadpublica.go.cr/"
    },

    {
        "programa": "VIF",
        "tipo": "Video",
        "titulo": "Video de sensibilización",
        "descripcion": "Video de apoyo para prevención y sensibilización.",
        "url": "https://www.youtube.com/watch?v=NVBf1AgIjBQ"
    },
    {
        "programa": "VIF",
        "tipo": "Juego",
        "titulo": "Actividad virtual de apoyo",
        "descripcion": "Página externa de juegos para dinámicas educativas.",
        "url": "https://www.friv.com/"
    },
    {
        "programa": "VIF",
        "tipo": "PDF",
        "titulo": "Material informativo VIF",
        "descripcion": "Espacio para enlazar PDF o guía sobre prevención de violencia intrafamiliar.",
        "url": "https://www.seguridadpublica.go.cr/"
    },
]

PROGRAMAS = {
    "GREAT": {
        "emoji": "🌟",
        "clase": "great",
        "descripcion": "Recursos, actividades, videos y herramientas preventivas para jóvenes."
    },
    "MPAS": {
        "emoji": "🛡️",
        "clase": "mpas",
        "descripcion": "Materiales de apoyo preventivo, actividades educativas y recursos digitales."
    },
    "DARE": {
        "emoji": "🎓",
        "clase": "dare",
        "descripcion": "Videos, dinámicas, juegos y material formativo para prevención."
    },
    "PSCC": {
        "emoji": "🤝",
        "clase": "pscc",
        "descripcion": "Herramientas comunitarias, seguridad ciudadana y recursos de apoyo."
    },
    "VIF": {
        "emoji": "🏠",
        "clase": "vif",
        "descripcion": "Material para prevención, sensibilización y orientación en violencia intrafamiliar."
    },
}

# ============================================================
# FUNCIONES
# ============================================================

def seleccionar_programa(nombre_programa):
    st.session_state["programa_seleccionado"] = nombre_programa
    st.rerun()


def volver_inicio():
    st.session_state["programa_seleccionado"] = None
    st.rerun()


def obtener_icono_tipo(tipo):
    if tipo == "Video":
        return "🎥"
    if tipo == "Juego":
        return "🎮"
    if tipo == "PDF":
        return "📄"
    if tipo == "Presentación":
        return "📊"
    if tipo == "Actividad":
        return "🧩"
    return "🔗"


def mostrar_tarjeta(programa):
    datos = PROGRAMAS[programa]

    st.markdown(f"""
    <div class="card {datos["clase"]}">
        <h2>{datos["emoji"]} {programa}</h2>
        <p>{datos["descripcion"]}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(f"Entrar a {programa}", key=f"btn_{programa}", use_container_width=True):
        seleccionar_programa(programa)


def mostrar_menu_principal():
    st.markdown('<div class="main-title">🧰 Caja de Herramientas</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Programas Preventivos Policiales</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-box">
    Esta caja de herramientas permite centralizar materiales digitales de los programas preventivos policiales:
    videos, juegos virtuales, documentos PDF, guías, presentaciones y recursos externos.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        mostrar_tarjeta("GREAT")

    with col2:
        mostrar_tarjeta("MPAS")

    with col3:
        mostrar_tarjeta("DARE")

    col4, col5 = st.columns(2)

    with col4:
        mostrar_tarjeta("PSCC")

    with col5:
        mostrar_tarjeta("VIF")

    st.markdown("---")
    st.caption("Caja de Herramientas Digital | Programas Preventivos Policiales")


def mostrar_pagina_programa(programa):
    datos = PROGRAMAS[programa]

    if st.button("⬅️ Volver a la caja de herramientas", use_container_width=True):
        volver_inicio()

    st.markdown(f"""
    <div class="program-header {datos["clase"]}">
        <h1>{datos["emoji"]} {programa}</h1>
        <p>{datos["descripcion"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-box">
    <b>Carpeta del programa:</b> {programa}<br>
    Aquí se muestran únicamente los recursos relacionados con este programa:
    videos, juegos virtuales, documentos PDF, guías, actividades y enlaces externos.
    </div>
    """, unsafe_allow_html=True)

    recursos_filtrados = [
        recurso for recurso in RECURSOS
        if recurso["programa"] == programa
    ]

    filtro_tipo = st.selectbox(
        "Filtrar por tipo de recurso",
        ["Todos", "Video", "Juego", "PDF", "Presentación", "Actividad", "Enlace"],
        key=f"filtro_{programa}"
    )

    if filtro_tipo != "Todos":
        recursos_filtrados = [
            recurso for recurso in recursos_filtrados
            if recurso["tipo"] == filtro_tipo
        ]

    if not recursos_filtrados:
        st.warning("No hay recursos registrados para este filtro.")
        return

    for recurso in recursos_filtrados:
        icono = obtener_icono_tipo(recurso["tipo"])

        st.markdown(f"""
        <div class="resource-card">
            <div class="resource-type">{icono} {recurso["tipo"]}</div>
            <div class="resource-title">{recurso["titulo"]}</div>
            <div class="resource-desc">{recurso["descripcion"]}</div>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            f"{icono} Abrir recurso",
            recurso["url"],
            use_container_width=True
        )


# ============================================================
# CONTROL DE NAVEGACIÓN
# ============================================================

if "programa_seleccionado" not in st.session_state:
    st.session_state["programa_seleccionado"] = None

programa_actual = st.session_state["programa_seleccionado"]

if programa_actual:
    mostrar_pagina_programa(programa_actual)
else:
    mostrar_menu_principal()






