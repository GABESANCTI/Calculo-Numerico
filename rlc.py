import math

'''Um problema de projeto típico em engenharia ( elétrica, controle, computação) poderia
envolver a determinação do resistor apropriado para dissipar energia a uma taxa
específica , com valores conhecidos para L e C. Para esse Problema, suponha que a
carga deve ser dissipada a 1% do seu valor original (q/q0 = 0,01) em t=0,05s, com L = 5
H eC=10-4F
PS: Use o método da Bissecção. O método de Newton-Raphson pode ser incoveniente
em virtude do cálculo da derivada de (1) ser trabalhoso.
Avariável implícita da equação é R. '''

L = 5.0           
C = 1e-4            
t = 0.05           
alvo = 0.01         


a = 0.0            # Limite inferior de Resistência (R)
b = 400.0          # Limite superior de Resistência (R)
tol = 0.0001      


f = lambda R: math.exp(-R * t / (2 * L)) * \
              math.cos(math.sqrt(abs(1 / (L * C) - (R / (2 * L))**2)) * t) - alvo

if f(a) * f(b) >= 0:
    print("O intervalo [a, b] não é válido (não há troca de sinal).")
else:
    print(f"{'i':<5} | {'R (Aproximação)':<18} | {'Erro (b-a)/2':<15} {'Intervalo [a, b]':<20}")
    print("-" * 45)
    
    i = 1
    while (b - a) / 2 > tol:
        p = (a + b) / 2
        
        print(f"{i:<5} | {p:<18.6f} | {(b-a)/2:<15.6f} | [{a:.6f}, {b:.6f}]")
        
        # Teste de sinal para decidir o próximo intervalo [cite: 92, 94]
        if f(a) * f(p) < 0:
            b = p  
        else:
            a = p 
        i += 1

    print("-" * 45)
    print(f"Resistência calculada (R): {p:.4f} Ohms")