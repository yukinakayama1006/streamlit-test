import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Display Image')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iterration {i+1}')
    bar.progress(i)
    time.sleep(0.01)

'Done!!!'

# left_column, right_column = st.beta_columns(2)
left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')



# text = st.text_input('あなたの趣味は？')
# 'あなたの趣味は', text, 'です'

# condition = st.slider('あなたの今の調子は？',0, 100, 50)
# 'あなたの調子は', condition, 'です'



# text = st.sidebar.text_input('あなたの趣味は？')
# 'あなたの趣味は', text, 'です'

# condition = st.sidebar.slider('あなたの今の調子は？',0, 100, 50)
# 'あなたの調子は', condition, 'です'



# condition = st.slider('あなたの今の調子は？',0, 100, 50)
# 'あなたの調子は', condition, 'です'

# text = st.text_input('あなたの趣味は？')
# 'あなたの趣味は', text, 'です'



# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 11))
# )

# 'あなたの好きな数字は、', option, 'です'


# if st.checkbox('Show Image'):
#     img = Image.open('test.png')
#     st.image(img, caption='test image', use_column_width=True)






# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )

# st.map(df)



# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# st.line_chart(df)

# st.area_chart(df)

# st.bar_chart(df)





# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })


# # st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=300, height=100)

# st.table(df)


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









