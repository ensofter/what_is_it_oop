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
            return super().handle(request)
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
            return super().handle(request)
        else:
            return False


class DebuggerLoadHandler(AbstractLoadHandler):
    def handle(self, request: dict) -> bool:
        stat = request.get('stat')
        if stat is None:
            stat = {}
        debugger = request.get('debugger')
        stat['debugger'] = debugger != ''
        request['stat'] = stat
        if debugger != '':
            return super().handle(request)
        else:
            return False


if __name__ == '__main__':
    hw_handler = HardwareLoadHandler()
    bios_handler = BiosLoadHandler()
    debugger_handler = DebuggerLoadHandler()

    hw_handler.set_next(bios_handler).set_next(debugger_handler)

    request = {
        'cpu': 'Intel',
        'bios': 'Hello',
        'debugger': 'World'
    }

    print(hw_handler.handle(request))

    print(request)
