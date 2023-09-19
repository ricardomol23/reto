import timeit


def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

start_time = timeit.default_timer()
end_time = 0
factorial_recursivo(100)
end_time = timeit.default_timer()

print("----------------")
print("----------------")
print(end_time-start_time)