from abstract_fabric import Button, Checkbox, ElementFabric


class MacOsButton(Button):

    def click(self):
        print('Mac button Click')


class WindowsButton(Button):

    def click(self):
        print('Windows button Click')


class LinuxCheckbox(Checkbox):

    def checkbox(self):
        print('Linux checkbox')


class LinuxButton(Button):

    def click(self):
        print('Linux button click')


class WindowsCheckbox(Checkbox):

    def checkbox(self):
        print('Windows checkbox')


class MacOsCheckbox(Checkbox):

    def checkbox(self):
        print('Mac checkbox')


class MacOsElementsFactory(ElementFabric):

    def create_button(self) -> Button:
        return MacOsButton()

    def create_checkbox(self) -> Checkbox:
        return MacOsCheckbox()


class WindowsElementsFactory(ElementFabric):

    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class LinuxElementsFactory(ElementFabric):

    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()
