class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array_2d = ['']*numRows
        insert_pos = 0
        is_diagonal = False
        for letter in s:
            if insert_pos > numRows -1:
                insert_pos = (insert_pos - 2) if (insert_pos - 2) >= 0 else 0
                is_diagonal = not is_diagonal
            if insert_pos < 0:
                insert_pos = (insert_pos + 2) if (insert_pos + 2) <= (numRows-1) else (numRows-1)
                is_diagonal = not is_diagonal
            array_2d[insert_pos] += letter

            if is_diagonal:
                insert_pos -= 1
            else:
                insert_pos += 1
        return ''.join(array_2d)