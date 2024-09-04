import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools import PythonREPLTool


def python_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        streaming=True,
    )

    tools = [PythonREPLTool()]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    st.session_state["python_agent"] = agent


def python_agent_3():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo-16k",
        streaming=True,
    )

    tools = [PythonREPLTool()]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    st.session_state["python_agent_3"] = agent
