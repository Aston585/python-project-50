import json

data = [{'status': 'unchanging', 'key': 'common', 'value': [{'status': 'added', 'key': 'follow', 'value': 'false'}, {'status': 'unchanging', 'key': 'setting1', 'value': 'Value 1'}, {'status': 'removed', 'key': 'setting2', 'value': 200}, {'status': 'changing', 'key': 'setting3', 'from': 'true', 'to': 'null'}, {'status': 'added', 'key': 'setting4', 'value': 'blah blah'}, {'status': 'added', 'key': 'setting5', 'value': {'key5': 'value5'}}, {'status': 'unchanging', 'key': 'setting6', 'value': [{'status': 'unchanging', 'key': 'doge', 'value': [{'status': 'changing', 'key': 'wow', 'from': '', 'to': 'so much'}]}, {'status': 'unchanging', 'key': 'key', 'value': 'value'}, {'status': 'added', 'key': 'ops', 'value': 'vops'}]}]}, {'status': 'unchanging', 'key': 'group1', 'value': [{'status': 'changing', 'key': 'baz', 'from': 'bas', 'to': 'bars'}, {'status': 'unchanging', 'key': 'foo', 'value': 'bar'}, {'status': 'changing', 'key': 'nest', 'from': {'key': 'value'}, 'to': 'str'}]}, {'status': 'removed', 'key': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'status': 'added', 'key': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

def json_output(data):
    return json.dumps(data)



    #with open('./gendiff/formaters/json_dump_file.json', 'w') as f:
        #json.dump(data, f)

    #with open('./gendiff/formaters/json_dump_file.json') as f:
        #return f.read()




print(json_output(data))
