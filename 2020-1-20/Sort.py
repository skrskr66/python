# 冒泡排序
def Bubble_Sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 -i):
            if arr[j] > arr[j + 1]:
                arr[j],arr[j + 1] = arr[j + 1],arr[j]
    print(arr)
# 选择排序
def Select_Sort(arr):
    for i in range(len(arr) - 1):
        min_num = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min_num]:
                min_num = j
        arr[i],arr[min_num] = arr[min_num],arr[i]
    print(arr)
# 