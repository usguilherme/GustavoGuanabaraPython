# Este programa lê nome e preço de produtos, calcula o total da compra,
# conta produtos caros e encontra o produto mais barato.

total_gasto = 0
cont_produtos_caros = 0
menor_preco = 0
nome_produto_barato = ''
cont_produtos = 0

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    total_gasto += preco
    cont_produtos += 1

    if preco > 1000:
        cont_produtos_caros += 1

    if cont_produtos == 1 or preco < menor_preco:
        menor_preco = preco
        nome_produto_barato = nome

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('=' * 8, ' FIM DO PROGRAMA ', '=' * 8)
print(f'O total da compra foi R${total_gasto:.2f}.')
print(f'Temos {cont_produtos_caros} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {nome_produto_barato} que custa R${menor_preco:.2f}.')