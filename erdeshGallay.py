def is_graphic(vector):
    n = len(vector)
    total_sum = sum(vector)
    if total_sum % 2 != 0:
        return False
    vector.sort(reverse=True)
    for k in range(1, n+1):
        left_sum = sum(vector[:k])
        right_sum = k*(k-1) + sum(min(vector[i], k) for i in range(k, n))
        if left_sum > right_sum:
            return False
    return True

if __name__ == "__main__":
    with open("inputGallay.txt") as file:
        array = [int(row.strip()) for row in file]
        if is_graphic(array):
            print("Вектор является графическим")
        else:
            print("Вектор не является графическим")
