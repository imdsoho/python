import re

#def multiBlank2SingleBlank(sentence:str) -> str:
def multiBlank2SingleBlank(sentence):
    """
    하나 이상의 공백을 한개로 변경합니다.
    :param sentence: 변경할 문자열
    :return: 
    """

    #if re.findall(" +", sentence):
    #    replace_str = re.sub(" +", " ", sentence)

    # 또는
    replace_str = re.sub(" +", ' ', sentence)

    return replace_str

sentence = "동해물과   백두산이 마르고  닳도록  하나님이     보호하사 우리나라  만세"

ret_str = multiBlank2SingleBlank(sentence)
print(ret_str)