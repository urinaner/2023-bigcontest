from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent, create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import streamlit as st
from langchain.tools import Tool, PythonREPLTool

from const.const import (
    CUSTOM_PANDAS_AGENT_PREFIX_GPT4,
)

load_dotenv()


def tab4_inspect_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        streaming=True,
    )

    pandas_dataframe_agent_executor = create_pandas_dataframe_agent(
        llm=llm,
        df=st.session_state.log_data_drop,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        prefix=CUSTOM_PANDAS_AGENT_PREFIX_GPT4,
        handle_parsing_errors="Check your output and make sure it conforms!",
        max_iterations=8,
    )

    tools = [
        Tool(
            name="PandasDataFrameAgent",
            func=pandas_dataframe_agent_executor.run,
            description="""Useful when you need to run Pandas code.
                        This agent only recognizes the phrase entered in the Action Input,
                        so be sure to describe your requirements clearly.
                        """,
        ),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    st.session_state["tab4_inspect_agent"] = agent


def tab4_execute_agent():
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

    st.session_state["tab4_execute_agent"] = agent
