# app.py
import streamlit as st
import tempfile, os
from dotenv import load_dotenv
from core_rag import build_rag_chain
from config import config
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

st.set_page_config(
    page_title=config.app_title,
    page_icon=config.app_icon,
    layout=config.layout
)

# -- Styling
st.markdown("""
<style>
.main-header { font-size: 2.2rem; font-weight: 700; color: #1a56db; }
.sub-header  { font-size: 1rem; color: #6b7280; margin-bottom: 1.5rem; }
.stat-box    { background: #f0f4ff; border-radius: 10px; padding: 1rem; text-align: center; }
.footer      { text-align: center; color: #9ca3af; font-size: 0.8rem; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# -- Header
st.markdown(f'<p class="main-header">{config.app_title}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-header">{config.app_description}</p>', unsafe_allow_html=True)

# -- Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "display_history" not in st.session_state:
    st.session_state.display_history = []
if "chain" not in st.session_state:
    st.session_state.chain = None
if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0

# -- Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/pdf.png", width=60)
    st.header("Upload Document")
    uploaded_file = st.file_uploader(
        f"Choose a PDF (max {config.max_file_size_mb}MB)",
        type="pdf"
    )
    if uploaded_file:
        file_mb = uploaded_file.size / (1024 * 1024)
        if file_mb > config.max_file_size_mb:
            st.error(f"File too large! Max size is {config.max_file_size_mb}MB.")
        elif st.button("⚡ Process PDF", type="primary", use_container_width=True):
            with st.spinner("Indexing your document..."):
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
                    f.write(uploaded_file.read())
                    tmp_path = f.name
                try:
                    chain, count = build_rag_chain(tmp_path)
                    st.session_state.chain = chain
                    st.session_state.chunk_count = count
                    st.session_state.chat_history = []
                    st.session_state.display_history = []
                    st.success(f"✅ Ready! {count} chunks indexed.")
                except Exception as e:
                    st.error(f"Error processing PDF: {e}")
                finally:
                    os.unlink(tmp_path)
    st.markdown("---")
    if st.session_state.chain:
        st.markdown("**📊 Session Stats**")
        col1, col2 = st.columns(2)
        col1.metric("Chunks", st.session_state.chunk_count)
        col2.metric("Messages", len(st.session_state.display_history))
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.display_history = []
            st.rerun()
    st.markdown("---")
    st.markdown(f"""
**⚙️ Model Config**
🤖 `{config.llm_model}`
🌡️ Temp: `{config.llm_temperature}`
🔍 Top-K: `{config.retriever_k}`
""")
    st.markdown("---")
    st.markdown(f"""
<p>Built by <strong>{config.author_name}</strong><br>
<a href="{config.github_url}" target="_blank">GitHub</a> · 
<a href="{config.linkedin_url}" target="_blank">LinkedIn</a></p>
""", unsafe_allow_html=True)

# -- Main Chat Area
if not st.session_state.chain:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stat-box">⚡<br><strong>LLaMA 3.1 8B</strong><br>via Groq</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-box">🔍<br><strong>RAG Pipeline</strong><br>LangChain</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-box">💰<br><strong>100% Free</strong><br>No cost to run</div>', unsafe_allow_html=True)
    st.info("👈 Upload a PDF from the sidebar to start chatting with your document!")
else:
    for msg in st.session_state.display_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            if msg["role"] == "assistant" and msg.get("sources"):
                with st.expander("📖 View Sources"):
                    for i, src in enumerate(msg["sources"], 1):
                        st.markdown(f"**Chunk {i} · Page {src.metadata.get('page', '?') + 1}**")
                        st.caption(src.page_content[:400] + "...")
                        st.divider()
    if question := st.chat_input("Ask anything about your document..."):
        st.session_state.display_history.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = st.session_state.chain.invoke({
                    "input": question,
                    "chat_history": st.session_state.chat_history
                })
                answer = result["answer"]
                sources = result.get("context", [])
                st.write(answer)
                if sources:
                    with st.expander("📖 View Sources"):
                        for i, src in enumerate(sources, 1):
                            st.markdown(f"**Chunk {i} · Page {src.metadata.get('page', '?') + 1}**")
                            st.caption(src.page_content[:400] + "...")
                            st.divider()
        st.session_state.chat_history.extend([
            HumanMessage(content=question),
            AIMessage(content=answer)
        ])
        st.session_state.display_history.append({
            "role": "assistant",
            "content": answer,
            "sources": sources
        })

# -- Footer
st.markdown(
    f'<p class="footer">AI Study Assistant · Built by {config.author_name} · Powered by LangChain, Groq & Streamlit</p>',
    unsafe_allow_html=True
)
