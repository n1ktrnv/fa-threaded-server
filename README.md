# Лабораторная работа "Многопоточный сервер" по Практикуму по программированию

### Задания для самостоятельного выполнения

1. Модифицировать простой эхо-сервер таким образом, чтобы при подключении клиента создавался новый поток, в котором происходило взаимодействие с ним.

Данный функционал можно увидеть в п. 3, когда к многопоточному серверу одновременно смогут подлючиться несколько пользователей, следовательно, взаимодействие с каждым происходит в новом потоке.

2. Реализовать простой чат сервер на базе сервера аутентификации. Сервер должен обеспечивать подключение многих пользователей одновременно, отслеживание имен пользователей, поддерживать историю сообщений и пересылку сообщений от каждого пользователя всем остальным. 

Сервер:
![screenshot](images/1.png)

Клиент 1 (регистрация):
![screenshot](images/2.png)

Клиент 2 (регистрация):
![screenshot](images/3.png)

Клиент 1:
![screenshot](images/4.png)

Клиент 2:
![screenshot](images/5.png)

Клиент 2:
![screenshot](images/6.png)

Клиент 1:
![screenshot](images/7.png)

Клиент 2 (выходит):
![screenshot](images/8.png)


Клиент 2 (вход, неверный пароль):
![screenshot](images/9.png)


Клиент 2 (вход):
![screenshot](images/10.png)

Клиент 1:
![screenshot](images/11.png)

3. Реализовать сервер с управляющим потоком. При создании сервера прослушивание портов происходит в отдельном потоке, а главный поток программы в это время способен принимать команды от пользователя. Необходимо реализовать следующие команды:

Сервер (ввод не существующей команды):
![screenshot](images/12.png)

Клиент:
![screenshot](images/13.png)
    
    1. Отключение сервера (завершение программы);

![screenshot](images/14.png)
    
    2. Пауза (остановка прослушивание порта);
    
![screenshot](images/15.png)

При подключении клиента его не приветсвуют (запрещают взаимодействовать с сервером) до тех пор, пока сервер не будет снят с паузы.
![screenshot](images/16.png)

![screenshot](images/17.png)

![screenshot](images/18.png)

    3. Показ логов;
    
![screenshot](images/19.png)

    4. Очистка логов;
    
![screenshot](images/20.png)
    
    5. Очистка файла идентификации.
 
![screenshot](images/21.png)

При попытке зайти нас уже не пропускает по имеющемуся токену, хотя он остался с послнеднего логина до очистки, значит, нас просят зарегистрироваться, а значит файл очищен.
![screenshot](images/22.png)
