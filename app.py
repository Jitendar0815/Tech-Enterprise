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

# ---- HEADER ----
st.markdown("""
<div style="text-align: center; margin-top: -2rem;">
    <h1>🎬 Media, Entertainment & Attention Analytics</h1>
    <p style="font-size: 1.2rem; color: #B0B0B0;">
        Understand what captures attention in a world of infinite content.
    </p>
</div>
<hr style="border: 1px solid rgba(255,255,255,0.08); margin: 1.5rem 0;">
""", unsafe_allow_html=True)

# ---- KPI METRICS ----
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
df_summary = get_daily_summary()

with kpi1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="value">{df_summary['total_users'].iloc[-1]:,}</div>
        <div class="label">👥 Total Users</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="value">{df_summary['avg_attention_min'].iloc[-1]:.1f} min</div>
        <div class="label">⏱️ Avg. Attention Span</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="value">{df_summary['content_pieces'].iloc[-1]}</div>
        <div class="label">🎞️ Content Pieces</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="value">{df_summary['engagement_rate'].iloc[-1]:.1f}%</div>
        <div class="label">📈 Engagement Rate</div>
    </div>
    """, unsafe_allow_html=True)

# ---- TREND CHART ----
st.markdown("### 📅 Daily Active Users & Attention Trend")
fig = px.area(
    df_summary, x='date', y='total_users',
    title="Total Daily Active Users (Last 30 Days)",
    labels={'date': '', 'total_users': 'Users'},
    template="plotly_dark",
    color_discrete_sequence=['#FF4B4B']
)
fig.update_traces(line=dict(width=2), opacity=0.6)
fig.update_layout(height=400, margin=dict(l=0, r=0, t=40, b=0),
                  hovermode='x unified', paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig, use_container_width=True)

# ---- QUICK NAVIGATION CARDS ----
st.markdown("---")
st.subheader("📌 Explore the Dashboard")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📊 Attention Analytics</h3>
        <p>Heatmaps & trends of audience attention spans.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Attention Analytics", key="go1"):
        st.switch_page("pages/1_📊_Attention_Analytics.py")

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎬 Content Performance</h3>
        <p>Ratings, box office & genre breakdowns.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Content Performance", key="go2"):
        st.switch_page("pages/2_🎬_Content_Performance.py")

with col3:
    st.markdown("""
    <div class="card">
        <h3>💬 Social Media Buzz</h3>
        <p>Sentiment scores and trending hashtags.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Social Media Buzz", key="go3"):
        st.switch_page("pages/3_💬_Social_Media_Buzz.py")

with col4:
    st.markdown("""
    <div class="card">
        <h3>👥 Audience Insights</h3>
        <p>Demographics, devices & geography.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Go to Audience Insights", key="go4"):
        st.switch_page("pages/4_👥_Audience_Insights.py")

# Footer
st.markdown("---")
st.caption("© 2026 Media Attention Analytics · Built with Streamlit")
