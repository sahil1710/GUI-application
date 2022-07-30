import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def mergeSort(my_list):
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


    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1


    def mergesort(arr,l,r):
        if l < r:
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            mergesort(arr, l, m)
            mergesort(arr, m + 1, r)
            merge(arr, l, m, r)

    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 16

    a = np.array(my_list)
    l = len(my_list)
    arr = TrackArray(a)
    mergesort(arr,0,l-1)


    fig, ax = plt.subplots()
    container = ax.bar(np.arange(0, len(arr), 1), arr, align='edge', width=0.8)
    ax.set_xlim([0, l])
    ax.set(xlabel="Index", ylabel="Values", title="Merge sort")

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
