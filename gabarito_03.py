# # Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de
# serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o
# valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
# 1. Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
# 2. Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
# 3. Converter para número decimal (float).
# 4. Calcular o valor do imposto (15% do valor bruto).
# 5. Exibir uma mensagem formatada com f-string mostrando o valor do imposto com
# duas casas decimais.

fat = input("Digite o faturamento:")
fat = fat.replace("R$", "").replace(".", "").replace(",", ".")
fat_numerico = float(fat)
perc_imposto = 0.15
imposto = fat_numerico * perc_imposto
print(f"Imposto pago: R${imposto:,.2f}")

# # Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH) Ao cadastrar um novo
# funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o
# e-mail. Crie um programa que:
# 1. Peça o nome completo do colaborador.
# 2. Peça o e-mail pessoal do colaborador.
# 3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
# 4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
# 5. Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail
# padronizado]".

mensagem = "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail padronizado]"

nome = input("Digite o nome completo do colaborador:")
email = input("Digite o email do colaborador:")

nome = nome.strip()
email = email.strip().lower()

posicao_espaco = nome.find("")
pri_nome = nome[:posicao_espaco].capitalize()

mensagem = mensagem.replace("[Primeiro Nome]", pri_nome).replace("[E-mail padronizado]", email)
print(mensagem)

# # Exercício 3: Análise de Metas de Vendas (Setor Comercial) Um gerente quer comparar o
# desempenho de duas filiais. O programa deve:
# 1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar
# números decimais).
# 2. Calcular o faturamento total das duas lojas.
# 3. Calcular a média de faturamento entre elas.
# 4. Exibir uma única mensagem formatada informando o total e a média, utilizando o
# separador de milhar e duas casas decimais.

fat_lojaA = input("Faturamento da Loja A:")
fat_lojaB = input("Faturamento da Loja B:")

fat_lojaA = fat_lojaA.replace("R$", "").replace(".", "").replace(",", ".")
fat_lojaA = float(fat_lojaA)

fat_lojaB = fat_lojaB.replace("R$", "").replace(".", "").replace(",", ".")
fat_lojaB = float(fat_lojaB)

total_fat = fat_lojaA + fat_lojaB
media_fat = total_fat / 2

print(f"Faturamento Total: R${total_fat:,.2f}, Média de Faturamento: R${media_fat:,.2f}")