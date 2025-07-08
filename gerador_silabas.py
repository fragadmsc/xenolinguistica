import random

#assobios
letras = {
    'A' : ["A", "B", "C", "D", "E", "F"],
    '1' : ["a", "b", "c", "d", "e", "f", "g", "h"],
    '2' : ["a", "e", "h"],
    '3' : ["b", "c", "d", "f", "g"],
}

silabas = ["A",
           "A2",
           "3A",
           "3A2",
           "31A",
           "31A2",
           "311A2"]

if __name__ == "__main__":
    
    tipo = int(input("digite o tipo da silaba (de 1 a 7): ").strip())
    qnt = int(input("digite a quantidade de silabas: ").strip())

    for i in range(qnt):
        silaba = silabas[tipo-1]
        for letra in silaba:
            print(random.choice(letras[letra]), end="")
        print()
