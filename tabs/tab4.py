import os

import streamlit as st
import pandas as pd
from langchain.callbacks import StreamlitCallbackHandler

from agent.tab4_agent import (
    tab4_execute_agent,
    tab4_inspect_agent,
)
from prompt.tab4_prompt import (
    tab4_template_execute,
    tab4_template_inspect,
)


def run(tab):
    with tab:
        st.header("log_data 전처리")

        # step0
        st.subheader("Step1. 현황 분석")
        load_btn0 = st.button("log 불러오기", key="tab4_load_btn0")
        if load_btn0:
            st.session_state["tab4_template_inspect"] = tab4_template_inspect()
            st.session_state.log_data_drop = pd.read_csv(
                os.getcwd() + "/log_data_drop.csv"
            )
            tab4_inspect_agent()

        query0 = st.text_area(
            "위 버튼을 눌러주세요.",
            value=st.session_state["tab4_template_inspect"],
            key="tab4_text_area_step0",
        )
        query_btn0 = st.button("요청하기", key="tab4_query_btn0")

        if query_btn0:
            if not st.session_state["tab4_inspect_agent"]:
                st.write("위 버튼을 먼저 눌러주세요.")
                return

            agent = st.session_state["tab4_inspect_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query0, callbacks=[st_cb])
                st.write(response)
                st.session_state.tab4_inspect_result = response

        # TODO::테스트 완료 후 삭제
        st.session_state.tab4_inspect_result = """
        Categorized event categories: ['Loan Application Process' : 'StartLoanApply', 'ViewLoanApplyIntro', 'EndLoanApply', 'CompleteIDCertification'], ['Other Events' : 'OpenApp', 'UseLoanManage', 'UsePrepayCalc', 'Login', 'UseDSRCalc', 'SignUp', 'GetCreditInfo']
log_data_drop.csv preprocessing strategy:
1. Create a new column 'event_category' in the dataframe. For each row, if the 'event' value is in the 'Loan Application Process' category, set the 'event_category' value to 'Loan Application Process'. Otherwise, set it to 'Other Events'.
2. Group the dataframe by 'user_id' and 'event_category', and count the number of events in each category for each user.
3. Reset the index of the new dataframe to make 'user_id' a column again.
4. Save the new dataframe to a new CSV file for future use.
        """

        # step3
        st.subheader("Step2. 전략 실행")
        load_btn3 = st.button("CSV로드 및 프롬프트 생성", key="tab4_load_btn3")
        if load_btn3:
            st.session_state["tab4_template_execute"] = tab4_template_execute()
            if st.session_state.log_data_drop is None:
                st.session_state.log_data_drop = pd.read_csv(
                    os.getcwd() + "/log_data_drop.csv"
                )
            tab4_execute_agent()

        query3 = st.text_area(
            "요청을 입력하세요.",
            value=st.session_state["tab4_template_execute"],
            key="tab4_text_area_step3",
        )
        query_btn3 = st.button("요청하기", key="tab4_query_btn3")

        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.chat_message(msg["role"]).write(msg["content"])

        if query_btn3:
            # agent가 initialized 되었는지 확인
            if not st.session_state["tab4_execute_agent"]:
                st.write("위 버튼을 먼저 눌러주세요.")
                return

            agent = st.session_state["tab4_execute_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query3, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab4_execute_result = response
                print(st.session_state.tab4_execute_result)
