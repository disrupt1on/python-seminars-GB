import datetime

def log_cash(mode, result):
    with open('Seminar-7\Handbook\log.txt', 'a', encoding='utf-8') as file:
        if mode == 'импорт' or mode == 'Импорт':
            file.write(f'Поиск по фамилии <<{result}>> в справочнике. Время запроса: {str(datetime.datetime.now())} \n')
        elif mode == 'экспорт' or mode == 'Экспорт':
            file.write(f'<<{result}>> внесен в справочник. Время запроса: {str(datetime.datetime.now())} \n')
