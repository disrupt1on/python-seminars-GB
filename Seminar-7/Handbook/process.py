def search (surname):
    result_list = []
    with open ('Seminar-7\Handbook\data.txt', 'r', encoding='utf-8') as file:
        while True:
            book = file.readline()
            if not book:
                if not file.readline():
                    break
            if book.rstrip().lower() == surname.lower():
                result_list.append(book.rstrip())
                for _ in range(1, 5):
                    result_list.append(file.readline().rstrip())
                result_list.append('')
        if len(result_list) > 0:
            return result_list
        else:
            return 'Резултат не найден'


def export (result):
    path = 'Seminar-7\Handbook\data.txt'
    with open (path, 'a', encoding='utf-8') as file:
        for i in range(5):
            file.write(result[i] + '\n')
        file.write(result[5])

    with open ('Seminar-7\Handbook\data.csv', 'a', encoding='utf-8') as file:
        for i in range(5):
            file.write(result[i] + '\n')
        file.write(result[5])