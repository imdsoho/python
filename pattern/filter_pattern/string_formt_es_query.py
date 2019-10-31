import json

def make_range_filter(filter_data):
    '''
        인자값을 받아서 Elasticsearch query_string 내용을 구성합니다.
        범위를 필터링하는 포맷입니다.
    :param 튜플 data: 
    :return: string 타입의 query_string 구성 내용
    '''
    range_filter_format = '''{{ "{0}": {{
                                "{1}": {{
                                        "{2}": {3},
                                        "{4}": {5}
                                    }}
                                }}
                            }}'''

    ret_range_filter_str = range_filter_format.format(*filter_data)
    return ret_range_filter_str


es_fields_str = "id, title, contents"
bool_dict = {
    "query": {
        "bool": {
            "should": [],
            "filter": []
        }
    },
    "from": 0,
    "size": 300,
    "_source": es_fields_str.split(","),
    "min_score": 0.1
}

date_filter_data = ("range", "date", "gte", "20190101", "lte", "20191231")
date_filter_str = make_range_filter(date_filter_data)
# string type 데이터를 받아 json.loads를 사용하여 dictionay로 변경
date_filter_dict = json.loads(date_filter_str)

bool_dict["query"]["bool"]["filter"].append(date_filter_dict)
print(bool_dict)
