def list_create(path):
    with open(path, 'r') as file:
        nums = []
        for num in file:
            n = int(num)
            nums.append(n)
    return nums


def get_average(num_list):
    ave = int(sum(num_list) / len(num_list))
    counts = 0
    for num in num_list:
        counts += abs(num-ave)
    print(counts)


def main():
    get_average(list_create('numbers.txt'))


main()
