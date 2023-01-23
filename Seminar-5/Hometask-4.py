#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def compress(string):
 
    compression = ""
 
    i = 0
    while i < len(string):
        count = 1
 
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count = count + 1
            i = i + 1
 
        compression += str(count) + string[i]
        i = i + 1
 
    return compression
 
 
if __name__ == '__main__':
 
    string = 'ABBCCCD'
    print(compress(string))