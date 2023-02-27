from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def get_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass


class UserRepositoryPostgreSql(UserRepository):

    def create_user(self):
        pass

    def get_user(self):
        pass

    def delete_user(self):
        pass


class UserRepositoryMongoDb(UserRepository):

    def create_user(self):
        pass

    def get_user(self):
        pass

    def delete_user(self):
        pass

class Controller:

    def __init__(self, user_repo: UserRepository)
    self.user_repo = user_repo


if __name__ == '__main__':
    usm = UserRepositoryMongoDb
    uspsql = UserRepositoryPostgreSql
    c = Controller(user_repo=usm)

