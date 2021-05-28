import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('Display Image')

'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')


# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせ回答')

# if st.checkbox('Show Image'):
#     img = Image.open('image.jpg')
#     st.image(img, caption='我老婆', use_column_width=True)



# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1, 11))
# )
# 'あなたが好きな数字は', option, 'です。'


text = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたが好きな趣味は', text

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

