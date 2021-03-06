import streamlit as st


def authenticate_ver_simple():
    st.sidebar.title("Authentication")
    st.sidebar.text("인증정보를 입력하세요.")
    st.sidebar.text("\n")

    username = st.sidebar.text_input('Username')
    password = st.sidebar.text_input('Password', type='password')

    st.sidebar.markdown("""
이 페이지는 샘플페이지 입니다.  
다음 정보를 입력하세요.
    
> - `username` : hello
> - `password` : world    
    """)

    if username == 'hello' and password == 'world':
        auth_result = 'success'
    else:
        auth_result = 'failed'
    return auth_result