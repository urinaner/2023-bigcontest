import os

import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from agent.tab2_agent import (
    tab2_init_agent,
    tab2_strategy_chain,
    tab2_code_chain,
    tab2_execute_agent,
    tab2_log_agent,
)
from prompt.tab2_prompt import (
    tab2_template_plain,
    tab2_template_strategy,
    tab2_template_code,
    tab2_template_execute,
    tab2_log_template,
)
import pandas as pd


def run(tab):
    with tab:
        # step1
        st.header("user, loan 파일 결측치 분석")
        st.subheader("Step1. 결측치 현황 분석")
        load_btn = st.button("merged 불러오기", key="tab2_merge_load_btn")
        if load_btn:
            st.session_state["tab2_template_plain"] = tab2_template_plain()
            st.session_state.merged_df = pd.read_csv(os.getcwd() + "/merged.csv")
            tab2_init_agent()

        query = st.text_area(
            "위 버튼을 눌러주세요.", value=st.session_state["tab2_template_plain"]
        )
        query_btn = st.button("요청하기", key="query_btn")

        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.chat_message(msg["role"]).write(msg["content"])

        if query_btn:
            # merge_agent가 initialized 되었는지 확인
            if not st.session_state["tab2_merge_agent"]:
                st.write("'merged 불러오기' 버튼을 먼저 눌러주세요.")
                return

            merge_agent = st.session_state["tab2_merge_agent"]

            st.session_state.messages.append({"role": "User", "content": query})
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = merge_agent.run(query, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab2_step1_result = response

        # TODO::테스트 완료 후 삭제
        st.session_state.tab2_step1_result = """
        [['total rows', 13,527,250], ['birth_year', 128,096], ['gender', 128,096], ['credit_score', 1,509,276], ['yearly_income', 6], ['company_enter_month', 400,337], ['personal_rehabilitation_yn', 5,888,701], ['personal_rehabilitation_complete_yn', 11,793,977], ['existing_loan_cnt', 2,685,709], ['existing_loan_amt', 3,890,163], ['loan_limit', 7,382], ['loan_rate', 7,382], ['is_applied', 3,257,239]]
        """

        # step2
        st.subheader("Step2. 결측치 처리 전략 수립")
        load_btn2 = st.button("프롬프트 생성하기", key="tab2_load_btn2")
        if load_btn2:
            st.session_state["tab2_strategy"] = tab2_template_strategy().template

        query2 = st.text_area(
            "위에서 분석된 결과를 바탕으로 자동으로 생성된 프롬프트입니다.",
            value=st.session_state.tab2_strategy,
        )
        st.write("gpt-4 모델을 사용합니다.")
        query_btn2 = st.button("전략 수립하기", key="tab2_query_btn2")

        if query_btn2:
            chain = tab2_strategy_chain()
            st.write("잠시만 기다려주세요...최대 1분 소요됩니다.")

            with st.chat_message("assistant"):
                response = chain.run({})
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab2_step2_result = response
                print(st.session_state.tab2_step2_result)

        # TODO::테스트 완료 후 삭제
        st.session_state.tab2_step2_result = """
        [['birth_year', 'Imputation with median', 'Birth year is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers'], ['gender', 'Imputation with mode', 'Gender is a categorical variable, so mode (most frequent value) can be used for imputation'], ['credit_score', 'Imputation with median', 'Credit score is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers'], ['yearly_income', 'Imputation with median', 'Yearly income is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers'], ['company_enter_month', 'Imputation with median', 'Company enter month is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers'], ['personal_rehabilitation_yn', 'Imputation with mode', 'Personal rehabilitation is a binary categorical variable, so mode (most frequent value) can be used for imputation'], ['personal_rehabilitation_complete_yn', 'Imputation with mode', 'Personal rehabilitation complete is a binary categorical variable, so mode (most frequent value) can be used for imputation'], ['existing_loan_cnt', 'Imputation with median', 'Existing loan count is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers'], ['existing_loan_amt', 'Imputation with median', 'Existing loan amount is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers'], ['loan_limit', 'Imputation with median', 'Loan limit is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers'], ['loan_rate', 'Imputation with median', 'Loan rate is a numerical variable and median is a robust measure as compared to mean which can be affected by outliers']]
        """

        # step3
        st.subheader("Step3. 코드 작성")
        load_btn3 = st.button("프롬프트 생성하기", key="tab2_load_btn3")
        if load_btn3:
            st.session_state["tab2_code"] = tab2_template_code().template

        query3 = st.text_area(
            "위에서 분석된 결과를 바탕으로 자동으로 생성된 프롬프트입니다.",
            value=st.session_state.tab2_code,
            key="tab2_text_area_step3",
        )
        st.write("gpt-4 모델을 사용합니다.")
        query_btn3 = st.button("전략 수립하기", key="tab2_query_btn3")

        if query_btn3:
            chain = tab2_code_chain()
            st.write("잠시만 기다려주세요...최대 1분 소요됩니다.")

            with st.chat_message("assistant"):
                response = chain.run({})
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab2_step3_result = response
                print(st.session_state.tab2_step3_result)

        # TODO::테스트 완료 후 삭제
        st.session_state.tab2_step3_result = """
        Here is a Python code to handle the missing values in merged.csv using pandas library:
    ```python
    import pandas as pd
    from scipy.stats import mode
    
    # Load the data
    df = pd.read_csv('merged.csv')
    
    # Define the imputation strategy
    strategy = {
        'birth_year': 'median',
        'gender': 'mode',
        'credit_score': 'median',
        'yearly_income': 'median',
        'company_enter_month': 'median',
        'personal_rehabilitation_yn': 'mode',
        'personal_rehabilitation_complete_yn': 'mode',
        'existing_loan_cnt': 'median',
        'existing_loan_amt': 'median',
        'loan_limit': 'median',
        'loan_rate': 'median'
    }
    
    # Apply the imputation strategy
    for column, method in strategy.items():
        if method == 'median':
            df[column].fillna(df[column].median(), inplace=True)
        elif method == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)
    
    # Save the processed data
    df.to_csv('merged_missing_processed.csv', index=False)
    ```
    
    This code first loads the data from the 'merged.csv' file into a pandas DataFrame. Then, it defines an imputation strategy as a dictionary where the keys are the column names and the values are the imputation methods. It iterates over this dictionary and applies the corresponding imputation method to each column. Finally, it saves the processed data to a new CSV file named 'merged_missing_processed.csv'.
        """

        # step4
        st.subheader("Step4. 결측치 처리 실행")
        load_btn4 = st.button("프롬프트 생성하기", key="tab2_load_btn4")
        if load_btn4:
            st.session_state["tab2_template_execute"] = tab2_template_execute()
            tab2_execute_agent()

        query4 = st.text_area(
            "요청을 입력하세요.",
            value=st.session_state["tab2_template_execute"],
            key="tab2_text_area_step4",
        )
        query_btn4 = st.button("요청하기", key="query_btn4")

        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.chat_message(msg["role"]).write(msg["content"])

        if query_btn4:
            # agent가 initialized 되었는지 확인
            if not st.session_state["tab2_execute_agent"]:
                st.write("위 버튼을 먼저 눌러주세요.")
                return

            agent = st.session_state["tab2_execute_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query4, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab2_step4_result = response

        # step5
        st.divider()
        st.header("log파일 결측치 분석")

        st.subheader("Step5. log 결측치 처리")
        load_btn5 = st.button("log 불러오기", key="tab2_log_load_btn")
        if load_btn5:
            st.session_state["tab2_log_template"] = tab2_log_template()

        query5 = st.text_area(
            "위 버튼을 눌러주세요.",
            value=st.session_state["tab2_log_template"],
            key="tab2_text_area_step5",
        )
        query_btn5 = st.button("요청하기", key="query_btn5")

        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.chat_message(msg["role"]).write(msg["content"])

        if query_btn5:
            agent = st.session_state["python_agent"]

            st.session_state.messages.append({"role": "User", "content": query5})
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query5, callbacks=[st_cb])
                st.write(response)
                st.session_state.tab2_step5_result = response

        # TODO::테스트 완료 후 삭제
        st.session_state.tab2_step5_result = """
        [['total rows', 17843993], ['mp_os', 980], ['mp_app_version', 660597]]
        """
