import streamlit as st

from const.const import (
    DATASET_CONTEXT,
    FINDA_QUESTION,
    FINDA_SERVICE_INFO,
)


def tab4_template_inspect():
    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_SERVICE_INFO}
        {FINDA_QUESTION}
        
        Previously, you removed unneeded columns from the log_data.csv file, imputed missing values, and saved it as log_data_drop.csv.
        
        TASK: You need to preprocess the 'log_data_drop.csv' file. 
        1. Classify the event information into two groups. One category is the flow until the loan application is completed.
        2. log_data stores all app usage events for each user. In order to merge it with other files, you will need to do some preprocessing and simplify the dataset using the categories you classified above. 
        Think about the strategy step by step. You can utilize the Pandas agent to query for the information you need. 
        
        The final TASK is to output the event categories and preprocessing strategy. 
        Make sure to write each step clearly.
        
        Output Format:
        Categorized event categories: ['category name1' : 'item1','item2',...], ['category name2' : 'item1','item2',...]
        log_data_drop.csv preprocessing strategy:
        1. explain step 1
        2. explain step 2
        3. ...
        
        """
    return template_plain


def tab4_template_execute():
    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_SERVICE_INFO}
        {FINDA_QUESTION}
        
        You have successfully removed unneeded columns, imputed missing values, and saved it as log_data_drop.csv before.
        
        You need to preprocess the 'log_data_drop.csv' file and simplify the dataset.
        You've categorized the events in the log, and you need to use this information to preprocess them.
        
        Here is a preprocessing strategy for the file 'log_data_drop.csv':
        {st.session_state.tab4_inspect_result}

        TASK: Refer to the strategy code and preprocess the 'log_data_drop.csv' file and simplify the dataset.
            Process and save as a 'log_data_preprocessed.csv' file.
        """
    return template_plain
