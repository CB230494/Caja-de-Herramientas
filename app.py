import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Caja de Herramientas - Programas Preventivos Policiales",
    page_icon="🧰",
    layout="wide"
)

PROGRAMAS = {
    "GREAT": {
        "icon": "🌟",
        "color1": "#FF7B00",
        "color2": "#FFD166",
        "descripcion": "Prevención de violencia, pandillas, presión de grupo y fortalecimiento de habilidades para la vida.",
        "recursos": [
            {"tipo": "🌐 Sitio oficial", "nombre": "G.R.E.A.T. Online", "url": "https://www.great-online.org/"},
            {"tipo": "📄 PDF", "nombre": "Presentación The G.R.E.A.T. Program", "url": "https://neglected-delinquent.ed.gov/sites/default/files/20100505_webinar201004cowan.pdf"},
            {"tipo": "📚 Información", "nombre": "National Gang Center - GREAT", "url": "https://www.nationalgangcenter.org/Strategies/GREAT"},
            {"tipo": "🎮 Juego virtual", "nombre": "Juegos de convivencia y ciudadanía", "url": "https://wordwall.net/es-cl/community/convivencia-y-ciudadan%C3%ADa"},
        ],
    },
    "MPAS": {
        "icon": "🛡️",
        "color1": "#00B4D8",
        "color2": "#0077B6",
        "descripcion": "Material preventivo para seguridad, convivencia, autoprotección y articulación comunitaria.",
        "recursos": [
            {"tipo": "📄 PDF", "nombre": "Manual de Seguridad Comunitaria", "url": "https://costaricaporsiempre.org/wp-content/uploads/2021/03/Manual-de-Seguridad-Comunitaria-1.pdf"},
            {"tipo": "📄 PDF", "nombre": "Policía Comunitaria en Costa Rica", "url": "https://multimedia.uned.ac.cr/ecsh/simposio-policiales-2023/wp-content/uploads/sites/34/2023/09/Policia-comunitaria-en-Costa-Rica.pdf"},
            {"tipo": "🎮 Juego virtual", "nombre": "Recursos de seguridad ciudadana", "url": "https://wordwall.net/es-pe/community/seguridad-ciudadana"},
            {"tipo": "🎮 Juego virtual", "nombre": "Normas de convivencia", "url": "https://wordwall.net/es-cl/community/normas-de-convivencia"},
        ],
    },
    "DARE": {
        "icon": "🎓",
        "color1": "#7B2CBF",
        "color2": "#C77DFF",
        "descripcion": "Educación preventiva para toma de decisiones, habilidades de resistencia y vida saludable.",
        "recursos": [
            {"tipo": "🌐 Información", "nombre": "DARE Ohio - Recursos", "url": "https://dare-oh.org/resources/"},
            {"tipo": "📚 Información", "nombre": "OJP - Introducción al programa DARE", "url": "https://www.ojp.gov/ncjrs/virtual-library/abstracts/introduction-dare-drug-abuse-resistance-education-program-program"},
            {"tipo": "📄 PDF", "nombre": "DARE Educators Guide", "url": "https://depolarisation.eu/wp-content/uploads/2023/03/English-DARE-Educators-Guide.pdf"},
            {"tipo": "🎮 Juego virtual", "nombre": "Juegos de convivencia escolar", "url": "https://wordwall.net/es-mx/community/convivencia-paz-y-ciudadan%C3%ADa"},
        ],
    },
    "PSCC": {
        "icon": "🤝",
        "color1": "#06D6A0",
        "color2": "#118AB2",
        "descripcion": "Recursos para seguridad comunitaria, convivencia ciudadana y participación local.",
        "recursos": [
            {"tipo": "📄 PDF", "nombre": "Manual de Seguridad Comunitaria", "url": "https://costaricaporsiempre.org/wp-content/uploads/2021/03/Manual-de-Seguridad-Comunitaria-1.pdf"},
            {"tipo": "📄 PDF", "nombre": "Policía Comunitaria en Costa Rica", "url": "https://multimedia.uned.ac.cr/ecsh/simposio-policiales-2023/wp-content/uploads/sites/34/2023/09/Policia-comunitaria-en-Costa-Rica.pdf"},
            {"tipo": "🎮 Juego virtual", "nombre": "Seguridad ciudadana", "url": "https://wordwall.net/es-pe/community/seguridad-ciudadana"},
            {"tipo": "🎮 Juego virtual", "nombre": "Convivencia y ciudadanía", "url": "https://wordwall.net/es-cl/community/convivencia-y-ciudadan%C3%ADa"},
        ],
    },
    "VIF": {
        "icon": "🏠",
        "color1": "#EF476F",
        "color2": "#D62828",
        "descripcion": "Material de prevención, sensibilización y atención relacionada con violencia intrafamiliar.",
        "recursos": [
            {"tipo": "📄 PDF", "nombre": "Guía metodológica VIF para policías", "url": "https://www.seguridadpublica.go.cr/oieg/biblioteca/legislacion%20y%20normativa/normativa%20interna%20msp/manuales%20programas%20vifa/Guia%20Metodologica%20Masculinidades%20y%20Violencia%20Intrafamiliar%20para%20Policias.pdf"},
            {"tipo": "📚 Normativa", "nombre": "Protocolo policial VIF - Costa Rica", "url": "https://pgrweb.go.cr/scij/Busqueda/Normativa/Normas/nrm_texto_completo.aspx?nValor1=1&nValor2=90682&nValor3=119570&param1=NRTC&strTipM=TC"},
            {"tipo": "🎮 Juego virtual", "nombre": "Violencia familiar - Wordwall", "url": "https://wordwall.net/es-mx/community/violencia-familiar"},
            {"tipo": "🎮 Juego virtual", "nombre": "Juego completar: Violencia intrafamiliar", "url": "https://es.educaplay.com/recursos-educativos/22227239-juego_de_completar_la_violencia_intrafamiliar.html"},
            {"tipo": "🎮 Juego virtual", "nombre": "La rueda del buen trato", "url": "https://es.educaplay.com/recursos-educativos/6142482-la_ruleta_de_las_emociones.html"},
        ],
    },
}

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #fff7ec 50%, #f4f0ff 100%);
}
.main-title {
    text-align:center;
    font-size: 46px;
    font-weight: 900;
    color: #083B5C;
    margin-bottom: 0px;
}
.subtitle {
    text-align:center;
    font-size: 22px;
    color: #555;
    margin-bottom: 25px;
}
.card {
    border-radius: 26px;
    padding: 28px 22px;
    color: white;
    min-height: 250px;
    box-shadow: 0 12px 26px rgba(0,0,0,.18);
    text-align: center;
    margin-bottom: 10px;
}
.card .icon {
    font-size: 48px;
}
.card h2 {
    font-size: 32px;
    margin: 8px 0;
    color: white;
}
.card p {
    font-size: 16px;
    line-height: 1.35;
}
.resource-box {
    background: white;
    border-radius: 18px;
    padding: 18px;
    margin: 10px 0;
    box-shadow: 0 6px 18px rgba(0,0,0,.08);
    border-left: 8px solid #118AB2;
}
.badge {
    display:inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background:#eef6ff;
    color:#0b5c88;
    font-weight:700;
    margin-bottom: 8px;
}
.footer {
    text-align:center;
    color:#666;
    margin-top:35px;
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧰 Caja de Herramientas</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Programas Preventivos Policiales</div>', unsafe_allow_html=True)

st.info("Versión de ejemplo con enlaces públicos. Antes de usar oficialmente, revise y sustituya los recursos por enlaces institucionales validados.")

if "programa" not in st.session_state:
    st.session_state.programa = None

cols = st.columns(5)
for i, (nombre, data) in enumerate(PROGRAMAS.items()):
    with cols[i]:
        st.markdown(
            f"""
            <div class="card" style="background:linear-gradient(135deg,{data['color1']},{data['color2']});">
                <div class="icon">{data['icon']}</div>
                <h2>{nombre}</h2>
                <p>{data['descripcion']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"Ingresar a {nombre}", key=f"btn_{nombre}", use_container_width=True):
            st.session_state.programa = nombre

st.divider()

programa = st.session_state.programa

if programa is None:
    st.markdown("### 👆 Seleccione un programa para ver videos, juegos, PDFs y materiales.")
else:
    data = PROGRAMAS[programa]
    st.markdown(f"## {data['icon']} Recursos del programa {programa}")
    st.write(data["descripcion"])

    filtro = st.selectbox(
        "Filtrar por tipo de recurso",
        ["Todos", "🌐 Sitio oficial", "📄 PDF", "📚 Información", "📚 Normativa", "🎮 Juego virtual"],
    )

    recursos = data["recursos"]
    if filtro != "Todos":
        recursos = [r for r in recursos if r["tipo"] == filtro]

    if not recursos:
        st.warning("No hay recursos con ese filtro.")
    else:
        c1, c2 = st.columns(2)
        for idx, r in enumerate(recursos):
            with (c1 if idx % 2 == 0 else c2):
                st.markdown(
                    f"""
                    <div class="resource-box">
                        <div class="badge">{r['tipo']}</div>
                        <h3>{r['nombre']}</h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.link_button("Abrir recurso", r["url"], use_container_width=True)

    st.divider()
    st.markdown("### ➕ Agregar recurso manual temporal")
    with st.form("form_recurso"):
        tipo = st.selectbox("Tipo", ["🎥 Video", "🎮 Juego virtual", "📄 PDF", "🌐 Enlace", "📚 Información"])
        nombre = st.text_input("Nombre del recurso")
        url = st.text_input("Enlace")
        guardar = st.form_submit_button("Mostrar recurso agregado")
        if guardar:
            if nombre and url:
                st.success("Recurso agregado temporalmente en pantalla. Para guardarlo permanente, se debe conectar a Google Sheets, Excel o Supabase.")
                st.markdown(f"**{tipo} {nombre}**")
                st.link_button("Abrir recurso agregado", url)
            else:
                st.error("Debe completar nombre y enlace.")

st.markdown(
    f'<div class="footer">Caja de Herramientas Preventiva Policial | Generado el {datetime.now().strftime("%d/%m/%Y")}</div>',
    unsafe_allow_html=True
)









