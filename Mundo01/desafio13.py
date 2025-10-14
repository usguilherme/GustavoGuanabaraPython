# Programa que lê o preço de um produto e mostra o novo preço com 15% de desconto
preco = float(input("Digite o preço do produto: R$ "))
novo_preco = preco * 0.85
print(f"Preço com 15% de desconto: R$ {novo_preco:.2f}")
