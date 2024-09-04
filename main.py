from dotenv import load_dotenv
import streamlit as st

import tabs
from agent.tab_agent import python_agent, python_agent_3
from const.sessions import session_state_init
from ui.homescreen import home_screen
from ui.sidebar import appsidebar


load_dotenv()
session_state_init()

home_screen()
appsidebar()

python_agent()
python_agent_3()


(
    tab0,
    tab1,
    tab2,
    tab3,
    tab4,
    tab5,
    tab6,
    tab7,
    tab8,
    tab9,
) = st.tabs(
    [
        "Intro",
        "CSV병합",  # 1
        "결측치",  # 2
        "불필요열제거",  # 3
        "전처리",  # 4
        "파생변수",  # 5
        "스케일링.인코딩",  # 6
        "모델학습",  # 7
        "군집화",  # 8
        "추천메시지",  # 9
    ]
)

tabs.tab0.run(tab0)
tabs.tab1.run(tab1)
tabs.tab2.run(tab2)
tabs.tab3.run(tab3)
tabs.tab4.run(tab4)
tabs.tab5.run(tab5)
tabs.tab6.run(tab6)
tabs.tab7.run(tab7)
tabs.tab8.run(tab8)
tabs.tab9.run(tab9)
