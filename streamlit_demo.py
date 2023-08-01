"""
# My first App
"""

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time
import os

#Basic function demo
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is a text')
st.markdown('Streamlit is **_really_ cool**.')

path = r'./data'

if not os.path.exists(path):
    os.makedirs(path)

uploadedfile = st.file_uploader('File uploader')
if uploadedfile is not None:
    with open(r'./data/'+uploadedfile.name, 'wb') as f:
        f.write(uploadedfile.getbuffer())

data_entry = st.text_area('Area for textual entry')
with open('./data/data.txt', 'a+') as file:
    file.write(data_entry + '\n')

# 如果int, 指定要插入的列数，并且所有列的宽度相等。
# 如果一个数字列表, 为每个数字创建一列，每列的宽度与提供的数字成比例。数字可以是整数或浮点数，但它们必须是正数。
# 下例中col1占表格1/6宽度，col2占表格1/6宽度，col3占表格4/6宽度，
col1, col2, col3 = st.columns([1,1,4])
with col1:
    #如果st.button被点击
    if st.button('Clear'):
        with open('./data/data.txt', 'w') as file:
            file.write('')
with col2:
    with open('./data/data.txt') as f:
        st.download_button('Download', f)

code = '''
    def hello():
        print('Hello, Streamlit!')
'''
st.code(code, language='python')

data = 'just a test'

# st.button('Hit me')     #button 方法返回一布尔值，表示迎按钮是否被点击
if st.button('Hit me'):
    st.write('Button is clicked')

# st.download_button('On the dl', data)
st.checkbox('Check me out')

# st.radio('Radio', [1,2,3])
rd = st.radio('Radio', [1,2,3])
for item in [1,2,3]:
    if item == rd:
        st.write(f'your selection is {item}')

st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
# st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
# st.file_uploader('File uploader')
# st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')

date = st.date_input('when is your birthday?', datetime.date(2019, 7, 6))
st.write('Your birthday is:', date)


#Checkbox demo
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

#selectbox demo
df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2':['a', 'b', 'c', 'd']
})
option = st.selectbox(
    'Which number do you like best?',
     df['col1'])

'You selected: ', option

#selectBox in sidebar
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['col2'])

'You selected:', option

#show map demo
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df)


df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=('a','b','c')
)
st.dataframe(df.style.highlight_max(axis=0))

#put a placeholder
my_placeholder = st.empty()
# Now replace the placeholder with some text:
my_placeholder.text("Hello world!")


#show information
st.info('This is a purely informational message')

#show exection, wait for annimation
with st.spinner('Wait for it...'):
    time.sleep(5)

st.success('Done!')

#progress bar example
iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    iteration.text(f'Iteration {i+1}')
    # iteration.text('Iteration %d'%(i+1))
    bar.progress(i+1)
    time.sleep(0.1)
st.write('... and now we are done!!!')
