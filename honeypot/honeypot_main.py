import socket
import sys
import datetime

LOG_FILE = "logs.log"
LISTENING_PORT = 22
MAX_CONNECTIONS = 10

# Создание TCP-сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка к порту
server_socket.bind(('0.0.0.0', LISTENING_PORT))

# Прослушивание сокета
server_socket.listen(MAX_CONNECTIONS)

# Открытие файла с логами
logfile = open("logs.log", "a")

# Основной цикл

try:
    while True:
        # Ожидание соединения
        client_socket, address = server_socket.accept()
        print(f"Connection from: {address}")

        # Запись информации о подключении в лог-файл
        log_mess = f"{datetime.datetime.now()}: New connetcion from {address[0]}:{address[1]}\n"
        logfile.write(log_mess)
        logfile.flush()

        try:
            # Чтение данных клиента
            data = client_socket.recv(1024)

            if data:
                # Вывод полученных данных
                print(f"Received data: {data.decode()}")

                # Вывод приветственного сообщения
                welcome_mess = b"Welcome to ssh server!\n"
                client_socket.send(welcome_mess)

                # Запись данных в лог-файл
                logfile.write(f"Received data: {data.decode()}")
                logfile.flush()     # <- нужно, чтобы при неожиданном завершении программы данные сохранились в логи

        except Exception as ex:
            print(f"Something went wrong: {ex}")

        finally:
            # Закрытие соединения
            client_socket.close()

except KeyboardInterrupt:
    print("Shutting down ^")
    server_socket.close()
    logfile.close()
    sys.exit(0)