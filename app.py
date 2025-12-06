import streamlit as st
from chat_backend import answer_query

# Basic page config
st.set_page_config(
    page_title="AgriEdge AI – Demo Chat",
    page_icon="🌱",
    layout="wide",
)

# Keep history in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of dicts: {"role": "user"/"assistant", "content": str}

# Title + intro
st.title("AgriEdge AI – Demo Chat")
st.write(
    "Ask questions about your project/status reports here. "
    "This is a prototype running on your own AI framework."
)

# Render previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your question…")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build simple text history for backend
    history_texts = [m["content"] for m in st.session_state.messages if m["role"] == "user"]

    # Call backend safely
    try:
        reply = answer_query(user_input, history_texts)
    except Exception as e:
        reply = f"⚠️ Error calling backend: {e}"

    # Show assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
