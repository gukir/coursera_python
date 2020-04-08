from sys import stdin
stdin = open('input.txt', 'r', encoding='utf8')


class MatrixError(BaseException):
    def __init__(self, first_operand, other):
        self.matrix1 = first_operand
        self.matrix2 = other


class Matrix:
    def __init__(self, lists):
        tmp_size = [0, 0]
        self.data = []
        for row in lists:
            tmp_size[0] += 1
            tmp_size[1] = 0
            tmp_row = []
            for elem in row:
                tmp_row.append(elem)
                tmp_size[1] += 1
            self.data.append(tmp_row)
        self.sz = tuple(tmp_size)

    def __str__(self):
        out_str = ''
        for row in self.data:
            row_str = ''
            for elem in row:
                row_str += (str(elem) + '\t')
            row_str = row_str.strip()
            row_str += '\n'
            out_str += row_str
        out_str = out_str.strip()
        return out_str

    def size(self):
        return self.sz

    def __add__(self, other):
        result = []
        if isinstance(other, Matrix) and self.size() == other.size():
            for srow, orow in zip(self.data, other.data):
                row_res = []
                for selem, oelem in zip(srow, orow):
                    row_res.append(selem + oelem)
                result.append(row_res)
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        if isinstance(other, int) or isinstance(other, float):
            for row in self.data:
                row_res = []
                for elem in row:
                    row_res.append(elem * other)
                result.append(row_res)
        elif isinstance(other, Matrix) and self.sz[1] == other.sz[0]:
            tmp_matr = Matrix.transposed(other)
            for n_row in range(self.sz[0]):
                row_res = []
                for n_col in range(other.sz[1]):
                    row_res.append(
                        sum(
                            map(
                                lambda x, y: x * y, self.data[n_row],
                                tmp_matr.data[n_col])))
                result.append(row_res)
        else:
            raise MatrixError(self, other)
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        self.data = list(map(list, zip(*self.data)))
        rows = len(self.data)
        if rows:
            cols = len(self.data[0])
            self.sz = (rows, cols)
        else:
            self.sz = (rows, 0)
        return self

    def solve(self, b_vec):
        new_m = Matrix(self.data)
        if new_m.sz[0] == new_m.sz[1]:
            n_row = 0
            n_col = 0
            while n_row < new_m.sz[0] and n_col < new_m.sz[1]:
                e_max = 0.
                row_max = -1
                for o_row in range(n_row, new_m.sz[0]):
                    if abs(new_m.data[o_row][n_col]) > e_max:
                        row_max = o_row
                        e_max = abs(new_m.data[o_row][n_col])
                if e_max < 1e-15:
                    n_col += 1
                    continue
                if row_max != n_row:
                    b_vec[row_max], b_vec[n_row] =\
                        b_vec[n_row], b_vec[row_max]
                    for o_col in range(new_m.sz[1]):
                        new_m.data[n_row][o_col],\
                            new_m.data[row_max][o_col] = \
                            new_m.data[row_max][o_col],\
                            new_m.data[n_row][o_col]
                for o_row in range(n_row + 1, new_m.sz[0]):
                    coeff =\
                        new_m.data[o_row][n_col] / new_m.data[n_row][n_col]
                    b_vec[o_row] -= coeff * b_vec[n_row]
                    for o_col in range(new_m.sz[1]):
                        new_m.data[o_row][o_col] -=\
                            coeff * new_m.data[n_row][o_col]
                n_col += 1
                n_row += 1
            if n_row < new_m.sz[0]:
                raise Exception
            else:
                x = [0 for i in range(new_m.sz[1])]
                for n_row in range(new_m.sz[0] - 1, -1, -1):
                    left = 0
                    for n_col in range(new_m.sz[1]):
                        left += new_m.data[n_row][n_col] * x[n_col]
                    x[n_row] =\
                        (b_vec[n_row] - left) / new_m.data[n_row][n_row]
                return x

    @staticmethod
    def updiag(matrix):
        new_m = Matrix(matrix.data)
        if new_m.sz[0] == new_m.sz[1]:
            n_row = 0
            n_col = 0
            while n_row < new_m.sz[0] and n_col < new_m.sz[1]:
                e_max = 0.
                row_max = -1
                for o_row in range(n_row, new_m.sz[0]):
                    if abs(new_m.data[o_row][n_col]) > e_max:
                        row_max = o_row
                        e_max = abs(new_m.data[o_row][n_col])
                if e_max < 1e-15:
                    n_col += 1
                    continue
                if row_max != n_row:
                    for o_col in range(new_m.sz[1]):
                        new_m.data[n_row][o_col],\
                            new_m.data[row_max][o_col] = \
                            new_m.data[row_max][o_col],\
                            new_m.data[n_row][o_col]
                for o_row in range(n_row + 1, new_m.sz[0]):
                    coeff =\
                        new_m.data[o_row][n_col] / new_m.data[n_row][n_col]
                    for o_col in range(new_m.sz[1]):
                        new_m.data[o_row][o_col] -=\
                            coeff * new_m.data[n_row][o_col]
                n_col += 1
                n_row += 1

            return new_m

    @staticmethod
    def transposed(matrix):
        new_m = Matrix(matrix.data)
        return new_m.transpose()


class SquareMatrix(Matrix):
    def __mul__(self, other):
        res_m = super().__mul__(other)
        return SquareMatrix(res_m.data)

    def __pow__(self, power, modulo=None):
        result = SquareMatrix(self.data)
        if power == 0:
            result.data = [[0 for i in range(self.sz[1])]
                           for j in range(self.sz[0])]
            for i in range(self.sz[0]):
                result.data[i][i] = 1
            return result
        elif power == 1:
            return result
        elif power == 2:
            return result * result
        elif power % 2 == 1:
            return result * (result ** (power - 1))
        else:
            return (result ** (power // 2)) * (result ** (power // 2))


exec(stdin.read())
