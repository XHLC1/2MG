import yaml
# with open('test.yaml', encoding='utf-8') as file1:
#     data = yaml.load_all(file1, Loader=yaml.FullLoader)#读取yaml文件
#     print(data)

# import yaml
#
# users = [{'name': ['John Doe3', '1'], 'occupation': 'gardener'},
#          {'name': 'Lucy Blackk', 'occupation': 'teacher'}]
#
# with open('test.yaml', 'w') as f:
#
#     data = yaml.dump(users, f)

import yaml

with open('test.yaml', 'r', encoding='utf-8') as f:
    result = yaml.load(f.read(), Loader=yaml.FullLoader)
# print(result, type(result))
print(result['os'], type(result['os']))
print(result['osVersion'], type(result['osVersion']))
print(result['account'], type(result['account']))
print(result['account']['username'])
print(result['deviceName'])
print(result['appPackage'])
print(result['bool1'], type(result['bool1']))


