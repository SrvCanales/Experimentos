"""Visualizadores interactivos de producto punto (R2) y producto cruz (R3) para Streamlit.

Cada visualizador es un componente HTML autocontenido (canvas + panel de valores) que vive en
`components/`. Se renderiza con `st.components.v1.html`, de modo que arrastrar los vectores
actualiza la vista y los números al instante, sin recargar el script de Streamlit.
"""
from pathlib import Path

import streamlit.components.v1 as components

_DIR = Path(__file__).parent / "components"


def _load(name: str) -> str:
    base_css = (_DIR / "base.css").read_text(encoding="utf-8")
    html = (_DIR / name).read_text(encoding="utf-8")
    return html.replace("/*__BASE_CSS__*/", base_css)


def dot_product_visualizer(height: int = 660) -> None:
    """Producto punto en R2: ángulo θ, proyección y A·B = |A||B|cos θ."""
    components.html(_load("dot_product.html"), height=height, scrolling=False)


def cross_product_visualizer(height: int = 700) -> None:
    """Producto cruz en R3: paralelogramo, vector perpendicular y |A×B| = |A||B|sin θ."""
    components.html(_load("cross_product.html"), height=height, scrolling=False)
