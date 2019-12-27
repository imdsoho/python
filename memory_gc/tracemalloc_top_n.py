import tracemalloc
import gc
import time

tracemalloc.start(10)

time1 = tracemalloc.take_snapshot()

def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b

fibonacci(30)

def make_es():
    field_dict = {"a","b","c","d","e","f"}
    data_dict = {"1", "2", "3", "4", "5", "6"}
    ret_dict = {"field":field_dict, "data":data_dict}
    zip_dict = zip(field_dict, data_dict)
    ret_dict['zip'] = list(zip_dict)
    print(ret_dict)

'''vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
amount = sum(vals)
norm_and_move = [(x / amount) + 1 for x in vals]
print(norm_and_move)

no_primes = {j for i in range(2, 5) for j in range(i*2, 10, i)}
print(no_primes)'''

make_es()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'filename')
for stat in stats:
    print(stat)


'''top_stat = time2.statistics('filename')
stat = top_stat[0]
for line in stat.traceback.format():
    print(line)
'''

tracemalloc.stop()
