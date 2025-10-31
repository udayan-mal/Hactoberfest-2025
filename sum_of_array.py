def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
    arr = [12, 3, 4, 15]
    print("Sum of given array is", sum_array(arr))
