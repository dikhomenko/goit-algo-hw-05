def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = t = h = 0
    result = []

    # Значення h буде 'pow(d, m-1)%q'
    h = pow(d, m-1) % q

    # Обрахування значення хешу для паттерна та перших 'm' символів тексту
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    # Переміщення паттерну по тексту
    for i in range(n - m + 1):
        if p == t:  # Якщо хеші співпадають, перевіряємо символи один за одним
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            else:
                result.append(i)

        if i < n - m:
            t = (t - ord(text[i]) * h) * d + ord(text[i + m]) % q
            t = (t + q) % q  # Додати q для уникнення від'ємного значення

    return result

