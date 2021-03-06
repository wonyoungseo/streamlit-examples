# -*- coding: utf-8 -*-

import streamlit as st


def display_page():
    st.markdown('\n')
    st.markdown('\n')

    st.subheader("가이드라인")

    st.markdown('\n')

    with st.beta_expander("QC 파일"):
        st.markdown("""
    - 다운로드 QC 파일명은 `pred-result-QC_날짜-날짜.xlsx` 의 형태로 저장하세요.
    - QC가 완료된 파일명은 `pred-result-QC_날짜-날짜-upload.xlsx`의 형식으로 저장하세요.
            """)

    st.markdown('\n')
    st.markdown('\n')

    with st.beta_expander("QC 방법"):
        st.markdown("""
    1. 좌측 메뉴에서 `Download - QC Template` 페이지 선택 후 QC 파일을 다운로드 한다.
    2. `qc_result`에 예측 결과에 대한 ACCEPT/REJECT 여부를 기입한다.
    3. 좌측 메뉴에서 `Upload - QC Result` 페이지 선택 후 QC 결과 파일을 업로드 한다.
    """)

    st.markdown('\n')
    st.markdown('\n')

    with st.beta_expander("자주 하는 질문"):
        st.markdown("내용 없음")

    st.markdown('\n')
    st.markdown('\n')