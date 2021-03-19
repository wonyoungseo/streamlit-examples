
# Demo App : 영화 댓글 감성분류 결과 QC 툴

## 1. 동작 시나리오

1. 영화 댓글 감성분류 이후 결과에 대한 QC 작업 템플릿을 엑셀파일로 생성
2. 생성한 템플릿에 분류 결과에 대한 ACCEPT/REJECT 여부를 기입
3. QC 결과 파일을 업로드


## 2. Dependency Library 설치

**Requirements**

python3.x

- pandas 
- streamlit 
- xlsxwriter
- openpyxl

**Install via `requirements.txt`**

```bash
pip install -r requirements.txt
```

## 3. 실행

```bash
streamlit run app.py
```
