import streamlit as st
import requests

def is_valid_image_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200 and 'image' in response.headers.get('Content-Type', '')
    except:
        return False

def main():
    st.title("귀여운 포켓몬 이미지")
    
    cute_pokemon_urls = [
        "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",  # 피카츄
        "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png",  # 이브이
        "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png",  # 푸린
        "https://assets.pokemon.com/assets/cms2/img/pokedex/full/174.png",  # 토게피
        "https://assets.pokemon.com/assets/cms2/img/pokedex/full/190.png"   # 꼬르곤
    ]
    
    valid_urls = [url for url in cute_pokemon_urls if is_valid_image_url(url)]
    
    if len(valid_urls) < 5:
        st.warning("일부 이미지 URL에 문제가 있습니다.")
    
    for idx, url in enumerate(valid_urls, 1):
        st.subheader(f"포켓몬 이미지 {idx}")
        st.image(url, use_column_width=True)

if __name__ == "__main__":
    main()
