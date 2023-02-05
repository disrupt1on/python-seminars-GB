def inp_mode():
    mode = input('Введите режим работы (импорт или экспорт): ')
    return mode


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def inp_export():
    name = input('Введите фамилию: ')
    surname = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    return name, surname, phone

def view_import(result):
    print('По введённой фамилии найдены следующие результаты: ', result)

def view_export():
    print('Введённые данные успешно сохранены')