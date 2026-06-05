import streamlit as st

def load_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def navbar():
    """Render a persistent top navigation bar with links to all pages."""
    # Inject minimal additional CSS for the navbar container
    st.markdown("""
    <style>
    .nav-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.8rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

    # Use st.page_link for native Streamlit navigation (since version 1.31.0)
    cols = st.columns([1, 1, 1, 1, 1])
    pages = [
        ("🏠 Home", "app.py"),
        ("📊 Attention", "pages/1_📊_Attention_Analytics.py"),
        ("🎬 Content", "pages/2_🎬_Content_Performance.py"),
        ("💬 Social", "pages/3_💬_Social_Media_Buzz.py"),
        ("👥 Audience", "pages/4_👥_Audience_Insights.py"),
    ]

    for idx, (label, path) in enumerate(pages):
        with cols[idx]:
            st.page_link(path, label=label, use_container_width=True)
