def sum_divisible_by(n, limit):
    m = (limit - 1) // n
    return n * m * (m + 1) // 2
print(sum_divisible_by(3, 1000) + sum_divisible_by(5, 1000) - sum_divisible_by(15, 1000))