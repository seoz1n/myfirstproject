import streamlit as st

# ✅ 반드시 가장 위에서 설정
st.set_page_config(page_title="MBTI 선물 추천", page_icon="🎁")

# 🎁 페이지 제목
st.title("🎁 MBTI 기반 선물 추천 사이트")

# 🎯 MBTI별 선물 추천 딕셔너리
mbti_gift_recommendations = {
    "INTJ": "📓 프리미엄 다이어리, ✒️ 고급 만년필, ♟️ 전략 보드게임",
    "INTP": "🧩 퍼즐, 📚 독특한 책, 🔧 실험 키트",
    "ENTJ": "⌚ 스마트 워치, 💼 노트북 가방, 📈 자기계발서",
    "ENTP": "📒 아이디어 노트, 🚁 드론, ✈️ 즉흥 여행 티켓",
    "INFJ": "🕯️ 향초, 💌 감성 편지, 📘 일기장",
    "INFP": "🎨 핸드메이드 소품, 📖 문학책, 💌 엽서 세트",
    "ENFJ": "🌸 플라워 박스, 🛠️ DIY 키트, 💝 감사 카드",
    "ENFP": "📷 폴라로이드 카메라, 🌈 무드등, 📎 스티커북",
    "ISTJ": "🕰️ 기능성 시계, 📁 정리 아이템, 📱 전자책 리더기",
    "ISFJ": "🧣 포근한 담요, ☕ 머그컵 세트, 🍪 수제 쿠키",
    "ESTJ": "🖋️ 고급 펜, 💳 명함지갑, 🖨️ 사무용 소형 가전",
    "ESFJ": "🎉 파티용품, 🥂 커플 머그, 🏡 홈데코 아이템",
    "ISTP": "🛠️ 멀티툴, 🚗 차량용 액세서리, 🏕️ 아웃도어 기어",
    "ISFP": "🖼️ 아트북, 🕯️ 캔들 키트, 🎨 감성 포스터",
    "ESTP": "🎧 무선 이어폰, 🏋️‍♂️ 스포츠 용품, 💪 피트니스 기어",
    "ESFP": "💡 LED 거울, 🔊 블루투스 스피커, ✨ 네온 조명"
}

# ✅ 사용자 입력
st.header("1️⃣ 당신의 MBTI를 선택하세요")
selected_mbti = st.selectbox("MBTI 유형 선택", [""] + list(mbti_gift_recommendations.keys()))

# ✅ 결과 출력
if selected_mbti:
    st.subheader(f"🎀 {selected_mbti} 유형에게 추천하는 선물:")
    st.write(mbti_gift_recommendations[selected_mbti])


