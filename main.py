import collections
import json
from pprint import pprint

from src.psutil_aggregator import current

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def all_data():
    data = current()
    pprint(data)

def cpu_draw():

    sec = 3
    limit = int(60/sec)
    cpu_lst = collections.deque(limit*[0], limit)
    x_axis = [x for x in range(limit)]

    fig = plt.figure()
    sp = fig.add_subplot(1,1,1)

    def run(i):
        data = current()
        cpu_percent = data['cpu']['percent']
        pprint(cpu_percent)
        cpu_lst.appendleft(cpu_percent)

        y_axis = cpu_lst.copy()
        y_axis.reverse()
        
        sp.clear()
        sp.plot(x_axis, y_axis)

    ani = animation.FuncAnimation(fig, run, interval=sec*1000)
    plt.show()

def main():
    all_data()
    cpu_draw()

if __name__ == "__main__":
    main()