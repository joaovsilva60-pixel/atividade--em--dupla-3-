import os
os.system("cls")

print("=== CARDÁPIO E SISTEMA DO RESTAURANTE ===")

cardapio = {
    1: ("Picanha", 25.00),
    2: ("Lasanha", 20.00),
    3: ("Strogonoff", 18.00),
    4: ("Bife Acebolado", 15.00),
    5: ("Pão com ovo", 5.00)
}

pedido = []

print("=" * 40)
print("       CARDÁPIO DO RESTAURANTE")
print("=" * 40)

# Exibir cardápio
for codigo, (nome, valor) in cardapio.items():
    print(f"{codigo} - {nome:<20} R$ {valor:.2f}")

print("=" * 40)

# Registrar os pratos escolhidos
while True:
    codigo = int(input("\nDigite o código do prato: "))

    if codigo in cardapio:
        nome, valor = cardapio[codigo]
        pedido.append((nome, valor))
        print(f"{nome} adicionado ao pedido!")
    else:
        print("Código inválido! Escolha novamente.")
        continue

    outro = input("\nDeseja escolher outro prato? (S/N): ").strip().upper()

    if outro != "S":
        break

# Exibir resumo do pedido
print("\n" + "=" * 40)
print("          RESUMO DO PEDIDO")
print("=" * 40)

total = 0

for nome, valor in pedido:
    print(f"{nome:<25} R$ {valor:.2f}")
    total += valor

# Calcular taxa do garçom
taxa_garcom = total * 0.10
total_final = total + taxa_garcom

print("-" * 40)
print(f"{'SUBTOTAL:':<25} R$ {total:.2f}")
print(f"{'TAXA DO GARÇOM (10%):':<25} R$ {taxa_garcom:.2f}")
print("-" * 40)
print(f"{'TOTAL FINAL:':<25} R$ {total_final:.2f}")
print("=" * 40)

print("\nObrigado pela preferência!")
