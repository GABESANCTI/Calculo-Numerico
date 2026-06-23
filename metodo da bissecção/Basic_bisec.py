import math

#função a ser analisada ex slide 23 exercicio 1
f = lambda x: (-0.5*x**2)+(2.5*x) + 4.5  

#intervalo inicial
a = 5
b = 10
tol = 0.0001

if f(a) * f(b) < 0: 
    while (b - a) / 2 > tol: 
        p = a + (b - a) / 2
        if f(a) * f(p) < 0:
            b = p 
        else:
            a = p 
    print(f"raiz aproximada eh: {a}")