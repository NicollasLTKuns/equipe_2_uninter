#//////////////////////////////////////////////////
#/////////       Código Pizzaria          /////////
#//////////////////////////////////////////////////

total = 0  # variável que guarda o total do pedido
pizzas_total = 0  # contador de pizzas no pedido
refrigerantes_total = 0  # contador de refrigerantes no pedido
distancia_entrega = 0  # distância de entrega (será perguntada no final)

while True:  # loop infinito (fica repetindo até usar break)

    print("\n--- Pizzaria LEN ---")  # mostra o título
    print("1 - Doce")  # opção 1
    print("2 - Salgado") # opção 2
    print("3 - Refrigerante")  # opção 3
    print("0 - Fechar pedido")  # opção para sair

    opcao = input("Escolha o tipo: ")  # usuário digita a opção

    if opcao == "0":  # se escolher 0
        break  # sai do loop (encerra o programa)

    if opcao == "1":  # se escolher doce
        sabor = "Doce"  # define sabor como doce

    elif opcao == "2":  # se escolher salgado
        sabor = "Salgado"  # define sabor como salgado

    elif opcao == "3":  # se escolher refrigerante
        quantidade = int(input("Quantos refrigerantes deseja? "))  # pede quantidade
        if quantidade <= 0 or quantidade > 2:  # se quantidade inválida
            print("Quantidade inválida! Máximo 2 refrigerantes por pedido.")  # mostra erro
            continue  # volta pro início do loop
        if refrigerantes_total + quantidade > 2:  # verifica se não ultrapassa o limite
            print(f"Limite excedido! Você já pediu {refrigerantes_total} refrigerante(s). Máximo 2 no total.")
            continue
        preco = 15 * quantidade  # preço do refrigerante (R$15 por unidade)
        subtotal = preco  # calcula subtotal (sem frete ainda)
        total = total + subtotal  # soma no total geral
        refrigerantes_total += quantidade  # adiciona ao contador de refrigerantes
        print(f"\nVocê pediu {quantidade} refrigerante(s)")  # mostra o pedido
        print(f"Subtotal: R${subtotal:.2f}")  # mostra subtotal
        print(f"Total até agora: R${total:.2f}")  # mostra total acumulado
        continue  # volta pro início do loop para novo pedido

    else:  # se digitar algo diferente
        print("Opção inválida!")  # mostra erro
        continue  # volta pro início do loop

    print("\nTamanhos:")  # título da escolha de tamanho
    print("1 - Pequeno")  # opção pequeno
    print("2 - Médio")  # opção médio
    print("3 - Grande")  # opção grande

    tamanho_opcao = input("Escolha o tamanho: ")  # usuário escolhe tamanho

    if tamanho_opcao == "1":  # se escolher pequeno
        tamanho = "P"  # define tamanho P

        if sabor == "Doce":  # se for doce
            preco = 34.00  # preço do doce pequeno
        else:  # se for salgado
            preco = 30.00  # preço do salgado pequeno

    elif tamanho_opcao == "2":  # se escolher médio
        tamanho = "M"  # define tamanho M

        if sabor == "Doce":  # se for doce
            preco = 48.00  # preço do doce médio
        else:  # se for salgado
            preco = 45.00  # preço do salgado médio

    elif tamanho_opcao == "3":  # se escolher grande
        tamanho = "G"  # define tamanho G

        if sabor == "Doce":  # se for doce
            preco = 66.00  # preço do doce grande
        else:  # se for salgado
            preco = 60.00  # preço do salgado grande

    else:  # se digitar tamanho inválido
        print("Tamanho inválido!")  # mostra erro
        continue  # volta pro início do loop

    quantidade = int(input("Quantas Pizzas deseja? "))
    if quantidade <= 0 or quantidade > 5:
        print("Quantidade inválida! Máximo 5 pizzas por pedido.")
        continue
    if pizzas_total + quantidade > 5:
        print(f"Limite excedido! Você já pediu {pizzas_total} pizza(s). Máximo 5 no total.")
        continue

    subtotal = preco * quantidade  # calcula o valor desse pedido (sem frete ainda)
    total = total + subtotal  # soma no total geral
    pizzas_total += quantidade  # adiciona ao contador de pizzas

    print(f"\nVocê pediu {quantidade} pizza(s) {sabor} tamanho {tamanho}")  # mostra o pedido
    print(f"Subtotal: R${subtotal:.2f}")  # mostra subtotal
    print(f"Total até agora: R${total:.2f}")  # mostra total acumulado

print("\n--- PEDIDO FINALIZADO ---")  # mensagem final
print(f"Total de pizzas: {pizzas_total}")  # mostra total de pizzas
print(f"Total de refrigerantes: {refrigerantes_total}")  # mostra total de refrigerantes

# Cálculo do frete por distância
try:
    distancia_entrega = float(input("Digite a distância da entrega em km (ex: 3.5): "))
    if distancia_entrega < 0:
        raise ValueError
except ValueError:
    print("Distância inválida. Usando 0 km para o cálculo do frete.")
    distancia_entrega = 0.0

frete = distancia_entrega * 5.0  # R$5 por km (ajuste conforme a política da pizzaria)
total_com_frete = total + frete

print(f"Frete (R$5 por km): R${frete:.2f}")
print(f"Total a pagar (itens + frete): R${total_com_frete:.2f}") #.2f quer dizer que vai mostrar 2 casas decimais

input("Pressione ENTER para sair...")  # pausa o programa


#Comentando apenas para deixar registrado que consegui clonar o github.
# Segundo commit para ver se vai dar certo mesmo, e para deixar registrado que consegui fazer o commit.