import streamlit as st
import plotly.express as px
from utils.styling import load_css, navbar
from utils.data_loader import get_audience_data

st.set_page_config(page_title="Audience Insights", page_icon="👥", layout="wide")
load_css("assets/style.css")
navbar()

st.markdown('<div class="fade-in"><h1>👥 Audience Insights</h1></div>', unsafe_allow_html=True)
st.markdown("Who is watching, on what device, and from where.")

age_df, device_df, geo_df = get_audience_data()

# ---- AGE DISTRIBUTION (Donut) ----
st.markdown('<div class="fade-in"><h2>🎂 Age Group Distribution</h2></div>', unsafe_allow_html=True)
fig_pie = px.pie(age_df, values='percentage', names='age_group',
                 hole=0.6, color_discrete_sequence=px.colors.sequential.RdBu,
                 template='plotly_dark')
fig_pie.update_traces(textinfo='percent+label', textfont_color='white')
fig_pie.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                      paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_pie, use_container_width=True)

# ---- DEVICE USAGE ----
st.markdown('<div class="fade-in"><h2>📱 Device Usage</h2></div>', unsafe_allow_html=True)
fig_bar = px.bar(device_df, x='device', y='users_percent',
                 labels={'users_percent': '% of Users'},
                 color='device', color_discrete_sequence=['#ff4b6e','#00b4d8','#ffd700','#2ecc71'],
                 template='plotly_dark')
fig_bar.update_layout(showlegend=False, margin=dict(l=0, r=0, t=30, b=0),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_bar, use_container_width=True)

# ---- TOP COUNTRIES ----
st.markdown('<div class="fade-in"><h2>🌍 Top Countries by Viewers</h2></div>', unsafe_allow_html=True)
fig_geo = px.bar(geo_df.head(12), x='country', y='viewers_millions',
                 labels={'viewers_millions': 'Viewers (Millions)'},
                 color='viewers_millions', color_continuous_scale='tealrose',
                 template='plotly_dark')
fig_geo.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      coloraxis_showscale=False)
st.plotly_chart(fig_geo, use_container_width=True)

st.caption("Demographic data for the last 30 days (simulated)")
