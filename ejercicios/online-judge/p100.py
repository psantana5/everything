def cycle_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def max_cycle_length(i, j):
    max_length = 0
    for num in range(i, j + 1):
        current_length = cycle_length(num)
        max_length = max(max_length, current_length)
    return max_length


input_pairs = [(1, 10), (100, 200), (201, 210), (900, 1000)]

for pair in input_pairs:
    i, j = pair
    max_len = max_cycle_length(i, j)
    print(i, j, max_len)
