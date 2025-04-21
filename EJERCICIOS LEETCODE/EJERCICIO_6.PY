class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        filas = [""] * numRows
        fila_actual = 0
        bajando = False

        for caracter in s:
            filas[fila_actual] += caracter
            if fila_actual == 0 or fila_actual == numRows - 1:
                bajando = not bajando
            fila_actual += 1 if bajando else -1

        return "".join(filas)


sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"