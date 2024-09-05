def calcular_media(notas):

    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def verificar_situacao(media):

    if media == 10:
        print("Parabéns, Sua média é 10!")
    elif media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")

def main():
    notas = []
    
    while True:
        valor = input("Digite uma nota (ou 'sair' para encerrar): ")
        
        if valor.lower() == 'sair':
            break
        
        if valor.replace('.', '', 1).isdigit() or (valor.startswith('-') and valor[1:].replace('.', '', 1).isdigit()):
            nota = float(valor)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota deve estar entre 0 e 10. Tente novamente.")
        else:
            print("Por favor, digite um número válido para a nota.")
    
    if notas:
        media = calcular_media(notas)
        print(f"\n Sua Média é: {media:.2f}")
        verificar_situacao(media)
    else:
        print("Nenhuma nota foi digitada.")

if __name__ == "__main__":
    main()


