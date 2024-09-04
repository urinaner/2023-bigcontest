import os

import streamlit as st
import pandas as pd

from const.const import (
    DATASET_CONTEXT,
    FINDA_QUESTION,
    FINDA_SERVICE_INFO,
)


def tab9_template_inspect():
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


def tab9_template_execute():
    result = pd.read_csv(os.getcwd() + "/merged_encoded.csv", nrows=3)
    result_text = result.to_csv(index=False)

    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_QUESTION}
    
        After preprocessing the files and creating derivatives, I compiled all the data into a single file, scaled and decoded it, and saved it as merged_encoded.csv.
        The first three rows of this file are as follows:
        {result_text}
    
        TASK: Judge the data from merged_encoded.csv and select the model that can predict the 'is_applied' column the fastest, most accurately.
        Think of a step-by-step procedure for training and testing the predictive model. And then execute.
        
        Output the resulting accuracy of the model.
        """
    return template_plain
