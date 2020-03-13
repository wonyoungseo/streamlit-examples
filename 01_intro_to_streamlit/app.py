## import Streamlit Library
import streamlit as st


## Title
st.title('Streamlit Tutorial')


## Header/Subheader
st.header('This is header')
st.subheader('This is subheader')


## Text
st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")


st.markdown("* * *")


## Markdown syntax
st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown header")
st.markdown("### This is a Markdown subheader")
st.markdown("- item 1\n"
            "   - item 1.1\n"
            "   - item 1.2\n"
            "- item 2\n"
            "- item 3")
st.markdown("1. item 1\n"
            "   1. item 1.1\n"
            "   2. item 1.2\n"
            "2. item 2\n"
            "3. item 3")


st.markdown("* * *")


## Latex
st.latex(r"Y = \alpha + \beta X_i")

## Latex-inline
st.markdown(r"회귀분석에서 잔차식은 다음과 같습니다 $e_i = y_i - \hat{y}_i$")


st.markdown("* * *")


## Error/Colorful Text
st.success("Successful")
st.info("Information!")
st.warning("This is a warning")
st.error("This is an error!")
st.exception("NameError('Error name is not defined')")


st.markdown("* * *")


## Load data
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris['target']
iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))

## Return table/dataframe
# table
st.table(iris_df.head())

# dataframe
st.dataframe(iris_df)
st.write(iris_df)


st.markdown("* * *")


##Show image
from PIL import Image
img = Image.open("files/example_cat.jpeg")
st.image(img, width=400, caption="Image example: Cat")

## Show videos
vid_file = open("files/example_vid_cat.mp4", "rb").read()
st.video(vid_file, start_time=2)

## Play audio file.
audio_file = open("files/loop_w_bass.mp3", "rb").read()
st.audio(audio_file, format='audio/mp3', start_time=10)


st.markdown("* * *")


## Widget
## Checkbox
if st.checkbox("Show/Hide"):
    st.text("체크박스가 선택되었습니다.")


st.markdown("* * *")


## Radio button
status = st.radio("Select status.", ("Active", "Inactive"))
if status == "Active":
    st.success("활성화 되었습니다.")
else:
    st.warning("비활성화 되었습니다.")


st.markdown("* * *")


# Select Box (ex)
occupation = st.selectbox("직군을 선택하세요.",
                          ["Backend Developer",
                           "Frontend Developer",
                           "ML Engineer",
                           "Data Engineer",
                           "Database Administrator",
                           "Data Scientist",
                           "Data Analyst",
                           "Security Engineer"])
st.write("당신의 직군은 ", occupation, " 입니다.")


st.markdown("* * *")


## MultiSelect
location = st.multiselect("선호하는 유투브 채널을 선택하세요.",
                          ("운동", "IT기기", "브이로그",
                           "먹방", "반려동물", "맛집 리뷰"))
st.write(len(location), "가지를 선택했습니다.")


st.markdown("* * *")


## Buttons
if st.button("About"):
    st.text("Streamlit을 이용한 튜토리얼입니다.")


st.markdown("* * *")


# Text Input
first_name = st.text_input("이름을 입력하세요.", "Type Here ...")
if st.button("Submit", key='first_name'):
    result = first_name.title()
    st.success(result)


# Text Area
message = st.text_area("메세지를 입력하세요.", "Type Here ...")
if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)


st.markdown("* * *")


## Date Input
import datetime
today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.", datetime.time())


st.markdown("* * *")


# Display Raw Code - one line
st.subheader("Display one-line code")
st.code("import numpy as np")

# Display Raw Code - snippet
st.subheader("Display code snippet")
with st.echo():
    # 여기서부터 아래의 코드를 출력합니다.
    import pandas as pd
    df = pd.DataFrame()



## Display JSON
st.subheader("Display JSON")
st.json({'name' : '민수', 'gender':'male', 'Age': 29})


st.markdown("* * *")


## Sidebars
st.sidebar.header("사이드바 메뉴")
st.sidebar.selectbox("메뉴를 선택하세요.",
                    ["데이터",
                     "EDA",
                     "코드"])


## Plotting
st.subheader("Matplotlib으로 차트 그리기")
iris_df[iris_df['target']=='virginica']['petal length (cm)'].hist()
st.pyplot()





