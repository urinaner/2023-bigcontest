import streamlit as st
from langchain.callbacks import StreamlitCallbackHandler

from prompt.tab6_prompt import (
    tab6_template_execute,
)


def run(tab):
    with tab:
        st.header("스케일링 및 인코딩")

        # step3
        st.subheader("Step. 실행")
        load_btn3 = st.button("프롬프트 생성", key="tab6_load_btn3")
        if load_btn3:
            st.session_state["tab6_template_execute"] = tab6_template_execute()

        query3 = st.text_area(
            "요청을 입력하세요.",
            value=st.session_state["tab6_template_execute"],
            key="tab6_text_area_step3",
        )
        query_btn3 = st.button("요청하기", key="tab6_query_btn3")

        if query_btn3:
            agent = st.session_state["python_agent"]
            with st.chat_message("assistant"):
                st_cb = StreamlitCallbackHandler(st.container())
                response = agent.run(query3, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.write(response)
                st.session_state.tab6_execute_result = response
                print(st.session_state.tab6_execute_result)
