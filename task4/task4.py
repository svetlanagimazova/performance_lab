import sys


def read_list(path):
    with open(path, 'r') as file:
        return [int(line.strip()) for line in file]


def get_median(num_list):
    num_list.sort()
    median = num_list[len(num_list)//2]
    sum = 0
    for num in num_list:
        sum += abs(num - median)
    return sum



def main():
    if len(sys.argv) != 2:
        print('Данных недостаточно!')
        sys.exit(1)

    print(get_median(read_list(sys.argv[1])))


main()
