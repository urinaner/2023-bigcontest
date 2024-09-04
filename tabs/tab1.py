import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from agent.tab1_agent import tab1_init_agent
from prompt.tab1_prompt import get_tab1_template_plain


def run(tab1):
    with tab1:
        st.subheader("Step1. csv 파일 로드 및 병합")
        load_btn = st.button("파일 불러오기", key="tab1_load_btn")
        if load_btn:
            tab1_init_agent()

        query = st.text_area("요청을 입력하세요.", value=get_tab1_template_plain())
        query_btn = st.button("요청하기", key="tab1_query_btn")

        for msg in st.session_state.messages:
            if msg["role"] == "assistant":
                st.chat_message(msg["role"]).write(msg["content"])

        if query_btn:
            if not st.session_state["tab1_merge_agent"]:
                st.write("'파일 불러오기' 버튼을 먼저 눌러주세요.")
                return

            st.session_state.messages.append({"role": "User", "content": query})
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = st.session_state["tab1_merge_agent"].run(
                    st.session_state.messages, callbacks=[st_cb]
                )
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
