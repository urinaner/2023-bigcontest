from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
import streamlit as st
from langchain.tools import PythonREPLTool, Tool

load_dotenv()


def tab1_init_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name=st.session_state["GPT_MODEL"],
        streaming=True,
    )

    merge_agent = initialize_agent(
        tools=[PythonREPLTool()],
        llm=llm,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        handle_parsing_errors=True,
    )

    st.session_state["tab1_merge_agent"] = merge_agent
    # return merge_agent
