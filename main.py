from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

## 1. Выполните пункты 1-3 задания.
pattern = r"(\+7|8)\s*\(?(\d{3})\)?[ -]*(\d{3})[- ]*(\d{2})[ -]*(\d{2})[ -(]*(доб.)?[- ]*(\d{4})*\)*"
#subst_pattern = r"+7(\2)\3-\4-\5 (?(\6)доб. \7/|)"
dic = {}
new_contact_list = []
for s in contacts_list[1:]:
  fio = ' '.join(s[:3])
  s[:3] = fio.split()
  dic_key = ' '.join(s[:2])
  if dic_key in dic:
    l = []
    for i, j in zip(dic[dic_key], s[2:]):
      if i == '' or j == '':
        l.append(i + j)
      else:
        l.append(i)
    dic[dic_key] = l
  else:
    dic[dic_key] = s[2:]

new_contact_list.append(contacts_list[0])
for i, j in list(dic.items()):
  list = i.split()
  list.extend(j)
  match = re.search(pattern, list[5])
  if match.group(6):
    list[
        5] = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)} доб. {match.group(7)}"
  else:
    list[
        5] = f"+7({match.group(2)}){match.group(3)}-{match.group(4)}-{match.group(5)}"
  new_contact_list.append(list)
pprint(new_contact_list)

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  ## Вместо contacts_list подставьте свой список:
  datawriter.writerows(new_contact_list)
