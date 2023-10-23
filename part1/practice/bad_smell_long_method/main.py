# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def main():
    data = _read(csv)
    res = _sort(data)
    return check(res)


def _read(csv):
    return [i.split(';') for i in csv.split('\n')]


def _sort(lst):
    return sorted(lst, key=lambda x: int(x[1]))


def check(lst):
    return [i for i in lst if int(i[1]) > 10]


if __name__ == '__main__':
    print(main())
