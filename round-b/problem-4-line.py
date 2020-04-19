def solve_case():
    [W, H, L, U, R, D] = list(map(int, input().split(' ')))
    L, U, R, D = L - 1, U - 1, R - 1, D - 1

    probas = [1] * H
    for i in range(R, -1, -1):
        for j in range(H - 1, -1, -1):
            if i >= L and j >= U and j <= D:
                probas[j] = 0
            elif j != H - 1:
                if i != W - 1:
                    probas[j] = 0.5 * probas[j] + 0.5 * probas[j + 1]
                else:
                    probas[j] = probas[j + 1]

    return probas[0]


T = int(input())
for t in range(T):
    p = solve_case()
    print("Case #{}: {}".format(t + 1, p))
