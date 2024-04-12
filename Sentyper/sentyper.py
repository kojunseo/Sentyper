from kiwipiepy import Kiwi, Match
from .simple import _detect_type_2, _detect_type_3 # 단문 분석
from .complex import _detect_embedded_sentence, _detect_connection_sentence
from .help import help

kiwi = Kiwi()

def analyze_sentence_type(text):
    tokens = kiwi.tokenize(text, match_options=Match.SPLIT_COMPLEX | Match.ALL)
    
    # 복문인 경우 탐지
    # 내포문과 접속문을 엄밀히 구분하기 쉽지 않음

    is_connected = _detect_connection_sentence(tokens)
    if is_connected:
        return f"Complex::Connected" # 접속문
    
    is_embeded, which_type = _detect_embedded_sentence(tokens)
    if is_embeded:
        return f"Complex::Embedded->{which_type}" # 내포문
    
    # 단문인 경우 탐지
    # 내포문과 접속문이 아닌 경우 단문으로 간주
    is_type3, which_type = _detect_type_3(tokens)
    if is_type3:
        return f"Simple::Type3->{which_type}"

    is_type2, which_type = _detect_type_2(tokens)
    if is_type2:
        return f"Simple::Type2->{which_type}"
    
    return "Simple::Normal"


def analyze_sentences_type(text, use_help=False):
    """
    문장을 받아서 문장을 분리합니다. 
    """
    sentences = kiwi.split_into_sents(text)
    if use_help:
        return [(sent.text, help(analyze_sentence_type(sent.text))) for sent in sentences]
    else:
        return [(sent.text, analyze_sentence_type(sent.text)) for sent in sentences]
