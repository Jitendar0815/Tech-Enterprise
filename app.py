import streamlit as st
import plotly.express as px
from utils.styling import load_css
from utils.data_loader import get_daily_summary

st.set_page_config(
    page_title="Media Attention Analytics",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css("assets/style.css")

# ---- ANIMATED HERO SECTION ----
st.markdown("""
<div class="fade-in" style="text-align: center; margin-top: -2rem;">
    <h1>🎬 Media, Entertainment & Attention Analytics</h1>
    <p style="font-size: 1.3rem; color: #b0b0ff; margin-top: -0.5rem; letter-spacing: 1px;">
        Decode what captures the world's attention.
    </p>
</div>
<hr>
""", unsafe_allow_html=True)

# ---- KPI CARDS (Animated numbers) ----
df_summary = get_daily_summary()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.1s">
        <div class="value">{df_summary['total_users'].iloc[-1]:,}</div>
        <div class="label">👥 Total Active Users</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.2s">
        <div class="value">{df_summary['avg_attention_min'].iloc[-1]:.1f} min</div>
        <div class="label">⏱️ Avg Attention Span</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.3s">
        <div class="value">{df_summary['content_pieces'].iloc[-1]}</div>
        <div class="label">🎞️ Content Pieces</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="metric-card fade-in" style="animation-delay: 0.4s">
        <div class="value">{df_summary['engagement_rate'].iloc[-1]:.1f}%</div>
        <div class="label">📈 Engagement Rate</div>
    </div>
    """, unsafe_allow_html=True)

# ---- MAIN TREND CHART ----
st.markdown("""
<div class="fade-in" style="animation-delay: 0.5s">
    <h2>📅 Daily Active Users Trend</h2>
</div>
""", unsafe_allow_html=True)

fig = px.area(
    df_summary, x='date', y='total_users',
    labels={'date': '', 'total_users': 'Users'},
    template="plotly_dark",
    color_discrete_sequence=['#ff4b6e']
)
fig.update_traces(line=dict(width=3, shape='spline'), opacity=0.7,
                  fill='tozeroy', fillcolor='rgba(255,75,110,0.15)')
fig.update_layout(
    height=420,
    margin=dict(l=0, r=0, t=30, b=0),
    hovermode='x unified',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white'),
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
)
st.plotly_chart(fig, use_container_width=True)

# ---- NAVIGATION CARDS ----
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div class="fade-in" style="text-align: center; animation-delay: 0.6s">
    <h2 style="border: none; padding-left: 0;">📌 Explore the Dashboard</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:
    st.markdown("""
    <div class="nav-card fade-in" style="animation-delay: 0.7s">
        <h3>📊 Attention</h3>
        <p>Heatmaps & trends of audience attention</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("→ Open", key="nav1"):
        st.switch_page("pages/1_📊_Attention_Analytics.py")

with col2:
    st.markdown("""
    <div class="nav-card fade-in" style="animation-delay: 0.8s">
        <h3>🎬 Performance</h3>
        <p>Genres, ratings, and box office</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("→ Open", key="nav2"):
        st.switch_page("pages/2_🎬_Content_Performance.py")

with col3:
    st.markdown("""
    <div class="nav-card fade-in" style="animation-delay: 0.9s">
        <h3>💬 Social Buzz</h3>
        <p>Sentiment & trending topics</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("→ Open", key="nav3"):
        st.switch_page("pages/3_💬_Social_Media_Buzz.py")

with col4:
    st.markdown("""
    <div class="nav-card fade-in" style="animation-delay: 1.0s">
        <h3>👥 Audience</h3>
        <p>Who's watching & from where</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("→ Open", key="nav4"):
        st.switch_page("pages/4_👥_Audience_Insights.py")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("© 2026 Media Attention Analytics · Built with Streamlit & Passion")
