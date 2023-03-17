#AFTER

class FormatData:
    def __init__(self, raw_data: list[dict]):
        self.raw_data = raw_data

    def prepare(self) -> str:
        result = ''
        for item in self.raw_data:
            new_line = ','.join(
                (item['name'], item['surname'], item['occupation'])
            )
            result += f'{new_line}\n'
        return result


class FileWriter:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def write(self, data: str):
        with open(self.file_name, 'w', encoding='UTF8') as f:
            f.write(data)


if __name__ == '__main__':
    data = [
        dict(name='Shuha', surname='Musha', occupation='Pipidrol'),
        dict(name='Sherlok', surname='Holmes', occupation='Private investigator'),
        dict(name='Poopa', surname='Loopa', occupation='Salary taker')
    ]

    format_data = FormatData(data)
    csv_data = format_data.prepare()

    writer = FileWriter('out.csv')
    writer.write(data=csv_data)

