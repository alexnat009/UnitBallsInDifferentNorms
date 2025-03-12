import numpy as np
import matplotlib.pyplot as plt
import random

# np.random.seed(0)
number_of_balls = 10
NORMS = [[1, 2, -1, -2, np.inf, -np.inf], ['fro', 'nuc', 'ky-fan', 'schatten']]
X_center = np.random.randint(0, 21, number_of_balls)
Y_center = np.random.randint(0, 21, number_of_balls)
centers = np.random.randint(0, 21, (number_of_balls, 2))
colors = np.random.randint(0, 256, (number_of_balls, 3)).astype(float) / 255
norms = np.random.uniform(0.1, 5, number_of_balls)


def closest_pair(array):
    if len(array) < 2:
        return None  # Handle edge case

    min_diff = float('inf')
    closest_pair = None
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            diff = abs(array[i] - array[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (i, j, diff)

    return closest_pair


def unit_circle_in_p_norm(X_center, Y_center, p_norm):
    p_norm = max(0.1, p_norm)  # Avoid division errors

    x = np.linspace(X_center - 1, X_center + 1, 1000)
    y1 = (1 - np.abs(x - X_center) ** p_norm) ** (1 / p_norm) + Y_center
    y2 = -(1 - np.abs(x - X_center) ** p_norm) ** (1 / p_norm) + Y_center

    return [x, [y1, y2]]


def ball_measure(x_center, y_center, colors, norms=NORMS):
    circle_measure_with_color_and_location = []
    functions = []
    p_norms = []
    normtype = random.choice(norms[0] + norms[1])
    for x_c, y_c, col in zip(x_center, y_center, colors):
        matrix = np.vstack((np.array([x_c, y_c, 21]) / 21, np.array(col), np.ones(3)))
        svd = np.linalg.svd(matrix, compute_uv=False)

        # Compute norm correctly
        if normtype == 'ky-fan':
            measure = np.linalg.norm(svd[:2], ord=2)
        elif normtype == 'schatten':
            measure = np.linalg.norm(svd, ord=2)
        else:
            measure = np.linalg.norm(matrix, ord=normtype)

        circle_measure_with_color_and_location.append(measure)
        p_norm = np.round(np.random.uniform(0.1, 5), 3)
        functions.append(unit_circle_in_p_norm(x_c, y_c, p_norm))
        p_norms.append(p_norm)

    return list(zip(x_center, y_center, colors, circle_measure_with_color_and_location, functions)), p_norms


# Compute circles and their norms
circles, p_norms = ball_measure(X_center, Y_center, colors, norms=NORMS)
distances = [circle[3] for circle in circles]
closest = closest_pair(distances)

# Plot the closest pair connection
if closest:
    closest_x = [circles[closest[0]][0], circles[closest[1]][0]]
    closest_y = [circles[closest[0]][1], circles[closest[1]][1]]
    plt.plot(closest_x, closest_y, color='black')

# Plot circles
for i, circle in enumerate(circles):
    plt.plot(circle[4][0], circle[4][1][0], color=circle[2], label=p_norms[i])
    plt.plot(circle[4][0], circle[4][1][1], color=circle[2])

plt.legend(title='Circles created with p-norms')
plt.grid()
plt.show()
