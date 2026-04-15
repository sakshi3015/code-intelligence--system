
import streamlit as st
from model import predict_tag, get_data
from search import search_code
from explain import explain_code

# Page config
st.set_page_config(page_title="Code AI", layout="wide")

# Load data
df, embeddings, embedder = get_data()

# Title
st.markdown("<h1 style='text-align: center;'>💻 Code Intelligence System</h1>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Code")
    uploaded_file = st.file_uploader("📁 Upload Python file", type=["py"])

# Initialize code_input
code_input = ""

# If file uploaded, read content
if uploaded_file is not None:
    code_input = uploaded_file.read().decode("utf-8")

# Text area (user can edit or paste code)
code_input = st.text_area("Paste your code here:", height=250, value=code_input)

# Buttons in columns (better UI)
btn1, btn2 = st.columns(2)

with btn1:
    if st.button("🔍 Predict Tag"):
        if code_input.strip():
            try:
                with st.spinner("Predicting tag..."):
                    tag = predict_tag(code_input)
                st.success(f"Tag: {tag}")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter or upload code first.")

with btn2:
    if st.button("🧠 Explain Code"):
        if code_input.strip():
            try:
                with st.spinner("Generating explanation..."):
                    explanation = explain_code(code_input)
                st.info(explanation)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter or upload code first.")

with col2:
    st.subheader("🔎 Semantic Search")
    query = st.text_input("Search something like 'binary search'")

    if st.button("Search"):
        if query:
            results = search_code(query, embedder, embeddings, df)
            for res in results:
                st.code(res["code"], language="python")
                st.write(f"Tag: {res['tag']}")
                st.progress(float(res["score"]))
