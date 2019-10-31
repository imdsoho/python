from urllib.parse import parse_qs
import re
import sysconfig

print(sysconfig.get_python_version())

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

#print(my_values)
# {'red': ['5'], 'blue': ['0'], 'green': ['']}

red = my_values.get('red', ['']) or 0     # 배열로 값을 전달
red = my_values.get('red', [''])[0] or 0   # 배열의 첫번째 값
opacity = my_values.get('opacity', [''])[0] or 0

#print(red)
#print(opacity)

#a = [1,2,3,4,5,6,7]
#b = a[:]

#c =[1,2,3,4,5]
#d = c
#c[:] = ['A','B','C']


def __remove_special_char_py3(query_str):
    '''
        한글 자음, 모음 및 특수문자를 제거
        공백 유지
    :param query_str: 
    :return: 
    '''
    if query_str is None or len(query_str) == 0:
        return query_str
    else:
        rm_not_hangul_list = []

        for ch in list('%s' % query_str):
            if not ((ord('ㄱ') <= ord(ch) <= ord('ㅎ')) or
                        (ord('ㅏ') <= ord(ch) <= ord('ㅣ'))):
                rm_not_hangul_list.append(ch)

        query_str = ''.join(rm_not_hangul_list).strip()

        #pattern = "[\\{\\}\\[\\]\\/?.;:|\\)*`!^_+<>@\\#$%&\\\=\\(\\'\"]"   # ~ 문자는 삭제되지 않음
        pattern = "[\\{\\}\\[\\]\\/?.;:|\\)*~`!^_+<>@\\#$%&\\\=\\(\\'\"]"   # ~ 문자 삭제

        query_str = re.sub(pattern, '', query_str)

    return query_str.strip()

query_str = "  ㄱ ㄴ ㄷ 대한민국 만세!! 3.1절 독립만세 운동 ~ News Topic..!!"
print(__remove_special_char_py3(query_str))


