def binary_search_with_upper_bound(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    closest = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            closest = arr[mid]  # Запам'ятовуємо поточний елемент як можливу верхню межу
            high = mid - 1
        else:
            # Якщо ми знайшли точне значення, верхня межа буде саме це значення
            return (iterations, arr[mid])

    # Якщо точне значення не знайдено, то використовуємо останнє запам'ятоване значення як верхню межу
    if closest is None:
        # Якщо все ще None, це означає, що всі елементи менші за target
        closest = arr[-1] if arr[-1] > target else None

    return (iterations, closest)

# Приклад використання
arr = [1.1, 1.5, 3.5, 4.5, 5.5, 6.7, 8.8]
target = 4.0
result = binary_search_with_upper_bound(arr, target)
print("Iterations:", result[0], "Upper Bound:", result[1])
