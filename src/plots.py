import csv
import matplotlib.pyplot as plt

sizes = [10, 500, 1000, 50000, 1000000]
data_types = ["Random", "Sorted", "Reversed", "Almost Sorted"]
interpreters = ["CPython", "PyPy"]

data = []
with open("results.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        data.append(row)


def get_points(row):
    x = []
    y = []
    for n in sizes:
        val = row.get(f"N={n} (время, мс)")
        if val and val not in ("TIMEOUT", "Замеры не производились"):
            x.append(n)
            y.append(float(val))
    return x, y


for interp in interpreters:
    for dtype in data_types:
        for row in data:
            if row["Интерпретатор"] == interp and row["Тип данных"] == dtype:
                x, y = get_points(row)
                if x and y:
                    plt.plot(x, y, marker="o", markersize=5, label=row["Алгоритм"])
        plt.xscale("log")
        plt.yscale("log")
        plt.xticks(sizes, labels=[str(n) for n in sizes])
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.title(f"Скорость ({interp}): {dtype}")
        plt.xlabel("Количество элементов N")
        plt.ylabel("Время (мс)")
        plt.legend()
        filename = f"img/plot_{interp.lower()}_{dtype.lower().replace(' ', '_')}.png"
        plt.savefig(filename, dpi=200)
        plt.clf()