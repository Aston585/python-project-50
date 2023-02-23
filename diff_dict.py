d1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

d2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}


def get_status(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []
    for key in sorted(keys):
        if key not in data2:
            result.append(('-', key, data1[key]))
        elif key in data1 and data2:
            if  data1[key] == data2[key]:
                result.append((' ', key,  data1[key]))
            elif data1[key] != data2[key]:
                result.append(('-', key,  data1[key]))
                result.append(('+', key, data2[key]))
        else:
            result.append(('+', key, data2[key]))
    return result


def get_output_data(data):
    status, key, value = data
    return f"{status} {key}: {value}"


def get_diff(source1, source2):
    output = map(get_output_data, (i for i in get_status(source1, source2)))
    result = '\n'.join(output)
    return '{' + '\n' + result + '\n' + '}'


print(get_diff(d1, d2))
