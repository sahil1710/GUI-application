import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bubbleSort(my_list):
    class TrackArray():
        def __init__(self, arr):
            self.arr = np.copy(arr)
            self.reset()

        def reset(self):
            self.indicies = []
            self.values = []
            self.access_type = []
            self.full_copies = []

        def track(self, key, access_type):
            self.indicies.append(key)
            self.values.append(self.arr[key])
            self.access_type.append(access_type)
            self.full_copies.append(np.copy(self.arr))

        def GetActivity(self, idx=None):
            if isinstance(idx, type(None)):
                return [(i, op) for (i, op) in zip(self.indicies, self.access_type)]
            else:
                return (self.indicies[idx], self.access_type[idx])

        def __getitem__(self, key):
            self.track(key, "get")
            return self.arr.__getitem__(key)

        def __setitem__(self, key, value):
            self.arr.__setitem__(key, value)
            self.track(key, "set")

        def __len__(self):
            return self.arr.__len__()

    def bubblesort(arr):
        for i in range(len(arr)):

            # Last i elements are already in place
            for j in range(0, len(arr) - i - 1):

                # Traverse the list from 0 to size of lst - i - 1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 16

    a = np.array(my_list)
    l = len(my_list)
    arr = TrackArray(a)
    bubblesort(arr)


    fig, ax = plt.subplots()
    container = ax.bar(np.arange(0, len(arr), 1), arr, align='edge', width=0.8)
    ax.set_xlim([0,l])
    ax.set(xlabel="Index", ylabel="Values", title="Bubble sort")



    def update(frame):

        for (rectangle, height) in zip(container.patches, arr.full_copies[frame]):
            rectangle.set_height(height)
            rectangle.set_color("#1f77b4")

        idx, op = arr.GetActivity(frame)
        if op == "get":
            container.patches[idx].set_color("green")
        else:
            container.patches[idx].set_color("red")
        return (*container,)

    ani = FuncAnimation(fig, update, frames=range(len(arr.full_copies)),
                    blit=True, interval=1000./60, repeat=False)
    plt.show()
