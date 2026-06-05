import streamlit as st

def load_css(file_name: str):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def navbar():
    """Top navigation bar that works on every page (buttons + switch_page)."""
    # Custom container to apply CSS class
    with st.container():
        st.markdown('<div class="navbar">', unsafe_allow_html=True)
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
                if st.button(label, key=f"nav_{path}", use_container_width=True):
                    st.switch_page(path)
        st.markdown('</div>', unsafe_allow_html=True)
