def index_words_iter(text):
    if text:
        yield 0

    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


address = "Four score and seven years ago ..."
result = list(index_words_iter(address))
print(result)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize_fun(get_iter):
    total = sum(get_iter())

    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)

    return result

path = "E:/tmp/my_number.txt"
percentages = normalize_fun(lambda : read_visits(path))

lambda_type = lambda: read_visits(path)
print(lambda_type)

def nomalize(numbers):
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = 100 * value / total
        result.append(percent)

    return result

class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = nomalize(visits)
print(percentages)