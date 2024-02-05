import math

def new_coordinates(x1, y1, distance, azimuth):
    azimuth_rad = math.radians(azimuth)

    # вычисление новых координат
    if 0 <= azimuth <= 90:
        x2 = x1 + distance * math.sin(azimuth_rad)
        y2 = y1 + distance * math.cos(azimuth_rad)
    elif 90 < azimuth <= 180:
        azimuth_rad = math.radians(azimuth - 90)
        x2 = x1 + distance * math.cos(azimuth_rad)
        y2 = y1 + distance * math.sin(azimuth_rad) * -1
    elif 180 < azimuth <= 270:
        azimuth_rad = math.radians(azimuth - 180)
        x2 = x1 + distance * math.sin(azimuth_rad) * -1
        y2 = y1 + distance * math.cos(azimuth_rad) * -1
    elif 270 < azimuth <= 360:
        azimuth_rad = math.radians(azimuth - 270)
        x2 = x1 + distance * math.cos(azimuth_rad) * -1
        y2 = y1 + distance * math.sin(azimuth_rad)

    return x2, y2

# список измерений ускорения по оси у за 1 сек с частотой 14 Hz (14 измерений)
a_list = [2.0, 0.33, 0.5, 0.33, 1.33, -0.5, 2.0, -0.33, 0, -2.0, 0.5, -2.33, -2.1, -3.3]

# время прохождения отрезка (1/14 сек)
t = 1 / 14

# начальная скорость
v_init = 0

# начальные координаты
x1 = 0
y1 = 0

s_list = []

s_sum = 0

for a in a_list:
    s = v_init * t + a * t * t / 2
    v_init += a * t
    s_list.append(s)
    print(f"Пройдено расстояние {round(s, 4)} м с ускорением {a} м/с2, текущая скорость {round(v_init, 4)} м/с")
    s_sum += s

print(f"\nИтого пройдено: {round(s_sum, 4)} м")

x2, y2 = new_coordinates(x1, y1, s_sum, 350)
print(f"\nСтарые координаты: {x1}, {y1}")
print(f"\nНовые координаты: {x2}, {y2}\n")





