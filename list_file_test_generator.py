import os

print('*** Файлы в директории ***')
list_file = os.listdir()
for item in list_file:
    if os.path.isfile(item):
        print(item)

print('*** Файлы в директории ***')
result_list = [item for item in os.listdir() if os.path.isfile(item)]
print('\n'.join(result_list))
