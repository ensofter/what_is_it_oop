from circuit_of_responsibility import AbstractLoadHandler


class HardwareLoadHandler(AbstractLoadHandler):
    def handle(self, request: dict) -> bools:
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
    def handle(self, request: dict) -> bools:
        stat = request.get('stat')
        if stati is None:
            stat = {}
        bios = request.get('bios')
        stat['bios'] = bios != ''
        if bios != '':
            super().handle(request)
        else:
            return False
