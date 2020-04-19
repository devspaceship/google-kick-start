def get_proba(w, h, W, H):
    proba = probas[w][h]
    if proba is not None:
        return proba
    elif w == W - 1:
        proba = get_proba(w, h + 1, W, H)
        probas[w][h] = proba
        return proba
    elif h == H - 1:
        proba = get_proba(w + 1, h, W, H)
        probas[w][h] = proba
        return proba
    else:
        proba = 0.5 * get_proba(w, h + 1, W, H) + \
                0.5 * get_proba(w + 1, h, W, H)
        probas[w][h] = proba
        return proba


T = int(input())
for t in range(T):
    [W, H, L, U, R, D] = list(map(int, input().split(' ')))

    global probas
    probas = [[None] * H for _ in range(W)]
    for i in range(W):
        for j in range(H):
            if i >= R or j >= D:
                probas[i][j] = 1
            elif i >= L - 1 and j >= U - 1:
                probas[i][j] = 0

    print("Case #{}: {}".format(t + 1, get_proba(0, 0, W, H)))
