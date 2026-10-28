def unique_routes(n,m):
    if n == 1 or m == 1:
        return 1

    return unique_routes(n - 1,m) + unique_routes(n, m - 1)

print(unique_routes(3,3))