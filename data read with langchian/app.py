import streamlit as st
from langchain.agents.agent_types import AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.agents import create_csv_agent

st.title("Knowledge Extraction with Prompts")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])



question = st.text_area("Enter your question or Python code")

button = st.button("Submit")


# Initialize the agent only if a file is uploaded
if uploaded_file:
    agent = create_csv_agent(
        ChatGoogleGenerativeAI(google_api_key= api_key, model="gemini-1.5-pro-latest"),
        uploaded_file,  # Pass the uploaded file to the agent
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        allow_dangerous_code=True
    )

    
    if button:
        if question:
            # Get the result from the agent
            result = agent.run(question)

            # Display the result
            st.write(f"**Result:** {result}")
        else:
            st.write("Please enter a question or code.")
else:
    st.write("Please upload a CSV file to proceed.")
    
