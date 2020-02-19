b = [1, 46, 5, 8]

kernel = 0

for i in range(len(b)-1, -1, -1):
    for j in range(len(b)-1 - kernel, -1, -1):
        print("backward backward", b[i], b[j])

    kernel += 1


kernel = 0

for i in range(len(b)-1, -1, -1):
    for j in range(len(b) - kernel):
        print("backward forward", b[i], b[j])

    kernel += 1


kernel = 0

for i in range(len(b)):
    for j in range(len(b)-1 - kernel, -1, -1):
        print("forward backward", b[i], b[j])

    kernel += 1


kernel = 0

for i in range(len(b)):
    for j in range(len(b) - kernel):
        print("forward forward", b[i], b[j])

    kernel += 1


# for i in range(10):
#     print(i)
