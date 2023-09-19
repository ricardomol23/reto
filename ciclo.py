import timeit

def factorial_ciclo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


start_time = timeit.default_timer()
end_time = 0
factorial_ciclo(100)
end_time = timeit.default_timer()

print("----------------")
print("----------------")
print(end_time-start_time)