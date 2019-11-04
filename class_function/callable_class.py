class ESQueryBuilder():
    def __init__(self, query):
        self.query = query

    def __call__(self):
        '''
        get_result(query_str) 메소드 작업
        
        :return: 
        '''
        result_dict = {"query":self.query, "type":0, "count":0}
        return result_dict


'''
__call__() 함수를 구현하면
클래스 인스턴스를 생성하고, 해당 인스턴스를 함수처럼 호출할 수 있습니다.

ESQueryBuilder의 메소드가 get_result() 한개라면 
위와 같이 구현하는 것에 대해서 한번 검토해주세요

ESQueryBuilder에서 필요한 method가 여러 개면 PASS.. 실패입니다.
'''

query = "args['query']"
es_query_builder = ESQueryBuilder(query)
query_result_dict = es_query_builder()
print(query_result_dict)