# #01 Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
# Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
# equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa
# após subtrair esse bônus.

fat = 50_000
perc_bonus = 0.1
bonus_total = fat * perc_bonus
fat_liquido = fat - bonus_total
print("Faturamento liquido:" , fat_liquido)
print("Bonus Total:" , bonus_total)

# #2 Exercício 2: Controle de Estoque de E-commerce (Logística)
# Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no
# estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um
# fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.

estoque = 250
vendas = 78 
reposicao = 100
estoque = estoque - vendas + reposicao
print("O estoque final é de:" , estoque)

# Exercício 3: Divisão de Cargas (Logística/Transporte)
# Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
# caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
# totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
# última viagem menor? (Use %)

caixas = 1250
capacidade_caminhao = 12
caminhoes_completos = caixas // capacidade_caminhao
print("Caminhoes completos;" , caminhoes_completos)
caixas_restantes = caixas % capacidade_caminhao
print("Caixas restantes:" , caixas_restantes)

# Exercício 4: Análise de Margem de Lucro (Financeiro)
# Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
# 5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
# líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
# chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

fat = 15000
custos = 5000
perc_imposto = 0.15 

imposto = fat * perc_imposto
lucro = fat - custos - imposto
margem = lucro / fat 
print("faturamento" , fat)
print("O imposto é de:" , imposto)
print("O lucro líquido é de:" , lucro)
print("A margem de lucro é de:" , margem)

margem_atingida = margem > 0.3
print("Meta atingida:" , margem_atingida)

# Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
# Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente
# quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de
# divisão inteira e resto da divisão para converter os 40 meses.

duracao = 40
anos = 40 // 12
meses = 40 % 12
print("o contrato tem" , anos , "anos e" , meses , "meses.")