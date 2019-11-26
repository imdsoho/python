import my_module

try:
    weight = my_module.determine_weight(1, -1)
except my_module.InvalidDesityError:
    weight = 0

