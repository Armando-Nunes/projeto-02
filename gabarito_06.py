# Exercício 1: Atualização de Cadastro de Clientes (Setor de CRM) Você tem um
# dicionário com o faturamento acumulado de alguns clientes: clientes = {"Lira":
# 5000, "Alon": 3000, "Julia": 4500}. O cliente "Alon" fez uma nova compra de R$
# 1.500,00. Crie um código que:
# 1. Atualize o valor do cliente "Alon" somando o novo valor ao faturamento antigo.
# 2. Adicione um novo cliente chamado "Marcos" com um faturamento inicial de R$
# 2.000,00.
# 3. Exiba o dicionário atualizado.

clientes = {"Lira": 5000, "Alon": 3000, "Julia": 4500}

nova_compra = 1500
clientes["Alon"] = clientes["Alon"] + nova_compra

clientes["Marcos"] = 2000
print(clientes)


# Exercício 2: Consulta de Estoque Interativa (Setor de Logística) A empresa possui o
# seguinte estoque: estoque = {"teclado": 50, "mouse": 120, "monitor": 30}.
# Crie um programa que peça para o usuário digitar o nome de um produto.
# 1. Se o produto existir no estoque, exiba a quantidade disponível.
# 2. Se o produto não existir, exiba a mensagem: "Produto não encontrado no sistema".
# Dica: Lembre-se de tratar o input para evitar erros de letras maiúsculas ou espaços.

estoque = {"teclado": 50, "mouse": 120, "monitor": 30}
produto = input("Digite o nome do produto:")

produto = produto.strip().lower()

if produto in estoque:
    print(f"{produto} encontrado: {estoque[produto]} unidades no estoque")
else:
    print(f"{produto} não encontrado")


# Exercício 3: Análise de Faturamento por Região (Setor Financeiro) Dada a lista de
# faturamento por região: vendas_regiao = {"Norte": 15000, "Sul": 22000,
# "Leste": 18000, "Oeste": 25000}. Seu programa deve:
# 1. Extrair todos os valores (faturamentos) para uma lista.
# 2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões).
# 3. Calcular e exibir o faturamento médio das regiões.

vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}

lista_vendas = list(vendas_regiao.values())
total_vendas = sum(lista_vendas)
qtde_vendas = len(lista_vendas)
media_vendas = total_vendas / qtde_vendas
print("Total Vendas", total_vendas)
print("Media de Vendas", media_vendas)

# Exercício 4: Sistema de RH – Média de Desempenho (Setor de RH) O RH armazena as
# últimas 3 notas de desempenho de cada funcionário em um dicionário: desempenho =
# {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}. O gestor
# quer saber a média da funcionária "Paula". Crie um código que:
# 1. Acesse a lista de notas da "Paula".
# 2. Calcule a média das notas (soma das notas dividida pela quantidade de notas).
# 3. Exiba o resultado: "A média de Paula foi [media]".

desempenho = {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}
nome = input("Digite o nome de um colaborador:")

notas = desempenho[nome]
print("Nome:", nome)
print("Notas", notas)
media_notas = sum(notas) / len(notas)
print("Media", media_notas)


# Exercício 5: Limpeza de Banco de Dados (Setor de TI) O sistema de e-commerce
# descontinuou alguns produtos. Você tem o dicionário: produtos = {"celular": 1500,
# "camera": 800, "radio": 200, "fone": 100}. O item "radio" deve ser removido
# por estar obsoleto. Crie um código que:
# 1. Remova o item "radio" do dicionário usando o método .pop().
# 2. Imprima o valor do produto que foi removido para fins de log.
# 3. Verifique se o produto "celular" ainda existe no dicionário e imprima True ou False.

produtos = {"celular": 1500, "camera": 800, "radio": 200, "fone": 100}
item_removido = "celular"

produtos.pop(item_removido)
print(produtos)

celular_no_dic = "celular" in produtos
print("Celular no estoque?", celular_no_dic)