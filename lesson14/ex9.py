class ProviderCommunication:
    def receive(self):
        print('Получение продукции производителя')

    def payment(self):
        print('Оплата поставщику с удержанием комиссии')


class Site:
    def placement(self):
        print('Размещение на сайте')

    def delete(self):
        print('Удаление с сайта')


class DataBase:
    def insert(self):
        print('Запись в базу данных')

    def delete(self):
        print('Удаление из базы данных')


class MarketPlace:
    def __init__(self):
        self._provider_commenication = ProviderCommunication()
        self._site = Site()
        self._data_base = DataBase()

    def product_receive(self):
        self._provider_commenication.receive()
        self._site.placement()
        self._data_base.insert()

    def product_release(self):
        self._provider_commenication.payment()
        self._site.delete()
        self._data_base.delete()


if __name__ == '__main__':
    market_place = MarketPlace()
    market_place.product_receive()
    print()
    market_place.product_release()