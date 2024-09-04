import os

import streamlit as st
import pandas as pd

from const.const import (
    DATASET_CONTEXT,
    FINDA_QUESTION,
    FINDA_SERVICE_INFO,
    FINDA_QUESTION_2,
)


def tab8_template_execute():
    template_plain = f"""
        You are a professional data analyst.
        {FINDA_QUESTION_2}
        
        I have preprocessed the data files, carrying out scaling and encoding operations. 
        I then ran a model to extract the importance of each feature.
        
        This is the variable importance.
        
                                       Feature  Importance
14                   loan_rate         466
1                 credit_score         391
11                     bank_id         333
12                  product_id         317
13                  loan_limit         228
6               desired_amount         219
3                  income_type         176
19                   login_cnt         172
0                   birth_year         150
9            existing_loan_cnt         124
2                yearly_income         110
16           employment_period          95
7                      purpose          80
10           existing_loan_amt          70
20                    loan_cnt          37
4              employment_type          18
17             loan_limit_rank           6
18              loan_rate_rank           4
8   personal_rehabilitation_yn           3
5                houseown_type           1
15                   age_group           0
        
    
        TASK: Select several items with high Feature Importance.
        Use 'merged_derivative.csv' as input data. 'merged_encoded.csv' is the file in which merged_derivative.csv is encoded.
        
        Determine the optimal number of clusters and perform clustering on these selected features.
        If the determined number of clusters is greater than 5, select 5. If it is less than 5, use the determined number of clusters.
        Perform clustering on these selected high-importance features.
        The final output should be saved in a file named 'clustered.csv'.
        
        The expected format of the 'clustered.csv' file is as follows:
col1, col2, col3, ...
cluster                                       
0   10.686072   0.536512   0.440022   ...
1   13.309187   -0.080851   -0.326207 ...
...

        Each row corresponds to one cluster and contains mean values (or other representative statistics) for each feature within that cluster.
        
        Note: Do not output graphs or images. DO NOT use functions like plt.show() or st.pyplot() which would generate graphical outputs; 
        this task requires only numerical results saved in a CSV file.
        """
    return template_plain
