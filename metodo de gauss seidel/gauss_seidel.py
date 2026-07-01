
A = [
    [10.0, -1.0,  2.0,  0.0,  1.0],
    [-1.0, 11.0, -1.0,  3.0,  0.0],
    [ 2.0, -1.0, 10.0, -1.0,  0.0],
    [ 0.0,  3.0, -1.0,  8.0, -2.0],
    [ 1.0,  0.0,  0.0, -2.0,  5.0]
]

# Vetor de termos independentes b
b = [6.0, 25.0, -11.0, 15.0, 11.0]

# Parâmetros das iterações (Slide 11, 12 e 19)
x0 = [0.0, 0.0, 0.0, 0.0, 0.0]  # Aproximações iniciais nulas
es = 5.0                        # Tolerância de erro percentual de 5% 
max_iter = 50                    # Limite de iterações

#GAUSS-SEIDEL 
n = len(b)
x_atual = list(x0)

print("Iterações do Método de Gauss-Seidel ")
print(f"{'i':<5} | {'Vetor Solução x':<48} | {'Maior Erro %':<12}")
print("-" * 75)

for iteracao in range(1, max_iter + 1):
    x_anterior = list(x_atual)   # Salva o x velho (j-1) para calcular o erro
    
    # Loop passando de linha em linha isolando a diagonal 
    for i in range(n):
        soma = 0.0
        for j in range(n):
            if i != j:
                soma += A[i][j] * x_atual[j] # Usa o x_atual mais recente disponível
        
        # Fórmula de isolamento: x_i = (b_i - soma) / A_ii (Slide 10)
        x_atual[i] = (b[i] - soma) / A[i][i]
        
    # Cálculo do Erro Percentual Relativo para cada componente (Slide 12)
    erros_componentes = []
    for k in range(n):
        if x_atual[k] != 0: # Evita divisão por zero caso o x atual seja nulo
            # Fórmula da Equação (5) do seu Slide 12
            ep_k = abs((x_atual[k] - x_anterior[k]) / x_atual[k]) * 100
            erros_componentes.append(ep_k)
        else:
            erros_componentes.append(0.0)
            
    # O erro da iteração é o maior erro encontrado entre todas as incógnitas
    maior_erro_pct = max(erros_componentes)
    
    # Formatação do vetor para a tabela
    vetor_formatado = "[" + ", ".join(f"{val:.4f}" for val in x_atual) + "]"
    
    # Na primeira iteração o erro dá 100%, igualzinho ao exemplo do seu Slide 7 (Newton) e Slide 15
    if iteracao == 1:
        print(f"{iteracao:<5} | {vetor_formatado:<48} | {'100.0000%':<12}")
    else:
        print(f"{iteracao:<5} | {vetor_formatado:<48} | {maior_erro_pct:.4f}%")
        
    # Critério de parada: se o maior erro percentual for menor que es (Slide 12)
    if iteracao > 1 and maior_erro_pct < es:
        print("-" * 75)
        print(f"Convergência atingida na iteração {iteracao}!")
        break
else:
    print("-" * 75)
    print("Aviso: O número máximo de iterações foi atingido.")

print("\nSolução final encontrada:")
for idx, val in enumerate(x_atual):
    print(f"x{idx+1} = {val:.4f}")