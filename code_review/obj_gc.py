# -*- coding: utf-8 -*-

import json
import re
import os
import sys
import datetime
import logging
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))))

from elasticsearch import Elasticsearch
from index_builder.utils.dBManager import DBManager
from index_builder.utils.index_tokenizer import IndexTokenizer
from index_builder.vo.simpan_labor_vo import SimpanLaborVO
from index_builder.utils.require_comm import require_comm as rq


class SimpanLaborBuilder:

    def __init__(self, logger):

        self.logger = logger

        self.es_host = {'host': '203.245.3.107', 'port': 9200}
        self.index_name = 'ulex_simpan_labor_v2-0-0'
        self.alias_name = 'ulex_simpan_labor'
        self.type_name = 'simpan_labor'

        self.db = DBManager('248')
        self.es = Elasticsearch(hosts=[self.es_host])
        self.tokenizer = IndexTokenizer()

        self.target_list = list()

    def update(self):

        self.logger.info('[ES][노동] 인덱스에 새로운 노동_심판례를 입력합니다.')

        total_doc_count = len(self.target_list) - 1
        for idx, judicase_seq in enumerate(self.target_list):
            self.logger.info('[ES][노동] 노동_심판례 인덱스 생성중. judicase_seq='+str(judicase_seq)+' (' + str(idx) + '/' + str(total_doc_count) + ')')
            self.bulk_es(judicase_seq)

    @staticmethod
    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    def create_index(self, delete=False):
        if self.es.indices.exists(self.index_name):
            print('[ES][노동] 동일한 이름의 인덱스가 이미 존재합니다.')
            if delete:
                res = self.es.indices.delete(index=self.index_name)
                print('[ES][노동] 인덱스 "%s"를 삭제하고 새로 생성 합니다. (%s)' % (self.index_name, res))
                res = self.es.indices.create(index=self.index_name, body=self.load_settings_dict())
                print('[ES][노동] 인덱스 "%s"를 생성 합니다. (%s)' % (self.index_name, res))
                res = self.es.indices.put_mapping(index=self.index_name, doc_type=self.type_name,
                                                  body=self.load_mapping_dict())
                print('[ES][노동] 인덱스 "%s"의 매핑정보를 입력 합니다. (%s)' % (self.index_name, res))
            else:
                print('[ES][노동] 이미 생성되어 있는 인덱스를 사용합니다.')

        else:
            res = self.es.indices.create(index=self.index_name, body=self.load_settings_dict())
            print('[ES][노동] 인덱스 "%s"를 생성 합니다. (%s)' % (self.index_name, res))
            res = self.es.indices.put_mapping(index=self.index_name, doc_type=self.type_name,
                                              body=self.load_mapping_dict())
            print('[ES][노동] 인덱스 "%s"의 매핑정보를 입력 합니다. (%s)' % (self.index_name, res))

    def load_seq_from_lg_db(self):
        query = "SELECT idx FROM erp_labor1.erp_laborJudge WHERE collectionGroup = '심판례';" \
                # " AND idx > 21300;"
                # "AND idx BETWEEN 44271 AND 44295;"
        print(query)
        sno_list = self.db.get_data_array(query)
        sno_list = [str(sno[0]) for sno in sno_list]
        return sno_list

    def load_seq_from_es(self):
        response = self.es.search(index=self.index_name, size=200, body=self.get_all_ids_query_dict())
        sno_list = []
        if len(response['hits']['hits']) > 0:
            for hits in response['hits']['hits']:
                sno = hits['_source']['pidx']
                sno_list.append(sno)
            return sno_list
        else:
            return [], {}

    def bulk_es(self, judicase_seq):
        try:
            print(judicase_seq)
            self.es.indices.put_alias(self.index_name, self.alias_name)

            bulk_data_list = []
            new_data_dict = self.load_new_data_from_lg_db(judicase_seq)

            count = 0
            max_count = len(new_data_dict.keys())
            for seq in new_data_dict.keys():
                vo = new_data_dict[seq]
                info_dict = {
                    "index": {
                        "_index": self.index_name,
                        "_type": self.type_name,
                        "_id": int(vo.simpan_labor_idx)
                    }
                }
                data_dict = vo.convert_vo_to_dict()

                if data_dict.keys():
                    bulk_data_list.append(info_dict)
                    bulk_data_list.append(data_dict)

                    count += 1
                    if count % 1000 == 0:
                        self.es.bulk(index=self.index_name, body=bulk_data_list, refresh=True, request_timeout=100)
                        bulk_data_list = []
                    else:
                        pass
                else:
                    pass

            if len(bulk_data_list) > 0:
                self.es.bulk(index=self.index_name, body=bulk_data_list, refresh=True, request_timeout=100)
            else:
                pass
        except Exception as ex:
            print("ERROR (pidx=%s) :" % judicase_seq, ex)
        # print '[ES][판례] 모든 신규 판례를 저장했습니다.'

    def load_new_data_from_lg_db(self, seq):
        data_dic = dict()
        error_seq_list = list()

        query = "SELECT idx, collection, collectionType, interactivityType, genre, author, datePublished, " \
                "alternativeHeadline, identifier, displayFlag " \
                "FROM erp_labor1.erp_laborJudge WHERE idx = %s" % seq

        data = self.db.get_data_array(query)

        for row in data:
            pidx = row[0]
            print(pidx)
            if pidx in data_dic.keys():
                value_object = data_dic[pidx]
            else:
                value_object = SimpanLaborVO()
                value_object.simpan_labor_idx = pidx

            value_object.collection = str(row[1])
            value_object.collectionType = str(row[2])

            interac_type = str(row[3])
            value_object.interactivityNm = interac_type

            if interac_type == '각하':
                value_object.interactivityType = '1'
            elif interac_type == '기각':
                value_object.interactivityType = '2'
            elif interac_type == '일부인정':
                value_object.interactivityType = '3'
            elif interac_type == '전부인정':
                value_object.interactivityType = '4'
            elif interac_type == '초심유지':
                value_object.interactivityType = '5'
            elif interac_type == '초심취소':
                value_object.interactivityType = '6'
            else:
                value_object.interactivityType = '99'

            genre = str(row[4])
            value_object.genreNM = genre

            if genre == '공정대표 의무위반':
                value_object.genre = '1'
            elif genre == '교섭단위 결정':
                value_object.genre = '2'
            elif genre == '교섭창구 단일화 절차':
                value_object.genre = '3'
            elif genre == '부당해고·부당노동행위':
                value_object.genre = '4'
            elif genre == '조정':
                value_object.genre = '5'
            elif genre == '차별시정':
                value_object.genre = '6'
            else:
                value_object.genre = '99'

            author = str(row[5])
            value_object.authorNm = author
            author_dict = self.set_author_dict()

            for k, v in author_dict.items():
                if v in author:
                    value_object.author = k
                    break
                elif '중앙' in author:
                    value_object.author = '1'
                else:
                    value_object.author = '99'
                    pass

            value_object.alternativeHeadline = rq.remove_pattern7(str(row[7]))
            value_object.identifierStr = rq.remove_special_chars(str(row[8]).replace(' ', ''))
            value_object.identifier = str(row[8]).replace(' ', '')
            value_object.displayFlag = str(row[9])

            date_str = row[6]
            if date_str:
                date = date_str.replace(u'.', u'-').replace(' ', '')
                if date.startswith('0') or date == '-':
                    value_object.datePublished = ''

                else:
                    if len(date_str) >= 8:
                        date = rq.check_date_format(date)
                        value_object.datePublished = date
                    else:
                        pass
            else:
                value_object.datePublished = date_str

            data_dic[pidx] = value_object

        query = "SELECT pidx, content_pars FROM erp_labor1.erp_laborJudge_body " \
                "WHERE pidx = %s order by pidx, num" % seq
        data = self.db.get_data_array(query)
        for row in data:
            pidx = row[0]

            if pidx in error_seq_list:
                continue
            else:
                pass

            if pidx in data_dic.keys():
                value_object = data_dic[pidx]
            else:
                print('[에러6] 새로운 노동_심판례 데이터를 로드하던 중 기본 정보가 없는 데이터 발견(pidx=%s)' % str(pidx))
                error_seq_list.append(pidx)
                continue

            body_cont = rq.remove_pattern7(row[1])
            value_object.body.append(rq.remove_pattern4(body_cont))
            data_dic[pidx] = value_object

        query = "SELECT pidx, content_pars FROM erp_labor1.erp_laborJudge_reason " \
                "WHERE pidx = %s order by pidx, num2" % seq
        data = self.db.get_data_array(query)
        for row in data:
            pidx = row[0]

            if pidx in error_seq_list:
                continue
            else:
                pass

            if pidx in data_dic.keys():
                value_object = data_dic[pidx]
            else:
                print('[에러7] 새로운 노동_심판례 데이터를 로드하던 중 기본 정보가 없는 데이터 발견(pidx=%s)' % str(pidx))
                error_seq_list.append(pidx)
                continue
            value_object.reason.append(rq.remove_pattern4(str(row[1])))
            data_dic[pidx] = value_object

        query = "SELECT pidx, content_pars FROM erp_labor1.erp_laborJudge_claim WHERE pidx = %s" % seq
        data = self.db.get_data_array(query)
        for row in data:
            pidx = row[0]

            if pidx in error_seq_list:
                continue
            else:
                pass

            if pidx in data_dic.keys():
                value_object = data_dic[pidx]
            else:
                print('[에러9] 새로운 노동_심판례 데이터를 로드하던 중 기본 정보가 없는 데이터 발견(pidx=%s)' % str(pidx))
                error_seq_list.append(pidx)
                continue
            value_object.claim.append(rq.remove_pattern4(str(row[1])))
            data_dic[pidx] = value_object

        query = "SELECT pidx, content_pars FROM erp_labor1.erp_laborJudge_history WHERE pidx = %s" % seq
        data = self.db.get_data_array(query)
        for row in data:
            pidx = row[0]
            content = str(row[1])
            if pidx in error_seq_list:
                continue
            else:
                pass

            if pidx in data_dic.keys():
                value_object = data_dic[pidx]
            else:
                print('[에러11] 새로운 노동_심판례 데이터를 로드하던 중 기본 정보가 없는 데이터 발견(pidx=%s)' % str(pidx))
                error_seq_list.append(pidx)
                continue
            content = rq.remove_pattern4(content)
            content = rq.remove_pattern6(content)
            value_object.history.append(content)
            data_dic[pidx] = value_object

        # print '[ES][판례][데이터로드] 텍스트데이터 로드 완료'

        # 토큰생성
        for pidx in data_dic.keys():
            vo = data_dic[pidx]
            cont_no_list = list()

            temp_name = vo.alternativeHeadline
            if temp_name is not None and temp_name != ' ':
                token_list = list()
                tokens = self.tokenizer.get_tokens(str(temp_name))[0]
                token_list += tokens
                vo.alternativeHeadline_tokens = token_list
            else:
                pass

            temp_list = vo.body
            token_list = list()
            for text in temp_list:
                tokens, cont_no = self.tokenizer.get_tokens(str(text))
                if cont_no:
                    cont_no_list += cont_no
                else:
                    pass
                token_list += tokens
            vo.body_tokens = token_list

            temp_list = vo.reason
            token_list = list()
            for text in temp_list:
                tokens, cont_no = self.tokenizer.get_tokens(str(text))
                if cont_no:
                    cont_no_list += cont_no
                else:
                    pass
                token_list += tokens
            vo.reason_tokens = token_list

            temp_list = vo.history
            token_list = list()
            for text in temp_list:
                tokens, cont_no = self.tokenizer.get_tokens(str(text))
                if cont_no:
                    cont_no_list += cont_no
                else:
                    pass
                token_list += tokens
            vo.history_tokens = token_list

            temp_list = vo.claim
            token_list = list()
            for text in temp_list:
                tokens, cont_no = self.tokenizer.get_tokens(str(text))
                if cont_no:
                    cont_no_list += cont_no
                else:
                    pass
                token_list += tokens
            vo.claim_tokens = token_list

            vo.cont_case_no = set(cont_no_list)
            data_dic[pidx] = vo

        # print '[ES][판례][데이터로드] 토큰생성 완료'
        # print '[ES][판례][데이터로드] 모든데이터 로드를 완료했습니다.'

        return data_dic

    @staticmethod
    def set_author_dict():
        author_dict = dict()
        total_author_list = ['연습', '강원', '경기', '경남', '경북', '부산', '서울',
                             '울산', '인천', '전남', '전북', '제주', '충남', '충북']

        for i in range(1, len(total_author_list)):
            author_dict[str(i + 1)] = total_author_list[i]

        return author_dict

    @staticmethod
    def create_insert_list(db_list, es_list):
        insert_seq_list = []
        for db_seq in db_list:
            if db_seq not in es_list:
                insert_seq_list.append(db_seq)
            else:
                pass
        return insert_seq_list

    @staticmethod
    def get_all_ids_query_dict():
        temp = {
            "query": {
                "match_all": {}
            },
            'from': 0,
            'size': 500000,
            '_source': 'pidx'
        }
        return json.dumps(temp)

    @staticmethod
    def load_settings_dict():
        body = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 2
            }
        }
        return body

    @staticmethod
    def load_mapping_dict():
        temp = {
            "properties": {
                "id": {
                    "type": "long",
                    "index": "not_analyzed"
                },
                "pidx": {
                    # 판례 일련번호
                    # erp_tax1 - idx
                    "type": "long",
                    "index": "not_analyzed"
                },
                "collection": {
                    # 판례 판결유형
                    # erp_panre - interactiveType
                    "type": "text",
                    "index": "not_analyzed",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "null_value": ""
                        }
                    }
                },
                "collectionType": {
                    # 판례 판결유형
                    # erp_panre - interactiveType
                    "type": "text",
                    "index": "not_analyzed",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "null_value": ""
                        }
                    }
                },
                "interactivityNm": {
                    # 판례 판결유형
                    # erp_panre - interactiveType
                    "type": "text",
                    "index": "not_analyzed"
                },
                "interactivityType": {
                    # 판례 판결유형
                    # erp_panre - interactiveType
                    "type": "text",
                    "index": "not_analyzed",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "null_value": ""
                        }
                    }
                },
                "genreNm": {
                    # 세목
                    # erp_tax1 - genre
                    "type": "text",
                    "index": "not_analyzed"
                },
                "genre": {
                    # 세목
                    # erp_tax1 - genre
                    "type": "text",
                    "index": "not_analyzed",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "null_value": ""
                        }
                    }
                },
                "authorNM": {
                    # 판단기관
                    # erp_panre - identifier
                    "type": "text",
                    "index": "not_analyzed"
                },
                "author": {
                    # 판단기관
                    # erp_panre - identifier
                    "type": "text",
                    "index": "not_analyzed",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "null_value": ""
                        }
                    }
                },
                "date": {
                    # 생산일자
                    # erp_panre - datePublished
                    "type": "date",
                    "format": "yyyyMMdd",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "null_value": ""
                        }
                    }
                },
                "title": {
                    # 사건명
                    "type": "text",
                    "index": "not_analyzed"
                },
                "alternativeHeadline": {
                    # 사건명
                    "type": "text",
                    "index": "not_analyzed"
                },
                "search_identifier": {
                    # 사건번호
                    "type": "text",
                    "index": "not_analyzed"
                },
                "identifier": {
                    # 판례 사건번호
                    # erp_tax1 - identifier
                    "type": "text",
                    "index": "not_analyzed"
                },
                "display_flag": {
                    # 판례 노출 여부
                    "type": "text",
                    "index": "not_analyzed"
                },
                "body": {
                    # 판례 전문
                    # erp_panre_body - content
                    "type": "text",
                    "index": "not_analyzed"
                },
                "reason": {
                    # 이유
                    # erp_panre_reason - content
                    "type": "text",
                    "index": "not_analyzed"
                },
                "claim": {
                    # 판례 청구취지
                    # erp_panre_claim - content
                    "type": "text",
                    "index": "not_analyzed"
                },
                "history": {
                    # 판례 사건 경과
                    "type": "text",
                    "index": "not_analyzed"
                },
                "alternativeHeadline_tokens": {
                    # 판례 사건명 별칭 토큰
                    # erp_panre - anotherName
                    "type": "text",
                    "similarity": "BM25",
                    "analyzer": "whitespace"
                },
                "body_tokens": {
                    # 판례 전문 토큰
                    # erp_panre_body - content
                    "type": "text",
                    "similarity": "BM25",
                    "analyzer": "whitespace"
                },
                "reason_tokens": {
                    # 이유 토큰
                    # erp_panre_reason - content
                    "type": "text",
                    "similarity": "BM25",
                    "analyzer": "whitespace"
                },
                "claim_tokens": {
                    # 판례 청구취치 항소취치 토큰
                    # erp_panre_psuk - content
                    "type": "text",
                    "similarity": "BM25",
                    "analyzer": "whitespace"
                },
                "history_tokens": {
                    # 판례 사건경과 토큰
                    # erp_panre_psuk - content
                    "type": "text",
                    "similarity": "BM25",
                    "analyzer": "whitespace"
                },

                "cont_case_no": {
                    # 판례 본문에서 찾은 판례 사건번호
                    "type": "keyword"
                },
                "information": {
                    # 현재 [기관 / 종류 / 분류 / 사건번호 / 결과 / 일자] 순으로 되어있음.
                    "type": "text",
                    "index": "not_analyzed"
                },
                "summary": {
                    # 판례 요약문
                    "type": "text",
                    "index": "not_analyzed"
                },
            }
        }
        return json.dumps(temp)

    def run(self, start_idx=None, divide=True):

        print(start_idx)

        start_time = time.time()

        print('[ES][노동] 노동_심판례 인텍스를 확인합니다.')
        self.create_index(delete=False)

        print('[ES][노동] DB에 저장된 모든 노동_심판례 SEQ를 가져옵니다.')
        seq_list_from_db = self.load_seq_from_lg_db()

        print('[ES][노동] 인덱스에 저장된 노동_심판례의 SEQ를 가져옵니다.')
        seq_list_from_es = self.load_seq_from_es()

        print('[ES][노동] 새로 추가할 노동_심판례의 SEQ를 찾습니다.')
        insert_seq_list = self.create_insert_list(seq_list_from_db, seq_list_from_es)

        print('[ES][노동] 인덱스에 새로운 노동_심판례를 입력합니다.')

        if divide:
            divide10 = int((len(insert_seq_list) / 10) + 1)
            divided_sno_list = list()
            for group in self.chunker(list(insert_seq_list), divide10):
                divided_sno_list.append(group)

            max_count = len(divided_sno_list[int(start_idx)]) - 1
            for list_idx, judicase_seq in enumerate(divided_sno_list[int(start_idx)]):
                print('[ES][노동] 노동_심판례 인덱스 생성중. (' + str(list_idx) + '/' + str(max_count) + ')')
                self.bulk_es(judicase_seq)
        else:
            for judicase_seq in insert_seq_list:
                self.bulk_es(judicase_seq)
                pass

        print('[ES][노동] 노동_심판례 인덱스 생성완료.')
        print(time.time() - start_time)


if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    es_builder = SimpanLaborBuilder(logging)

    # divide = sys.argv[2]
    # start_idx = 0
    # start_idx = sys.argv[1]
    es_builder.run(divide=False)
    # es_builder.run(start_idx)
