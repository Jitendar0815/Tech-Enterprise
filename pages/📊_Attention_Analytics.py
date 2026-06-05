import streamlit as st
import plotly.express as px
from utils.data_loader import get_attention_data
from utils.styling import load_css

st.set_page_config(page_title="Attention Analytics", page_icon="📊", layout="wide")
load_css("assets/style.css")

st.markdown('<div class="fade-in"><h1>📊 Attention Analytics</h1></div>', unsafe_allow_html=True)
st.markdown("Deep dive into how user attention fluctuates across hours and days.", unsafe_allow_html=True)

df = get_attention_data()

# ---- HEATMAP ----
st.markdown('<div class="fade-in"><h2>🔥 Attention Heatmap (Hour vs Day of Week)</h2></div>', unsafe_allow_html=True)
heatmap_data = df.pivot_table(values='attention_score', index='day_name', columns='hour', aggfunc='mean')
day_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
heatmap_data = heatmap_data.reindex(day_order)

fig_heat = px.imshow(
    heatmap_data,
    labels=dict(x="Hour of Day", y="Day of Week", color="Avg Attention"),
    x=[f"{h}:00" for h in range(24)],
    y=day_order,
    color_continuous_scale='OrRd',
    template='plotly_dark',
    aspect='auto'
)
fig_heat.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_heat, use_container_width=True)

# ---- LINE CHART: TREND ----
st.markdown('<div class="fade-in"><h2>📈 30-Day Attention Trend</h2></div>', unsafe_allow_html=True)
daily_trend = df.groupby('date')['attention_score'].mean().reset_index()
fig_line = px.line(daily_trend, x='date', y='attention_score',
                   labels={'attention_score': 'Avg Attention Score'},
                   template='plotly_dark', color_discrete_sequence=['#ffd700'])
fig_line.update_traces(line_width=3)
fig_line.update_layout(hovermode='x unified', margin=dict(l=0, r=0, t=30, b=0),
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_line, use_container_width=True)

# ---- HISTOGRAM ----
st.markdown('<div class="fade-in"><h2>📊 Distribution of Attention Span (min)</h2></div>', unsafe_allow_html=True)
fig_hist = px.histogram(df, x='attention_span_min', nbins=35,
                        labels={'attention_span_min': 'Attention Span (min)'},
                        color_discrete_sequence=['#00b4d8'], template='plotly_dark')
fig_hist.update_layout(margin=dict(l=0, r=0, t=30, b=0),
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
st.plotly_chart(fig_hist, use_container_width=True)

st.caption("Data simulated for demonstration · Refresh for new patterns")
