# Exercício 1: Validação de Investimento (Setor Financeiro) Uma corretora de valores
# quer automatizar a recomendação básica de perfil. Crie um programa que peça ao usuário o
# valor que ele deseja investir.
# 1. Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro
# Direto".
# 2. Se o valor for entre R$ 1.000,00 e R$ 5.000,00 (inclusive), exiba: "Perfil moderado:
# Sugerimos Fundos Imobiliários".
# 3. Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações".
# *Lembre-se de tratar o input caso o usuário digite "R$" ou use vírgula.*


valor = input("Digite o valor que você vai querer investir:")
valor = valor.replace("R$", "").replace(".", "").replace(",", ".")
valor = float(valor)

if valor < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor <= 5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários")
else:
    print("Perfil arrojado: Sugerimos Ações")


# Exercício 2: Controle de Acesso ao Sistema (Setor de Segurança) Você tem uma lista
# de e-mails de administradores: admins = ["ana@empresa.com",
# "guilherme@empresa.com", "felipe@empresa.com"]. Crie um programa que peça
# o e-mail do usuário. O programa deve:
# 1. Padronizar o e-mail (letras minúsculas e sem espaços).
# 2. Verificar se o e-mail está na lista de admins.
# 3. Se estiver, exibir: "Acesso liberado! Bem-vindo ao painel de controle".
# 4. Caso contrário, exibir: "Acesso negado. Você não tem permissões de administrador".

admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]

email = input("Digite seu e-mail:")
email = email.strip().lower()

if email in admins:
    print("Acesso liberado! Bem-vindo ao painel de controle")
else:
    print("Acesso negado. Você não tem permissões de administrador")


# Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas) Um e-commerce
# aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da
# compra e aplique a seguinte lógica:
# ● Compras a partir de R$ 500,00: 15% de desconto.
# ● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
# ● Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do
# desconto e o valor final a pagar, formatados em R$.

valor_carrinho = 400

if valor_carrinho < 200:
    perc_desconto = 0
elif valor_carrinho < 500:
    perc_desconto = 0.1
else:
    perc_desconto = 0.15

desconto = valor_carrinho * perc_desconto
valor_final = valor_carrinho - desconto
print(f"Desconto: R${desconto:,.2f}. Valor Total: R${valor_final:,.2f}")


# Exercício 4: Análise de Metas Combinadas (Setor Comercial) Uma empresa paga bônus
# se a meta individual do vendedor E a meta da loja forem batidas.
# 1. Peça as vendas do vendedor e a meta individual dele.
# 2. Peça as vendas totais da loja e a meta da loja.
# 3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre
# as vendas do vendedor.
# 4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês é de:
# R$[valor]".

meta = 1000
vendas_vendedor = 1000

meta_loja = 5000
vendas_loja = 4000

if vendas_loja >= meta_loja and vendas_vendedor >= meta:
    bonus = 0.2 * vendas_vendedor
else:
    bonus = 0

print(f"Seu bônus este mês é de: R${bonus:.2f}")


# Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience) Crie um
# sistema que ajude a filtrar para qual departamento uma reclamação deve ir. O usuário deve
# digitar o assunto do e-mail.
# ● Se no assunto aparecer a palavra "pagamento" ou "boleto", exiba: "Encaminhado
# para o Financeiro".
# ● Se no assunto aparecer a palavra "entrega" ou "atraso", exiba: "Encaminhado para a
# Logística".

# ● Caso não seja nenhum desses, exiba: "Encaminhado para o Suporte Geral". Dica:

assunto = "Problemas com acesso"

assunto = assunto.lower()

if "pagamento" in assunto or "boleto" in assunto:
    print("Encaminhado para o Financeiro")
elif "entrega" in assunto or "atraso" in assunto:
    print("Encaminhado para a Logística")
else:
    print("Encaminhado para o Suporte Geral")
