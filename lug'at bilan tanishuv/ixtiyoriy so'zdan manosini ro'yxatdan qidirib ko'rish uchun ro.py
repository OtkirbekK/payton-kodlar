python_izohli_lugat = {'integer': 'butun son',
                       'float': 'O\'nlik son',
                       'string': 'Matn',
                       'list': 'Ro\'yxat'}
tarjima = input('So\'zni yozing: ')
if tarjima in python_izohli_lugat:
    print(python_izohli_lugat[tarjima])
else:
    print('bunday so\'z mavjud emas')