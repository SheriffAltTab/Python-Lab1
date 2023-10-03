import ray

# Ініціалізація Ray
ray.init()

# Функція, яку ми хочемо виконати паралельно
def my_function(x):
    return x * x

# Створюємо дві паралельні задачі
result1 = ray.remote(my_function).remote(3)
result2 = ray.remote(my_function).remote(6)

# Очікуємо на результати
result1_value = ray.get(result1)
result2_value = ray.get(result2)

# Виводимо результати
print("Результат 1:", result1_value)
print("Результат 2:", result2_value)

# Завершуємо роботу з Ray
ray.shutdown()
