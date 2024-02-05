import math
import matplotlib.pyplot as plt

def plot_arrays(x_values, y_values):
    # Check if the arrays have the same length
    if len(x_values) != len(y_values):
        raise ValueError("Input arrays must have the same length")

    # Create a scatter plot
    plt.scatter(x_values, y_values)

    # Set labels and title
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('X, Y axis coordinates')

    # Display the plot
    plt.show()

def new_coordinates(x1, y1, distance_total, distance_x, azimuth):
    azimuth_rad = math.radians(azimuth)

    angle_rad = math.asin(distance_x / distance_total)
    angle_total = math.degrees(angle_rad + azimuth_rad)
    angle_total_rad = angle_rad + azimuth_rad
    print(f"angle = {math.degrees(angle_rad)}, angle + azimuth = {angle_total}")

    # вычисление новых координат
    if 0 <= angle_total <= 90:
        x2 = x1 + distance_total * math.sin(angle_total_rad)
        y2 = y1 + distance_total * math.cos(angle_total_rad)
    elif 90 < angle_total <= 180:
        angle_total_rad = math.radians(angle_total - 90)
        x2 = x1 + distance_total * math.cos(angle_total_rad)
        y2 = y1 + distance_total * math.sin(angle_total_rad) * -1
    elif 180 < angle_total <= 270:
        angle_total_rad = math.radians(angle_total - 180)
        x2 = x1 + distance_total * math.sin(angle_total_rad) * -1
        y2 = y1 + distance_total * math.cos(angle_total_rad) * -1
    elif 270 < angle_total <= 360:
        angle_total_rad = math.radians(angle_total - 270)
        x2 = x1 + distance_total * math.cos(angle_total_rad) * -1
        y2 = y1 + distance_total * math.sin(angle_total_rad)


    return x2, y2

# список измерений ускорения по осям х и у за 1 сек с частотой 21 Hz (м/с2)
a_y_list = [1.5, 0.75, 2.0, 1.4, 2.1, -0.2, -0.1, -0.3, -0.1, -2.0, -0.15, -0.5, 0.9, -1.3, -0.7, -1,7, 0.9, -3.0, -1.6, -2.0]
a_x_list = [-0.33, -0.1, -0.7, 1.1, 0, 1.5, 0.8, 1.7, -1.3, 2.4, -1.6, 2.4, -0.25, 1.7, -0.5, 1.5, -0.1, 0.5, -0.4, 0.95, -0.8]

# время прохождения отрезка (сек)
t = 1 / 21

# начальная скорость (м/с)
v_y = 0
v_x = 0

# начальные координаты
x1 = 0
y1 = 0

s_list = []

s_y_sum = 0
s_x_sum = 0

x_list = []
y_list =[]

new_x_list = []
new_y_list =[]

azimuth_input = int(input())

for a_y in a_y_list:
    s_y = v_y * t + a_y * t * t / 2
    v_y += a_y * t
    print(f"Пройдено расстояние по y {round(s_y, 4)} м с ускорением {a_y} м/с2, текущая скорость {round(v_y, 4)} м/с")
    
    s_y_sum += s_y
    y_list.append(s_y_sum)
    

print(f"\nИтого пройдено по оси у: {round(s_y_sum, 4)} м\n")

for a_x in a_x_list:
    s_x = v_x * t + a_x * t * t / 2
    v_x += a_x * t
    print(f"Пройдено расстояние по x {round(s_x, 4)} м с ускорением {a_x} м/с2, текущая скорость {round(v_x, 4)} м/с")
    s_x_sum += s_x
    x_list.append(s_x_sum)
    

print(f"\nИтого пройдено по оси x: {round(s_x_sum, 4)} м\n")

s_total = math.sqrt(math.pow(s_x_sum, 2) + math.pow(s_y_sum, 2))
print(f"\nИтого пройдено по обеим осям: {round(s_total, 4)} м")

for a in range(0, len(y_list)):
    x52 = x_list[a]
    y52 = y_list[a]
    x53, y53 = new_coordinates(x52, y52, s_total, s_x_sum, 45)
    new_x_list.append(x53)
    new_y_list.append(y53)

x2, y2 = new_coordinates(x1, y1, s_total, s_x_sum, azimuth_input)
print(f"\nСтарые координаты: {x1}, {y1}")
print(f"\nНовые координаты: {x2}, {y2}\n")

# print(plot_arrays(x_list, y_list))
print(plot_arrays(new_x_list, new_y_list))







