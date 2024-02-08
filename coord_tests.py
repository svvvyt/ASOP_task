import numpy as np

def optimize_variable(x, i, func, step_size=0.01):
    # Простой шаг вдоль координаты с постоянным шагом
    new_x = x.copy()
    new_x[i] += step_size

    if func(new_x) < func(x):
        return new_x
    else:
        new_x[i] = x[i] - step_size
        if func(new_x) < func(x):
            return new_x
        else:
            return x

def cyclic_coordinate_descent(x0, func, tol=1e-6, max_iter=10000):
    x = np.array(x0)
    n = len(x)

    for _ in range(max_iter):
        for i in range(n):
            old_xi = x[i]
            x = optimize_variable(x, i, func)
            if np.abs(old_xi - x[i]) < tol:
                return x

    return x

# Пример использования для функции Розенброка
def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

initial_guess = np.array([0.9, 0.9])
result = cyclic_coordinate_descent(initial_guess, rosenbrock)

print("Метод циклического покоординатного спуска для Розенброка")
print("Минимум найден в точке:", result)
print("Значение функции в минимуме:", rosenbrock(result))

# Пример использования для другой функции
def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

initial_guess_other = np.array([-2.7, 3.0])
result_other = cyclic_coordinate_descent(initial_guess_other, himmelblau)

print("Метод циклического покоординатного спуска для Химмельблау")
print("Минимум найден в точке:", result_other)
print("Значение функции в минимуме:", himmelblau(result_other))

input()