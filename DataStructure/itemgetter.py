# 딕셔너리 리스트가 있고, 하나 혹은 그 이상의 딕셔너리 값으로 데이터를 정렬

from operator import itemgetter

rows = [{'fname':'', 'uid':'', 'lname':''}]

rows_by_lf_name = sorted(rows, key=itemgetter('lname', 'fname'))

rows_by_lname = sorted(rows, key=lambda r: r['fname'])
rows_by_lf_name2 = sorted(rows, key=lambda r: (r['lname'], r['fname']))

min(rows, key=itemgetter('uid'))
max(rows, key=itemgetter('uid'))


# sorted()

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(1), User(2), User(3)]
sorted(users, key=lambda u: u.user_id)

sorted(users, key=itemgetter('user_id'))