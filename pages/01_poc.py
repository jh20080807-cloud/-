import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="🔮 MBTI별 찰떡 포켓몬 찾기!", page_icon="⚡", layout="centered")

# 제목과 소개
st.title("⚡ 내 MBTI와 닮은 포켓몬은 누구?")
st.subheader("16가지 MBTI 유형별 포켓몬과 성격 분석 완료! 📜")
st.write("안녕! 네 MBTI를 선택하면, 너랑 성격이 꼭 닮은 싱크로율 100% 포켓몬을 소개해 줄게! 궁금하지? 👇")

# MBTI별 포켓몬 데이터 (이미지 URL, 이름, 성격 특징)
pokemon_data = {
    "ISTJ": {
        "name": "레어코일 (Magneton)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/82.png",
        "desc": "규칙적이고 빈틈없는 너는 기계처럼 정확한 레어코일과 닮았어! 책임감이 강해서 맡은 일은 끝까지 완벽하게 해내는 모범생 타입이야. 🤖"
    },
    "ISFJ": {
        "name": "메가니움 (Meganium)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/154.png",
        "desc": "주변 사람들을 따뜻하게 챙겨주는 너는 치유의 에너지를 뿜어내는 메가니움이랑 찰떡! 다정다감하고 친구들의 이야기를 정말 잘 들어줘. 🌸"
    },
    "INFJ": {
        "name": "뮤 (Mew)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/151.png",
        "desc": "신비롭고 생각이 깊은 너는 전설의 포켓몬 뮤와 닮았어! 통찰력이 뛰어나서 사람들의 마음을 잘 꿰뚫어 보고, 세상을 더 따뜻하게 만들고 싶어 해. 🔮"
    },
    "INTJ": {
        "name": "뮤츠 (Mewtwo)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "desc": "엄청난 브레인을 가진 너는 냉철하고 전략적인 뮤츠와 똑 닮았어! 혼자 생각하는 걸 좋아하고, 목표를 세우면 엄청난 집중력으로 달성해 내지. 🎯"
    },
    "ISTP": {
        "name": "개굴닌자 (Greninja)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/658.png",
        "desc": "말수가 적지만 상황 판단이 빠르고 손재주가 좋은 너는 날렵한 개굴닌자 같아! 위기 상황에서도 당황하지 않고 쿨하게 해결하는 능력자야. 🥷"
    },
    "ISFP": {
        "name": "메타몽 (Ditto)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/132.png",
        "desc": "어디든 부드럽게 맞춰주는 너는 변신의 귀재 메타몽이야! 예술적인 감각이 있고, 평화를 사랑해서 주변 사람들을 편안하게 만들어주는 매력이 있어. 🎨"
    },
    "INFP": {
        "name": "이브이 (Eevee)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "desc": "무한한 가능성과 따뜻한 감수성을 가진 너는 이브이와 딱이야! 상상력이 풍부하고 착한 마음씨를 가졌으며, 자신만의 특별한 꿈을 소중히 간직하고 있어. 🌟"
    },
    "INTP": {
        "name": "후딘 (Alakazam)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/65.png",
        "desc": "끊임없이 질문하고 분석하는 지식인인 너는 IQ 5000의 후딘이야! 호기심이 엄청나서 관심 있는 분야는 밤을 새워서라도 파고드는 천재 스타일! 💡"
    },
    "ESTP": {
        "name": "루카리오 (Lucario)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "desc": "몸으로 부딪히는 걸 좋아하고 에너지가 넘치는 너는 파워풀한 루카리오야! 두려움 없이 도전을 즐기고, 실전에서 엄청난 능력을 발휘하는 행동파지! ⚡"
    },
    "ESFP": {
        "name": "피카츄 (Pikachu)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "desc": "어딜 가나 사랑받는 최고의 인기쟁이, 바로 피카츄가 너의 영혼의 동반자야! 낙천적이고 흥이 많아서 주변 사람들에게 늘 밝은 에너지를 뿜뿜 전파해! 🎉"
    },
    "ENFP": {
        "name": "푸린 (Jigglypuff)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "desc": "통통 튀는 매력과 호기심으로 가득 찬 너는 사랑스러운 푸린과 닮았어! 창의적이고 감정이 풍부해서 친구들을 즐겁게 만드는 아이디어 뱅크야. 🌈"
    },
    "ENTP": {
        "name": "팬텀 (Gengar)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "desc": "장난기 가득하고 두뇌 회전이 빠른 너는 개구쟁이 팬텀과 똑같아! 토론이나 말싸움에서 절대 지지 않고, 기발한 생각으로 사람들을 깜짝 놀라게 해. 👅"
    },
    "ESTJ": {
        "name": "윈디 (Arcanine)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "desc": "당당하고 리더십이 넘치는 너는 듬직한 호랑이 포켓몬 윈디야! 계획적이고 책임감이 강해서 무리를 이끄는 대장 역할을 완벽하게 소화해 내지. 🦁"
    },
    "ESFJ": {
        "name": "해피너스 (Blissey)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "desc": "정이 많고 사람들을 돕는 걸 행복해하는 너는 친절한 해피너스야! 리액션도 최고고 친구들의 고민을 자기 일처럼 걱정해 주는 다정한 친구지. 💝"
    },
    "ENFJ": {
        "name": "토게키스 (Togekiss)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/468.png",
        "desc": "평화와 행복을 전파하는 카리스마 리더인 너는 토게키스와 닮았어! 친구들을 이끄는 다정한 카리스마가 있고, 주변을 긍정적으로 변화시켜. ✨"
    },
    "ENTJ": {
        "name": "리자몽 (Charizard)",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "desc": "거대한 비전과 열정으로 무장한 통솔자인 너는 강력한 리자몽이야! 야망이 크고 자신감이 넘쳐서, 어떤 장애물이든 다 불태우고 나아가는 열정 가득한 리더지! 🔥"
    }
}

# 셀렉트 박스로 MBTI 선택 받기
mbti_list = list(pokemon_data.keys())
selected_mbti = st.selectbox("👉 네 MBTI는 뭐야? 골라봐!", mbti_list)

# 구분선
st.divider()

# 결과 보여주기
if selected_mbti:
    pokemon = pokemon_data[selected_mbti]
    
    # 예쁜 결과를 위한 풍선 이펙트! 🎉
    st.balloons()
    
    # 2개의 컬럼으로 나누어서 왼쪽엔 그림, 오른쪽엔 설명을 배치!
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        # 공식 포켓몬 일러스트 이미지 출력
        st.image(pokemon["image"], use_container_width=True)
        
    with col2:
        st.markdown(f"### 🐾 [{selected_mbti}]의 단짝 포켓몬")
        st.success(f"### **{pokemon['name']}**")
        st.write("")
        st.info(pokemon["desc"])

st.divider()
st.write("💡 *친구들의 MBTI 결과도 같이 확인해 보면 더 재밌을 거야! 단짝 포켓몬이랑 즐거운 하루 보내!* ⚡")
