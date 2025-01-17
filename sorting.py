class Solution:
    def select(self, arr, i):
        n = len(arr)
        for i in range(0, n):
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

    def selectionSort(self, arr, n):
        self.select(arr, 0)