import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

def retention_curve(df, meta):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['timestamp_sec'], y=df['retention_pct'],
        mode='lines', fill='tozeroy',
        line=dict(color='#6C63FF', width=3, shape='spline'),
        name='Retention'
    ))
    fig.add_hline(y=50, line_dash="dot", line_color="rgba(255,255,255,0.4)",
                  annotation_text="50%", annotation_font_color="white")
    fig.update_layout(
        title=dict(text=f"Attention Curve: {meta['title']}", font=dict(color='white')),
        xaxis_title="Seconds",
        yaxis_title="% Watching",
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=400,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    return fig

def attention_heatmap(df, meta):
    z = [df['retention_pct'].values]
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=df['timestamp_sec'],
        y=['Engagement'],
        colorscale='RdYlGn',
        zmin=0, zmax=100,
        showscale=True,
        colorbar=dict(title='Retention %', titlefont=dict(color='white'), tickfont=dict(color='white'))
    ))
    fig.update_layout(
        title=dict(text="Attention Heatmap (green = high, red = drop-off)", font=dict(color='white')),
        xaxis_title="Seconds",
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=200,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def interaction_spikes(df):
    fig = px.bar(df, x='timestamp_sec', y='interactions',
                 labels={'timestamp_sec':'Seconds', 'interactions':'Interactions'},
                 color_discrete_sequence=['#48C9B0'])
    fig.update_layout(
        title=dict(text="Interaction Spikes (Likes/Comments)", font=dict(color='white')),
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    return fig

def trend_forecast(historical, predicted):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=historical['dates'], y=historical['scores'],
        mode='lines+markers', name='Past Score',
        line=dict(color='#6C63FF', width=3)
    ))
    # Add forecast
    last_date = pd.to_datetime(historical['dates'][-1])
    future_dates = [last_date + pd.DateOffset(days=i) for i in range(1, 4)]
    fig.add_trace(go.Scatter(
        x=future_dates, y=predicted,
        mode='lines+markers', name='Forecast',
        line=dict(color='#48C9B0', dash='dash', width=3)
    ))
    fig.update_layout(
        title=dict(text="Attention Score Forecast (Next 3 Days)", font=dict(color='white')),
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    return fig
