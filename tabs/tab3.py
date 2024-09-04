import os

import streamlit as st
import pandas as pd
from langchain.callbacks import StreamlitCallbackHandler

from agent.tab3_agent import (
    tab3_strategy_chain,
    tab3_code_chain,
    tab3_execute_agent,
    tab3_log_execute_agent,
    tab3_log_strategy_chain,
    tab3_log_code_chain,
)
from prompt.tab3_prompt import (
    tab3_template_strategy,
    tab3_template_code,
    tab3_template_execute,
    tab3_log_template_execute,
    tab3_log_template_strategy,
    tab3_log_template_code,
)


def run(tab):
    with tab:
        st.header("user, loan 불필요열 제거")
        # step1
        st.subheader("Step1. 전략 수립")
        load_btn1 = st.button("프롬프트 생성하기", key="tab3_load_btn1")
        if load_btn1:
            st.session_state["tab3_strategy"] = tab3_template_strategy().template

        query1 = st.text_area(
            "위에서 분석된 결과를 바탕으로 자동으로 생성된 프롬프트입니다.",
            value=st.session_state.tab3_strategy,
            key="tab3_text_area_step1",
        )
        query_btn1 = st.button("전략 수립하기", key="tab3_query_btn1")

        if query_btn1:
            chain = tab3_strategy_chain()
            st.write("잠시만 기다려주세요...최대 1분 소요됩니다.")

            with st.chat_message("assistant"):
                response = chain.run({})
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab3_step1_result = response
                print(st.session_state.tab3_step1_result)

        # TODO::테스트 완료 후 삭제
        st.session_state.tab3_step1_result = """
        [[application_id, Keep, It is a unique identifier for each loan application.], [user_id, Keep, It is a unique identifier for each user.], [birth_year, Keep, It can be used to calculate the age of the user, which can be a significant factor in loan approval.], [gender, Keep, Gender can be a significant factor in loan approval.], [insert_time, Keep, It can be used to track the time of loan application.], [credit_score, Keep, Credit score is a crucial factor in loan approval.], [yearly_income, Keep, Yearly income can affect the loan approval and the loan amount.], [income_type, Keep, The type of income can affect the loan approval.], [company_enter_month, Keep, The duration of employment can affect the loan approval.], [employment_type, Keep, The type of employment can affect the loan approval.], [houseown_type, Keep, The type of housing can affect the loan approval.], [desired_amount, Keep, The desired loan amount can affect the loan approval.], [purpose, Keep, The purpose of the loan can affect the loan approval.], [personal_rehabilitation_yn, Keep, The personal rehabilitation status can affect the loan approval.], [personal_rehabilitation_complete_yn, Keep, The completion of personal rehabilitation can affect the loan approval.], [existing_loan_cnt, Keep, The number of existing loans can affect the loan approval.], [existing_loan_amt, Keep, The amount of existing loans can affect the loan approval.], [loanapply_insert_time, Keep, It can be used to track the time of loan application.], [bank_id, Keep, It is a unique identifier for each bank.], [product_id, Keep, It is a unique identifier for each loan product.], [loan_limit, Keep, The approved loan limit can affect the loan approval.], [loan_rate, Keep, The approved loan rate can affect the loan approval.], [is_applied, Keep, It is the target variable for prediction.]]
        """

        # step2
        st.subheader("Step2. 코드 작성")
        load_btn2 = st.button("프롬프트 생성하기", key="tab3_load_btn2")
        if load_btn2:
            st.session_state["tab3_code"] = tab3_template_code().template

        query2 = st.text_area(
            "위에서 분석된 결과를 바탕으로 자동으로 생성된 프롬프트입니다.",
            value=st.session_state.tab3_code,
            key="tab3_text_area_step2",
        )
        query_btn2 = st.button("전략 수립하기", key="tab3_query_btn2")

        if query_btn2:
            chain = tab3_code_chain()
            st.write("잠시만 기다려주세요...최대 1분 소요됩니다.")

            with st.chat_message("assistant"):
                response = chain.run({})
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab3_step2_result = response
                print(st.session_state.tab3_step2_result)

        # TODO::테스트 완료 후 삭제
        st.session_state.tab3_step2_result = """
Here is the Python code to drop the columns based on the strategy above. However, according to the strategy, all columns are to be kept. Therefore, no columns will be dropped.

```python
import pandas as pd

# Load the data
df = pd.read_csv('merged_missing_processed.csv')

# List of columns to drop
columns_to_drop = []  # No columns to drop according to the strategy

# Drop the columns
df = df.drop(columns=columns_to_drop)

# Save the processed data
df.to_csv('merged_drop.csv', index=False)
```

Please note that if there were any columns to drop, you would simply add them to the `columns_to_drop` list.
        """

        # step3
        st.subheader("Step3. 코드 실행")
        load_btn3 = st.button("CSV로드 및 프롬프트 생성", key="tab3_load_btn3")
        if load_btn3:
            st.session_state["tab3_template_execute"] = tab3_template_execute()
            st.session_state.merged_processed_df = pd.read_csv(
                os.getcwd() + "/merged_missing_processed.csv"
            )
            tab3_execute_agent()

        query3 = st.text_area(
            "요청을 입력하세요.",
            value=st.session_state["tab3_template_execute"],
            key="tab3_text_area_step3",
        )
        query_btn3 = st.button("요청하기", key="tab3_query_btn3")

        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.chat_message(msg["role"]).write(msg["content"])

        if query_btn3:
            # agent가 initialized 되었는지 확인
            if not st.session_state["tab3_execute_agent"]:
                st.write("위 버튼을 먼저 눌러주세요.")
                return

            agent = st.session_state["tab3_execute_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query3, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab3_step3_result = response

        # log 처리
        st.divider()
        st.header("log 불필요열 제거")
        # step1
        st.subheader("Step1. 전략 수립")
        load_btn1 = st.button("프롬프트 생성하기", key="tab3_log_load_btn1")
        if load_btn1:
            st.session_state[
                "tab3_log_strategy"
            ] = tab3_log_template_strategy().template

        query1 = st.text_area(
            "위에서 분석된 결과를 바탕으로 자동으로 생성된 프롬프트입니다.",
            value=st.session_state.tab3_log_strategy,
            key="tab3_log_text_area_step1",
        )
        query_btn1 = st.button("전략 수립하기", key="tab3_log_query_btn1")

        if query_btn1:
            chain = tab3_log_strategy_chain()
            st.write("잠시만 기다려주세요...최대 1분 소요됩니다.")

            with st.chat_message("assistant"):
                response = chain.run({})
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab3_log_step1_result = response
                print(st.session_state.tab3_log_step1_result)

        # TODO::테스트 완료 후 삭제
        st.session_state.tab3_log_step1_result = """
        [['user_id', 'keep', 'This is a unique identifier for each user, which is crucial for merging with other files and tracking user behavior.'], ['event', 'keep', 'This column records the actions of users, which is important for understanding user behavior and predicting future actions.'], ['timestamp', 'keep', 'This column records the time of each action, which can be used to analyze the time pattern of user behavior.'], ['mp_os', 'keep', 'This column records the operating system of the device used by the user. Although there are some missing values, it can be used to analyze the user's device preference.'], ['mp_app_version', 'keep', 'This column records the version of the app used by the user. Although there are some missing values, it can be used to analyze the user's app update behavior and the impact of different app versions on user behavior.'], ['date_cd', 'remove', 'This column seems to be a date derived from the timestamp. Since we already have the timestamp column, this column is redundant and can be removed.']]
        """

        # step2
        st.subheader("Step2. 코드 작성")
        load_btn2 = st.button("프롬프트 생성하기", key="tab3_log_load_btn2")
        if load_btn2:
            st.session_state["tab3_log_code"] = tab3_log_template_code().template

        query2 = st.text_area(
            "위에서 분석된 결과를 바탕으로 자동으로 생성된 프롬프트입니다.",
            value=st.session_state.tab3_log_code,
            key="tab3_log_text_area_step2",
        )
        query_btn2 = st.button("전략 수립하기", key="tab3_log_query_btn2")

        if query_btn2:
            chain = tab3_log_code_chain()
            st.write("잠시만 기다려주세요...최대 1분 소요됩니다.")

            with st.chat_message("assistant"):
                response = chain.run({})
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab3_log_step2_result = response
                print(st.session_state.tab3_log_step2_result)

        # TODO::테스트 완료 후 삭제
        st.session_state.tab3_log_step2_result = """
import pandas as pd

# Load the data
df = pd.read_csv('log_data.csv')

# Drop the 'date_cd' column
df = df.drop('date_cd', axis=1)

# Save the processed data
df.to_csv('log_data_drop.csv', index=False)
        """

        # step3
        st.subheader("Step3. 코드 실행")
        load_btn3 = st.button("CSV로드 및 프롬프트 생성", key="tab3_log_load_btn3")
        if load_btn3:
            st.session_state["tab3_log_template_execute"] = tab3_log_template_execute()
            st.session_state.log_df = pd.read_csv(os.getcwd() + "/log_data.csv")
            tab3_log_execute_agent()

        query3 = st.text_area(
            "요청을 입력하세요.",
            value=st.session_state["tab3_log_template_execute"],
            key="tab3_log_text_area_step3",
        )
        query_btn3 = st.button("요청하기", key="tab3_log_query_btn3")

        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.chat_message(msg["role"]).write(msg["content"])

        if query_btn3:
            # agent가 initialized 되었는지 확인
            if not st.session_state["tab3_log_execute_agent"]:
                st.write("위 버튼을 먼저 눌러주세요.")
                return

            agent = st.session_state["tab3_log_execute_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query3, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab3_log_step3_result = response
