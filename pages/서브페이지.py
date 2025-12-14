import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="하교수의 Streamlit",   # 브라우저 탭 제목
    page_icon="🎓",                   # 탭 아이콘
    layout="wide",                   # wide 또는 centered
    initial_sidebar_state="expanded", # 사이드바 기본 표시 상태
    menu_items={                     # 우측 상단 메뉴 구성
        'Get help': 'https://docs.streamlit.io',
        'Report a bug': 'https://streamlit.io',
        'About': (
            "### 하정훈 교수 \n"
            "[홍익대학교 산업·데이터공학과]"
            "(https://ie.hongik.ac.kr/ie/0201.do?mode=view&deptCd=AAB530&S1=2006&S2=10077)"
        )
    }
)

# 사이드바 설정
st.sidebar.title('다양한 사이드바 위젯들')

# 체크박스
st.sidebar.checkbox('외국인 포함')
st.sidebar.checkbox('고령인구 포함')

# 구분선
st.sidebar.divider()

# 라디오 버튼
gender = st.sidebar.radio('데이터 타입', ['전체', '남성', '여성'])

# 슬라이더
age_range = st.sidebar.slider('나이', 0, 100, (20, 50))

# 셀렉트박스
region = st.sidebar.selectbox('지역', ['서울', '경기', '인천', '대전', '대구', '부산', '광주'])
