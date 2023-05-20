import yaml
import json

with open('./tests/fixtures/file1.yaml') as f1:
    save_loader1 = yaml.load(f1, Loader=yaml.SafeLoader)
with open('./tests/fixtures/file2.yaml') as f2:
    save_loader2 = yaml.load(f2, Loader=yaml.SafeLoader)

with open('./tests/fixtures/file1.yaml') as f1:
    base_loader1 = yaml.load(f1, Loader=yaml.BaseLoader)
with open('./tests/fixtures/file2.yaml') as f2:
    base_loader2 = yaml.load(f2, Loader=yaml.BaseLoader)

with open('./tests/fixtures/file1.yaml') as f1:
    full_loader1 = yaml.load(f1, Loader=yaml.FullLoader)
with open('./tests/fixtures/file2.yaml') as f2:
    full_loader2 = yaml.load(f2, Loader=yaml.FullLoader)


with open('./tests/fixtures/file1.json') as f1:
    json_loader1 = json.load(f1)
with open('./tests/fixtures/file2.json') as f2:
    json_loader2 = json.load(f2)


print(save_loader1, save_loader2, sep='\n\n')
#print('*' * 150)
#print(full_loader1, full_loader2, sep='\n\n')
#print('*' * 150)
#print(base_loader1, base_loader2, sep='\n\n')
print('#' * 150)
print(json_loader1, json_loader2, sep='\n\n')
