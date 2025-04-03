import streamlit as st
from llama_cpp import Llama

MODEL_PATH = "/Users/pritamreddy/Downloads/llama-2-7b.Q4_K_M.gguf"

@st.cache_resource
def load_model():
    return Llama(model_path=MODEL_PATH, n_ctx=512)

llama_model = load_model()

st.title("Llama Placement Help Bot")

user_input = st.text_input("Ask me anything about career guidance:")
if st.button("Submit"):
    if user_input.strip():
        response = llama_model(user_input, max_tokens=100)["choices"][0]["text"].strip()
        st.write(response)
    else:
        st.warning("Please enter a question!")