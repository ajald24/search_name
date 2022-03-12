import streamlit as st
import pandas as pd

st.title('店舗情報検索アプリβ版')
st.markdown('### 検索ワード入力')

st.sidebar.title('オプション')
max_low=st.sidebar.slider('最大表示列',1,20)
action=st.sidebar.selectbox(
    '検索オプション',
    ('を含む','から始まる','で終わる')
)

df=pd.read_csv('新店面接会スケジュール - 面接会場.csv',encoding='utf-8')
df=df.loc[:,['店番','OP日','店名','店舗住所']]
search_columns=st.selectbox(
    '検索列',
    df.columns
)

search_word=st.text_input('検索ワードを入力してください：')
st.write(action)





def display(search_columns,action):
    if action=='を含む':
        output=df[df[search_columns].str.contains(str(search_word),na=False)]
    elif action=='から始まる':
        output=df[df[search_columns].str.startswith(str(search_word),na=False)]
    if action=='で終わる':
        output=df[df[search_columns].str.endswith(str(search_word),na=False)]
    st.table(output.reset_index(drop=True).head(max_low))
    st.write(f'{len(output)}店舗')

if st.button('検索'):
    display(search_columns,action)
