def chessboard(n = 8):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(" #" * int(n/2))
        else:
            print("# " * int(n/2))

print(chessboard(8))
