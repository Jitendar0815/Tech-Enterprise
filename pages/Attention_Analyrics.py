import streamlit as st
import plotly.express as px
from utils.data_loader import get_attention_data
from utils.styling import load_css

st.set_page_config(page_title="Attention Analytics", page_icon="📊", layout="wide")
load_css("assets/style.css")

st.title("📊 Attention Analytics")
st.markdown("Deep dive into how user attention fluctuates across hours and days.")

df = get_attention_data()

# ---- HEATMAP ----
st.subheader("🔥 Attention Heatmap (Hour vs Day of Week)")
heatmap_data = df.pivot_table(
    values='attention_score', index='day_name', columns='hour', aggfunc='mean'
)
# Ensure days are ordered
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
heatmap_data = heatmap_data.reindex(day_order)

fig_heat = px.imshow(
    heatmap_data,
    labels=dict(x="Hour of Day", y="Day of Week", color="Avg Attention"),
    x=[f"{h}:00" for h in range(24)],
    y=day_order,
    color_continuous_scale='Reds',
    template='plotly_dark',
    aspect='auto'
)
fig_heat.update_layout(margin=dict(l=0, r=0, t=30, b=0), paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_heat, use_container_width=True)

# ---- LINE CHART: TREND ----
st.subheader("📈 30-Day Attention Trend")
daily_trend = df.groupby('date')['attention_score'].mean().reset_index()
fig_line = px.line(
    daily_trend, x='date', y='attention_score',
    labels={'attention_score': 'Avg Attention Score'},
    template='plotly_dark', color_discrete_sequence=['#FFD700']
)
fig_line.update_traces(line_width=2.5)
fig_line.update_layout(hovermode='x unified', margin=dict(l=0,r=0,t=30,b=0),
                       paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_line, use_container_width=True)

# ---- HISTOGRAM ----
st.subheader("📊 Distribution of Attention Span (minutes)")
fig_hist = px.histogram(
    df, x='attention_span_min', nbins=30,
    labels={'attention_span_min': 'Attention Span (min)'},
    color_discrete_sequence=['#1E90FF'], template='plotly_dark'
)
fig_hist.update_layout(margin=dict(l=0,r=0,t=30,b=0), paper_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_hist, use_container_width=True)

st.caption("Data simulated for demonstration · Refresh for new patterns")
