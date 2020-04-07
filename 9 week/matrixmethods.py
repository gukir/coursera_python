from sys import stdin
stdin = open('input.txt', 'r', encoding='utf8')


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
        for srow, orow in zip(self.data, other.data):
            row_res = []
            for selem, oelem in zip(srow, orow):
                row_res.append(selem + oelem)
            result.append(row_res)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for row in self.data:
            row_res = []
            for elem in row:
                row_res.append(elem * other)
            result.append(row_res)
        return Matrix(result)

    __rmul__ = __mul__


exec(stdin.read())
