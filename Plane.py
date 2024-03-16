from matplotlib import pyplot as plt
import math

delta_t = 0.1  # Время шага
v = 1 / delta_t  # Частота
desired_h = 1 # Желаемая высота
total_time = 45 # Общее время полета
angle = 45  # Угол наклона в градусах
conditions = [desired_h + 10, desired_h - 10, desired_h]  # 3 начальных состояния


def decision_function(_h, _desired_h):
    return 1 if _h <= _desired_h else -1


plt.figure(figsize=(12, 6))
plt.axhline(y=desired_h, color='r', linestyle='--', label="Желаемая высота")
plt.title("Моделирование системы автоматического контроля высоты с обновленными исходными условиями")
plt.xlabel('Time (t)')
plt.ylabel('Height (y(t))')
plt.legend()
plt.grid(True)

for h_initial in conditions:
    h = h_initial
    time_points = [i * delta_t for i in range(int(total_time // delta_t) + 1)]  # Координаты X
    height_points = []  # Координаты Y

    for t in time_points:
        height_points.append(h)
        delta_y = delta_t * math.tan(math.radians(angle)) * decision_function(h, desired_h)
        h += delta_y  # Расчет новой высоты

    plt.plot(time_points, height_points, label=f"Начало = {h_initial}")

plt.show()

