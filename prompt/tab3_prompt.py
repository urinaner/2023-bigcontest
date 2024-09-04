import os

import pandas as pd
import streamlit as st
from langchain import PromptTemplate

from const.const import DATASET_CONTEXT


def tab3_template_strategy():
    merged_result = pd.read_csv(os.getcwd() + "/merged_missing_processed.csv", nrows=2)
    merged_result_text = merged_result.to_csv(index=False)

    template = f"""
    You are a professional data analyst.
    
    {DATASET_CONTEXT}

    You previously successfully merged user_spec.csv, loan_result.csv and processed missing values.
    Here is the first 2 rows of merged_missing_processed.csv:
    {merged_result_text}

    TASK: You have to judge duplicate or unnecessary columns in merged_missing_processed.csv.
    Think step by step about the meaning and importance of each column. A hidden meaning may exist in a column.
    Think twice about what you've decided to remove.
    Consider that you should merge with log_data.csv later and extract derivatives.

    Output format: [[col1,strategy,short basis for judgment],[col2,strategy,short basis for judgment]...]
    """

    prompt_template = PromptTemplate(
        input_variables=[],
        template=template,
    )

    return prompt_template


def tab3_template_code():
    merged_result = pd.read_csv(os.getcwd() + "/merged_missing_processed.csv", nrows=2)
    merged_result_text = merged_result.to_csv(index=False)

    template = f"""
    You are a professional data analyst.

    You previously successfully merged user_spec.csv, loan_result.csv and processed missing values.
    Here is the first 2 rows of merged_missing_processed.csv:
    {merged_result_text}

    Here is a decision on whether to remove or not for each column:
    {st.session_state.tab3_step1_result}

    TASK: Write python code to drop the columns in merged_missing_processed.csv based on the strategy above.
    Process and save as a 'merged_drop.csv' file.

    Output format: (Output only code. Do not write a description of the code.)
    """

    prompt_template = PromptTemplate(
        input_variables=[],
        template=template,
    )

    return prompt_template


def tab3_template_execute():
    template_plain = f"""
        You are a professional data analyst.
        You have successfully merged user_spec.csv, loan_result.csv before.

        Here is a strategy for removing each column in merged_missing_processed.csv.
        {st.session_state.tab3_step2_result}

        TASK: Refer to the strategy code and drop the columns in merged_missing_processed.csv.
            Process and save as a 'merged_drop.csv' file. Even if there are no columns to process, you should still create a merged_drop.csv.
        """
    return template_plain


# log_data.csv 처리
def tab3_log_template_strategy():
    result = pd.read_csv(os.getcwd() + "/log_data.csv", nrows=2)
    result_text = result.to_csv(index=False)

    template = f"""
    You are a professional data analyst.

    {DATASET_CONTEXT}

    Here is the first 2 rows of log_data.csv:
    {result_text}
    Here is the missing values of log_data.csv:
    {st.session_state.tab2_step5_result}

    TASK: You have to judge duplicate or unnecessary columns in log_data.csv.
    Think step by step about the meaning and importance of each column. A hidden meaning may exist in a column.
    Consider that you should merge with other files later and extract derivatives.

    Output format: [[col1,strategy,short basis for judgment],[col2,strategy,short basis for judgment]...]
    """

    prompt_template = PromptTemplate(
        input_variables=[],
        template=template,
    )

    return prompt_template


def tab3_log_template_code():
    result = pd.read_csv(os.getcwd() + "/log_data.csv", nrows=2)
    result_text = result.to_csv(index=False)

    template = f"""
    You are a professional data analyst.

    Here is the first 2 rows of log_data.csv:
    {result_text}

    Here is a decision on whether to remove or not for each column:
    {st.session_state.tab3_log_step1_result}

    TASK: Write python code to drop the columns in log_data.csv based on the strategy above.
    Process and save as a 'log_data_drop.csv' file.

    Output format: (Output only code. Do not write a description of the code.)
    """

    prompt_template = PromptTemplate(
        input_variables=[],
        template=template,
    )

    return prompt_template


def tab3_log_template_execute():
    template_plain = f"""
        You are a professional data analyst.

        Here is a strategy for removing each column in log_data.csv.
        {st.session_state.tab3_log_step2_result}

        TASK: Refer to the strategy code and drop the columns in log_data_drop.csv.
            Process and save as a 'log_data_drop.csv' file. Even if there are no columns to process, you should still create a log_data_drop.csv.
        """
    return template_plain
