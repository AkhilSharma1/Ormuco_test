
def is_overlap(x1, x2, x3, x4): return x1 <= x3 <= x2 or x1 <= x4 <= x2


if __name__ == '__main__':
    print('please enter the 4 points separated by space( example : 1 5 2 6\\n)')
    x1, x2, x3, x4 = map(int, input().split())

    result = "Overlap" if is_overlap(x1, x2, x3, x4) else "No overlap"
    print(result)
