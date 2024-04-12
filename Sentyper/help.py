def help(output_text) -> str:
    templates = ""

    output_text_split = output_text.split("::")
    if output_text_split[0] == "Complex":
        templates += "(복문) "
    elif output_text_split[0] == "Simple":
        templates += "(단문) "
    else:
        templates += "알 수 없는 문장입니다. 출력 결과를 확인하세요. [Error]"
        return templates
    
    if len(output_text_split[1].split("->")) == 1:
        if output_text_split[1] == "Connected":
            templates += "접속문"
        elif output_text_split[1] == "Normal":
            templates += "능동/주동문"


    elif output_text_split[1].split("->")[0] == "Embedded":
        # templates += "내포문입니다. 종류는 "
        the_type = output_text_split[1].split("->")[1]
        types = {
            "noun": "명사절 내포문",
            "adj": "관형사절 내포문",
            "adv": "부사절 내포문",
            "quote": "인용절 내포문",
            "describe": "서술절 내포문",
        }
        templates += types[the_type]
        # templates += types[the_type] + "입니다."
    else:
        the_level = output_text_split[1].split("->")[0]
        the_type = output_text_split[1].split("->")[1]
        levels = {
            "Type2": "단형",
            "Type3": "장형",
        }
        types = {
            "inflection": "사동문",
            "passive": "피동문",
        }
        templates += levels[the_level] + " " + types[the_type]


    return templates
    

