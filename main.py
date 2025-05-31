import streamlit as st

# MBTI별 추천 여행 코스 데이터
mbti_travel_recommendations = {
    "INTJ": "조용하고 역사적인 도시, 예: 교토, 오스트리아 잘츠부르크",
    "INTP": "지적 탐험이 가능한 도시, 예: 옥스퍼드, 도쿄의 박물관 투어",
    "ENTJ": "계획적인 투어가 가능한 도시, 예: 싱가포르, 취리히",
    "ENTP": "다양한 체험이 있는 도시, 예: 샌프란시스코, 베를린",
    "INFJ": "자연과 예술이 있는 여행, 예: 아이슬란드, 포르투갈 포르투",
    "INFP": "감성적인 풍경과 문학적 공간, 예: 프라하, 브루즈",
    "ENFJ": "사람들과의 교류가 활발한 여행, 예: 바르셀로나, 방콕",
    "ENFP": "자유로운 분위기와 축제가 있는 곳, 예: 리우데자네이루, 암스테르담",
    "ISTJ": "계획적이고 질서 있는 여행, 예: 바젤, 도쿄",
    "ISFJ": "전통적인 문화 체험, 예: 교토, 세비야",
    "ESTJ": "활동적인 일정이 있는 여행, 예: 뉴욕, 싱가포르",
    "ESFJ": "사람들과 어울릴 수 있는 여행, 예: 파리, 나폴리",
    "ISTP": "모험적인 활동이 있는 여행, 예: 뉴질랜드 퀸스타운, 알래스카",
    "ISFP": "자연과 함께하는 힐링 여행, 예: 발리, 제주도",
    "ESTP": "익스트림 스포츠가 가능한 여행, 예: 인터라켄, 두바이",
    "ESFP": "엔터테인먼트가 가득한 여행, 예: 라스베이거스, 서울 홍대"
}

# 웹 앱 제목
st.title("MBTI 기반 여행 추천")

# 사용자에게 MBTI 선택받기
mbti_list = list(mbti_travel_recommendations.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_list)

# 선택 시 추천 여행지 출력
if selected_mbti:
    recommendation = mbti_travel_recommendations[selected_mbti]
    st.subheader(f"🎒 {selected_mbti} 타입을 위한 추천 여행 코스:")
    st.write(f"👉 {recommendation}")
