import matplotlib.pyplot as plt


def build_func(ground_speed, water_speed, x1, y1, x2, y2):
    def wrap(x):
        term1 = (1 / ground_speed) * ((x - x1) / ((x - x1) ** 2 + y1 ** 2) ** 0.5)
        term2 = (1 / water_speed) * ((x - x2) / ((x - x2) ** 2 + y2 ** 2) ** 0.5)
        return term1 + term2

    return wrap


def find_optimal_x(ground_speed, water_speed, x1, y1, x2, y2):
    func = build_func(ground_speed, water_speed, x1, y1, x2, y2)

    left_border, right_border = min(x1, x2), max(x1, x2)

    cur_x = (right_border + left_border) / 2

    while True:
        cur_v = func(cur_x)
        if abs(cur_v) < 0.0000001:
            return cur_x

        if cur_v > 0:
            right_border = cur_x
        else:
            left_border = cur_x

        cur_x = (right_border + left_border) / 2


def show_graph(x, ground_speed, water_speed, x1, y1, x2, y2):
    fig, ax = plt.subplots(figsize=(10, 6))
    if y2 >= 0:
        ax.plot([x1, x], [y1, 0], 'bo-')
        ax.plot([x, x2], [0, y2], 'ro-')
        ax.text(x, 0, f'({x}, 0)', fontsize=12, verticalalignment='top', horizontalalignment='right')
    else:
        ax.plot([x1, x2], [y1, y2], 'bo-')

    ax.text(x1, y1, f'({x1}, {y1})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    ax.text(x2, y2, f'({x2}, {y2})', fontsize=12, verticalalignment='bottom', horizontalalignment='left')

    ax.text(0, 0, '(0, 0) - Граница воды и суши', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
    ax.text(0, -0.1, f"Скорость по земле: {ground_speed}\nСкорость по воде: {water_speed}",
            transform=ax.transAxes, ha="left", va="center")

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Визуализация спасения')

    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.show()


def main():
    ground_speed, water_speed = 5, 1
    x1, y1 = 10, -10
    x2, y2 = 100, 15

    x = find_optimal_x(ground_speed, water_speed, x1, y1, x2, y2)
    show_graph(round(x, 4), ground_speed, water_speed, x1, y1, x2, y2)


if __name__ == "__main__":
    main()
