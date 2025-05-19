import json
import sys


def change_value(tests, values):
    values_dict = {item['id']: item['value'] for item in values}

    def get_values(tests):
        for test in tests:
            test_id = test.get('id')
            if test_id in values_dict:
                test['value'] = values_dict[test_id]
            if 'values' in test:
                get_values(test['values'])

    get_values(tests)
    return tests


def main():
    if len(sys.argv) != 4:
        print('Данных недостаточно!')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding='utf-8') as file:
        test_py = json.load(file)

    with open(sys.argv[2], 'r', encoding='utf-8') as file:
        values_py = json.load(file)

    data = change_value(test_py['tests'], values_py['values'])

    with open(sys.argv[3], 'w', encoding='utf-8') as file:
        json.dump({'tests': data}, file, indent=2)


main()
