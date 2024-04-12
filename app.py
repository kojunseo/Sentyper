import streamlit as st
import Sentyper


st.title("문장 분석기")

# st.subheader("문장이 주동/피동/내포문/접속절 중 어떤 문장인지 분석해드립니다.")


if value:= st.text_input("문장을 입력하세요. (엔터를 눌러 입력)"):
    sentences = Sentyper.analyze_sentences_type(value, use_help=True)
    for sentence in sentences:
        if len(sentence[0]) > 20:

            st.write(sentence[0][:20] + "...", ": ", sentence[1])
        else:
            st.write(sentence[0], ": ", sentence[1])
