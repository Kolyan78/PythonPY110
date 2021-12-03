# Задание 2.
# Напишите программу Python для разделения заданного словаря списков на список словарей с помощью функции map().
#
# Пример:
# INPUT:  {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
# OUTPUT: [{'Наука': 88, 'Язык': 77}, {'Наука': 89, 'Язык': 78}, {'Наука': 62, 'Язык': 84}, {'Наука': 95, 'Язык': 80}]

# def conv(dict2):
#     a = [ _ for _ in dict2.keys()] # получить список все ключей
#     result = [] #создается пустой список, который потом будет возвращать функция
#     for i in range(len(dict2[a[0]])): # внешний цикл, число шагов которого равно количеству элементов в списке. Предполагается что все списки одинаковой длины
#         d = {} #создается пустой словарь, который будет наполняться во внутреннем цикле
#         for j in range(len(a)): # внутренний цикл, число шагов которого равно количеству элементов в словаре.
#             d[a[j]] = dict2[a[j]][i]
#         result.append(d)
#     return result
#
# dict_ = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}#, "Лженаука": [22, 34, 18, 90]}
# print(conv(dict_))
#print(list(map(conv2, dict_)))

def list_of_dicts(marks):
    step1 = [[(k, v) for v  in value] for k, value in marks.items()]
    science = step1[0]
    lang = step1[1]

    step2 = zip(science, lang)

    # for elem in step2:
    #     print(dict(elem))

    return list(map(dict, zip(science, lang)))
    #return list(map(dict, zip(*[[(k, v) for v in value] for k, value in marks.items()])))

if __name__ == '__main__':
    marks = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
    print(marks)
    print(list_of_dicts(marks))