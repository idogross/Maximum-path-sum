import time


def max_path_sum(pyramid, row=0, col=0):
    if row == len(pyramid) - 1:
        return pyramid[row][col]
    return pyramid[row][col] + max(max_path_sum(pyramid, row+1, col+1), max_path_sum(pyramid, row+1, col))


def max_path_sum_mem(pyramid, row=0, col=0, memo=None):
    if row == len(pyramid) - 1:
        return pyramid[row][col]
    if memo is None:
        memo = {}
    if (row, col) not in memo:
        memo[(row, col)] = pyramid[row][col] + max(max_path_sum_mem(pyramid, row+1, col, memo),
                                                   max_path_sum_mem(pyramid, row+1, col+1, memo))
    return memo[(row, col)]


with open('pyramid.txt') as f:
    pyramids = [line.rstrip().split(" ") for line in f]
int_pyramid = []
for line in pyramids:
    int_pyramid.append(list(map(int, line)))

t0 = time.time()
sum1 = max_path_sum(int_pyramid)
t1 = time.time()
sum2 = max_path_sum_mem(int_pyramid)
t2 = time.time()
print(f'Recursive answer: {sum1}, calculation time: {t1-t0}')
print(f'Recursive with memoization answer: {sum2}, calculation time: {t2-t1}')
