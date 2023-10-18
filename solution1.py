# Write code for algorithm 1 below


def recursion(num):
    if num == 0:
        return
    else:
        print(num)
        return recursion(num - 1)


n = 4
print(recursion(n))
