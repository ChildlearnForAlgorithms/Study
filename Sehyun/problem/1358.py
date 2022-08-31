W, H, X, Y, P = map(int, input().split())
cnt = 0


def athlete_in():
    global cnt
    x, y = map(int, input().split())
    if X <= x <= (X + W) and Y <= y <= (Y + H):
        cnt += 1
    else:
        R = 1 / 2 * H
        d1 = ((x - X) ** 2 + (y - (Y + R)) ** 2) ** 0.5
        d2 = ((x - (X + W)) ** 2 + (y - (Y + R)) ** 2) ** 0.5
        if d1 <= R or d2 <= R:
            cnt += 1


for _ in range(P):
    athlete_in()

print(cnt)
