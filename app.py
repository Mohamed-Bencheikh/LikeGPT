import streamlit as st
import openai
st.title('Welcome to :blue[LikeGPT]')
st.subheader('your AI assistant')

openai.api_key = st.secrets['OPENAI_API_KEY']
openai.organization = 'org-eAOUVxljdBHPYMZAJYP92RJx'
prompt = st.chat_input(placeholder='Your message goes here.', key='msg')
if prompt:
    res = openai.Completion.create(model='text-davinci-003', prompt=prompt)
    st.divider()
    output = res['choices'][0]['text']
    st.divider()
    st.markdown(f':green[{output}]')
