import csv
import os
import platform
import sys
import time

try:
    import tracemalloc
    memory_control = True
except ImportError:
    memory_control = False

# Импорт из файла algorithms.py
from algorithms import algorithms
from generators import sizes, data_types

sys.setrecursionlimit(2000000)

slow_sorts = ["Bubble", "Selection", "Insertion"]


def run_benchmark():
    interpreter = platform.python_implementation()
    fieldnames = [
        "Интерпретатор", "Тип данных", "Алгоритм",
        "N=10 (время, мс)", "N=10 (память, КБ)",
        "N=500 (время, мс)", "N=500 (память, КБ)",
        "N=1000 (время, мс)", "N=1000 (память, КБ)",
        "N=50000 (время, мс)", "N=50000 (память, КБ)",
        "N=1000000 (время, мс)", "N=1000000 (память, КБ)",
    ]
    rows = []

    for dtype_name, gen_func in data_types.items():
        print(f"Тестирование: {dtype_name}...")
        for sort_name, sort_func in algorithms.items():
            row = {
                "Интерпретатор": interpreter,
                "Тип данных": dtype_name,
                "Алгоритм": sort_name,
            }
            for n in sizes:
                if n >= 50000 and sort_name in slow_sorts:
                    row[f"N={n} (время, мс)"] = "TIMEOUT"
                    row[f"N={n} (память, КБ)"] = "TIMEOUT"
                    continue
                nums = gen_func(n)
                if memory_control:
                    tracemalloc.start()
                start = time.perf_counter()
                sort_func(nums)
                end = time.perf_counter()
                if memory_control:
                    peak = tracemalloc.get_traced_memory()[1]
                    tracemalloc.stop()
                    mem_kb = round(peak / 1024, 2)
                else:
                    mem_kb = "Замеры не производились"
                t_ms = round((end - start) * 1000, 3)
                row[f"N={n} (время, мс)"] = t_ms
                row[f"N={n} (память, КБ)"] = mem_kb
            rows.append(row)

    file_exists = os.path.exists("results.csv")

    with open("results.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    run_benchmark()