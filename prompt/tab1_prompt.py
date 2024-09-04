import os
import pandas as pd
from langchain import PromptTemplate


def get_tab1_template_plain():
    # csv에서 처음 3줄 읽기
    user_spec = pd.read_csv(os.getcwd() + "/user_spec.csv", nrows=3)
    loan_result = pd.read_csv(os.getcwd() + "/loan_result.csv", nrows=3)

    user_spec_text = user_spec.to_csv(index=False)
    loan_result_text = loan_result.to_csv(index=False)

    template_plain = f"""You are a professional data analyst.
        develop a strategy to merge the two files for data analysis.
        
        Here is the first 3 rows of user_spec.csv:
        {user_spec_text}
        
        Here is the first 3 rows of loan_result.csv:
        {loan_result_text}
        
        TASK: merge the two files and save the result as 'merged.csv'.
        """

    return template_plain


# 참고 : LLMChain을 사용하는 경우, PromptTemplate 클래스를 사용하여 템플릿을 정의
template = """
    You are a professional data analyst.

    Here is the first 8 rows of user_spec.csv:
    {user_spec_text}

    Here is the first 8 rows of loan_result.csv:
    {loan_result_text}
    """


def get_prompt_template():
    prompt = PromptTemplate(
        input_variables=["user_spec_text", "loan_result_text"],
        template=template,
    )
    return prompt
