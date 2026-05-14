#função a ser analisada ex slide 23 exercicio 1
f = lambda x: (-0.5*x**2)+(2.5*x) + 4.5    
#intervalo inicial
a = 5
b = 10
tol = 0.0001
          

if f(a) * f(b) >= 0:
    print("Erro: f(a) e f(b) devem ter sinais opostos.")
else:
    print(f"{'Iteração':<10} | {'Aproximação ':<10}| {'Erro (b-a)/2':<10}| {'Intervalo [a, b]':<20}")
    print("-" * 60)
    i = 1
    while (b - a) / 2 > tol:
        p = (a + b) / 2        
        
        print(f"{i:<10} | {p:<10.6f} | {(b-a)/2:<10.6f}|a={a:.6f}| b={b:.6f}")

        if f(a) * f(p) < 0:
            b = p 
        else:
            a = p  
        
        i += 1

    print("-" * 60)
    print(f"Raiz final aproximada: {a:.6f}")