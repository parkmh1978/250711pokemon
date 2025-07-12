import streamlit as st
import requests

def is_valid_image_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200 and 'image' in response.headers.get('Content-Type', '')
    except:
        return False

def main():
    st.title("🌈 귀여운 포켓몬 도감 🎉")
    
    pokemon_info = {
        "피카츄": {
            "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
            "description": "⚡ 볼頰에 전기를 저장하는 귀여운 전기 쥐 포켓몬! 초당 100,000볼트의 전기를 방출할 수 있어요.",
            "emoji": "⚡",
            "type": "전기"
        },
        "이브이": {
            "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png",
            "description": "🐾 진화 능력이 뛰어난 아기 포켓몬! 8가지 형태로 진화할 수 있는 특별한 능력을 가졌어요.",
            "emoji": "🐾",
            "type": "노말"
        },
        "푸린": {
            "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png",
            "description": "🎤 노래를 부르면 상대방을 잠들게 하는 마법 같은 능력을 가진 핑크빛 포켓몬!",
            "emoji": "🎤",
            "type": "노말/요정"
        },
        "토게피": {
            "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/174.png",
            "description": "🥚 행운을 상징하는 귀여운 알 포켓몬! 행복하고 평화로운 에너지를 가지고 있어요.",
            "emoji": "🥚",
            "type": "요정"
        },
        "꼬르곤": {
            "url": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/190.png",
            "description": "🍃 나무 위에서 살아가는 다람쥐 포켓몬! 긴 꼬리로 균형을 잡고 나뭇가지 사이를 날아다녀요.",
            "emoji": "🍃",
            "type": "노말"
        }
    }
    
    valid_pokemon = {name: info for name, info in pokemon_info.items() if is_valid_image_url(info['url'])}
    
    if len(valid_pokemon) < 5:
        st.warning("일부 이미지 URL에 문제가 있습니다.")
    
    col1, col2 = st.columns(2)
    
    for idx, (name, info) in enumerate(valid_pokemon.items()):
        with col1 if idx % 2 == 0 else col2:
            st.subheader(f"{info['emoji']} {name} 포켓몬")
            st.image(info['url'], use_container_width=True)
            
            with st.expander(f"{name} 상세 정보"):
                st.write(info['description'])
                st.write(f"타입: {info['type']}")
                
                if st.button(f"{name} 좋아요!", key=name):
                    st.balloons()
    
    st.markdown("### 🌟 당신의 귀여운 포켓몬은 무엇인가요? 🌟")

    # 이미지 업로드 섹션
    st.markdown("### 🌟 나만의 특별한 사진 업로드 🌟")
    
    uploaded_file = st.file_uploader(
        "혜인 백일 사진을 업로드해주세요 👶", 
        type=['png', 'jpeg', 'jpg'], 
        help="최대 10MB까지 업로드 가능합니다."
    )
    
    if uploaded_file is not None:
        # 이미지 용량 제한 (10MB)
        if uploaded_file.size > 10 * 1024 * 1024:
            st.error("이미지 크기가 너무 큽니다. 10MB 이하로 업로드해주세요.")
        else:
            # 이미지 표시
            st.subheader("🎉 업로드된 혜인이 사진 🎉")
            st.image(uploaded_file, use_container_width=True)
            
            # 추가 정보 입력 칸
            baby_name = st.text_input("아기 이름을 알려주세요", placeholder="혜인")
            birthday = st.date_input("백일 날짜를 선택해주세요")
            
            # 추가 설명 입력
            description = st.text_area("혜인이의 특별한 점을 알려주세요", 
                                       placeholder="예: 웃음이 너무 귀여워요!")
            
            # 공유 버튼
            if st.button("📸 혜인이 사진 공유하기"):
                st.success(f"{baby_name}의 소중한 순간을 축하합니다! 🎊")
                st.balloons()

if __name__ == "__main__":
    main()
