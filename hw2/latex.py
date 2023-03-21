def row_generator(row):
    length = len(row)
    return " ".join([str(row[i]) + " &"  if i != (length-1)
                    else str(row[i]) for i in range(length)])


def table(matrix):
    start = "\\begin{table}[] \\begin{tabular}"
    columns = "{" + "|l"*len(matrix[0]) + "|}" + " \hline"
    rows = " \\\ \\hline ".join([row_generator(row) for row in matrix])
    end = "\\\ \hline \\end{tabular} \\end{table}"
    return start + columns + rows + end


with open("artifacts/easy/latex.tex", "w") as file:
    file.write(table([[1, 2, 3, 0],
                      [4, 5, 6, 0],
                      [7, 8, 9, 0]]))