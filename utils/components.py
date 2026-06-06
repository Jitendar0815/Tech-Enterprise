import streamlit as st
import json
from streamlit_lottie import st_lottie

def load_lottie_url(url: str):
    """Load Lottie animation from URL."""
    import requests
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def hero_section():
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
            <h1 style='font-size: 3.5rem; font-weight: 700; margin-bottom: 0.5rem; 
                       background: linear-gradient(135deg, #6C63FF, #48C9B0);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
                AttentiX
            </h1>
            <p style='font-size: 1.3rem; color: #A0A4B8; margin-top: 0;'>
                Measure what matters – <span class='typewriter' id='typewriter'></span>
            </p>
        """, unsafe_allow_html=True)
    with col2:
        # Public Lottie animation (attention/data) – replace with any URL
        lottie_attention = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_qdch1q0k.json")
        if lottie_attention:
            st_lottie(lottie_attention, height=200, key="hero_lottie")
        else:
            st.image("https://via.placeholder.com/400x200?text=Attention+Analytics", use_column_width=True)

def glass_metric_card(label, value, suffix="%", delta=None, key=None):
    """Custom metric card with count‑up animation."""
    card_html = f"""
    <div class="glass-card">
        <p style='color: #A0A4B8; font-size: 0.85rem; margin: 0;'>{label}</p>
        <p class='metric-value count-up' id='{key}' data-end='{value}'>{value}{suffix}</p>
        <p style='color: {'#48C9B0' if (delta or 0) > 0 else '#E74C3C'}; font-size: 0.85rem;'>{delta if delta else ''}</p>
    </div>
    """
    return card_html

def navigation_bar():
    st.markdown("""
    <div class="top-nav">
        <a class="nav-link" href="#dashboard">📊 Dashboard</a>
        <a class="nav-link" href="#forecast">🔮 Forecast</a>
        <a class="nav-link" href="#raw-data">📁 Raw Data</a>
        <a class="nav-link" href="#about">ℹ️ About</a>
    </div>
    """, unsafe_allow_html=True)

def footer():
    st.markdown("""
    <div class="footer">
        <p>Built with ❤️ using Streamlit • AttentiX © 2025 • 
        <a href='https://github.com' style='color: #6C63FF;'>GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)

def inject_css():
    with open("assets/css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def inject_js():
    with open("assets/js/animations.js") as f:
        js_code = f.read()
    st.components.v1.html(f"<script>{js_code}</script>", height=0, width=0)
