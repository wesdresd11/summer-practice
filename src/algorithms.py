

# Bubble Sort: O(n ** 2)
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


# Selection Sort: O(n ** 2)
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


# Insertion Sort: O(n ** 2)
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


# Quick Sort: O(n log n)
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort: O(n log n)
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    return nums


# Heap Sort: O(n log n)
def heapify(nums, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)


def heap_sort(nums):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    return nums


# Counting Sort: O(n)
def counting_sort(nums):
    if not nums:
        return nums
    min_val = min(nums)
    max_val = max(nums)
    count = [0] * (max_val - min_val + 1)
    for x in nums:
        count[x - min_val] += 1
    k = 0
    for val_offset in range(len(count)):
        for _ in range(count[val_offset]):
            nums[k] = val_offset + min_val
            k += 1
    return nums


# Radix Sort: O(n)
def radix_sort(nums):
    if not nums:
        return nums
    min_val = min(nums)
    if min_val < 0:
        for i in range(len(nums)):
            nums[i] -= min_val
    max_val = max(nums)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in nums:
            digit = (x // exp) % 10
            buckets[digit].append(x)
        k = 0
        for b in buckets:
            for x in b:
                nums[k] = x
                k += 1
        exp *= 10
    if min_val < 0:
        for i in range(len(nums)):
            nums[i] += min_val
    return nums


# Bucket Sort: O(n)
def bucket_sort(nums):
    if not nums:
        return nums
    min_val = min(nums)
    max_val = max(nums)
    if min_val == max_val:
        return nums
    bucket_count = max(10, len(nums) // 50)
    buckets = [[] for _ in range(bucket_count)]
    step = (max_val - min_val + 1) / bucket_count
    for x in nums:
        idx = int((x - min_val) / step)
        if idx >= bucket_count:
            idx = bucket_count - 1
        buckets[idx].append(x)
    k = 0
    for b in buckets:
        insertion_sort(b)
        for x in b:
            nums[k] = x
            k += 1
    return nums


# Builtin Sort:
def builtin_sort(nums):
    nums.sort()
    return nums


algorithms = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Quick": quick_sort,
    "Merge": merge_sort,
    "Heap": heap_sort,
    "Counting": counting_sort,
    "Radix": radix_sort,
    "Bucket": bucket_sort,
    "Builtin": builtin_sort,
}