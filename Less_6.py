# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна
# описывать учебный предмет и наличие лекционных, практических и лабораторных
# занятий по предмету. Сюда должно входить и количество занятий. Необязательно,
# чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
# sum([i for i in (item.split(' ')[1:]) if i.isdigit()])

m_file = open('text_5.txt', 'r', encoding='utf-8')
lines = m_file.read().splitlines()
d = {}
for item in lines:
    key = item.split(': ')[0]
    value = item.split(' ')[1:]
    d.update({key: value})
print(d)
m_file.close()
# Не знаю как правльно распарсить сроку...
