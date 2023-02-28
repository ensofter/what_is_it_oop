from circuit_of_responsibility import AbstractLoadHandler


class HardwareLoadHandler(AbstractLoadHandler):
    def handle(self, request: dict) -> bool:
        stat = request.get('stat')
        if stat is None:
            stat = {}
        cpu = request.get('cpu')
        stat['cpu'] = cpu != ''
        request['stat'] = stat
        if cpu != '':
            super().handle(request)
        else:
            return False

class BiosLoadHandler(AbstractLoadHandler):
    def handle(self, request: dict) -> bool:
        stat = request.get('stat')
        if stat is None:
            stat = {}
        bios = request.get('bios')
        stat['bios'] = bios != ''
        request['stat'] = stat
        if bios != '':
            super().handle(request)
        else:
            return False


if __name__ == '__main__':
    hw_handler = HardwareLoadHandler()
    bios_handler = BiosLoadHandler()


    hw_handler.set_next(bios_handler)

    request = {
        'cpu': 'Intel',
        'bios': ''
    }

    hw_handler.handle(request)

    print(request)
