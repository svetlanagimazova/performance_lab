import json


def change_value(tests, values):
    new_list = []
    for i in tests:
        for key in values:
            if i['id'] == key['id']:
                i.update({'value': key['value']})
                new_list.append(i)
            if 'values' in i:
                change_value(i['values'], values)
    return new_list


def main():
    with open('tests.json', 'r') as ts:
        test_py = json.load(ts)['tests']

    with open('values.json', 'r') as vl:
        values_py = json.load(vl)['values']

    data = {'tests': change_value(test_py, values_py)}

    with open('report.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


main()
