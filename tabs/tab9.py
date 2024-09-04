import os

import streamlit as st
import pandas as pd
from langchain.callbacks import StreamlitCallbackHandler

from prompt.tab9_prompt import (
    tab9_template_execute,
    tab9_template_inspect,
)


def run(tab):
    with tab:
        st.header("추천 메시지")

        # step0
        st.subheader("Step1. 현황 분석")
        load_btn0 = st.button("프롬프트 생성", key="tab9_load_btn0")
        if load_btn0:
            st.session_state["tab9_template_inspect"] = tab9_template_inspect()

        query0 = st.text_area(
            "위 버튼을 눌러주세요.",
            value=st.session_state["tab9_template_inspect"],
            key="tab9_text_area_step0",
        )
        query_btn0 = st.button("요청하기", key="tab9_query_btn0")

        if query_btn0:
            agent = st.session_state["python_agent"]

            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query0, callbacks=[st_cb])
                st.write(response)
                st.session_state.tab9_inspect_result = response

        # TODO::테스트 완료 후 삭제
        st.session_state.tab9_inspect_result = """
        """

        # step3
        st.subheader("Step3. 전략 실행")
        load_btn3 = st.button("프롬프트 생성", key="tab9_load_btn3")
        if load_btn3:
            st.session_state["tab9_template_execute"] = tab9_template_execute()

        query3 = st.text_area(
            "요청을 입력하세요.",
            value=st.session_state["tab9_template_execute"],
            key="tab9_text_area_step3",
        )
        query_btn3 = st.button("요청하기", key="tab9_query_btn3")

        if query_btn3:
            agent = st.session_state["python_agent"]
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query3, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab9_execute_result = response
                print(st.session_state.tab9_execute_result)
