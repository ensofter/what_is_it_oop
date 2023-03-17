# single responsibility
# один класс должен иметь только одну зону ответственности

# BEFORE

class ExportCsv:
    # класс, который покрывает сразу 2 зоны ответственности
    def __init__(self, raw_data: list[dict]):
        self.data = self.prepare(raw_data)

    # форматирование данных
    def prepare(self, raw_data: list[dict]) -> str:
        result = ''
        for item in raw_data:
            new_line = ','.join(
                (item['name'], item['surname'], item['occupation'])
            )
            result += f'{new_line}\n'
        return result

    # запись данных
    def write_file(self, file_name: str):
        with open(file_name, 'w', encoding='UTF8') as f:
            f.write(self.data)


if __name__ == '__main__':
    data = [
        {'name': 'Shuha', 'surname': 'Musha', 'occupation': 'pipidrol'},
        {'name': 'Sherlok', 'surname': 'Holmes', 'occupation': 'private investigator'},
        dict(name='poopa', surname='loopa', occupation='salary taker')
    ]

    csv = ExportCsv(raw_data=data)
    print(csv.data)
    csv.write_file(file_name='new.csv')

