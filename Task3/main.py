import timeit
from boyer_moore import boyer_moore
from kmp_search import kmp_search
from rabin_karp import rabin_karp

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Визначення текстів та шаблонів на рівні глобальних змінних
text1 = read_file('/Users/dina.khomenko/Downloads/Master_CS-SE/MS_Repos/goit-algo-hw-05/Task3/article1.txt')
text2 = read_file('/Users/dina.khomenko/Downloads/Master_CS-SE/MS_Repos/goit-algo-hw-05/Task3/article2.txt')
pattern1 = "умова припинення"
pattern2 = "кількість агентів 65536"

def main():
    global text1, text2, pattern1, pattern2

    time_rk_text1 = timeit.timeit('rabin_karp(text1, pattern1)', globals=globals(), number=10)
    time_rk_text2 = timeit.timeit('rabin_karp(text2, pattern1)', globals=globals(), number=10)
    time_rk_text3 = timeit.timeit('rabin_karp(text1, pattern2)', globals=globals(), number=10)
    time_rk_text4 = timeit.timeit('rabin_karp(text2, pattern2)', globals=globals(), number=10)

    print(f"Час Рабіна-Карпа зі зразком 1 на тексті 1: {time_rk_text1}")
    print(f"Час Рабіна-Карпа зі зразком 1 на тексті 2: {time_rk_text2}")
    print(f"Час Рабіна-Карпа зі зразком 2 на тексті 1: {time_rk_text3}")
    print(f"Час Рабіна-Карпа зі зразком 2 на тексті 2: {time_rk_text4}")

    time_bm_text1 = timeit.timeit('boyer_moore(text1, pattern1)', globals=globals(), number=10)
    time_bm_text2 = timeit.timeit('boyer_moore(text2, pattern1)', globals=globals(), number=10)
    time_bm_text3 = timeit.timeit('boyer_moore(text1, pattern2)', globals=globals(), number=10)
    time_bm_text4 = timeit.timeit('boyer_moore(text2, pattern2)', globals=globals(), number=10)

    print(f"Час Бойера-Мура зі зразком 1 на тексті 1: {time_bm_text1}")
    print(f"Час Бойера-Мура зі зразком 1 на тексті 2: {time_bm_text2}")
    print(f"Час Бойера-Мура зі зразком 2 на тексті 1: {time_bm_text3}")
    print(f"Час Бойера-Мура зі зразком 2 на тексті 2: {time_bm_text4}")

    time_kmp_text1 = timeit.timeit('kmp_search(text1, pattern1)', globals=globals(), number=10)
    time_kmp_text2 = timeit.timeit('kmp_search(text2, pattern1)', globals=globals(), number=10)
    time_kmp_text3 = timeit.timeit('kmp_search(text1, pattern2)', globals=globals(), number=10)
    time_kmp_text4 = timeit.timeit('kmp_search(text2, pattern2)', globals=globals(), number=10)

    print(f"Час КМП зі зразком 1 на тексті 1: {time_kmp_text1}")
    print(f"Час КМП зі зразком 1 на тексті 2: {time_kmp_text2}")
    print(f"Час КМП зі зразком 2 на тексті 1: {time_kmp_text3}")
    print(f"Час КМП зі зразком 2 на тексті 2: {time_kmp_text4}")


if __name__ == "__main__":
    main()