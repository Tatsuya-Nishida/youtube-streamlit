import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)



#st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0) , width=300, height=300) #引数設定できる
# st.table(df.style.highlight_max(axis=0)) #ソートできない

# """ 
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """

# st.line_chart(df) #折れ線
# st.area_chart(df) #エリアチャート
#st.bar_chart(df) #棒グラフ

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69,139.70],
#     columns=['lat', 'lon'] #lat=緯度,lon=経度
# )

# st.map(df)

# st.write('Display Image')

# img = Image.open('C:\\Users\\t--n6\\OneDrive\\画像\\コメント 2020-06-19 155252.png')

# st.image(img, caption='Test', use_column_width=True)


#チェックボックス
# if st.checkbox('Show Image'):
#     img = Image.open('C:\\Users\\t--n6\\OneDrive\\画像\\コメント 2020-06-19 155252.png')
#     st.image(img, caption='Test', use_column_width=True)

#セレクトボックス
# option = st.selectbox(    
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、' , option , 'です。'

st.write('Interactive Widgets')

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


# text = st.text_input('あなたの趣味を教えてください。')

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は', text , 'ですね。'
# 'コンディション:', condition

