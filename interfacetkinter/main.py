import tkinter as tk


#abaixo, criamos a classe #calculadora jenny#
class Calculadorajenny:

    # No bloco abaixo, temos:
    # Linha1. Iniciamos nossa classe (usando o init) e atribuimos a janela principal "master" como argumento
    # Linha2. Atribui a master à variavel que chamei de "self.janela" / O self permite o acesso à "master" em toda a classe
    # Linha3. Define o título da "master" ou seja, nossa janela principal

    def __init__(self, master):
        self.janela = master
        master.title("s2 Olá s2")

        # Aqui configuramos o "Entry" widget para exibir o resultado

        # Na primeira linha criamos a variável "resultado_texto"
        # "tk.StringVar()" é uma função do Tk que cria uma variável de string vinculada
        # Ou seja, uma variável da qual o valor é sincronizado com o valor de outro objeto
        # Esse objeto pode ser uma caixa de texto por exemplo
        # Assim, toda que o valor de uma dessas variaveis muda, o da outra também.
        # Na segunda linha  criamos um objeto "Entry" que é uma caixa de texto padrão
        # Colocamos na variável "Self.Resultado"
        # usamos o "textvariable" como já foi dito pra vincular com a variável "resultado_texto"
        # Temos então 1 varável para o objeto em si e outra para o resultado
        # ambas estão vinculadas
        # a ultima linha irá usar o método "grid" para configurar a posição do objeto Entry.
        # o valor zero corresponde a primeira linha e primeira coluna (onde está o objeto)
        # terá a largura de 4 colunas (columspan=4)
        # e 5 pixels de espaço interno e externo em todas as direções

        self.resultado_texto = tk.StringVar()
        self.resultado = tk.Entry(master, textvariable=self.resultado_texto)
        self.resultado.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipadx=5, ipady=5)


        # Botões numéricos

        #Abaixo atribuimos valores ao objeto Tk.Button que chamamos de "criar_botao"
        #mais pra frente veremos uma função onde desenhamos os atributos desse objeto
        #entre "" temos o texto que vai aparecer no botão
        # os dois ultimos numeros de cada linha indicam a posição
        # "7" por exemplo está na segunda linha (numero 1)
        # e na primeira coluna (numero 0)
        #tudo isso foi definido abaixo na função que criou o objeto "criar_botão"
        #lembrando que em vários momentos em programação temos:
        #Contagens de indices, linhas e colunas que começam do "0"

        self.criar_botao("7", 1, 0)
        self.criar_botao("8", 1, 1)
        self.criar_botao("9", 1, 2)
        self.criar_botao("4", 2, 0)
        self.criar_botao("5", 2, 1)
        self.criar_botao("6", 2, 2)
        self.criar_botao("1", 3, 0)
        self.criar_botao("2", 3, 1)
        self.criar_botao("3", 3, 2)
        self.criar_botao("0", 4, 0)


        # Botões de operações
        # aqui seguimos criando mais botões
        # usamos as operações pra identificar
        # mas a lógica é a mesma

        self.criar_botao("+", 1, 3)
        self.criar_botao("-", 2, 3)
        self.criar_botao("*", 3, 3)
        self.criar_botao("/", 4, 3)
        self.criar_botao("=", 4, 2)
        self.criar_botao("C", 4, 1)

        # cor da janela
        root.configure(background='pink')


        #Abaixo é que de fato começamos à implementar a parte funcional da nossa calculadora.

        #Primeiro usamos o "def" que é uma palavra reservada do Python para definir uma função
        #Nela, vamos definir a função "criar_botao" que inventamos e que trabalhamos acima
        #acima, inserimos a posição desse elemento através dos valores de seus atributos
        #abaixo, vamos definir seus atributos, vamos criar o elemento com "tk.Button"
        #vamos dizer que está na master "self.janela"
        # A função "self.clique_botao(text)" é chamada quando o botão é clicado
        # Ela faz uma ação baseada no textot do botão
        # No nosso caso ela vai usar o texto do botão nas operações (o que é definido na função psoterior)
        # na função dizemos por exemplo que row recebe row e column recebe column pois para criar o objeto
        # precisamos passar valores à seus atributos mesmo na função
        # para os atributos padx e pady que servirão para todos os botões já atribuimos valor na propria função
        # command = lambda (Lembda é um elemento anônimo e palavra reservada do Python) faz parte
        # do atributo "command" que é o comando que vai chamar o "self.button_click(text)
        # temos então a criação de um objeto, usando atributos que vão definir seu texto, onde estará, posição e ação


    def criar_botao(self, text, row, column):
        botao = tk.Button(self.janela, text=text, command=lambda: self.clique_botao(text))
        botao.grid(row=row, column=column, padx=5, pady=5)


        # Abaixo temos a parte que mais gosto!
        # a função abaixo tem os argumentos self e text
        # se text for igual à "=" então ele deve tentar o que está dentro do If
        # no iff cria-se a variável resultado que armazena o resultado de uma operação
        # essa operação só pode acontecer através da função eval
        # a função eval pega o valor de strings (que indicamos e transforma na operação)


    def clique_botao (self, text):
        if text == "=":
            try:
                resultado = eval(self.resultado_texto.get())
                self.resultado_texto.set(resultado)
            except:
                self.resultado_texto.set("Error")
        elif text == "C":
            self.resultado_texto.set("")
        else:
            self.resultado_texto.set(self.resultado_texto.get() + text)

root = tk.Tk()
calculator = Calculadorajenny(root)
root.mainloop()
