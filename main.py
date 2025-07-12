import streamlit as st

st.title("귀여운 포켓몬 실사 이미지")
st.write("실제로 존재하는 듯한 귀여운 포켓몬 이미지 5개를 보여줍니다.")

# 実際に存在するような、または公開されている可愛いポケモン画像のURL
# These URLs are examples. You might want to find more diverse or higher-quality images.
image_urls = [
    "https://assets.nintendo.com/image/upload/ar_16:9,b_white,c_pad,dpr_2.0,f_auto,q_auto,w_500/ncom/en_US/articles/2022/pokemon-scarlet-and-pokemon-violet-launch-on-nintendo-switch-november-18/230105_PokemonScarletViolet_Thumbnail", # 피카츄
    "https://assets.nintendo.com/image/upload/ar_16:9,b_white,c_pad,dpr_2.0,f_auto,q_auto,w_500/ncom/en_US/articles/2022/pokemon-scarlet-and-pokemon-violet-launch-on-nintendo-switch-november-18/230105_PokemonScarletViolet_Body_02", # 냐오하
    "https://assets.nintendo.com/image/upload/ar_16:9,b_white,c_pad,dpr_2.0,f_auto,q_auto,w_500/ncom/en_US/articles/2022/pokemon-scarlet-and-pokemon-violet-launch-on-nintendo-switch-november-18/230105_PokemonScarletViolet_Body_03", # 뜨아거
    "https://assets.nintendo.com/image/upload/ar_16:9,b_white,c_pad,dpr_2.0,f_auto,q_auto,w_500/ncom/en_US/articles/2022/pokemon-scarlet-and-pokemon-violet-launch-on-nintendo-switch-november-18/230105_PokemonScarletViolet_Body_04", # 꾸왁스
    "https://assets.nintendo.com/image/upload/ar_16:9,b_white,c_pad,dpr_2.0,f_auto,q_auto,w_500/ncom/en_US/articles/2022/pokemon-scarlet-and-pokemon-violet-launch-on-nintendo-switch-november-18/230105_PokemonScarletViolet_Body_05"  # 레전드 아르세우스 포켓몬 (히스이 가디)
]

for url in image_urls:
    st.image(url, caption="귀여운 포켓몬")

st.write("출처: 닌텐도 공식 웹사이트 및 게임 홍보 자료")
