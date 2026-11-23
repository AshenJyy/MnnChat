
import streamlit as st
from llama_cpp import Llama

@st.cache_resource
def model():
    return Llama.from_pretrained(
        repo_id="taobao-mnn/MNN-Pocket-0.3B-GGUF",
        filename="MNN-Pocket-0.3B-Instruct-Q4_1.gguf"
    )

messages = st.session_state.setdefault("messages", [])

for m in messages:
    st.chat_message(m["role"]).write(m["content"])

if prompt := st.chat_input():
    messages.append({"role": "user", "content": prompt})
    answer = model().create_chat_completion(
        messages=messages[-6:]
    )["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": answer})
    st.rerun()
