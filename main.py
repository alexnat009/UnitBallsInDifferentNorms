import matplotlib.pyplot as plt
import numpy as np
import random

number_of_balls = 8


def unit_circle(x_center, y_center, norm):
    if norm <= 0:
        norm = 1

    x = np.linspace(x_center - 1, x_center + 1, 1000)
    y1 = (1 - np.abs(x - x_center) ** norm) ** (1 / norm) + y_center
    y2 = -(1 - np.abs(x - x_center) ** norm) ** (1 / norm) + y_center

    y = [y1, y2]
    return [x, y]


def order_circles_rgb_in_different_norms(norm, y_value, ball_norm):
    if norm <= 0:
        norm = 1

    # computing distances
    rgb_dist = []
    for t in colors:
        rgb_dist.append(round((t[0] ** norm + t[1] ** norm + t[2] ** norm) ** (1 / norm), 2))

    # create balls' dictionaries with indexes, distances and corresponding RGBs
    ball_dict = []
    for w in range(number_of_balls):
        ball_dict.append({"distance": rgb_dist[w], "RGB": colors[w], "counter": 0})
    rgb_dist.sort()

    # plotting rows
    x_value = 1
    for q in rgb_dist:
        for e in range(0, len(rgb_dist)):
            if q == ball_dict[e]['distance']:
                if ball_dict[e]['counter'] == 1:
                    break
                plt.plot(unit_circle(15 + x_value, y_value, ball_norm[e])[0],
                         unit_circle(15 + x_value, y_value, ball_norm[e])[1][0],
                         color=colors[e])
                plt.plot(unit_circle(15 + x_value, y_value, ball_norm[e])[0],
                         unit_circle(15 + x_value, y_value, ball_norm[e])[1][1],
                         color=colors[e])
                if q == rgb_dist[-1]:
                    plt.text(x_value + 17, y_value, "L_{norm}".format(norm=norm))
                x_value += 2.5
                ball_dict[e]['counter'] += 1


# data about centers, norms and colors
random.seed(0)
X_center = [(random.randint(-8, 7)) for i in range(number_of_balls)]
Y_center = [(random.randint(-8, 7)) for k in range(number_of_balls)]
ball_norms = [round(random.uniform(0.1, 5), 2) for j in range(number_of_balls)]
colors = [(round(random.uniform(0.0, 1.0), 2), round(random.uniform(0.0, 1.0), 2), round(random.uniform(0.0, 1.0), 2))
          for m in range(number_of_balls)]

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
for i in range(number_of_balls):
    plt.plot(unit_circle(X_center[i], Y_center[i], ball_norms[i])[0],
             unit_circle(X_center[i], Y_center[i], ball_norms[i])[1][0],
             color=colors[i], label="L_{norm}".format(norm=ball_norms[i]))
    plt.plot(unit_circle(X_center[i], Y_center[i], ball_norms[i])[0],
             unit_circle(X_center[i], Y_center[i], ball_norms[i])[1][1],
             color=colors[i])

# plot the rows
row_y_value = 6
row_norms = [round(random.uniform(0.1, 5), 2) for j in range(number_of_balls)]
for row_norm in row_norms:
    order_circles_rgb_in_different_norms(row_norm, row_y_value, ball_norms)
    row_y_value += 5

# plot the grid lines
plt.grid()

# show the labels of shapes
plt.legend()

# show the plot
plt.show()
