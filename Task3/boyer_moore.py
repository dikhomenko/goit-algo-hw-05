def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    result = []

    # Використання словника замість масиву
    bad_char = {}

    # Ініціалізація таблиці поганих символів
    for i in range(m):
        bad_char[pattern[i]] = i

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            result.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

    return result
