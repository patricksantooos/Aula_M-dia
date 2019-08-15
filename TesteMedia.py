def calculaMedia():
  lista = []

  for i  in range(3):
    nota = float(input("Digite  nota {}: ".format(i+1)))
    lista.append(nota)

    media = sum(lista)/3


