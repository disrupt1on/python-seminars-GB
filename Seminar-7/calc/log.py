import datetime

def log_cash(some_str, result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{some_str} = {result}. Время запроса: {str(datetime.datetime.now())} \n')
