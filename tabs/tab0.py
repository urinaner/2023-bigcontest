import streamlit as st
import os


def run(tab0):
    with tab0:
        st.write("작업 디렉토리 : " + os.getcwd())
        st.write("csv 파일을 최상단 work directory에 저장해주세요.")
        st.write("모든 버튼을 순차적으로 눌러주세요. 그렇지 않으면 오류가 발생합니다.")

        check = st.button("파일존재확인")

        if check:
            if os.path.isfile(os.getcwd() + "/user_spec.csv"):
                st.success("user_spec.csv 파일이 존재합니다.")
            else:
                st.error("user_spec.csv 파일이 존재하지 않습니다.")
            if os.path.isfile(os.getcwd() + "/loan_result.csv"):
                st.success("loan_result.csv 파일이 존재합니다.")
            else:
                st.error("loan_result.csv 파일이 존재하지 않습니다.")
            if os.path.isfile(os.getcwd() + "/log_data.csv"):
                st.success("log_data.csv 파일이 존재합니다.")
            else:
                st.error("log_data.csv 파일이 존재하지 않습니다.")
            if os.path.isfile(os.getcwd() + "/merged.csv"):
                st.error("경고 : merged.csv 파일이 이미 존재합니다. 삭제해주세요")
            else:
                st.success("merged.csv 파일이 존재하지 않습니다. 다음 탭에서 자동으로 머지를 진행할 것입니다.")
