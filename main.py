import concurrent.futures
def calculate_row_sum(row):
    return sum(row)
def main():
    matrix_size = int(input("Введите размер матрицы: "))
    matrix = []
    for i in range(matrix_size):
        row = list(map(int, input(f"Введите значения {i+1}-й строки через пробел: ").split()))
        matrix.append(row)
        row_sums = []
        for row in matrix:
            future = concurrent.futures.ProcessPoolExecutor().submit(calculate_row_sum, row)
            row_sums.append(future)
        total_row_sum = sum(future.result() for future in row_sums)
        print("Сумма элементов по строкам:", total_row_sum)
if __name__ == "__main__":
    main()