import random


def gen_random(n):
    return [random.randint(0, n * 2) for i in range(n)]


def gen_sorted(n):
    return list(range(n))


def gen_reversed(n):
    return list(range(n, 0, -1))


def gen_almost_sorted(n):
    nums = list(range(n))
    swaps = int(n * 0.05)
    if swaps == 0:
        swaps = 1
    for swap in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        nums[i], nums[j] = nums[j], nums[i]
    return nums


sizes = [10, 500, 1000, 50000, 1000000]

data_types = {
    "Random": gen_random,
    "Sorted": gen_sorted,
    "Reversed": gen_reversed,
    "Almost Sorted": gen_almost_sorted,
}