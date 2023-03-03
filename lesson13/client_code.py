from lesson13.abstract_fabric import ElementFabric
from lesson13.elements import LinuxElementsFactory, WindowsElementsFactory, MacOsElementsFactory

LINUX = 'linux'
WINDOWS = 'windows'
MACOS = 'macos'

class GUI:

    def __init__(self, element_factory: ElementFabric):
        self.el_factory = element_factory

    def render(self):
        btn = self.el_factory.create_button()
        btn.click()


if __name__ == '__main__':
    os = 'macos'

    elements_factory: ElementFabric = None
    if os == LINUX:
        elements_factory = LinuxElementsFactory()
    elif os == WINDOWS:
        elements_factory = WindowsElementsFactory()
    elif os == MACOS:
        elements_factory = MacOsElementsFactory()
    else:
        print('Мы не знаем что ето, если бы мы знали что ето, но мы не знаем')
        exit(1)

    gui = GUI(element_factory=elements_factory)
    gui.render()
