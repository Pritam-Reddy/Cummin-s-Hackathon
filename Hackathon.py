from llama_cpp import Llama

# Update model path to point to your Downloads folder
model_path = "/Users/pritamreddy/Downloads/llama-2-7b.Q4_K_M.gguf"

# Load the Llama model
llama_model = Llama(model_path=model_path, n_ctx=512)

# Function to generate responses
def generate_response(prompt):
    response = llama_model(prompt, max_tokens=100)
    return response["choices"][0]["text"].strip()

# Test the model
print(generate_response("Explain deep learning in simple terms."))

from langchain.llms import LlamaCpp

llm = LlamaCpp(model_path="./model/zephyr-7b-beta.Q4_0.gguf")
prompt = "What are the benefits of using LangChain?"
response = llm(prompt)
print(response)

import streamlit as st
from llama_cpp import Llama

# Load the model
model_path = "./model/zephyr-7b-beta.Q4_0.gguf"
llama_model = Llama(model_path=model_path)

# Streamlit app
st.title("Llama Placement Help Bot")
user_input = st.text_input("Ask me anything about career guidance:")
if st.button("Submit"):
    response = llama_model(user_input, max_tokens=100)["choices"][0]["text"].strip()
    st.write(response)
