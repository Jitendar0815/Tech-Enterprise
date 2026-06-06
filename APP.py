import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page config
st.set_page_config(page_title="AttentiX – Attention Analytics", page_icon="🎬", layout="wide")

# Custom CSS & JS
from src.components import inject_css, inject_js, hero_section, glass_metric_card, navigation_bar, footer
inject_css()
inject_js()

# Load data engine & visualizations
from src.data_generator import generate_attention
from src.analytics_engine import compute_trend
from src.visualizations import retention_curve, attention_heatmap, interaction_spikes, trend_forecast

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/eye-tracking.png", width=80)
    st.markdown("## ⚙️ Controls")
    media = st.selectbox("Content Type", ['video', 'music', 'article'])
    seed = st.number_input("Random Seed", 1, 999, 42)
    st.markdown("---")
    st.caption("This demo uses **synthetic data**. Connect real APIs in production.")

# ---------- MAIN CONTENT ----------
navigation_bar()

# Hero
hero_section()

# Dashboard Section
st.markdown('<div id="dashboard"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'><span style='color:#A0A4B8; font-size:1.5rem;'>📊 Dashboard</span></div>", unsafe_allow_html=True)

df, meta = generate_attention(media, seed)

# Metric row
cols = st.columns(4)
metrics = [
    ("Avg Retention", meta['avg_retention'], "%", f"+{round(np.random.uniform(0,5),1)}"),
    ("Completion Rate", meta['completion_rate'], "%", f"+{round(np.random.uniform(0,3),1)}"),
    ("Attention Score", meta['attention_score'], "/100", f"+{round(np.random.uniform(0,8),1)}"),
    ("Drop‑off Points", len(meta['dropoff_points']), "", f"-{len(meta['dropoff_points'])}" if len(meta['dropoff_points']) > 0 else None)
]
for idx, (label, val, suf, delta) in enumerate(metrics):
    with cols[idx]:
        card_key = f"metric_{idx}_{seed}"
        st.markdown(glass_metric_card(label, val, suf, delta, card_key), unsafe_allow_html=True)

if meta['dropoff_points']:
    st.warning(f"⚠️ Significant drop‑offs at seconds: {', '.join(map(str, meta['dropoff_points']))}")

# Charts
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(retention_curve(df, meta), use_container_width=True)
with col2:
    st.plotly_chart(attention_heatmap(df, meta), use_container_width=True)

st.plotly_chart(interaction_spikes(df), use_container_width=True)

# Forecast Section
st.markdown('<div id="forecast"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'><span style='color:#A0A4B8; font-size:1.5rem;'>🔮 3‑Day Attention Forecast</span></div>", unsafe_allow_html=True)

# Generate some historical data (last 10 days)
np.random.seed(seed)
historical_dates = pd.date_range(end=datetime.today(), periods=10, freq='D').strftime('%Y-%m-%d').tolist()
historical_scores = np.clip(np.random.normal(meta['attention_score'], 3, 10), 0, 100).tolist()
forecast = compute_trend({'dates': historical_dates, 'scores': historical_scores})

st.plotly_chart(trend_forecast(
    {'dates': historical_dates, 'scores': historical_scores},
    forecast
), use_container_width=True)

# Raw Data Section
st.markdown('<div id="raw-data"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'><span style='color:#A0A4B8; font-size:1.5rem;'>📁 Raw Attention Data</span></div>", unsafe_allow_html=True)
with st.expander("Click to expand data table"):
    st.dataframe(df.style.background_gradient(subset=['retention_pct'], cmap='RdYlGn'))

# About Section
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("<div class='section-divider'><span style='color:#A0A4B8; font-size:1.5rem;'>ℹ️ About AttentiX</span></div>", unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <p>AttentiX is a prototype <strong>media attention analytics platform</strong> that helps creators and studios understand 
    exactly when and why audiences stay engaged – or leave.</p>
    <p>Built with <strong>Streamlit, Plotly, and synthetic data</strong>. Ready to be plugged into real APIs.</p>
</div>
""", unsafe_allow_html=True)

# Footer
footer()
