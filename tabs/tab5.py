import os

import streamlit as st
import pandas as pd
from langchain.callbacks import StreamlitCallbackHandler

from prompt.tab5_prompt import (
    tab5_template_execute,
    tab5_template_inspect,
    tab5_template_inspect_event,
    tab5_template_inspect_final,
)


def run(tab):
    with tab:
        st.header("log_data 전처리")

        # step0
        st.subheader("Step1. 현황 분석")
        load_btn0 = st.button("프롬프트 생성", key="tab5_load_btn0")
        if load_btn0:
            st.session_state["tab5_template_inspect"] = tab5_template_inspect()

        query0 = st.text_area(
            "위 버튼을 눌러주세요.",
            value=st.session_state["tab5_template_inspect"],
            key="tab5_text_area_step0",
        )
        query_btn0 = st.button("요청하기", key="tab5_query_btn0")

        if query_btn0:
            agent = st.session_state["python_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query0, callbacks=[st_cb])
                st.write(response)
                st.session_state.tab5_inspect_result = response

        # TODO::테스트 완료 후 삭제
        st.session_state.tab5_inspect_result = """
        Derivative strategies:

Age calculation, Age might be a factor in a person's financial stability and their likelihood to apply for a loan, 80%.
Income to loan ratio, It might indicate the user's ability to repay the loan, 90%.
Credit utilization, It might indicate the user's creditworthiness, 85%.
Time between account creation and loan application, It might indicate how quickly users decide to apply for a loan after joining the app, 70%.
Loan limit to desired amount ratio, It might indicate how realistic the user's loan expectations are, 75%.
        """

        # step1
        st.subheader("Step1. 현황 분석-이벤트 로그")
        load_btn1 = st.button("프롬프트 생성", key="tab5_load_btn1")
        if load_btn1:
            st.session_state[
                "tab5_template_inspect_event"
            ] = tab5_template_inspect_event()

        query1 = st.text_area(
            "위 버튼을 눌러주세요.",
            value=st.session_state["tab5_template_inspect_event"],
            key="tab5_text_area_step1",
        )
        query_btn1 = st.button("요청하기", key="tab5_query_btn1")

        if query_btn1:
            agent = st.session_state["python_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query1, callbacks=[st_cb])
                st.write(response)
                st.session_state.tab5_inspect_event_result = response

        # TODO::테스트 완료 후 삭제
        st.session_state.tab5_inspect_event_result = """
        The strategy to create useful derivatives from the preprocessed log data could involve creating new features that represent the ratio of 'Loan Application Process' events to 'Other Events' for each user, and a binary feature that indicates whether a user has ever completed the 'Loan Application Process' event. These new features could then be evaluated by merging them with the existing user data and assessing their impact on the performance of a predictive model.
                """

        # step2
        st.subheader("Step2. 전략 선택")
        load_btn2 = st.button("프롬프트 생성", key="tab5_load_btn2")
        if load_btn2:
            st.session_state[
                "tab5_template_inspect_final"
            ] = tab5_template_inspect_final()

        query2 = st.text_area(
            "위 버튼을 눌러주세요.",
            value=st.session_state["tab5_template_inspect_final"],
            key="tab5_text_area_step2",
        )
        query_btn2 = st.button("요청하기", key="tab5_query_btn2")

        if query_btn2:
            agent = st.session_state["python_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query2, callbacks=[st_cb])
                st.write(response)
                st.session_state.tab5_inspect_final_result = response

        # TODO::테스트 완료 후 삭제
        st.session_state.tab5_inspect_final_result = """
        selected strategies:
1. Age calculation: Age might be a factor in a person's financial stability and their likelihood to apply for a loan.
2. Income to loan ratio: It might indicate the user's ability to repay the loan.
3. Credit utilization: It might indicate the user's creditworthiness.
4. The ratio of 'Loan Application Process' events to 'Other Events' for each user: This could indicate the user's engagement with the loan application process.
5. A binary feature that indicates whether a user has ever completed the 'Loan Application Process' event: This could indicate the user's intent to apply for a loan.
                """

        # step3
        st.subheader("Step3. 전략 실행")
        load_btn3 = st.button("프롬프트 생성", key="tab5_load_btn3")
        if load_btn3:
            st.session_state["tab5_template_execute"] = tab5_template_execute()

        query3 = st.text_area(
            "요청을 입력하세요.",
            value=st.session_state["tab5_template_execute"],
            key="tab5_text_area_step3",
        )
        query_btn3 = st.button("요청하기", key="tab5_query_btn3")

        if query_btn3:
            agent = st.session_state["python_agent"]
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query3, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab5_execute_result = response
                print(st.session_state.tab5_execute_result)
