import numpy as np
from scipy.optimize import minimize

# Функция Розенброка
def rosenbrock(x):
    return sum(100.0 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

# Начальное приближение
initial_guess_rosenbrock = np.array([-1.5, 1.5])

# Другая функция
def himmelblau(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2

# Начальное приближение другой функции
initial_guess = np.array([3.4, -1.7])

# Минимизация Розенброка с использованием метода Нелдера-Мида
result_rosenbrock = minimize(rosenbrock, initial_guess_rosenbrock, method='nelder-mead', options={'disp': False})

# Минимизация с использованием метода Нелдера-Мида
result = minimize(himmelblau, initial_guess, method='nelder-mead', options={'disp': False})

print("Метод Нелдера-Мида для функции Розенброка")
print("Минимум найден в точке:", result_rosenbrock.x)
print("Значение функции в минимуме:", result_rosenbrock.fun)

print("Метод Нелдера-Мида для функции Химмельблау")
print("Минимум найден в точке:", result.x)
print("Значение функции в минимуме:", result.fun)

input()