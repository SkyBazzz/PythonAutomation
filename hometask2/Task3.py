from csv import DictReader
from json import dump


# Task #3. Work with csv and json structures.
def create_data_from_csv(file_name):
    json_data = list()
    with open(file_name, encoding='utf-8') as csv_file:
        csv_cars = DictReader(csv_file)
        for csv_row in csv_cars:
            json_data.append(csv_row)
    return json_data


def write_to_json(data):
    with open('cars.json', mode='w', encoding='utf-8') as cars_json:
        dump(data, cars_json, indent=2)


def transform_to_json(file_name: str):
    json_data = create_data_from_csv(file_name)
    write_to_json(json_data)


if __name__ == '__main__':
    transform_to_json('cars.csv')
