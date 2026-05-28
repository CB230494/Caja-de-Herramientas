import streamlit as st

st.set_page_config(
    page_title="Caja de Herramientas Digital",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

LINK_VIF = "https://drive.google.com/drive/folders/1KNIbV3Rts_McZja4S5johnYgjmx6165u?usp=drive_link"

SUBCARPETAS_VIF = [
    ("🧑‍🏫 Taller Básico VIF Funcionarios(as) Policiales", "Talleres y material formativo para funcionarios policiales.", "taller", "https://drive.google.com/drive/folders/1DZpMMwG_lstXLiqQ569TZZY9zr_Ozh-L?usp=drive_link"),
    ("💻 SEGVIF", "Herramientas, matrices, guías y presentaciones relacionadas con SEGVIF.", "segvif", "https://drive.google.com/drive/folders/1j3nIHHCXnCdzTW1pYmaxNjHXDsOjrpUm?usp=drive_link"),
    ("🏫 Protocolos MEP", "Protocolos y lineamientos relacionados con el Ministerio de Educación Pública.", "mep", "https://drive.google.com/drive/folders/1ttKiViOQPxbL2nWvatvo7PzjlGqUWaQw?usp=drive_link"),
    ("📊 Presentaciones Metodologías para Aplicar", "Presentaciones, metodologías y recursos de aplicación práctica.", "presentaciones", "https://drive.google.com/drive/folders/1akHd5RATU1og2aBWgyY5JyCUAiSlRCUE?usp=drive_link"),
    ("📘 Política PLANOVI", "Documentación relacionada con la Política PLANOVI.", "planovi", "https://drive.google.com/drive/folders/1SyseXo-i4Ho9ZteeJRtw3O-8qXF5J_n5?usp=drive_link"),
    ("👧 Política Niñez y Adolescencia", "Política Nacional de Niñez y Adolescencia y documentos asociados.", "ninez", "https://drive.google.com/drive/folders/1qHA99zNANcn2PMBi_sMiVe02PF_EPH2z?usp=drive_link"),
    ("🚨 Política CONATT", "Material vinculado con CONATT, trata y tráfico ilícito de personas.", "conatt", "https://drive.google.com/drive/folders/1RrphoEjdnTV67rBMewthM4SHI2WqdV7k?usp=drive_link"),
    ("🧾 Matrices de Reporte", "Matrices, formatos y herramientas para reporte institucional.", "matrices", "https://drive.google.com/drive/folders/1t_XZKyl25HBq3tkhV452VZOUYdJXNcux?usp=drive_link"),
    ("⚖️ Justicia Restaurativa", "Material relacionado con justicia restaurativa y procesos asociados.", "justicia", "https://drive.google.com/drive/folders/16V3-Bu_ZHNu3zKPCpqPe-ByJv0cARdkC?usp=drive_link"),
    ("🟣 Eje 6 PLANOVI Prevención del Femicidio", "Material de prevención, abordaje y análisis relacionado con femicidio.", "eje6", "https://drive.google.com/drive/folders/1fdXk5buZ8ukUWABK6V4COLVygQ_BVTz7?usp=drive_link"),
    ("🟠 Eje 5 PLANOVI Prevención, Atención Integral y No Revictimización", "Recursos para prevención, atención integral y no revictimización.", "eje5", "https://drive.google.com/drive/folders/1rdTVYqWEG34UsdZa2LIPlITYy8cy-VPP?usp=drive_link"),
    ("🔵 Eje 4 PLANOVI Debida Diligencia", "Protocolos, procedimientos y acciones vinculadas con debida diligencia.", "eje4", "https://drive.google.com/drive/folders/1lu-CgdZhtiwA4I3DB72lAaONuh-CMmFe?usp=drive_link"),
    ("🟢 Eje 2 PLANOVI Masculinidad por la Igualdad", "Material sobre masculinidades positivas e igualdad.", "eje2", "https://drive.google.com/drive/folders/1n88toL-H_NBvBiq9YGp2B-yzNbtPX3Qj?usp=drive_link"),
    ("🔴 Eje 1 PLANOVI Cultura No Machista", "Recursos de sensibilización, cultura no machista y prevención.", "eje1", "https://drive.google.com/drive/folders/1KWbagUN-KG89gKehBMHTpANrs1MMx9WT?usp=drive_link"),
    ("📢 Circulares Directrices", "Circulares, directrices y comunicaciones oficiales.", "circulares", "https://drive.google.com/drive/folders/1EJN92ytdvWg_qvhF5IbdyzcSKhsvyjsp?usp=drive_link"),
    ("📚 Caracterización Programa VIF, Manual Puestos, Redes VIF y Subsistemas", "Manual, caracterización del programa, redes VIF y subsistemas.", "caracterizacion", "https://drive.google.com/drive/folders/1tX4ZUZicJFu7cnqNYW1uJMK5V_SWKyK7?usp=drive_link"),
]

ARCHIVOS_VIF = {
    "🧑‍🏫 Taller Básico VIF Funcionarios(as) Policiales": [
        ("📄 PLAN DE LECCION TALLER METODOLOGICO VIF 2025 SENTIR PENSAR (Octubre).pdf", "PDF", "https://drive.google.com/file/d/13e-XYfEkNAiNnWmnYcWvXeLfhd58xXOb/view?usp=drive_link"),
        ("📝 PLAN DE LECCION CLASES ANP INTERVENCION POLICIAL SITUACIONES VIOLENCIA INTRAFAMILIAR, 03 DICIEMBRE 2025.docx", "Word", "https://docs.google.com/document/d/1pvQvCZZISBIf3ChMNErnzXnCwo2OxXEw/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📄 Modulo para sentir, pensar y enfrentar la violencia intrafamiliar.pdf", "PDF", "https://drive.google.com/file/d/1eMims6rzPSzrNhBIosuFERs-CXtHJJUM/view?usp=drive_link"),
        ("📄 INTERVENCION POLICIAL EN SITUACIONES DE CRISIS POR VIOLENCIA INTRAFAMILIAR Y ABUSO SEXUAL.pdf", "PDF", "https://drive.google.com/file/d/15w8ueZJzY9ZUlM54tl2r94ynu3PTC6-l/view?usp=drive_link"),
        ("📊 DIA 05 EL PROCESO DE VIOLENCIA DOMÉSTICA PODER JUDICIAL.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1sP_IUv9o0TJoCb_4aVPQvbjKqjEHdKwx/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📊 DÍA 04 PROTOCOLO DE INTERVENCIÓN POLICIAL 2025.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1Ke0IXBeYQ5-ab9gKQNuTNZEN1sacyTKL/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📊 DÍA 04 PROTOCOLO DE INTERVENCIÓN POLICIAL 2025", "Presentación", "https://docs.google.com/presentation/d/1K72UcTQ9avSihXuPlljc0t2lQ9vGGsOq-Oc0SaleMqU/edit?usp=drive_link"),
        ("📊 DIA 04 PROTOCOLO 72 HORAS ERRVV General 2024.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1vPu7oXdqVf8Eok5HlvVS7erz90rg-P52/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📊 DIA 04 PRESENTACION INTERVENCIÓN EN CRISIS.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1SkfHSvBQ4SSdTpCn1DjfbR7kEUS0niua/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📊 DIA 04 ABC de los Primeros Auxilios Emocionales.ppt", "PowerPoint", "https://docs.google.com/presentation/d/1X6UYnMaIAbGCmeuroWOpU5MMXM-TMIr6/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📊 DIA 02 PRESENTACIÓN DERECHOS HUMANOS.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1t7O9wxizuv9GGopZz_868REzogr4sBdo/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📊 DIA 1 PLANOVI.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1WeQcudvv-ccUVeM8kefOvASeGWWKhT34/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📊 DIA 1 Ley y Sistema Presentación 8688.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1JokNYyPxUky2_p3Ek4ELEM74nZOA3ihd/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
    ],
    "💻 SEGVIF": [
        ("📊 TABLA EXCEL REPORTE SEGVIF 2025.xlsx", "Excel", "https://docs.google.com/spreadsheets/d/16vGfeAnVYXCpkAkAqRgDzSsPTGW_UybY/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
        ("📄 INSTRUCTIVO HERRAMIENTA SEGVIF 2020.pdf", "PDF", "https://drive.google.com/file/d/1BqiGiO2MxbxTN0mSe2tGNbjYOxa3YHVA/view?usp=sharing"),
        ("📊 Herramienta de Seguimientos SEVIF 2020 FINAL.pptx", "PowerPoint", "https://docs.google.com/presentation/d/1msGXbDyDkg0xdNppY7rLUSw7_edvHeMu/edit?usp=drive_link&ouid=110050131819372397900&rtpof=true&sd=true"),
    ],
}

st.markdown("""
<style>
:root, html, body, .stApp {
    background: #f3f6fb !important;
    color: #111827 !important;
    color-scheme: light !important;
}
* { color-scheme: light !important; }
h1,h2,h3,h4,h5,h6,p,span,label,div { color: #111827 !important; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
}
[data-testid="stSidebar"] * { color: white !important; }

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 900;
    color: #0f172a !important;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #475569 !important;
    margin-bottom: 30px;
}
.info-box {
    background: #e0f2fe !important;
    padding: 20px;
    border-radius: 18px;
    border-left: 7px solid #0284c7;
    margin-bottom: 25px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.08);
}
.info-box * { color: #1f2937 !important; }

.card {
    padding: 28px;
    border-radius: 25px;
    color: white !important;
    min-height: 230px;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.20);
    transition: transform 0.2s ease-in-out;
    margin-bottom: 15px;
}
.card:hover { transform: scale(1.03); }
.card * { color: white !important; }
.card h2 {
    font-size: 32px;
    font-weight: 900;
    margin-bottom: 10px;
}
.card p {
    font-size: 17px;
    line-height: 1.4;
}

.great { background: linear-gradient(135deg, #ff7b00, #ffb703); }
.mpas { background: linear-gradient(135deg, #0077b6, #00b4d8); }
.dare { background: linear-gradient(135deg, #7209b7, #c77dff); }
.pscc { background: linear-gradient(135deg, #06d6a0, #118ab2); }
.vif { background: linear-gradient(135deg, #ef476f, #d62828); }

.program-header {
    padding: 35px;
    border-radius: 28px;
    color: white !important;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.20);
}
.program-header * { color: white !important; }
.program-header h1 {
    font-size: 44px;
    font-weight: 900;
    margin-bottom: 8px;
}
.program-header p { font-size: 19px; }

.folder-card {
    padding: 24px;
    border-radius: 24px;
    color: white !important;
    min-height: 190px;
    box-shadow: 0px 10px 24px rgba(0,0,0,0.18);
    margin-bottom: 14px;
    transition: transform 0.2s ease-in-out;
}
.folder-card:hover { transform: scale(1.02); }
.folder-card * { color: white !important; }
.folder-card h3 {
    font-size: 22px;
    font-weight: 900;
    margin-bottom: 10px;
}
.folder-card p {
    font-size: 15px;
    line-height: 1.35;
}

.file-card {
    background: #ffffff !important;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    min-height: 130px;
}
.file-card * { color: #111827 !important; }
.file-card h3 {
    font-size: 18px !important;
    font-weight: 900 !important;
    line-height: 1.3;
}
.file-type {
    display: inline-block;
    background: #e0f2fe;
    color: #075985 !important;
    font-weight: 900;
    padding: 6px 12px;
    border-radius: 999px;
    margin-top: 6px;
}

.taller { background: linear-gradient(135deg, #f97316, #fb923c); }
.segvif { background: linear-gradient(135deg, #2563eb, #06b6d4); }
.mep { background: linear-gradient(135deg, #7c3aed, #a855f7); }
.presentaciones { background: linear-gradient(135deg, #16a34a, #22c55e); }
.planovi { background: linear-gradient(135deg, #dc2626, #f43f5e); }
.ninez { background: linear-gradient(135deg, #0891b2, #0ea5e9); }
.conatt { background: linear-gradient(135deg, #991b1b, #ef4444); }
.matrices { background: linear-gradient(135deg, #475569, #0f172a); }
.justicia { background: linear-gradient(135deg, #9333ea, #db2777); }
.eje6 { background: linear-gradient(135deg, #7e22ce, #a21caf); }
.eje5 { background: linear-gradient(135deg, #ea580c, #f97316); }
.eje4 { background: linear-gradient(135deg, #1d4ed8, #2563eb); }
.eje2 { background: linear-gradient(135deg, #15803d, #22c55e); }
.eje1 { background: linear-gradient(135deg, #be123c, #f43f5e); }
.circulares { background: linear-gradient(135deg, #0f766e, #14b8a6); }
.caracterizacion { background: linear-gradient(135deg, #1e293b, #334155); }

.stButton > button {
    width: 100% !important;
    min-height: 50px !important;
    border-radius: 16px !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg,#1d4ed8,#2563eb) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0px 6px 16px rgba(37,99,235,0.25);
}
.stButton > button:hover {
    background: linear-gradient(135deg,#1e40af,#1d4ed8) !important;
    color: white !important;
}
.stButton > button:disabled {
    background: linear-gradient(135deg,#64748b,#94a3b8) !important;
    color: white !important;
    opacity: 1 !important;
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
    box-shadow: 0px 6px 16px rgba(22,163,74,0.25);
}
.stLinkButton > a:hover {
    background: linear-gradient(135deg,#15803d,#16a34a) !important;
    color: white !important;
}
.sidebar-card {
    background: rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    margin-bottom: 16px;
}
.sidebar-card * { color: white !important; }

@media (max-width: 768px) {
    .main-title { font-size: 34px !important; }
    .subtitle { font-size: 16px !important; }
    .card {
        min-height: 185px !important;
        padding: 22px !important;
    }
    .card h2 { font-size: 28px !important; }
    .program-header h1 { font-size: 32px !important; }
    .folder-card {
        min-height: auto !important;
        padding: 20px !important;
    }
    .file-card { min-height: auto !important; }
}
</style>
""", unsafe_allow_html=True)

if "programa_seleccionado" not in st.session_state:
    st.session_state["programa_seleccionado"] = None

if "carpeta_vif" not in st.session_state:
    st.session_state["carpeta_vif"] = None

PROGRAMAS = {
    "GREAT": {"emoji": "🌟", "clase": "great", "descripcion": "Recursos, actividades, videos y herramientas preventivas para jóvenes.", "activo": False},
    "MPAS": {"emoji": "🛡️", "clase": "mpas", "descripcion": "Materiales de apoyo preventivo, actividades educativas y recursos digitales.", "activo": False},
    "DARE": {"emoji": "🎓", "clase": "dare", "descripcion": "Videos, dinámicas, juegos y material formativo para prevención.", "activo": False},
    "PSCC": {"emoji": "🤝", "clase": "pscc", "descripcion": "Herramientas comunitarias, seguridad ciudadana y recursos de apoyo.", "activo": False},
    "VIF": {"emoji": "🏠", "clase": "vif", "descripcion": "Material VIF, PLANOVI, CONATT, SEGVIF, redes locales, manuales y políticas públicas.", "activo": True},
}

def seleccionar_programa(nombre_programa):
    st.session_state["programa_seleccionado"] = nombre_programa
    st.session_state["carpeta_vif"] = None
    st.rerun()

def volver_inicio():
    st.session_state["programa_seleccionado"] = None
    st.session_state["carpeta_vif"] = None
    st.rerun()

def volver_vif():
    st.session_state["carpeta_vif"] = None
    st.rerun()

def mostrar_tarjeta_programa(programa):
    datos = PROGRAMAS[programa]
    st.markdown(f"""
    <div class="card {datos["clase"]}">
        <h2>{datos["emoji"]} {programa}</h2>
        <p>{datos["descripcion"]}</p>
    </div>
    """, unsafe_allow_html=True)

    if datos["activo"]:
        if st.button(f"Entrar a {programa}", key=f"btn_{programa}", use_container_width=True):
            seleccionar_programa(programa)
    else:
        st.button("Próximamente", key=f"btn_{programa}", disabled=True, use_container_width=True)

def mostrar_menu_principal():
    st.markdown('<div class="main-title">🧰 Caja de Herramientas Digital</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Programas Preventivos Policiales</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <b>Biblioteca digital institucional:</b><br>
        Acceso a materiales, documentos, guías, videos, enlaces, carpetas de trabajo
        y recursos de los programas preventivos policiales.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        mostrar_tarjeta_programa("GREAT")
    with col2:
        mostrar_tarjeta_programa("MPAS")
    with col3:
        mostrar_tarjeta_programa("DARE")

    col4, col5 = st.columns(2)
    with col4:
        mostrar_tarjeta_programa("PSCC")
    with col5:
        mostrar_tarjeta_programa("VIF")

def mostrar_archivos_carpeta(nombre_carpeta, link_carpeta):
    archivos = ARCHIVOS_VIF.get(nombre_carpeta, [])

    if st.button("⬅️ Volver a subcarpetas VIF", use_container_width=True):
        volver_vif()

    st.markdown(f"""
    <div class="program-header vif">
        <h1>{nombre_carpeta}</h1>
        <p>Archivos disponibles dentro de esta subcarpeta</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("📁 Abrir carpeta completa en Drive", link_carpeta, use_container_width=True)
    st.markdown("---")

    if not archivos:
        st.info("Esta subcarpeta todavía no tiene archivos cargados individualmente en la app. Puede abrir la carpeta completa en Drive.")
        return

    st.subheader("📌 Archivos cargados en la app")

    cols = st.columns(2)
    for i, (nombre, tipo, link) in enumerate(archivos):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="file-card">
                <h3>{nombre}</h3>
                <span class="file-type">{tipo}</span>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("Abrir archivo", link, use_container_width=True)

def mostrar_vif():
    carpeta_actual = st.session_state["carpeta_vif"]

    if carpeta_actual:
        mostrar_archivos_carpeta(carpeta_actual["nombre"], carpeta_actual["link"])
        return

    if st.button("⬅️ Volver a la caja de herramientas", use_container_width=True):
        volver_inicio()

    st.markdown("""
    <div class="program-header vif">
        <h1>🏠 VIF</h1>
        <p>Violencia Intrafamiliar | PLANOVI | CONATT | SEGVIF | Redes Locales</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <b>Carpeta principal:</b> ACCIONES PROGRAMA VIF PLANOVI-CONATT<br>
        Subcarpetas y materiales institucionales del Programa VIF:
        talleres, protocolos, matrices, políticas públicas, ejes PLANOVI, SEGVIF,
        directrices, manuales y recursos metodológicos.
    </div>
    """, unsafe_allow_html=True)

    st.link_button("📁 Abrir carpeta principal VIF PLANOVI-CONATT", LINK_VIF, use_container_width=True)

    st.markdown("---")
    st.subheader("📂 Subcarpetas disponibles")

    cols = st.columns(2)
    for i, (nombre, descripcion, clase, link) in enumerate(SUBCARPETAS_VIF):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="folder-card {clase}">
                <h3>{nombre}</h3>
                <p>{descripcion}</p>
            </div>
            """, unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("Ver archivos", key=f"ver_{i}", use_container_width=True):
                    st.session_state["carpeta_vif"] = {"nombre": nombre, "link": link}
                    st.rerun()
            with col_b:
                st.link_button("Abrir Drive", link, use_container_width=True)

with st.sidebar:
    st.title("🧰 Caja Digital")
    st.markdown("""
    <div class="sidebar-card">
        <h3>Programas Preventivos</h3>
        <p>Acceso rápido a la biblioteca digital institucional.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🏠 Inicio", use_container_width=True):
        volver_inicio()

    st.link_button("📁 Drive VIF", LINK_VIF, use_container_width=True)

programa_actual = st.session_state["programa_seleccionado"]

if programa_actual == "VIF":
    mostrar_vif()
else:
    mostrar_menu_principal()
