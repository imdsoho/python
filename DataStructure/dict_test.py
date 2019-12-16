'''dict_data = {"id":"jsc"}

print(dir(dict_data))

for key, value in dict_data.items():
    print(key, value)
'''

serialize_field = {"username":"user_name", "password":"1234", "ip":"123.123.123.123"}
dict_make = {
    key: value
    for key, value in serialize_field.items()
}
print(dict_make)
