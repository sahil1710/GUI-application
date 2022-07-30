import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def quickSort(my_list):
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


    def partition(arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)


    def quicksort(arr,low,high):
        if len(arr) == 1:
            return arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 16


    a = np.array(my_list)
    l = len(my_list)
    arr = TrackArray(a)
    quicksort(arr,0,l-1)


    fig, ax = plt.subplots()
    container = ax.bar(np.arange(0, len(arr), 1), arr, align='edge', width=0.8)
    ax.set_xlim([0, l])
    ax.set(xlabel="Index", ylabel="Values", title="Quick sort")

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
