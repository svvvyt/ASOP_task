import numpy as np

def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def custom_function(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

def hooke_jeeves(f, x0, step_size=0.01, tol=1e-6, max_iter=10000):
    x = np.array(x0)
    pattern = np.eye(len(x))

    for _ in range(max_iter):
        improved = False
        for p in pattern:
            x_candidate = x + step_size * p
            if f(x_candidate) < f(x):
                x = x_candidate
                improved = True

        if not improved:
            step_size /= 2.0
            pattern = pattern / 2.0

        if step_size < tol:
            break

    return {'min_point': x.tolist(), 'min_value': f(x)}

# Rosenbrock
initial_guess = np.array([-3.0, -3.0])
result = hooke_jeeves(rosenbrock, initial_guess)

# Пример использования для функции Химмельблау
initial_guess_custom = np.array([2.9, 1.9])
result_custom = hooke_jeeves(custom_function, initial_guess_custom)

print("Метод Хука-Дживса для функции Розенброка")
print("Минимум найден в точке:", result['min_point'])
print("Значение функции в минимуме:", result['min_value'])

print("Метод Хука-Дживса для функции Химмельблау")
print("Минимум найден в точке:", result_custom['min_point'])
print("Значение функции в минимуме:", result_custom['min_value'])

input()