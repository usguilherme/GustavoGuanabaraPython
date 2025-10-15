# Pede ao usuário para inserir o preço normal do produto.
preco = float(input('Preço normal do produto: R$'))

print('''
FORMAS DE PAGAMENTO:
[ 1 ] à vista (dinheiro/cheque): 10% de desconto
[ 2 ] à vista (cartão): 5% de desconto
[ 3 ] em até 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros
''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.20
else:
    print('Opção inválida de pagamento. Tente novamente.')
    valor_final = preco

print(f'O valor a ser pago é de R${valor_final:.2f}')