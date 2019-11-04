

def helper(x):
    if x in group:
        return (0, x)

    return (1, x)


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        else:
            return (1, x)

number = [1,2,3,4,5,6,7,8,9,0]
priority = [0,2,4,6,8]          # error - group is not defiened
#number.sort(key=helper)
#print(number)

sort_priority(number, priority)
print(number)
