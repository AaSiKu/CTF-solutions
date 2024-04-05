from sympy import symbols, solve

'''
b + c + w = 319
t + d + u = 257
p + w + e = 351
v + l + j = 242
a + t + b = 313
b + j + m = 313
h + o + u = 196
q + l + o = 241
a + g + j = 245
q + x + q = 315
t + n + m = 264
d + b + g = 259
e + o + m = 330
v + v + u = 247
f + o + q = 259
s + o + j = 300
j + j + n = 241
s + u + l = 208
q + w + j = 304
i + d + r = 276
e + k + u = 250
w + n + a = 267
r + e + u = 239
q + l + f = 211
'''

# Define symbolic variables
# x, y, z = symbols('x y z')
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x = symbols('a b c d e f g h i j k l m n o p q r s t u v w x')


# Define the equations
eq1 = b + c + w - 319
eq2 = t + d + u - 257
eq3 = p + w + e - 351
eq4 = v + l + j - 242
eq5 = a + t + b - 313
eq6 = b + j + m - 313
eq7 = h + o + u - 196
eq8 = q + l + o - 241
eq9 = a + g + j - 245
eq10 = q + x + q - 315
eq11 = t + n + m - 264
eq12 = d + b + g - 259
eq13 = e + o + m - 330
eq14 = v + v + u - 247
eq15 = f + o + q - 259
eq16 = s + o + j - 300
eq17 = j + j + n - 241
eq18 = s + u + l - 208
eq19 = q + w + j - 304
eq20 = i + d + r - 276
eq21 = e + k + u - 250
eq22 = w + n + a - 267
eq23 = r + e + u - 239
eq24 = q + l + f - 211


# Solve the equation system
# solution = solve((eq1, eq2, eq3), (x, y, z))
solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9, eq10, eq11, eq12, eq13, eq14, eq15, eq16, eq17, eq18, eq19, eq20, eq21, eq22, eq23, eq24), (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x))

# Print the solution
print("Solution:", solution)

flag = ""
for key, value in solution.items():
    flag += chr(value)
print(flag)