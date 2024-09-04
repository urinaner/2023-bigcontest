import streamlit as st

from const.const import (
    DATASET_CONTEXT,
    FINDA_QUESTION,
)


def tab7_template_execute():
    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_QUESTION}
        
        This is the strategy for creating derived variables:
        {st.session_state.tab5_inspect_final_result}
    
        I have preprocessed the files, generated the derivatives, performed scaling and encoding tasks, and saved them as 'merged_encoded.csv'.

        TASK: 
        1. Refer to the DATASET_CONTEXT first to identify the target column.
        2. Before training the model, determine if there are any unnecessary columns. If so, drop these columns.
        3. Decide on an appropriate model for prediction. The model should be able to predict the target column quickly. The maximum time allowed is 1 minute.
        4. Divide your dataset into suitable proportions for your model and initiate it. Then evaluate its accuracy. Also determine variable importance.

        Please proceed step by step as described above to complete this task successfully.
        Finally, output the accuracy score and variable importance.
        """
    return template_plain
