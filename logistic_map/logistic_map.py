import matplotlib.pyplot as plt


def logistic_map_state(r, step, x0):
    x = x0
    x_list = [x]
    for n in range(step):
        x_n = r * x * (1 - x)
        x = x_n
        x_list += [x]
    return x_list

fig = plt.figure(figsize=(8, 3))
subplot = fig.add_subplot(1, 3, 1)
r = 2
x_list = logistic_map_state(r=r, step=50, x0=0.1)
x_list_d = logistic_map_state(r=r, step=50, x0=0.1+1e-8)
plt.plot(x_list)
plt.plot(x_list_d, c='red')
plt.ylim([-0.1, 1.1])
plt.title('r=2')
plt.ylabel('x')
plt.xlabel('step')
subplot = fig.add_subplot(1, 3, 2)
r = 3
x_list = logistic_map_state(r=r, step=50, x0=0.1)
x_list_d = logistic_map_state(r=r, step=50, x0=0.1+1e-8)
plt.plot(x_list)
plt.plot(x_list_d, c='red')
plt.ylim([-0.1, 1.1])
plt.title('r=3')
plt.xlabel('step')
subplot = fig.add_subplot(1, 3, 3)
r = 4
x_list = logistic_map_state(r=r, step=50, x0=0.1)
x_list_d = logistic_map_state(r=r, step=50, x0=0.1+1e-8)
plt.plot(x_list)
plt.plot(x_list_d, c='red')
plt.ylim([-0.1, 1.1])
plt.title('r=4')
plt.xlabel('step')
plt.tight_layout()
