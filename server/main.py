from server import ThreadedServer, ServerBaseHandler
from logger import Logger
from users_storage import JSONUsersStorage
from utils import ask_port


class ServerHandler(ServerBaseHandler):

    def handle(self):
        token = self.input('!get_token')
        if self.server.is_valid_token(self.ip, token):
            self.on_success()
        else:
            if self.server.exists(self.ip):
                password = self.input('!password')
                if self.server.is_valid_password(self.ip, password):
                    self.on_success()
                else:
                    self.send('!forbidden')
            else:
                username = self.input('!username')
                password = self.input('!password')
                self.server.add(self.ip, username, password)
                self.on_success()

    def on_success(self):
        self.send('!save_token')
        self.send(self.server.update_token(self.ip))
        username = self.server.users.get_field(self.ip, 'username')
        self.send('!success')
        self.send(f'Добро пожаловать {username}!')
        self.echo_forever()


def _main():
    port = ask_port()
    logger = Logger('log.txt')
    users = JSONUsersStorage('users.json')
    with ThreadedServer('', ServerHandler, port, logger, users) as server:
        server.threaded_accept_forever()
        server.command_line()


if __name__ == '__main__':
    _main()