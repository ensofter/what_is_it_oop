from abc import ABC, abstractmethod


class SocialNetwork(ABC):

    @abstractmethod
    def login(self) -> bool:
        pass

    @abstractmethod
    def send_data(self, data: dict):
        pass

    @abstractmethod
    def logout(self):
        pass

    def send_post(self, post: dict):
        ok = self.login()
        if ok:
            self.send_data(post)
            self.logout()


class FaceBook(SocialNetwork):

    def login(self):
        print('facebook login')
        return True

    def send_data(self, data: dict):
        print(f'facebook send data {data["message"]}')

    def logout(self):
        print('facebook logout')


class VK(SocialNetwork):

    def login(self):
        print('VK login')
        return True

    def send_data(self, data: dict):
        print(f'VK send data {data["message"]}')

    def logout(self):
        print('VK logout')


if __name__ == '__main__':
    fb_post = dict(id=1, message='Hello world!')
    fb = FaceBook().send_post(fb_post)

    vk_post = dict(id=2, message='vk govno mentovskoe')
    vk = VK().send_post(vk_post)

