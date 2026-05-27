import streamlit as st

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Caja de Herramientas Preventiva Policial",
    page_icon="🧰",
    layout="wide"
)

# ============================================================
# ESTILOS CSS
# ============================================================

st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

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

.info-box {
    background: #e0f2fe;
    padding: 18px;
    border-radius: 15px;
    border-left: 6px solid #0284c7;
    margin-bottom: 25px;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# BASE DE RECURSOS
# Aquí puedes agregar videos, juegos, PDF, presentaciones, etc.
# ============================================================

RECURSOS = [
    # GREAT
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

    # MPAS
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

    # DARE
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

    # PSCC
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

    # VIF
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


# ============================================================
# FUNCIONES
# ============================================================

def seleccionar_programa(nombre_programa):
    st.session_state["programa_seleccionado"] = nombre_programa


def mostrar_tarjeta(programa, emoji, descripcion, clase_css, boton_key):
    st.markdown(f"""
    <div class="card {clase_css}">
        <h2>{emoji} {programa}</h2>
        <p>{descripcion}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(f"Entrar a {programa}", key=boton_key, use_container_width=True):
        seleccionar_programa(programa)


def obtener_icono_tipo(tipo):
    if tipo == "Video":
        return "🎥"
    elif tipo == "Juego":
        return "🎮"
    elif tipo == "PDF":
        return "📄"
    elif tipo == "Presentación":
        return "📊"
    elif tipo == "Actividad":
        return "🧩"
    else:
        return "🔗"


def mostrar_recursos(programa):
    recursos_filtrados = [
        recurso for recurso in RECURSOS
        if recurso["programa"] == programa
    ]

    st.markdown("---")
    st.header(f"📁 Recursos disponibles para {programa}")

    st.markdown(f"""
    <div class="info-box">
        <b>Programa seleccionado:</b> {programa}<br>
        Desde esta sección puedes abrir videos, juegos virtuales, PDF, guías, actividades o enlaces externos.
    </div>
    """, unsafe_allow_html=True)

    if not recursos_filtrados:
        st.warning("No hay recursos registrados para este programa.")
        return

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

    for i, recurso in enumerate(recursos_filtrados):
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
# INTERFAZ PRINCIPAL
# ============================================================

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

# ============================================================
# TARJETAS DE PROGRAMAS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    mostrar_tarjeta(
        "GREAT",
        "🌟",
        "Recursos, actividades, videos y herramientas preventivas para jóvenes.",
        "great",
        "btn_great"
    )

with col2:
    mostrar_tarjeta(
        "MPAS",
        "🛡️",
        "Materiales de apoyo preventivo, actividades educativas y recursos digitales.",
        "mpas",
        "btn_mpas"
    )

with col3:
    mostrar_tarjeta(
        "DARE",
        "🎓",
        "Videos, dinámicas, juegos y material formativo para prevención.",
        "dare",
        "btn_dare"
    )

col4, col5 = st.columns(2)

with col4:
    mostrar_tarjeta(
        "PSCC",
        "🤝",
        "Herramientas comunitarias, seguridad ciudadana y recursos de apoyo.",
        "pscc",
        "btn_pscc"
    )

with col5:
    mostrar_tarjeta(
        "VIF",
        "🏠",
        "Material para prevención, sensibilización y orientación en violencia intrafamiliar.",
        "vif",
        "btn_vif"
    )

# ============================================================
# MOSTRAR RECURSOS DEL PROGRAMA SELECCIONADO
# ============================================================

programa_actual = st.session_state.get("programa_seleccionado")

if programa_actual:
    mostrar_recursos(programa_actual)

# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown("---")
st.caption("Caja de Herramientas Digital | Programas Preventivos Policiales")








