class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_print = ''
        for i in self.matrix:
            i_string = ''
            for j in i:
                i_string += str(j) + ' '
            matrix_print += i_string + '\n'
        return matrix_print

    def __add__(self, other):
        new_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
        return Matrix(new_matrix)


my_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matrix_2 = Matrix([[3, 4, 5], [6, 7, 8], [7, 8, 9]])
print(my_matrix)
print(my_matrix + my_matrix_2)
