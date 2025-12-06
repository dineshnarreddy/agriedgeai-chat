import streamlit as st
import sys
from pathlib import Path

# Make sure Python can see the mango-stack root so `import mango` works
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # C:\mango-stack
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ---------- 1. PAGE SETUP ----------
st.set_page_config(
    page_title="AgriEdge AI Chat",
    page_icon="??",
)

st.title("AgriEdge AI – Demo Chat")
st.write(
    "Ask questions about your project/status reports here. "
    "This is a prototype running on your own AI framework."
)

# ---------- 2. SIMPLE 'MODEL' WRAPPER ----------
def run_ai_framework(user_message: str, history: list[str]) -> str:
    """
    Connects the Streamlit chat UI to my mango-stack framework.
    Right now it calls mango.chat_backend.answer_query().
    """
    try:
        from chat_backend import answer_query


        result = answer_query(user_message, history)
        return result

    except Exception as e:
        # Fallback so the UI doesn’t crash
        return f"⚠️ Error calling backend: {e}"

# ---------- 3. CHAT STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {"role": "user"/"assistant", "content": str}

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- 4. USER INPUT ----------
user_input = st.chat_input("Type your question.")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call your AI framework
    history_texts = [m["content"] for m in st.session_state.messages]
    answer = run_ai_framework(user_input, history_texts)

    # Display assistant answer
    with st.chat_message("assistant"):
        st.markdown(answer)

    # Save to history
    st.session_state.messages.append({"role": "assistant", "content": answer})
