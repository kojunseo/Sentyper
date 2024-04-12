"""
1개의 문장만을 받아서 문장의 유형을 분석합니다. 

Type1: 주동/능동문
Type2.a: 단형 사동문 (inflection)
Type2.b: 단형 피동문 (passive)

Type3.a: 장형 사동문 (inflection) 
Type3.b: 장형 피동문 (passive)

유의점: 끌려가다 / 잡혀가다 -> 끌려V가다/잡혀V가다 로 표기해야함 (예시 찾아야할듯)
* 동사의 길이가 3개 이상이 될 경우 중간에 (이히리기우구추 + 여혀워)
"""


def _detect_type_2(tokens) -> bool:
    """
    단형 사동/피동문
    """
    target_suffix = ["이", "히", "리", "기", "우", "구", "추"]
    exception_verbs = ["때리"]

    object_flag = False
    suffix_flag = False
    for token in tokens:
        if token.tag == "VV": # 동사인 것들 중
            if token.form[-1] in target_suffix and token.form not in exception_verbs:
                suffix_flag = True
        if token.tag == "JKO": # 목적어가 있을 경우 -> 사동문 / 목적어가 부사로 교체되는 경우 -> 피동문
            object_flag = True
    return suffix_flag, "inflection" if object_flag else "passive"


def _detect_type_3(tokens) -> bool:
    """
    장형 사동/피동문
    """
    object_flag = False
    suffix_flag = False

    for t_idx in range(len(tokens)):
        if t_idx+2 < len(tokens) and tokens[t_idx].tag[:2] == "VV" and tokens[t_idx+1].tag == "EC" and tokens[t_idx+2].tag[:2] in ["VX", "VV"]:
            if tokens[t_idx+1].form == "게" and tokens[t_idx+2].form == "하":
                suffix_flag = True
        if tokens[t_idx].tag == "JKO":
            object_flag = True        

    return suffix_flag, "inflection" if object_flag else "passive"
