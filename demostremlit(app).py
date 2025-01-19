import streamlit as st

st.title('welcome guys')

st.image('plot.png')

#header
st.header('machine learning')

#sub header
st.subheader(' quantum computing')
#for info
st.info('information deatils of above things')
# waring
st.warning('learn about it')

st.write('employee name')
st.write(range(50))
# error message
st.error('everthing is wrong')
st.success('we achieved')
st.markdown('# akhilesh')
st.markdown('## akhilesh')
st.markdown(':moon:')
st.text('1/0')

# caption
st.caption('live')

# math eq
st.latex(r'''a+b x^2+''')

#widgets

#checkbox
st.checkbox('login')

#button
st.button('click')

#radio
st.radio('pick your gender',['male','female'])

#select
st.selectbox('pick your course',['ML','clousd','cybersec'])

#multiselct
st.multiselect('choose the dept',['content','sales','marketing'])

st.select_slider('rating',['bad','good','execellent'])

st.slider('enter no.',0,10)

#input
st.number_input('enter no.',0,100)

st.text_input('enter mail')

st.date_input('open')

st.time_input('hey whats the timing')

st.text_area('welcome for typing')

st.file_uploader('upload your file')

st.color_picker('color')

st.progress(90)

#spinner
import time as t
with st.spinner('just wait'):
    t.sleep(2)

#ballon
st.balloons()

st.sidebar.title('welcome to grenville')
st.sidebar.text_input('enter mailid')
st.sidebar.text_input('enter password')
st.sidebar.button('submit')
st.sidebar.radio('professional expert',['student','working','others'])

#data vis
import pandas as pd
import numpy as np
st.title('bar chart')
data=pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)

st.title('line chart')
st.line_chart(data)

st.title('area chart')
st.area_chart(data)