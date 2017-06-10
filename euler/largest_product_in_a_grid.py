def largest_product_in_a_grid(grid, window_size):
    rows = map(lambda row: list(map(int, row.split(' '))), grid)


    return list(map(list, rows))


if __name__ == '__main__':
    from solutions import q11

    print(q11())
