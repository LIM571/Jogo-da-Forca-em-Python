

def Nomes():
    print("===========================")
    print(" --------Feito por:--------")
    print("---Gabriel de Lima Dutra---")
    print("===========================")
def desenharForca(chancesRestantes):
    if chancesRestantes == 7:
        print()
        print("| - - - -")
        print("|       | ")
        print("|        ")
        print("|      ")
        print("|      ")
        print("        ")

    elif chancesRestantes == 6:
        print()
        print("| - - - -")
        print("|       | ")
        print("|       O ")
        print("|     ")
        print("|       ")
        print("       ")
      


    elif chancesRestantes == 5:
        print()
        print("| - - - -")
        print("|       | ")
        print("|       O ")
        print("|       |  ")
        print("|       ")
        print("        ")
       


    elif chancesRestantes == 4:
        print()
        print("| - - - -")
        print("|       | ")
        print("|       O ")
        print("|     / |  ")
        print("|       ")
        print("        ")
       


    elif chancesRestantes == 3:
        print()
        print("| - - - -")
        print("|       | ")
        print("|       O ")
        print("|     / | \ ")
        print("|       ")
        print("        ")
        


    elif chancesRestantes == 2:
        print()
        print("| - - - -")
        print("|       | ")
        print("|       O ")
        print("|     / | \ ")
        print("|       |")
        print("        ")
       


    elif chancesRestantes == 1:
        print()
        print("| - - - -")
        print("|       | ")
        print("|       O ")
        print("|     / | \ ")
        print("|       |")
        print("       /  ")
       

    elif chancesRestantes == 0:
        print()
        print("| - - - -")
        print("|       | ")
        print("|       O ")
        print("|     / | \ ")
        print("|       |")
        print("       / \ ")

def apagarPalavraNoTerminal():
  print("\n" * 130)  

def querContinuar(nomePessoa):
  resposta = input("Quer continuar novamente? (s/n)")
  if resposta == "s":
    jogo(nomePessoa)
  else:
    print("Tchau")
    
def jogo(nomePessoa):
  palavra = input("Digite palavra: ")
  apagarPalavraNoTerminal()
  
  qtdLetras = len(palavra)
  letrasRestantes = qtdLetras
  ver = ["_"] * qtdLetras #contar o numero de letras da palavra,e fazer a coversão de cada letra para um simbulo
  
  chances = 7
  
  while chances > 0 and letrasRestantes != 0:
    
    print("Chances disponíveis:", chances)
    print("Letras restantes:", letrasRestantes)
    
    letra = ""
    while len(letra) != 1:
      letra = input("Letra: ")
    
    letras_tirar = 0

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                ver[i] = letra
                letras_tirar += 1
    
    else:
      chances -= 1

    letrasRestantes -= letras_tirar
    
    desenharForca(chances)
    
    print(" " .join(ver))#comando para juntar
    
    if chances == 0:
      print("Você perdeu")
      querContinuar(nomePessoa)
        
    elif letrasRestantes == 0:
      print("{} ganhou".format(nomePessoa))
      querContinuar(nomePessoa)
      
#COMEÇO
print(Nomes())
nome = input("Digite seu nome: ")
jogo(nome)
