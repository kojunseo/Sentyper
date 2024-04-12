# Sentyper
한국어 문장 종류 분석기입니다.


### 지원 가능한 문장

[img](./src/문장구분.png)

- 단문/복문 구분
- (능동/주동/사동/피동) 1. 능동/주동 | 2. 단형 사동/피동 | 3. 장형 사동/피동
- 접속문 여부 구분
- (내포문) 1. 명사절 | 2. 관형사절 | 3. 부사절 | 4. 서술절 | 5. 인용절

* 위 종류들에 대해 구분이 가능합니다.

### 설치방법
```bash
pip install git+https://github.com/kojunseo/Sentyper
```


### 사용방법1 - 파이썬

#### 여러개의 문장이 한개의 텍스트로 합쳐져 있는 경우
```python
import Sentyper

text2b = "그녀는 지금 끌려가고 있다." 
print(Sentyper.analyze_sentences_type(text2b, use_help=True))
```
* `use_help`를 `True`로 설정할 경우, 한국어 설명이 나오며 `False`로 할 경우 영어로 된 타입명이 나옵니다.


### 사용방법2 - Streamlit
```bash
python3 -m streamlit run app.py
```
* Streamlit으로 실행되며, 입력해볼 수 있는 웹페이지가 띄워집니다. (포트번호: 8501)