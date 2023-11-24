#minha versão
pc = {"pedra", "papel", "tesoura"}
for _ in range(2): pc.pop()
pctry = ''.join(pc)

print(pctry)

player = input("Escolha pedra, papel ou tesoura ").lower()

if player == pctry:
    print(f"O computador escolheu {pctry} e vocês empataram!")
elif pctry == "pedra" and player == "tesoura" or pctry == "papel" and player == "pedra" or pctry == "tesoura" and player == "papel":
    print(f"O computador escolheu {pctry} e venceu!")
elif pctry == "pedra" and player == "papel" or pctry == "papel" and player == "tesoura" or pctry == "tesoura" and player == "pedra":
    print(f"O computador escolheu {pctry}, então você venceu!")
else:
    print("Por favor, digite apenas pedra, papel ou tesoura")

#versão da moça



