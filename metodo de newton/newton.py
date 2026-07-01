import sympy as sp

#nota: não esquecer que funções como sen, cos e etc tem q usar o prefixo sp. para serem reconhecidas como funções simbólicas do sympy
# Definindo 'x' como uma variável simbólica p não confundir com char ou string
x = sp.symbols('x')

#função a ser avaliada

f_simbolica =  2*x - sp.sin(x) + 4

# Passo 3: Defina o chute inicial e a tolerância do exercício
x0 = 0.0                # Chute inicial (x0 ou x_i)
tol = 0.001             # Tolerância 


# derivada via lib sympy
df_simbolica = sp.diff(f_simbolica, x)

# Transformamos as expressões simbólicas em funções executáveis lambdas
f = sp.lambdify(x, f_simbolica, 'math')
df = sp.lambdify(x, df_simbolica, 'math')


#header 
print(f"Função Avaliada: f(x) = {f_simbolica}")
print(f"Derivada Gerada: f'(x) = {df_simbolica}\n")

print(f"{'i':<5} | {'x_i (Atual)':<15} | {'x_i+1 (Próximo)':<15} | {'Erro Absoluto':<15}")
print("-" * 60)

i = 1
xi = x0

while True:
    f_xi = f(xi)
    df_xi = df(xi)
    
    if df_xi == 0:
        print("Erro: Inclinação nula (f'(x) = 0). O método falhou devido à derivada zero.")
        break
        
    #  Newton-Raphson
    xi_mais_1 = xi - (f_xi / df_xi)
    
    # Cálculo do erro de transição entre os passos
    erro_atual = abs(xi_mais_1 - xi)
    
    print(f"{i:<5} | {xi:<15.8f} | {xi_mais_1:<15.8f} | {erro_atual:<15.8f}")
    
    # Critério de parada 
    if erro_atual < tol:
        break
        
    # Atualiza a variável para próxima iteração
    xi = xi_mais_1
    i += 1

print("-" * 60)
print(f"Raiz final encontrada: {xi_mais_1:.8f}")