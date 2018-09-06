

clientes = {"Jose": [62981823545, 981234567], "Maria": 12, "Marcos": "da silva"}

print(clientes["Jose"])
print(clientes["Maria"])
print(clientes["Marcos"])

req = {"requisicao": 12345678,"pessoas": [{"nome": "Jose da Silva", "telefone": "3232123"},{"nome": "Maria da Silva", "telefone": "3232123"},{"nome": "Carlos", "telefone": "3232123"}]}

print(req["requisicao"])

for p in req["pessoas"]:
    print(p["nome"])



pessoas = [{"nome": "Maria","sexo": "F"}, {"nome": "Jose","sexo": "M"}, {"nome": "Carlos","sexo": "M"}, {"nome": "Janaina","sexo": "F"}]

for p in pessoas:
    final = "o" if p["sexo"] == "M" else "a"
    print("Prezad{} {}".format(final, p["nome"]))    

for p in pessoas:
    print("Prezad{} {}".format("o" if p["sexo"] == "M" else "a", p["nome"]))    

    