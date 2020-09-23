#Funcao para descobrir qual a operacao:
def checaOperador(elemento):
    if(elemento == "+"):
        print("Soma")
        return True
    elif(elemento == "-"):
        print("Subtracao")
        return True
    elif(elemento == "*"):
        print("Multiplicacao")
        return True
    elif(elemento == "/"):
        print("Divisao")
        return True
    else:
        return False
        
#Função para concluir a operação atual
def operacao(operacao,elementosAnt,elementosPost):
    resultado = 0
    if(operacao == "+"):
        resultado = elementosAnt + elementosPost
    elif(operacao == "-"):
        resultado = elementosAnt - elementosPost
    elif(operacao == "*"):
        resultado = elementosAnt * elementosPost
    elif(operacao == "/"):
        resultado = elementosAnt / elementosPost
    return resultado        

# Calculadora Simples, que ela mesma calcula
conta = input("Digite uma expressao:")
auxAnte = []
auxPost = []

#Passa de string para lista
conta = list(conta)

for i in range(len(conta)):
    print("Elemento na posicao {}, valor: {}".format(i,conta[i]))
    #Checa se o elemento atual é um operador
    if(checaOperador(conta[i])):
        #Vai pegar os elementos anteriores ao operador e guardar em uma lista
        print("Elementos anteriores ao operador:")
        for a in range(i):
            print("",a)
            auxAnte.append(conta[a])
        #Vai pegar os elementos posteriores ao operador e guardar em uma lista
        print("Elementos posteriores ao operador:")
        for p in range(i+1,len(conta)):
            print("",p)
            auxPost.append(conta[p])
        print("Resultado:")
        print(operacao(conta[i],auxAnte,auxPost))
        
    else:
        print("Não é um operador")


print("-------------")
print("AuxAnte:",auxAnte)
print("Tipo AuxAnte:",type(auxAnte))
print("-------------")
print("AuxPost:",auxPost)
print("Tipo AuxPost:",type(auxPost))
print("--------------------")
print("Valor",conta)
type(conta)    
