
def _detect_embedded_sentence(tokens) -> tuple[bool, str]:
    """
    복문 중 내포문을 탐색합니다.

    (명사절 내포문) <그가 범인임>이 밝혀졌다.
    (관형사절 내포문) <내가 본 영화는> 재미있었다.
    (부사절 내포문) 동규는 <잘생겨서> 인기가 많다.
    (서술절 내포문) 할아버지는 <코가 길다>.
    (인용절 내포문) 친구가 나에게 <시간 약속을 꼭 지키라고> 했다.
    """

    noun_emb_flag = False
    adj_emb_flag = False
    adv_emb_flag = False
    describe_emb_flag = False
    quote_emb_flag = False

    adv_ECs = ["어서", "으며", "면서", "자", "마자", "느라고", "다"]
    quote_ECs = ["라고", "다고", "냐고", "자고"]

    count_Vs = 0
    count_JKSs = 0
    count_JXs = 0

    for i, token in enumerate(tokens):
        # 명사절 내포문
        if token.tag == "ETN":
            noun_emb_flag = True
        
        # 관형사절 내포문
        if token.tag == "ETM":
            adj_emb_flag = True

        if token.tag == "EC":
            # 부사절 내포문
            if token.form in adv_ECs:
                adv_emb_flag = True
            # 인용절 내포문
            elif token.form in quote_ECs:
                quote_emb_flag = True

        if token.tag[:2] == "VV" or token.tag[:2] == "VA":
            count_Vs += 1
        if token.tag == "JKS" and token.form in ["은", "는", "이", "가"]:
            count_JKSs += 1
        if token.tag == "JX" and not tokens[i-1].tag == "JKS" and token.form in ["은", "는", "이", "가"]:
            count_JXs += 1

    if count_Vs < count_JKSs + count_JXs:
        describe_emb_flag = True

    which_type = "noun" if noun_emb_flag else "adj" if adj_emb_flag else "adv" if adv_emb_flag else "quote" if quote_emb_flag else "describe" if describe_emb_flag else "none"

    return noun_emb_flag or adj_emb_flag or adv_emb_flag or quote_emb_flag or describe_emb_flag, which_type



def _detect_connection_sentence(tokens) -> bool:
    """
    복문 중 접속문을 탐색합니다.

    """
    possible_ECs = ["고", "며", "으며", "으면서", "면서", "자", "나", "으나", "지만", "거나", "은데", "ᆫ데"]
    connection_flag = False
    for i, token in enumerate(tokens):
        if i+1<len(tokens) and token.tag == "EC" and token.form in possible_ECs and not tokens[i+1].tag in ["VX", "VV"]:
            connection_flag = True
    return connection_flag