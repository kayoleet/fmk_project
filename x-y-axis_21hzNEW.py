import math
import matplotlib.pyplot as plt

def plot_arrays(x_values, y_values):
    if len(x_values) != len(y_values):
        raise ValueError("Input arrays must have the same length")

    plt.scatter(x_values, y_values)

    plt.xlabel('X Axis')    
    plt.ylabel('Y Axis')
    plt.title('X, Y axis coordinates')

    plt.show()

def rotate_vectors(x_list, y_list, angle):
    
    angle = math.radians(360 - angle)
    
    for a in range(1, len(x_list)):
        # Move the origin of the vector to (0, 0)
        x_shifted = x_list[a] - x_list[a-1]
        y_shifted = y_list[a] - y_list[a-1]
        
        # Rotate the shifted vector
        x_rotated = x_shifted * math.cos(angle) - y_shifted * math.sin(angle)
        y_rotated = x_shifted * math.sin(angle) + y_shifted * math.cos(angle)
        
        # Move the end point back
        x_endpoint = x_rotated + new_x_list[a-1]
        y_endpoint = y_rotated + new_y_list[a-1]
        
        new_x_list.append(x_endpoint)
        new_y_list.append(y_endpoint)
    
    # print(new_x_list)
    # print(new_y_list)

    return new_x_list, new_y_list


def new_coordinates(x1, y1, distance_total, distance_x, azimuth):
    x1

# список измерений ускорения по осям х и у за 1 сек с частотой 21 Hz (м/с2)
a_y_list = [1.5, 0.75, 2.0, 1.4, 2.1, -0.2, -0.1, -0.3, -0.1, -2.0, -0.15, -0.5, 0.9, -1.3, -0.7, -1,7, 0.9, -3.0, -1.6, -2.0]
a_x_list = [-0.33, -0.1, -0.7, 1.1, 0, 1.5, 0.8, 1.7, -1.3, 2.4, -1.6, 2.4, -0.25, 1.7, -0.5, 1.5, -0.1, 0.5, -0.4, 0.95, -0.8]

# время прохождения отрезка (сек)
t = 1 / 21

# начальная скорость (м/с)
v_y = 0
v_x = 0

# начальные координаты
x1 = 5
y1 = 2

s_list = []

s_y_sum = y1
s_x_sum = x1

x_list = [x1]
y_list =[y1]

new_x_list = [x1]
new_y_list =[y1]

azimuth_input = int(input())

for a_y in a_y_list:
    s_y = v_y * t + a_y * t * t / 2
    v_y += a_y * t
    # print(f"Пройдено расстояние по y {round(s_y, 4)} м с ускорением {a_y} м/с2, текущая скорость {round(v_y, 4)} м/с")
    
    s_y_sum += s_y
    y_list.append(s_y_sum)
    

print(f"\nИтого пройдено по оси у: {round(s_y_sum - y1, 4)} м\n")

for a_x in a_x_list:
    s_x = v_x * t + a_x * t * t / 2
    v_x += a_x * t
    # print(f"Пройдено расстояние по x {round(s_x, 4)} м с ускорением {a_x} м/с2, текущая скорость {round(v_x, 4)} м/с")
    s_x_sum += s_x
    x_list.append(s_x_sum)
    
# print(x_list, y_list)

print(f"\nИтого пройдено по оси x: {round(s_x_sum - x1, 4)} м\n")

s_total = math.sqrt(math.pow(s_x_sum - x1, 2) + math.pow(s_y_sum - y1, 2)) # по вектору
print(f"\nИтого пройдено по обеим осям: {round(s_total, 4)} м\n")


# plot_arrays(x_list, y_list)

new_x_list, new_y_list = rotate_vectors(x_list, y_list, azimuth_input)
print(f"\nСтарые координаты: {x1}, {y1}")
print(f"\nНовые координаты: {new_x_list[-1]}, {new_y_list[-1]}\n")
plot_arrays(new_x_list, new_y_list)

