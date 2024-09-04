import streamlit as st


def session_state_init():
    st.session_state["TEMPERATURE"] = 0.0
    st.session_state["GPT_MODEL"] = "gpt-3.5-turbo-16k"

    if "python_agent" not in st.session_state:
        st.session_state.python_agent = None
    if "python_agent_3" not in st.session_state:
        st.session_state.python_agent_3 = None

    # TODO::탭마다 채팅세션 분리
    if "result" not in st.session_state:
        st.session_state["result"] = " "
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # tab1
    if "tab1_template_plain" not in st.session_state:
        st.session_state.tab1_template_plain = " "
    if "tab1_merge_agent" not in st.session_state:
        st.session_state.tab1_merge_agent = None

    # tab2
    if "merged_df" not in st.session_state:
        st.session_state.merged_df = None
    if "log_df" not in st.session_state:
        st.session_state.log_df = None

    if "tab2_template_plain" not in st.session_state:  # if문 처리 해야함
        st.session_state.tab2_template_plain = " "
    if "tab2_merge_agent" not in st.session_state:
        st.session_state.tab2_merge_agent = None
    st.session_state["tab2_step1_result"] = " "

    st.session_state["tab2_strategy"] = " "
    if "tab2_strategy_chain" not in st.session_state:
        st.session_state.tab2_strategy_chain = None
    st.session_state["tab2_step2_result"] = " "

    st.session_state["tab2_code"] = " "
    if "tab2_code_chain" not in st.session_state:
        st.session_state.tab2_code_chain = None
    st.session_state["tab2_step3_result"] = " "

    if "tab2_template_execute" not in st.session_state:
        st.session_state.tab2_template_execute = " "
    if "tab2_execute_agent" not in st.session_state:
        st.session_state.tab2_execute_agent = None
    st.session_state["tab2_step4_result"] = " "

    if "tab2_log_template" not in st.session_state:
        st.session_state.tab2_log_template = " "
    if "tab2_log_agent" not in st.session_state:
        st.session_state.tab2_log_agent = None
    st.session_state["tab2_step5_result"] = " "

    # tab3
    if "merged_processed_df" not in st.session_state:
        st.session_state.merged_processed_df = None

    st.session_state["tab3_strategy"] = " "
    if "tab3_strategy_chain" not in st.session_state:
        st.session_state.tab3_strategy_chain = None
    st.session_state["tab3_step1_result"] = " "

    st.session_state["tab3_code"] = " "
    if "tab3_code_chain" not in st.session_state:
        st.session_state.tab3_code_chain = None
    st.session_state["tab3_step2_result"] = " "

    if "tab3_template_execute" not in st.session_state:
        st.session_state.tab3_template_execute = " "
    if "tab3_execute_agent" not in st.session_state:
        st.session_state.tab3_execute_agent = None
    st.session_state["tab3_step3_result"] = " "
    # tab3 log
    st.session_state["tab3_log_strategy"] = " "
    if "tab3_log_strategy_chain" not in st.session_state:
        st.session_state.tab3_log_strategy_chain = None
    st.session_state["tab3_log_step1_result"] = " "

    st.session_state["tab3_log_code"] = " "
    if "tab3_log_code_chain" not in st.session_state:
        st.session_state.tab3_log_code_chain = None
    st.session_state["tab3_log_step2_result"] = " "

    if "tab3_log_template_execute" not in st.session_state:
        st.session_state.tab3_log_template_execute = " "
    if "tab3_log_execute_agent" not in st.session_state:
        st.session_state.tab3_log_execute_agent = None
    st.session_state["tab3_log_step3_result"] = " "

    # tab4
    if "log_data_drop" not in st.session_state:
        st.session_state.log_data_drop = None

    if "tab4_template_inspect" not in st.session_state:
        st.session_state.tab4_template_inspect = " "
    if "tab4_inspect_agent" not in st.session_state:
        st.session_state.tab4_inspect_agent = None
    st.session_state["tab4_inspect_result"] = " "

    if "tab4_template_execute" not in st.session_state:
        st.session_state.tab4_template_execute = " "
    if "tab4_execute_agent" not in st.session_state:
        st.session_state.tab4_execute_agent = None
    st.session_state["tab4_execute_result"] = " "

    # tab5
    if "tab5_template_inspect" not in st.session_state:
        st.session_state.tab5_template_inspect = " "
    st.session_state["tab5_inspect_result"] = " "

    if "tab5_template_inspect_event" not in st.session_state:
        st.session_state.tab5_template_inspect_event = " "
    st.session_state["tab5_inspect_event_result"] = " "

    if "tab5_template_inspect_final" not in st.session_state:
        st.session_state.tab5_template_inspect_final = " "
    st.session_state["tab5_inspect_final_result"] = " "

    if "tab5_template_execute" not in st.session_state:
        st.session_state.tab5_template_execute = " "
    st.session_state["tab5_execute_result"] = " "

    # tab6
    if "tab6_template_execute" not in st.session_state:
        st.session_state.tab6_template_execute = " "
    st.session_state["tab6_execute_result"] = " "

    # tab7
    if "tab7_template_execute" not in st.session_state:
        st.session_state.tab7_template_execute = " "
    st.session_state["tab7_execute_result"] = " "

    # tab8
    if "tab8_template_execute" not in st.session_state:
        st.session_state.tab8_template_execute = " "
    st.session_state["tab8_execute_result"] = " "

    # tab9
    if "tab9_template_inspect" not in st.session_state:
        st.session_state.tab9_template_inspect = " "
    st.session_state["tab9_inspect_result"] = " "

    if "tab9_template_execute" not in st.session_state:
        st.session_state.tab9_template_execute = " "
    st.session_state["tab9_execute_result"] = " "
