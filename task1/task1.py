import collections
import sys


def path_way(count, step):
    num_list = collections.deque(i for i in range(1, count+1))
    steps_list = [1]
    while num_list[step-1] != 1:
        steps_list.append(num_list[step-1])
        for _ in range(step-1):
            num_list.append(num_list[0])
            num_list.popleft()
    return steps_list


def main():
    n, m = int(sys.argv[1]), int(sys.argv[2])
    print(''.join(map(str, path_way(n, m))))


main()
