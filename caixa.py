# Nome: Edson Cuna
# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Projeto Integrador Extensionista – ADS 1
# Semestre Letivo: 1º Termo – 2025

while True:
    print("\n====Bem vindo ao Supermercado Sonda ====")
    total = 0
    produto = 1

    # Recebendo os valores dos produtos
    while True:
        preco = float(input(f"Produto {produto}: R$ "))
        if preco == 0:
            break
        total += preco
        produto += 1

    print(f"\nTotal: R$ {total:.2f}")

    # Recebendo o valor pago e calculando o troco
    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total

    print(f"Troco: R$ {troco:.2f}")

    # Perguntar se deseja continuar
    continuar = input("\nDeseja realizar uma nova compra? (sim/não): ").lower()
    if continuar != 'sim':
        print("Encerrando o sistema. Obrigado por confiar nos nossos produtos!")
        break
