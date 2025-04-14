class Solution:
    def isValid(self, s):
        stack = []
        for caracter in s:
            if caracter == '(':
                stack.append(')')
            elif caracter == '{':
                stack.append('}')
            elif caracter == '[':
                stack.append(']')
            else:
                if not stack or stack.pop() != caracter:
                    return False
        return not stack
    
entrada = input("Ingresá una cadena con paréntesis, llaves y corchetes: ")
solucion = Solution()
print(solucion.isValid(entrada))