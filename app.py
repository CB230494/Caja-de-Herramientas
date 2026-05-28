import streamlit as st

st.set_page_config(
    page_title="Caja de Herramientas Digital",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LINKS DRIVE
# =========================================================

LINK_VIF = "https://drive.google.com/drive/folders/1KNIbV3Rts_McZja4S5johnYgjmx6165u"

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

:root, html, body, .stApp {
    background: #f3f6fb !important;
    color: #111827 !important;
    color-scheme: light !important;
}

* {
    color-scheme: light !important;
}

h1,h2,h3,h4,h5,h6,p,span,label,div {
    color: #111827 !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.main-title {
    font-size: 52px;
    font-weight: 900;
    color: #0f172a !important;
    margin-bottom: 8px;
}

.main-subtitle {
    font-size: 18px;
    color: #475569 !important;
    margin-bottom: 30px;
}

.card {
    background: white !important;
    border-radius: 24px;
    padding: 24px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.card * {
    color: #111827 !important;
}

.module-card {
    border-radius: 28px;
    padding: 28px;
    min-height: 240px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

.module-card * {
    color: white !important;
}

.module-card h2 {
    font-size: 34px !important;
    margin-bottom: 10px;
}

.module-card p {
    font-size: 18px !important;
    line-height: 1.5;
}

.vif {
    background: linear-gradient(135deg,#dc2626,#f97316);
}

.dare {
    background: linear-gradient(135deg,#2563eb,#0891b2);
}

.great {
    background: linear-gradient(135deg,#16a34a,#22c55e);
}

.juegos {
    background: linear-gradient(135deg,#7c3aed,#a855f7);
}

.sidebar-card {
    background: rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 16px;
}

.sidebar-card * {
    color: white !important;
}

.stButton > button {
    width: 100% !important;
    min-height: 50px !important;
    border-radius: 16px !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg,#1d4ed8,#2563eb) !important;
    color: white !important;
    border: none !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg,#1e40af,#1d4ed8) !important;
    color: white !important;
}

.stLinkButton > a {
    width: 100% !important;
    min-height: 50px !important;
    border-radius: 16px !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg,#16a34a,#22c55e) !important;
    color: white !important;
    border: none !important;
    text-align: center !important;
}

.folder-card {
    background: white !important;
    border-radius: 22px;
    padding: 22px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.folder-card h3 {
    color: #0f172a !important;
}

.folder-card p {
    color: #475569 !important;
}

.info-box {
    background: #eff6ff !important;
    border-left: 8px solid #2563eb;
    border-radius: 18px;
    padding: 20px;
    margin-bottom: 25px;
}

.info-box * {
    color: #1e3a8a !important;
}

@media (max-width: 768px){

    .main-title{
        font-size:38px !important;
    }

    .module-card{
        min-height:180px !important;
        padding:22px !important;
    }

    .module-card h2{
        font-size:28px !important;
    }

    .module-card p{
        font-size:16px !important;
    }

}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("🧰 Caja Digital")

    st.markdown("""
    <div class="sidebar-card">
        <h3>Biblioteca institucional</h3>
        <p>Acceso rápido a herramientas, programas, guías y materiales digitales.</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📁 Abrir Drive VIF",
        LINK_VIF,
        use_container_width=True
    )

# =========================================================
# SESSION
# =========================================================

if "modulo" not in st.session_state:
    st.session_state.modulo = "inicio"

# =========================================================
# INICIO
# =========================================================

if st.session_state.modulo == "inicio":

    st.markdown(
        '<div class="main-title">Caja de Herramientas Digital</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-subtitle">Seleccione un programa para acceder a recursos, documentos, videos y materiales institucionales.</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
        <div class="module-card vif">
            <div>
                <h2>🛡️ VIF</h2>
                <p>Violencia Intrafamiliar, PLANOVI, redes locales, protocolos, guías, videos y documentación institucional.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ingresar a VIF", use_container_width=True):
            st.session_state.modulo = "vif"
            st.rerun()

    with c2:

        st.markdown("""
        <div class="module-card dare">
            <div>
                <h2>👮 DARE</h2>
                <p>Programas preventivos, materiales educativos, presentaciones y recursos de prevención.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.button("Próximamente", disabled=True, use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:

        st.markdown("""
        <div class="module-card great">
            <div>
                <h2>🧠 GREAT</h2>
                <p>Materiales de intervención preventiva, liderazgo juvenil y fortalecimiento comunitario.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.button("Próximamente ", disabled=True, use_container_width=True)

    with c4:

        st.markdown("""
        <div class="module-card juegos">
            <div>
                <h2>🎮 Juegos y Recursos</h2>
                <p>Herramientas digitales, dinámicas, juegos virtuales y materiales interactivos.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.button("Próximamente  ", disabled=True, use_container_width=True)

# =========================================================
# VIF
# =========================================================

elif st.session_state.modulo == "vif":

    st.markdown("""
    <div class="main-title">🛡️ Programa VIF</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Biblioteca digital institucional</h3>
        <p>
        Acceda a documentos, manuales, protocolos, ejes PLANOVI,
        guías metodológicas y recursos relacionados al programa VIF.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📁 Abrir carpeta principal VIF PLANOVI-CONATT",
        LINK_VIF,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # REDES VIF
    # =====================================================

    st.markdown("""
    <div class="folder-card">
        <h3>📂 Redes VIF y Marco Institucional</h3>
        <p>
        Contiene manuales, directorios institucionales,
        guías metodológicas, políticas públicas y documentación
        de funcionamiento de redes locales VIF.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📁 Abrir carpeta Redes VIF y Marco Institucional",
        LINK_VIF,
        use_container_width=True
    )

    # =====================================================
    # EJES
    # =====================================================

    st.markdown("""
    <div class="folder-card">
        <h3>📂 Eje 1 PLANOVI Cultura No Machista</h3>
        <p>
        Recursos relacionados a cultura preventiva,
        sensibilización y educación.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Eje 1",
        LINK_VIF,
        use_container_width=True
    )

    st.markdown("""
    <div class="folder-card">
        <h3>📂 Eje 2 PLANOVI Masculinidad por la Igualdad</h3>
        <p>
        Materiales relacionados a masculinidades positivas
        y prevención de violencia.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Eje 2",
        LINK_VIF,
        use_container_width=True
    )

    st.markdown("""
    <div class="folder-card">
        <h3>📂 Eje 4 PLANOVI Debida Diligencia</h3>
        <p>
        Protocolos, procedimientos institucionales y
        documentación operativa.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Eje 4",
        LINK_VIF,
        use_container_width=True
    )

    st.markdown("""
    <div class="folder-card">
        <h3>📂 Eje 5 PLANOVI Prevención y Atención Integral</h3>
        <p>
        Recursos de atención, prevención y coordinación
        interinstitucional.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Eje 5",
        LINK_VIF,
        use_container_width=True
    )

    st.markdown("""
    <div class="folder-card">
        <h3>📂 Eje 6 PLANOVI Prevención del Femicidio</h3>
        <p>
        Materiales de prevención, intervención y análisis
        relacionados al femicidio.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Eje 6",
        LINK_VIF,
        use_container_width=True
    )

    # =====================================================
    # RECURSOS EXTRA
    # =====================================================

    st.markdown("""
    <div class="folder-card">
        <h3>🎥 Videos y Multimedia</h3>
        <p>
        Videos educativos, material audiovisual,
        capacitaciones y contenido multimedia.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Videos",
        LINK_VIF,
        use_container_width=True
    )

    st.markdown("""
    <div class="folder-card">
        <h3>🎮 Juegos y Actividades Interactivas</h3>
        <p>
        Herramientas digitales y dinámicas para
        actividades preventivas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Juegos",
        LINK_VIF,
        use_container_width=True
    )

    st.markdown("""
    <div class="folder-card">
        <h3>📚 Protocolos y Guías</h3>
        <p>
        Protocolos institucionales, lineamientos y
        documentación oficial.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "Abrir Protocolos",
        LINK_VIF,
        use_container_width=True
    )

    st.divider()

    if st.button("⬅️ Volver al inicio", use_container_width=True):
        st.session_state.modulo = "inicio"
        st.rerun()
