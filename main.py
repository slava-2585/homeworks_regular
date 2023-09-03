from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
dic={}
new_contact_list=[]
for s in contacts_list[1:]:
    fio = ' '.join(s[:3])
    s[:3] = fio.split()
    dic_key = ' '.join(s[:2])
    if dic_key in dic:
        l_dic = dic[dic_key]
        s_dic = s[2:]
        #l = [i +j for i, j in zip(dic[s[0]+s[1]], s[3:]) if i == '' or j == '']
        l=[]
        for i, j in zip(dic[dic_key], s[2:]):
            if i == '' or j == '':
                l.append(i+j)
            else:
                l.append(i)
        dic[dic_key] = l
    else:
        dic[dic_key] = s[2:]
        pprint(dic)
    for i in dic.items():
        pass
        # list = []
        # list.append(i.split())
        # list.extend(j)
        # print(i)
        # new_contact_list.append(list)
#pprint(len(new_contact_list))
pattern = re.compile(r"(\+7|8)\s*\(?(\d{3})\)?[ -]*(\d{3})[- ]*(\d{2})[ -]*(\d{2})[ -(]*(доб.)?[- ]*(\d{4})*\)*")
## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
#   datawriter.writerows(contacts_list)