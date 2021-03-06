# -*- coding: utf-8 -*-

import streamlit as st
from utils import auth
from menu import page_main
from menu import page_gen_qc_template
from menu import page_upload_qc_result



def build_header(title_text):
    st.title(title_text)



def create_layout():
    auth_result = auth.authenticate_ver_simple()

    if auth_result == "success":
        st.sidebar.title("Menu")
        page = st.sidebar.selectbox(
            "Please select a page",
            [
                "Main",
                "Download - QC Template",
                "Upload - QC Result"
            ],
        )
        if page == "Main":
            build_header("영화 댓글 감성분석 결과 QC 툴")
            page_main.display_page()

        elif page == "Download - QC Template":
            build_header("Download QC Template File")
            page_gen_qc_template.display_page()

        elif page == "Upload - QC Result":
            build_header("Upload QC Result")
            page_upload_qc_result.display_page()

    elif auth_result == "failed":
        st.sidebar.warning("올바른 인증 정보를 입력하세요.")


def main():

    st.set_page_config(
        page_title="Sample File Uploader",
        initial_sidebar_state="expanded",
    )

    # adjust sidegar upper padding
    st.markdown("""
        <style>
        .css-1aumxhk {
            padding: 0em 1em;
        }
        </style>
    """, unsafe_allow_html=True)


    create_layout()

if __name__ == "__main__":
    main()