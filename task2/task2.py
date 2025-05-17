def get_circle(circle_file):
    with open(circle_file, 'r') as circle:
        circle_data = [int(n) for line in circle for n in line.strip().split()]

    return circle_data


def get_dot(dot_file):
    with open(dot_file, 'r') as dot:
        dot_data = [list(map(int, n.strip().split())) for n in dot]

    return dot_data


def is_in_circle(circle_data, dot_data):
    for dot in dot_data:
        math = (dot[0]-circle_data[0])**2 / circle_data[-1]**2
        + (dot[1]-circle_data[1])**2 / circle_data[-1]**2
        if math > 1:
            print(2)
        elif math == 1:
            print(0)
        else:
            print(1)


def main():
    is_in_circle(get_circle('circle.txt'), get_dot('dot.txt'))


main()
