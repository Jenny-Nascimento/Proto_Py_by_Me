import tkinter as tk

# Cria a janela principal

root = tk.Tk()
root.title("Calculadora de Média Bimestral:")
root.configure(bg='white', padx='15', pady='15')




def calc_valores():

    # Obtém os valores dos 12 widgets entry

    nota1ed = entry1ed.get()
    nota2ed = entry2ed.get()
    nota3ed = entry3ed.get()
    nota4ed = entry4ed.get()
    nota5ed = entry5ed.get()


    nota1fc = entry1fc.get()
    nota2fc = entry2fc.get()
    nota3fc = entry3fc.get()
    nota4fc = entry4fc.get()
    nota5fc = entry5fc.get()

    nota1pt = entry1pt.get()
    nota2pt = entry2pt.get()
    nota3pt = entry3pt.get()
    nota4pt = entry4pt.get()
    nota5pt = entry5fc.get()



    # Converte os valores para números float e calcula a soma
    try:
        nota1ed = float(nota1ed)
        nota2ed = float(nota2ed)
        nota3ed = float(nota3ed)
        nota4ed = float(nota4ed)
        nota5ed = float(nota5ed)

        nota1fc = float(nota1fc)
        nota2fc = float(nota2fc)
        nota3fc = float(nota3fc)
        nota4fc = float(nota4fc)
        nota5fc = float(nota5fc)

        nota1pt = float(nota1pt)
        nota2pt = float(nota2pt)
        nota3pt = float(nota3pt)
        nota4pt = float(nota4pt)
        nota5pt = float(nota5pt)

        result1 = (((nota1ed + nota2ed + nota3ed + nota4ed) / 4) * 0.4) + (nota5ed * 0.6)
        result2 = (((nota1fc + nota2fc + nota3fc + nota4fc) / 4) * 0.4) + (nota5fc * 0.6)
        result3 = (((nota1pt + nota2pt + nota3pt + nota4pt) / 4) * 0.4) + (nota5pt * 0.6)

    except ValueError:
        result1 = "VALOR INVÁLIDO!!"
        result2 = "VALOR INVÁLIDO!!"
        result3 = "VALOR INVÁLIDO!!"

    # Define o texto das duas labels com os valores obtidos
    label_soma1.config(text="A Nota Final de Estrutura de dados é: {}".format(result1))
    label_soma2.config(text="A Nota Final de Fundamentos para Certificação Técnica é : {}".format(result2))
    label_soma3.config(text="A Nota Final de Pesquisa, Ordenação e Técnicas de Armazenamento : {}".format(result3))


# Cria os  widgets  para pegar os valores

label_soma1 = tk.Label(root, foreground="magenta", background="white")
label_soma2 = tk.Label(root, foreground="magenta", background="white")
label_soma3 = tk.Label(root, foreground="magenta", background="white")


a1_label1 = tk.Label(root, text="A1", background="white")
a2_label1 = tk.Label(root, text="A2", background="white")
a3_label1 = tk.Label(root, text="A3", background="white")
a4_label1 = tk.Label(root, text="A4", background="white")
a5_label1 = tk.Label(root, text="A5", background="white")


a1_label2 = tk.Label(root, text="A1", background="white")
a2_label2 = tk.Label(root, text="A2", background="white")
a3_label2 = tk.Label(root, text="A3", background="white")
a4_label2 = tk.Label(root, text="A4", background="white")
a5_label2 = tk.Label(root, text="A5", background="white")

a1_label3 = tk.Label(root, text="A1", background="white")
a2_label3 = tk.Label(root, text="A2", background="white")
a3_label3 = tk.Label(root, text="A3", background="white")
a4_label3 = tk.Label(root, text="A4", background="white")
a5_label3 = tk.Label(root, text="A5", background="white")


entry1ed = tk.Entry(root)
entry2ed = tk.Entry(root)
entry3ed = tk.Entry(root)
entry4ed = tk.Entry(root)
entry5ed = tk.Entry(root)

entry1fc = tk.Entry(root)
entry2fc = tk.Entry(root)
entry3fc = tk.Entry(root)
entry4fc = tk.Entry(root)
entry5fc = tk.Entry(root)


entry1pt = tk.Entry(root)
entry2pt = tk.Entry(root)
entry3pt = tk.Entry(root)
entry4pt = tk.Entry(root)
entry5pt = tk.Entry(root)


