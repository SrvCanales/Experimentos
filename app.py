import streamlit as st

from visualizers import cross_product_visualizer, dot_product_visualizer

st.set_page_config(page_title="Producto punto y producto cruz", page_icon="◢", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap');

    :root{ --bg:#12141c; --panel:#181b26; --panel-line:#272b3a; --text:#eeeae2; --muted:#8c92a4; --sol:#e8b94e; }

    html, body, .stApp, [data-testid="stAppViewContainer"]{ background:var(--bg); font-family:'Figtree',system-ui,sans-serif; }
    [data-testid="stHeader"]{ background:transparent; }
    #MainMenu, footer{ visibility:hidden; }
    .block-container{ max-width:1320px; padding-top:2.4rem; padding-bottom:2rem; }

    .titulo{ font-family:'Newsreader',Georgia,serif; font-size:2.3rem; line-height:1.15; color:var(--text); margin:0 0 .3rem; }
    .subtitulo{ color:var(--muted); font-size:1.02rem; margin:0 0 1.4rem; max-width:60ch; }

    .stTabs [data-baseweb="tab-list"]{ gap:1.6rem; border-bottom:1px solid var(--panel-line); }
    .stTabs [data-baseweb="tab"]{ padding:.5rem 0; color:var(--muted); background:transparent; }
    .stTabs [aria-selected="true"]{ color:var(--text); }
    .stTabs [data-baseweb="tab-highlight"]{ background:var(--sol); height:2px; }
    .stTabs [data-baseweb="tab-border"]{ display:none; }

    .idea{ color:var(--muted); font-size:.98rem; line-height:1.6; max-width:78ch; margin:.9rem 0 0; }
    .idea b{ color:var(--text); font-weight:500; }
    iframe{ border:0; border-radius:14px; }
    </style>
    <h1 class="titulo">Producto punto y producto cruz</h1>
    <p class="subtitulo">Mueve los vectores y observa qué le pasa al ángulo, a la proyección y al área.</p>
    """,
    unsafe_allow_html=True,
)

tab_dot, tab_cross = st.tabs(["Producto punto", "Producto cruz"])

with tab_dot:
    dot_product_visualizer(height=660)
    st.markdown(
        '<p class="idea">El producto punto <b>mide cuánto apunta un vector en la dirección del otro</b>. '
        "Proyecta uno sobre el otro y multiplica esa componente por la longitud del vector base: "
        "es positivo si el ángulo es agudo, cero si son perpendiculares y negativo si es obtuso.</p>",
        unsafe_allow_html=True,
    )

with tab_cross:
    cross_product_visualizer(height=700)
    st.markdown(
        '<p class="idea">El producto cruz <b>construye un vector perpendicular a los dos originales</b>. '
        "Su longitud es el área del paralelogramo que forman, así que vale cero cuando son paralelos "
        "y es máxima cuando son perpendiculares. El sentido lo da la regla de la mano derecha.</p>",
        unsafe_allow_html=True,
    )
