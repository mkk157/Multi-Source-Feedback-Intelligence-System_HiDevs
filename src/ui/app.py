import sys
from pathlib import Path

# -------------------------------------------------
# Fix import issues in Streamlit
# -------------------------------------------------

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

# -------------------------------------------------
# Imports
# -------------------------------------------------

import streamlit as st
import pandas as pd
import plotly.express as px

from src.rag.rag_chain import answer_question

# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(
    page_title="Multi-Source Feedback Intelligence System",
    page_icon="📊",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------

st.markdown("""
<style>

/* TAB STYLING */

button[data-baseweb="tab"] {
    font-size: 20px !important;
    font-weight: 700 !important;
    padding: 14px 28px !important;
    margin-right: 15px !important;
    border-radius: 12px !important;
}

/* Selected Tab */

button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #1f77b4 !important;
    color: white !important;
    font-size: 20px !important;
    font-weight: 800 !important;
}

/* Non-selected Tabs */

button[data-baseweb="tab"][aria-selected="false"] {
    background-color: #f1f3f6 !important;
    color: #31333F !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Space Between Tabs */

div[data-baseweb="tab-list"] {
    gap: 15px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Load Data
# -------------------------------------------------

df = pd.read_csv(
    "data/processed/cleaned_feedback.csv"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("📊 Multi-Source Feedback Intelligence System")

st.caption(
    "AI-Powered Customer Feedback Analytics and RAG Assistant"
)

st.info(
    "✅ Google Play Reviews | ✅ Survey Feedback | ✅ LangChain | ✅ ChromaDB | ✅ Groq Llama 3 | ✅ Streamlit"
)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.title("Project Information")

st.sidebar.markdown("""
### Tech Stack

- Google Play Reviews
- Survey Feedback
- LangChain
- ChromaDB
- MiniLM Embeddings
- Groq Llama 3
- Streamlit
""")

# -------------------------------------------------
# Tabs
# -------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Dashboard",
        "🤖 AI Assistant",
        "🔍 Feedback Explorer",
        "🏗️ Architecture"
    ]
)

# ===================================================
# TAB 1 - DASHBOARD
# ===================================================

with tab1:

    st.header("📊 Feedback Dashboard")

    total_reviews = len(df)

    positive = (
        df["rating_category"] == "Positive"
    ).sum()

    negative = (
        df["rating_category"] == "Negative"
    ).sum()

    neutral = (
        df["rating_category"] == "Neutral"
    ).sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Reviews",
        total_reviews
    )

    c2.metric(
        "Positive",
        positive
    )

    c3.metric(
        "Negative",
        negative
    )

    c4.metric(
        "Neutral",
        neutral
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        sentiment_counts = (
            df["rating_category"]
            .value_counts()
            .reset_index()
        )

        sentiment_counts.columns = [
            "Sentiment",
            "Count"
        ]

        fig = px.pie(
            sentiment_counts,
            names="Sentiment",
            values="Count",
            title="Sentiment Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        source_counts = (
            df["source"]
            .value_counts()
            .reset_index()
        )

        source_counts.columns = [
            "Source",
            "Count"
        ]

        fig2 = px.bar(
            source_counts,
            x="Source",
            y="Count",
            color="Source",
            title="Feedback By Source"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    st.divider()

    st.subheader("📋 Quick Insights")

    st.success(
        f"""
Total Feedback Records: {total_reviews}

Positive Reviews: {positive}

Negative Reviews: {negative}

Neutral Reviews: {neutral}
"""
    )

# ===================================================
# TAB 2 - AI ASSISTANT
# ===================================================

with tab2:

    st.header("🤖 AI Feedback Assistant")

    st.write(
        "Ask questions about customer reviews and feedback."
    )

    example_questions = [
        "What are customers complaining about?",
        "Summarize negative feedback from customers.",
        "What login related issues are customers reporting?",
        "What product improvements should the team prioritize?"
    ]

    selected_question = st.selectbox(
        "Example Questions",
        example_questions
    )

    question = st.text_input(
        "Ask a question about customer feedback",
        value=selected_question
    )

    if st.button("Analyze"):

        if question:

            with st.spinner(
                "Analyzing feedback..."
            ):

                response = answer_question(
                    question
                )

                st.success(
                    "Analysis Completed"
                )

                st.markdown(response)

# ===================================================
# TAB 3 - FEEDBACK EXPLORER
# ===================================================

with tab3:

    st.header("🔍 Feedback Explorer")

    c1, c2 = st.columns(2)

    with c1:

        sentiment_filter = st.selectbox(
            "Select Sentiment",
            [
                "All",
                "Positive",
                "Negative",
                "Neutral"
            ]
        )

    with c2:

        source_filter = st.selectbox(
            "Select Source",
            ["All"]
            + sorted(
                df["source"]
                .unique()
                .tolist()
            )
        )

    filtered_df = df.copy()

    if sentiment_filter != "All":

        filtered_df = filtered_df[
            filtered_df["rating_category"]
            == sentiment_filter
        ]

    if source_filter != "All":

        filtered_df = filtered_df[
            filtered_df["source"]
            == source_filter
        ]

    st.write(
        f"Records Found: {len(filtered_df)}"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    csv = filtered_df.to_csv(
        index=False
    )

    st.download_button(
        label="📥 Download Filtered Feedback",
        data=csv,
        file_name="filtered_feedback.csv",
        mime="text/csv"
    )

# ===================================================
# TAB 4 - ARCHITECTURE
# ===================================================

with tab4:

    st.header("🏗️ Solution Architecture")

    st.markdown("""
### End-to-End Data Flow

Google Play Reviews  
⬇️  
Survey Feedback  
⬇️  
Data Preprocessing  
⬇️  
Chunking  
⬇️  
Embeddings (MiniLM-L6-v2)  
⬇️  
ChromaDB Vector Store  
⬇️  
Retriever  
⬇️  
Groq Llama 3  
⬇️  
Streamlit UI

---

### HiDevs Framework Mapping

✅ Step 1 – Data Sources

✅ Step 2 – Data Preprocessing

✅ Step 3 – Splitting & Chunking

✅ Step 4 – Embeddings + ChromaDB

✅ Step 5 – Query Processing & AI Engine

✅ Step 6 – UI Development

⬜ Step 7 – Testing & Optimization
""")