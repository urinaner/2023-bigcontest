from dotenv import load_dotenv
from langchain import LLMChain
from langchain.agents import AgentType, initialize_agent, create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import streamlit as st
from langchain.tools import Tool

from const.const import CUSTOM_PANDAS_AGENT_PREFIX, CUSTOM_PANDAS_AGENT_PREFIX_GPT4
from prompt.tab2_prompt import tab2_template_strategy, tab2_template_code

load_dotenv()


def tab2_init_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name=st.session_state["GPT_MODEL"],
        streaming=True,
    )

    pandas_dataframe_agent_executor = create_pandas_dataframe_agent(
        llm=llm,
        df=st.session_state.merged_df,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        prefix=CUSTOM_PANDAS_AGENT_PREFIX,
        handle_parsing_errors="Check your output and make sure it conforms!",
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

    merge_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    st.session_state["tab2_merge_agent"] = merge_agent


def tab2_strategy_chain():
    prompt = tab2_template_strategy()

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        streaming=True,
    )

    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    return chain


def tab2_code_chain():
    prompt = tab2_template_code()

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        streaming=True,
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    return chain


def tab2_execute_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        streaming=True,
    )

    pandas_dataframe_agent_executor = create_pandas_dataframe_agent(
        llm=llm,
        df=st.session_state.merged_df,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        prefix=CUSTOM_PANDAS_AGENT_PREFIX_GPT4,
        handle_parsing_errors="Check your output and make sure it conforms!",
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

    st.session_state["tab2_execute_agent"] = agent


def tab2_log_agent():
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-4",
        streaming=True,
    )

    pandas_dataframe_agent_executor = create_pandas_dataframe_agent(
        llm=llm,
        df=st.session_state.log_df,
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

    st.session_state["tab2_log_agent"] = agent