# Cria um botão para imprimir os valores
botao_calc = tk.Button(root, text="Imprimir valores", command=calc_valores, background="pink", foreground="black")

# Cria as labels para exibir os valores
label_soma1 = tk.Label(root, foreground="violet red", background="white")
label_soma2 = tk.Label(root, foreground="violet red", background="white")
label_soma3 = tk.Label(root, foreground="violet red", background="white")


# Posicionando os widgets na janela

tk.Label(root, text="", background="white").grid(row=0)
tk.Label(root, text="Entre com as notas de cada atividade:", background="white", font=("Calibri", 16)).grid(row=1, columnspan=5)
tk.Label(root, text="", background="white").grid(row=2)

label_soma1.grid(row=3, column=0, columnspan=5, sticky="w")

tk.Label(root, text="Notas de Estrutura de dados:", background="white", foreground="deep pink").grid(row=4, columnspan=5, sticky="w")
a1_label1.grid(row=5, column=0, sticky="w")
a2_label1.grid(row=5, column=1, sticky="w")
a3_label1.grid(row=5, column=2, sticky="w")
a4_label1.grid(row=5, column=3, sticky="w")
a5_label1.grid(row=5, column=4, sticky="w")


entry1ed.grid(row=6, column=0, sticky="w")
entry2ed.grid(row=6, column=1, sticky="w")
entry3ed.grid(row=6, column=2, sticky="w")
entry4ed.grid(row=6, column=3, sticky="w")
entry5ed.grid(row=6, column=4, sticky="w")
tk.Label(root, text="", background="white").grid(row=7)



label_soma2.grid(row=8, column=0, columnspan=5, sticky="w")

tk.Label(root, text="Notas de Fundamentos Para Certificação Técnica:", background="white", foreground="deep pink").grid(row=9, columnspan=5, sticky="w")
a1_label2.grid(row=10, column=0, sticky="w")
a2_label2.grid(row=10, column=1, sticky="w")
a3_label2.grid(row=10, column=2, sticky="w")
a4_label2.grid(row=10, column=3, sticky="w")
a5_label2.grid(row=10, column=4, sticky="w")


entry1fc.grid(row=11, column=0, sticky="w")
entry2fc.grid(row=11, column=1, sticky="w")
entry3fc.grid(row=11, column=2, sticky="w")
entry4fc.grid(row=11, column=3, sticky="w")
entry5fc.grid(row=11, column=4, sticky="w")
tk.Label(root, text="", background="white").grid(row=12)


label_soma3.grid(row=13, column=0, columnspan=5, sticky="w")

tk.Label(root, text="Notas de Pesquisa, Ordenação e Técnicas de Armazenamento: ", background="white", foreground="deep pink").grid(row=14, columnspan=5, sticky="w")
a1_label3.grid(row=15, column=0, sticky="w")
a2_label3.grid(row=15, column=1, sticky="w")
a3_label3.grid(row=15, column=2, sticky="w")
a4_label3.grid(row=15, column=3, sticky="w")
a5_label3.grid(row=15, column=4, sticky="w")


entry1pt.grid(row=16, column=0, sticky="w")
entry2pt.grid(row=16, column=1, sticky="w")
entry3pt.grid(row=16, column=2, sticky="w")
entry4pt.grid(row=16, column=3, sticky="w")
entry5pt.grid(row=16, column=4, sticky="w")
tk.Label(root, text="", background="white").grid(row=17)


tk.Label(root, text="", background="white").grid(row=18)

tk.Label(root, text="", background="white").grid(row=19)

botao_calc.grid(row=20, column=0, sticky="w")

tk.Label(root, text="", background="white").grid(row=21)


label_soma1.grid(row=22, column=0, columnspan=5, sticky="w")
tk.Label(root, text="", background="white").grid(row=19)
label_soma2.grid(row=23, column=0, columnspan=5, sticky="w")
tk.Label(root, text="", background="white").grid(row=24)
label_soma3.grid(row=24, column=0, columnspan=5, sticky="w")
tk.Label(root, text="", background="white").grid(row=25)

tk.Label(root, text="", background="white").grid(row=27)

tk.Label(root, text="Caso o resultado apresente *VALOR INVÁLIDO*, observe se não está digitando: \
Letras, caracteres especiais, ou se existem campos vazios", background="white", wraplength=700).grid(row=28, columnspan=5)

tk.Label(root, text="", background="white").grid(row=29)


# Inicia o loop principal da interface gráfica
root.mainloop()