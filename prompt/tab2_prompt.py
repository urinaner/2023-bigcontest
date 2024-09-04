import os

import pandas as pd
import streamlit as st
from langchain import PromptTemplate

from const.const import DATASET_CONTEXT, PANDAS_STABILIZATION


def tab2_template_plain():
    template_plain = f"""
        You are a professional data analyst.
        You have successfully merged user_spec.csv, loan_result.csv and saved the merged.csv file before.
        
        TASK: Observe the number of rows. Observe which columns in merged.csv are missing values and return which columns need to be processed and the number of missing values. 
        Output format of final answer: [['total rows', num of total rows],[name,number missing],[name,number missing]...]
        
        Do not use open('merged.csv'), use pandas.read_csv('merged.csv') instead.
        {PANDAS_STABILIZATION}
        """
    return template_plain


def tab2_template_strategy():
    merged_result = pd.read_csv(os.getcwd() + "/merged.csv", nrows=3)
    merged_result_text = merged_result.to_csv(index=False)

    template = f"""
    You are a professional data analyst.

    {DATASET_CONTEXT}

    You have successfully merged user_spec.csv, loan_result.csv and saved the merged.csv file before.
    Here is the first 3 rows of merged.csv:
    {merged_result_text}
    
    here is the missing values in merged.csv. Columns not listed below have no missing values.
    {st.session_state.tab2_step1_result}

    TASK: Think step by step. Devise one strategy for dealing with missing values for each item. 
    Due to the large size of the dataset, do not use complex methods using machine learning.
    Do not handle missing values for target variables.
    
    Output format: [[col1,strategy,short basis for judgment],[col2,strategy,short basis for judgment]...]
    """

    prompt_template = PromptTemplate(
        input_variables=[],
        template=template,
    )

    return prompt_template


def tab2_template_code():
    merged_result = pd.read_csv(os.getcwd() + "/merged.csv", nrows=3)
    merged_result_text = merged_result.to_csv(index=False)

    template = f"""
    You are a professional data analyst.

    You have successfully merged user_spec.csv, loan_result.csv and saved the merged.csv file before.
    Here is the first 3 rows of merged.csv:
    {merged_result_text}

    Here is a strategy for dealing with missing values in merged.csv.
    {st.session_state.tab2_step2_result}

    TASK: Think step by step. Write Python code to handle the missing values in merged.csv, with the strategy as a guide.
    Process the missing values and save as a 'merged_missing_processed.csv' file.
    
    Output format: (Output only code.)
    """

    prompt_template = PromptTemplate(
        input_variables=[],
        template=template,
    )

    return prompt_template


def tab2_template_execute():
    template_plain = f"""
        You are a professional data analyst.
        You have successfully merged user_spec.csv, loan_result.csv and saved the merged.csv file before.
        
        Here is a strategy for dealing with missing values in merged.csv.
        {st.session_state.tab2_step3_result}

        TASK: Refer to the strategy code and handle the missing values in merged.csv.
            Process the missing values and save as a 'merged_missing_processed.csv' file.
        """
    return template_plain


def tab2_log_template():
    template_plain = f"""
        You are a professional data analyst.
        You need to analyze the missing values in log_data.csv.

        TASK: Observe which columns are missing values. Devise one strategy for dealing with missing values for each item. 
        Process the missing values and save as a 'log_data_missing_processed.csv' file.
        

        """
    return template_plain
