import os

import pandas as pd

from const.const import (
    DATASET_CONTEXT,
    FINDA_QUESTION,
)


def tab6_template_execute():
    result = pd.read_csv(os.getcwd() + "/merged_derivative.csv", nrows=3)
    result_text = result.to_csv(index=False)

    template_plain = f"""
        You are a professional data analyst.
        {DATASET_CONTEXT}
        {FINDA_QUESTION}
    
        After preprocessing the files and creating the derivatives, I have compiled all the data into a single file named merged_derivative.csv. 
        The first three rows of this file are as follows:
        {result_text}
    
        TASK: 
        1. Identify columns in the dataset present in merged_derivative.csv that contain continuous data with large ranges of values. 
        Apply scaling to these selected features to ensure they have similar ranges of values.
        2. Analyze the data to determine an appropriate encoding scheme for any categorical (string) data present in the dataset.
        
        Think step by step for each task above,
        The first task involves identifying suitable columns for scaling (like Robust Scaler or Standardization) and applying it only on those columns in our dataset in merged_derivative.csv. 
        The second task involves determining a suitable encoder (like Label Encoder or One-Hot Encoder) for any string data within our dataset and applying it.
        
        Save the final result as merged_encoded.csv.
        """
    return template_plain
