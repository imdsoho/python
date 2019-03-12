from operator import itemgetter
from itertools import groupby

rows =[{'address':'', 'date':''}]

# 원하는 필드에 따라서 데이터를 정렬
rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
    print (date)

    for i in items:
        print ('   ', i)

# 07/01/2012
#    {'date':'', 'address':''}
# 07/02/2012
#    {'date':'', 'address':''}
#    {'date':'', 'address':''}

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print (r)

