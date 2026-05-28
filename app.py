import streamlit as st

st.set_page_config(
    page_title="Caja de Herramientas Digital",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

LINK_VIF = "https://drive.google.com/drive/folders/1KNIbV3Rts_McZja4S5johnYgjmx6165u?usp=drive_link"

SUBCARPETAS_VIF = [
    ("📁 Taller Básico VIF Funcionarios(as) Policiales", "https://drive.google.com/drive/folders/1DZpMMwG_lstXLiqQ569TZZY9zr_Ozh-L?usp=drive_link"),
    ("📁 SEGVIF", "https://drive.google.com/drive/folders/1j3nIHHCXnCdzTW1pYmaxNjHXDsOjrpUm?usp=drive_link"),
    ("📁 Protocolos MEP", "https://drive.google.com/drive/folders/1ttKiViOQPxbL2nWvatvo7PzjlGqUWaQw?usp=drive_link"),
    ("📁 Presentaciones Metodologías para Aplicar", "https://drive.google.com/drive/folders/1akHd5RATU1og2aBWgyY5JyCUAiSlRCUE?usp=drive_link"),
    ("📁 Política PLANOVI", "https://drive.google.com/drive/folders/1SyseXo-i4Ho9ZteeJRtw3O-8qXF5J_n5?usp=drive_link"),
    ("📁 Política Niñez y Adolescencia", "https://drive.google.com/drive/folders/1qHA99zNANcn2PMBi_sMiVe02PF_EPH2z?usp=drive_link"),
    ("📁 Política CONATT", "https://drive.google.com/drive/folders/1RrphoEjdnTV67rBMewthM4SHI2WqdV7k?usp=drive_link"),
    ("📁 Matrices de Reporte", "https://drive.google.com/drive/folders/1t_XZKyl25HBq3tkhV452VZOUYdJXNcux?usp=drive_link"),
    ("📁 Justicia Restaurativa", "https://drive.google.com/drive/folders/16V3-Bu_ZHNu3zKPCpqPe-ByJv0cARdkC?usp=drive_link"),
    ("📁 Eje 6 PLANOVI Prevención del Femicidio", "https://drive.google.com/drive/folders/1fdXk5buZ8ukUWABK6V4COLVygQ_BVTz7?usp=drive_link"),
    ("📁 Eje 5 PLANOVI Prevención, Atención Integral y No Revictimización", "https://drive.google.com/drive/folders/1rdTVYqWEG34UsdZa2LIPlITYy8cy-VPP?usp=drive_link"),
    ("📁 Eje 4 PLANOVI Debida Diligencia", "https://drive.google.com/drive/folders/1lu-CgdZhtiwA4I3DB72lAaONuh-CMmFe?usp=drive_link"),
    ("📁 Eje 2 PLANOVI Masculinidad por la Igualdad", "https://drive.google.com/drive/folders/1n88toL-H_NBvBiq9YGp2B-yzNbtPX3Qj?usp=drive_link"),
    ("📁 Eje 1 PLANOVI Cultura No Machista", "https://drive.google.com/drive/folders/1KWbagUN-KG89gKehBMHTpANrs1MMx9WT?usp=drive_link"),
    ("📁 Circulares Directrices", "https://drive.google.com/drive/folders/1EJN92ytdvWg_qvhF5IbdyzcSKhsvyjsp?usp=drive_link"),
    ("📁 Caracterización Programa VIF, Manual Puestos, Redes VIF y Subsistemas", "https://drive.google.com/drive/folders/1tX4ZUZicJFu7cnqNYW1uJMK5V_SWKyK7?usp=drive_link"),
]

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

.module-card {
    border-radius: 28px;
    padding: 28px;
    min-height: 230px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    margin-bottom: 15px;
}

.module-card * {
    color: white !important;
}

.module-card h2 {
    font-size: 36px !important;
    margin-bottom: 10px;
}

.module-card p {
    font-size: 18px !important;
    line-height: 1.5;
}

.vif { background: linear-gradient(135deg,#dc2626,#f97316); }
.dare { background: linear-gradient(135deg,#2563eb,#0891b2); }
.great { background: linear-gradient(135deg,#16a34a,#22c55e); }
.juegos { background: linear-gradient(135deg,#7c3aed,#a855f7); }

.folder-card {
    background: white !important;
    border-radius: 22px;
    padding: 22px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    min-height: 145px;
}

.folder-card h3 {
    color: #0f172a !important;
    font-size: 22px !important;
}

.folder-card p {
    color: #475569 !important;
    font-size: 15px !important;
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

@media (max-width: 768px){
    .main-title{
        font-size:36px !important;
    }

    .main-subtitle{
        font-size:16px !important;
    }

    .module-card{
        min-height:170px !important;
        padding:22px !important;
    }

    .module-card h2{
        font-size:28px !important;
    }

    .folder-card{
        min-height:auto !important;
    }
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🧰 Caja Digital")
    st.write("Programas Preventivos Policiales")
    st.link_button("📁 Abrir carpeta principal VIF", LINK_VIF, use_container_width=True)

if "modulo" not in st.session_state:
    st.session_state.modulo = "inicio"

if st.session_state.modulo == "inicio":

    st.markdown('<div class="main-title">Caja de Herramientas Digital</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="main-subtitle">Seleccione un programa para acceder a recursos, documentos, videos y materiales institucionales.</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="module-card vif">
            <h2>🛡️ VIF</h2>
            <p>Violencia Intrafamiliar, PLANOVI, redes locales, protocolos, guías, videos y documentación institucional.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ingresar a VIF", use_container_width=True):
            st.session_state.modulo = "vif"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="module-card dare">
            <h2>👮 DARE</h2>
            <p>Programas preventivos, materiales educativos, presentaciones y recursos de prevención.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Próximamente", disabled=True, use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("""
        <div class="module-card great">
            <h2>🧠 GREAT</h2>
            <p>Materiales de intervención preventiva, liderazgo juvenil y fortalecimiento comunitario.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Próximamente ", disabled=True, use_container_width=True)

    with c4:
        st.markdown("""
        <div class="module-card juegos">
            <h2>🎮 Juegos y Recursos</h2>
            <p>Herramientas digitales, dinámicas, juegos virtuales y materiales interactivos.</p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Próximamente  ", disabled=True, use_container_width=True)

elif st.session_state.modulo == "vif":

    st.markdown('<div class="main-title">🛡️ Programa VIF</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>Biblioteca digital institucional VIF</h3>
        <p>
        Acceso a carpetas y subcarpetas del Programa VIF PLANOVI-CONATT:
        manuales, protocolos, matrices, políticas, ejes PLANOVI, SEGVIF,
        talleres, directrices y material metodológico.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "📁 Abrir carpeta principal ACCIONES PROGRAMA VIF PLANOVI-CONATT",
        LINK_VIF,
        use_container_width=True
    )

    st.divider()

    st.subheader("📂 Subcarpetas disponibles")

    cols = st.columns(2)

    for i, (nombre, link) in enumerate(SUBCARPETAS_VIF):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="folder-card">
                <h3>{nombre}</h3>
                <p>Acceso directo a documentos, recursos y materiales disponibles en esta subcarpeta.</p>
            </div>
            """, unsafe_allow_html=True)

            st.link_button(
                "Abrir carpeta",
                link,
                use_container_width=True
            )

    st.divider()

    if st.button("⬅️ Volver al inicio", use_container_width=True):
        st.session_state.modulo = "inicio"
        st.rerun()
