def kmp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0  # Довжина попереднього найбільшого префіксу, який є суфіксом

    compute_lps_array(pattern, m, lps)

    i = 0  # Індекс для text
    result = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            result.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

def compute_lps_array(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

