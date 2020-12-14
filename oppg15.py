import numpy as np
import matplotlib.pyplot as plt
np.random.seed(12)

repeats = 5

for simulations in range(repeats):

    N_steps = 1000000
    expected_R = np.sqrt(N_steps)

    ###################################
    #     generate one random walk    #
    ###################################
    # a list of 4 directions 0,1,2,3
    dirs = np.random.randint(0, 4, N_steps)
    # a 2D list of steps, empty for now
    steps = np.empty((N_steps,2))
    # fill the list of steps according to direction
    steps[dirs == 0] = [0,1]  # 0 - right
    steps[dirs == 1] = [0,-1] # 1 - left
    steps[dirs == 2] = [1,0]  # 2 - up
    steps[dirs == 3] = [-1,0] # 3 - down
    ###################################
    # use cumsum to sum up the individual steps to get current position
    steps = steps.cumsum(axis=0)
    ###################################
    print('Final position:',steps[-1])



    ###################################
    # draw only a selection of points, max 5000, to save memory
    skip = N_steps//5000 + 1
    xs = steps[::skip,0]
    ys = steps[::skip,1]
    plt.plot(xs,ys)
    ###################################

    ###################################
    # add a circle with expected distance
    circle = plt.Circle((0,0), radius=expected_R, color='k')
    plt.gcf().gca().add_artist(circle)
    # equal axis size
    plt.gcf().gca().set_aspect('equal')
    ###################################

plt.title(f'{repeats} random walks of {N_steps} steps')
plt.axis([-2000, 2000, -2000, 2000])
# http://matplotlib.1069221.n5.nabble.com/How-to-center-axes-intersecting-at-0-0-td46427.html
# Tom for tid
plt.show()
