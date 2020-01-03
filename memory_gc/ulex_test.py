import tracemalloc


def make_es():
    field_dict = {"a","b","c","d","e","f"}
    data_dict = {"1", "2", "3", "4", "5", "6"}
    ret_dict = {"field":field_dict, "data":data_dict}
    zip_dict = zip(field_dict, data_dict)
    ret_dict['zip'] = list(zip_dict)
    print(ret_dict)

tracemalloc.start(5)

time1 = tracemalloc.take_snapshot().filter_traces((
    tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
    tracemalloc.Filter(False, "<frozen importlib._bootstrap_external>"),
    tracemalloc.Filter(False, "<unknown>"),
))

make_es()

time2 = tracemalloc.take_snapshot().filter_traces((
    tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
    tracemalloc.Filter(False, "<frozen importlib._bootstrap_external>"),
    tracemalloc.Filter(False, "<unknown>"),
))

stats = time2.compare_to(time1, 'lineno')

for stat in stats:
    print(stat)

