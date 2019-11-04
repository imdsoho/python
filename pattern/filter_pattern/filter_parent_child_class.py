import json


class EsQueryFilter():
    '''
        Elasticsearch query_string filter 구성을 위한 부모 클래스
    '''

    def __init__(self):
        pass

    def keys_exists(self, element, *keys):
        '''       
        :param element: 검사 dictionary
        :param keys: 중첩 key
        :return:
        '''

        if not isinstance(element, dict):
            raise AttributeError('argument Exception')

        if len(keys) == 0:
            raise AttributeError('key name is empty')

        _element = element
        for key in keys:
            try:
                _element = _element[key]
            except KeyError:
                return False

        return True


class EsQueryRangeFilter(EsQueryFilter):
    '''
        Elasticsearch query_string filter 구성 중 range query 구성
    '''

    def __init__(self):
        pass

    def make_range_filter(self, filter_data):
        '''
            인자값을 받아서 Elasticsearch query_string 내용을 구성합니다.
            범위를 필터링하는 포맷입니다.
        :param 튜플 data:
        :return: string 타입의 query_string 구성 내용
        '''

        if len(filter_data) != 6:
            raise AttributeError('range filter arguments length is 6')

        range_filter_format = '''{{ "{0}": {{
                               "{1}": {{
                                       "{2}": {3}, 
                                       "{4}": {5}
                                   }}
                               }}
                           }}'''

        ret_range_filter_str = range_filter_format.format(*filter_data)
        return ret_range_filter_str



es_range_filter = EsQueryRangeFilter()
bool_dict = {
    "query": {
        "bool": {
            "should": [],
            "filter": []
        }
    },
    "from": 0,
    "size": 300,
    "min_score": 0.1
}

# 필요한 key 여부 확인
bool_is_key = es_range_filter.keys_exists(bool_dict, "query", "bool", "filter")
print(bool_is_key)

# elasticseary query_string 구성
date_filter_data = ("range", "date", "gte", "20190101", "lte", "20191231")
date_filter_str = es_range_filter.make_range_filter(date_filter_data)

date_filter_dict = json.loads(date_filter_str)

bool_dict["query"]["bool"]["filter"].append(date_filter_dict)
print(bool_dict)

