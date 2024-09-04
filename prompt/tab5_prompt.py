import os

import streamlit as st
import pandas as pd

from const.const import (
    DATASET_CONTEXT,
    FINDA_QUESTION,
    FINDA_SERVICE_INFO,
)


def tab5_template_inspect():
    result = pd.read_csv(os.getcwd() + "/merged_drop.csv", nrows=3)
    result_text = result.to_csv(index=False)

    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_SERVICE_INFO}
        {FINDA_QUESTION}
        
        You have successfully merged the two files loan_result, user_spec before.
        Here is the first 3 rows of merged_drop.csv:
        {result_text}
        
        TASK: Think step by step. Referring to the table specification and merged_drop.csv above, think of five strategies for generating derivatives. 
        Then, evaluate each strategy. Express the probability of being useful as a percentage.

        Output Format:
        Derivative strategies:
        1. strategy, short basis for judgment, Probability of usefulness.
        2. strategy, short basis for judgment, Probability of usefulness.
        3. ...
        """
    return template_plain


def tab5_template_inspect_event():
    result = pd.read_csv(os.getcwd() + "/merged_drop.csv", nrows=2)
    result_text = result.to_csv(index=False)
    log = pd.read_csv(os.getcwd() + "/log_data_preprocessed.csv", nrows=15)
    log_text = log.to_csv(index=False)

    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_SERVICE_INFO}
        {FINDA_QUESTION}
    
        You have successfully merged the two files loan_result, user_spec before.
        Here is the first 2 rows of merged_drop.csv:
        {result_text}
        
        We've preprocessed the event entries in log_data by categorizing them into two categories. 
        One of them is the category of the user using the app until they complete the loan application function.
        Here is the first 15 rows of log_data_preprocessed.csv:
        {log_text}
        
        TASK: Think step by step. Referring to the log_data_preprocessed, think a strategy to create useful derivatives.
        Then, evaluate strategy.
    
        """
    return template_plain


def tab5_template_inspect_final():
    result = pd.read_csv(os.getcwd() + "/merged_drop.csv", nrows=2)
    result_text = result.to_csv(index=False)
    log = pd.read_csv(os.getcwd() + "/log_data_preprocessed.csv", nrows=10)
    log_text = log.to_csv(index=False)

    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_SERVICE_INFO}
        {FINDA_QUESTION}

        Here is the first 2 rows of merged_drop.csv:
        {result_text}
        Here is the first 10 rows of log_data_preprocessed.csv:
        {log_text}
        
        This is the strategy for creating derived variables related to user, loan_result.
        {st.session_state.tab5_inspect_result}
        This is a strategy for generating derived variables related to log events.
        {st.session_state.tab5_inspect_event_result}

        TASK: Think step by step. From the above strategies, select the one that you will ultimately use to generate derived variables. 
        There can be multiple strategies selected.

        Output Format:
        selected strategies:
        1. strategy: basis for judgment
        2. strategy: basis for judgment
        3. ...

        """
    return template_plain


def tab5_template_execute():
    result = pd.read_csv(os.getcwd() + "/merged_drop.csv", nrows=2)
    result_text = result.to_csv(index=False)
    log = pd.read_csv(os.getcwd() + "/log_data_preprocessed.csv", nrows=10)
    log_text = log.to_csv(index=False)

    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
    
        Here is the first 2 rows of merged_drop.csv:
        {result_text}
        Here is the first 10 rows of log_data_preprocessed.csv:
        {log_text}
    
        This is the strategy for creating derived variables:
        {st.session_state.tab5_inspect_final_result}
    
        TASK: Create a derivative variable. You need to execute the above strategies in code. 
        Solve the above strategy step by step. 
        
        Save the final result as merged_derivative.csv.
    
        """
    return template_plain
