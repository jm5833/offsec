from z3 import Ints, Solver

def sumof(a,b,c,d,e,f,g,h,i,j):
	return ((a * 227) + (b * 249) + (c * 104) + (d * 19) + (e * 33) + (f * 169) + (g * 154) + (h * 58) + (i * 98) + (j * 198) == 9595)

a,b,c,d,e,f,g,h,i,j = Ints('a b c d e f g h i j')
solve = sumof(a,b,c,d,e,f,g,h,i,j)
s = Solver()
s.add(solve == True)
s.add(a > 1, b >= 0, c >= 0, d >= 0, e >= 0, f >= 0, g >= 0, h >= 0, i >= 0, j >= 0)
s.add(a <= 7, b <= 7, c <= 7, d <= 7, e <= 7, f <= 7, g <= 8, h <= 8, i <= 8, j <= 8)  
print s.check()
print s.model()
'''
nnnRnnnnLRLnRLnnLLLn
'''
