import sys


def get_circle(circle_file):
    with open(circle_file, 'r') as circle:
        circle_data = [float(n) for line in circle for n in line.strip().split()]

    return circle_data


def get_dot(dot_file):
    with open(dot_file, 'r') as dot:
        dot_data = [list(map(float, n.strip().split())) for n in dot]

    return dot_data


def is_in_circle(circle_data, dot_data):
    xc, yc, r = circle_data[0], circle_data[1], circle_data[2]
    for x, y in dot_data:
        math = (x-xc)**2 + (y-yc)**2
        if math < r**2:
            print(1)
        elif (math - r**2) < 1e-6:
            print(0)
        else:
            print(2)


def main():
    if len(sys.argv) != 3:
        print('Данных недостаточно!')
        sys.exit(1)

    is_in_circle(get_circle(sys.argv[1]), get_dot(sys.argv[2]))


main()
