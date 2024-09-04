import streamlit as st


def appsidebar():
    st.sidebar.title("설정🛠")

    select_model = st.sidebar.selectbox(
        "에이전트에 사용할 모델을 선택하세요",
        ["gpt-3.5-turbo-16k", "gpt-3.5-turbo", "gpt-4"],
        index=0,
    )
    st.session_state["GPT_MODEL"] = select_model
    st.sidebar.write("선택한 모델: " + select_model)
    print(st.session_state["GPT_MODEL"])
    st.sidebar.write("경고: gpt-4는 과도한 요금이 발생할 수 있습니다.")

    st.session_state["TEMPERATURE"] = st.sidebar.slider("temperature", 0.0, 1.0, 0.0)
    print(st.session_state["TEMPERATURE"])

    start_button = st.sidebar.button("설정 적용 📊 ")
    if start_button:
        st.sidebar.success("Settings Applied!")
        st.balloons()
