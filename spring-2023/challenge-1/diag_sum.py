def diag_sum(matrix):
    matrix_len = [len(matrix[0]), len(matrix)]
    primary_diag = []
    secondary_diag = []
    matrix_flat = []
    for row in matrix:
        matrix_flat += [*row]

    for i in range(0, (matrix_len[0] * matrix_len[1]), matrix_len[0]+1):
        primary_diag += [matrix_flat[i]]
    for i in range((matrix_len[0] * matrix_len[1]) - matrix_len[0], 0, -matrix_len[0] +1):
        secondary_diag += [matrix_flat[i]]

    if primary_diag[len(primary_diag)//2] == secondary_diag[len(secondary_diag)//2]:
        primary_diag.pop(len(primary_diag)//2)

    sum_list = [*primary_diag, *secondary_diag]

    return sum(sum_list)