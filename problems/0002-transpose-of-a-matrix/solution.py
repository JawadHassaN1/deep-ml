def transpose_matrix(a):
    if not a:
        return []
    
    rows = len(a)
    cols = len(a[0])

    result = []

    for j in range(cols):
        new_row = []

        for i in range(rows):
            new_row.append(a[i][j])
        result.append(new_row)
    return result