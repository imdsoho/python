import re

org_word = "메밀"
input_cn_query = "+(+(((봉평메밀국수)^5.000) ((+(봉평) +(메밀국수를))^2.500) (+(봉평) +((메밀국수) (+(메밀) +(국수)))) (+(봉평) +(메밀국수))) +(((먹)^5.000) ((먹다)^2.500) (먹VV) (먹VV))) (((봉평) (메밀국수) (먹__02VV))^10.000) "
append_syn_word = "모밀 메밀"
only_syn_word = "['모밀']"

print("[1] ", org_word)
print("[2] ", input_cn_query)
print("[3] ", append_syn_word)
print("[4] ", only_syn_word)

if re.findall(org_word, input_cn_query):
    re.sub(org_word, append_syn_word, input_cn_query)

print("[1-] ", org_word)
print("[2-] ", input_cn_query)
print("[3-] ", append_syn_word)
print("[4-] ", only_syn_word)
