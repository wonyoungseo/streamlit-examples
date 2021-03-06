# -*- coding: utf-8 -*-

import os
from pathlib import Path
import re
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import pytz

FILE_SAVE_PATH = str(Path.home())+"/daily_qc_result/"




def test_submission_validity(df):
    col_check_no_blank = {
        "qc_result": None,
    }

    col_check_input_values = {
        "qc_result": None,
    }

    def check_result_no_blank(df, dict_no_blank):
        for column in dict_no_blank.keys():
            if df[column].isnull().values.any() or " " in list(df[column]):
                dict_no_blank[column] = False
            else:
                dict_no_blank[column] = True
        return dict_no_blank

    def check_input_validity(inputs, valid_check_type):

        valid_type = {
           'valid_qc_result' : ["ACCEPT", "REJECT"]
        }

        check = None
        inputs = inputs.astype('str').apply(lambda x: x.replace('.0', '')).unique()

        for element in inputs:
            if element not in valid_type[valid_check_type]:
                check = False
                break
            else:
                check = True

        return check

    def check_input_values(df, dict_input_values):
        dict_input_values["qc_result"] = check_input_validity(df['qc_result'], 'valid_qc_result')
        return dict_input_values

    result_no_blank = check_result_no_blank(df, col_check_no_blank)
    result_input_values = check_input_values(df, col_check_input_values)

    return result_no_blank, result_input_values


def return_test_pass(result_no_blank, result_input_values):
    list_test_result = []
    for key in result_no_blank.keys():
        if result_no_blank[key] == True:
            list_test_result.append(True)
        else:
            list_test_result.append(False)

    for key in result_input_values.keys():
        if result_input_values[key] == True:
            list_test_result.append(True)
        else:
            list_test_result.append(False)
    return np.all(list_test_result)


def return_qc_summary_overall(df):
    total_count = len(df)
    accept_count = len(df[df['qc_result'] == 'ACCEPT'])

    markdown_table = """
    |전체 기사 수| ACCEPT 기사 수 및 비율 |
    |:---:|:---:|
    | {0} | {1}({2}%) |
    """.format(
        total_count,
        accept_count,
        round(accept_count / total_count * 100, 2),
    )
    return markdown_table


def print_result(result_no_blank, result_input_values):
    def return_result(result):
        if result != True:
            return "**_Failed_**"
        else:
            return "**Passed**"

    text_result_no_blank = """**Test: No Blank**  
> Column `qc_result`: {0[0]}    
    """.format([return_result(result_no_blank[key]) for key in result_no_blank.keys()])

    text_result_input_values = """**Test: Input Value**  
> Column `qc_result`: {0[0]}    
    """.format([return_result(result_input_values[key]) for key in result_input_values.keys()])

    return text_result_no_blank, text_result_input_values


def append_upload_log(time, filename, user):

    line = "{} / {} / {}".format(
        time,
        filename,
        user)

    text_file = open(FILE_SAVE_PATH + "upload_log.txt", "a")
    text_file.write(line)
    text_file.write("\n")
    text_file.close()


def display_page():
    st.subheader("File Uploader")
    uploaded_file = st.file_uploader("Choose a file", type="xlsx")

    if uploaded_file is not None:
        filename_pattern = r"^pred-result-QC_\d{8}-\d{8}-upload\.xlsx$"
        if re.search(filename_pattern, uploaded_file.name) is None:
            st.error("File name format incorrect.")
            st.warning("Make sure your file name format is pred-result-QC_YYYYMMDD-YYYYMMDD-upload.xlsx")
        else:
            st.markdown("* * *")
            st.subheader("Preview QC Result")
            df = pd.read_excel(uploaded_file)
            st.dataframe(df)

            st.markdown("\n")

            st.subheader("QC Result Validity Test")
            result_no_blank, result_input_values = test_submission_validity(df)
            test_pass = return_test_pass(result_no_blank, result_input_values)
            result_no_blank, result_input_values = print_result(result_no_blank, result_input_values)

            st.markdown(result_no_blank)
            st.markdown(result_input_values)

            st.markdown("\n")

            if test_pass != True:
                st.error("QC파일에서 오류가 발생했습니다. QC파일을 다시 한번 확인해주십시오")
            else:
                st.markdown("* * *")
                st.subheader("QC Result Summary")

                st.markdown("**QC 결과 전체 요약**")
                st.markdown(return_qc_summary_overall(df))
                st.markdown("\n")

                st.markdown("* * *")


                st.subheader("QC 제출 전 셀프 체크")
                st.markdown("(예시)")
                check_1 = st.checkbox("셀프 체크 문항 1 : ex. 올바르게 기입했나요?")
                check_2 = st.checkbox("셀프 체크 문항 2 : ex. 부적절한 댓글을 제거했나요?")

                if not os.path.exists(FILE_SAVE_PATH):
                    os.makedirs(FILE_SAVE_PATH)

                if uploaded_file.name in os.listdir(FILE_SAVE_PATH):
                    st.error("QC file `{0}` 이 이미 제출된 바 있습니다. 중복 제출 여부를 확인하세요.".format(uploaded_file.name))
                else:
                    if check_1 and check_2:
                        st.markdown("\n")
                        st.subheader("QC 결과 제출하기")
                        user = st.selectbox("제출자를 선택하세요", ["홍길동", "김덕배", "무야호"])

                        if st.button("Save file"):
                            with st.spinner("Uploading ..."):
                                df.to_excel(FILE_SAVE_PATH + uploaded_file.name, index=False)
                                upload_time = str(datetime.now(tz=pytz.utc) + timedelta(hours=9))[:19]
                                append_upload_log(upload_time, uploaded_file.name, user)
                                st.success("QC가 성공적으로 제출되었습니다.")