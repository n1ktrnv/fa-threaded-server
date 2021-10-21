DEFAULT_PORT = 5050


def ask_port():
    while True:
        answer = input('Введите порт сервера (или Enter для '
                       'использования значения по умолчанию): ')
        if answer != '':
            try:
                port = int(answer)
            except ValueError:
                print('Ошибка: неверное значение порта')
            else:
                return port
        else:
            return DEFAULT_PORT
