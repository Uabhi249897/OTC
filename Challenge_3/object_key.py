from operator import le

def key_object(object, key):
    key_char = key.split('/')

    object_parse = {}

    # print(key_char[0])
    # print(object['a']['b']['c'])

    for i in range(len(key_char)): 
        if i == 0: 
            object_parse = object[key_char[i]]
            # print(object_parse)
        else:
            # print(i)
            object_parse = object_parse[key_char[i]]

    print(object_parse)


if __name__ == '__main__': 
    # object = {'a':{'b':{'c':'d'}}}
    object = {'x':{'y':{'z':'a'}}}

    # key = 'a/b/c'
    key = 'x/y/z'

    key_object(object,key)
    