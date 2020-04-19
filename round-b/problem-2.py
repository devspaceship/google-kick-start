T = int(input())
for t in range(T):
    [N, D] = list(map(int, input().split(' ')))
    xi = list(map(int, input().split(' ')))
    leave_times = []
    for x in reversed(xi):
        leave_time = (D // x) * x
        leave_times.append(leave_time)
        D = leave_time
    print("Case #{}: {}".format(t + 1, leave_times[-1]))