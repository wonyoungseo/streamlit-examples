# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import pytz
from datetime import datetime, timedelta
from utils.generate_excel_download_link import to_excel, get_download_link


def get_pred_result():
    df = pd.read_csv('sample-dataset/sample_pred_sentiment_rating.txt', sep='\t', encoding='utf-8')
    return df

def get_qc_missing_date(df):
    qc_missing_date = list(df.date.unique())
    return qc_missing_date


def create_qc_template(start_date, end_date, df):
    start_date = str(start_date)
    end_date = str(end_date)

    after_start_date = df["date"] >= start_date
    before_end_date = df["date"] <= end_date
    between_two_dates = after_start_date & before_end_date
    filtered_dates = df.loc[between_two_dates].copy()



    st.markdown("* * *")
    st.subheader("**QC File Summary**")
    st.markdown("- QC Date range: **{0}** ~ **{1}**".format(
        start_date.replace("-", ""),
        end_date.replace("-", "")
    ))
    st.markdown("- Total counts: {}".format(len(filtered_dates)))

    st.markdown("**QC File Preview**")
    st.dataframe(filtered_dates)
    st.markdown("* * *")

    if len(filtered_dates) == 0:
        st.subheader("No articles to be QC.")
    else:
        qc_file_name = "pred-result-QC_{0}-{1}.xlsx".format(start_date.replace('-', ''),
                                                     end_date.replace('-', ''))
        st.subheader("**Download table to `.xlsx` format.**")
        st.markdown("**Click** link below and **save file as** {}`".format(qc_file_name))
        st.markdown("(**아래 링크를 클릭 후** 엑셀파일을 `{}`으로 저장하세요)".format(qc_file_name))
        st.markdown(get_download_link(filtered_dates, qc_file_name), unsafe_allow_html=True)
        st.warning("QC를 시작하기 전에 꼭 가이드라인을 참조하세요!")


def display_page():
    CURR_TIME = datetime.now(tz=pytz.utc) + timedelta(hours=9)
    st.subheader("Today is {}".format(str(CURR_TIME)[:10]))

    df = get_pred_result()
    qc_missing_date = get_qc_missing_date(df)

    if len(qc_missing_date) == 0:
        st.success("Currently no article ready for QC.")
    else:
        st.warning("Current QC available date: `{}`".format(", ".join(qc_missing_date)))

    st.markdown('\n')

    start_date = st.date_input(label='QC START DATE')
    end_date = st.date_input(label='QC END DATE')

    if st.button(label='Set date'):
        create_qc_template(start_date, end_date, df)