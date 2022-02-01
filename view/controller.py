from tkinter import *
from tkinter import ttk
from src.consulta import ConsultaCep

class Interface:

    def __init__(self,index):
        cor1 = '#e60707' #vermelho
        cor2 = '#1851ba' #azul claro
        cor3 = '#01040d' #preto
        cor4 = '#d8eded' #cinza claro
        cor5 = '#09e820' #verde claro
        cor6 = '#f5ea25'  # amarelo

        fontePadrao = 'Ivy 10 bold'
        fonteHead = 'Ivy 11'
        fonteMenor = 'Ivy 7 bold'
        textoTeste = '===================================\n'\
                     '\n'\
                     'CONSULTE SEU CEP\n' \
                     '\n'\
                     'Inserir somente números (sem traço)\n' \
                     '\n'\
                     '===================================\n'

        index.title("Consulta CEP")
        index.geometry("400x400")
        index.configure(background=cor2)
        index.resizable(width=False, height=False)
        index.attributes("-alpha",0.8)

        #Frames
        self.frame1 = Frame(index, width=395, height=105, bg=cor2, relief=FLAT)
        self.frame1.pack()
        #self.frame1.grid(row=0, column=0)

        self.frame2 = Frame(index, width=360, height=210, bg=cor3, relief=FLAT)
        self.frame2.pack()
        #self.frame2.grid(row=1,column=0)

        self.frame3 = Frame(index, width=395, height=105, bg=cor2, relief=FLAT)
        self.frame3.pack()
        #self.frame3.grid(row=2, column=0)

        #Labels

        self.labelConsulta = Label(self.frame1, text='Insira o CEP abaixo e clique em CONSULTAR', width=43,
                            height=2, relief=FLAT, font=(fonteHead), bg=cor2, fg=cor4)
        self.labelConsulta.place(x=0,y=0)

        self.labelView = Label(self.frame2, text=textoTeste, width=40,height=12,relief=FLAT,
                          font=(fontePadrao), bg=cor3, fg=cor6, justify=CENTER)
        self.labelView.place(x=0, y=0)

        # Campos
        def limite_tamanho(p): #método para limitação a quantidade de digitos no Entry
            if len(p) > 8:
                return False
            return True

        vcmd = self.frame1.register(func=limite_tamanho)
        #limitando digitos, validate e validatecommand e o método

        self.campoConsulta = Entry(self.frame1, width=15, font=(fontePadrao), border=1, validate='key',
                                   validatecommand=(vcmd,'%P'))
        self.campoConsulta.focus_force()
        self.campoConsulta.place(x=140, y=41)


        # Botoes

        buttonConsulta = Button(self.frame1, text='CONSULTAR', width=8, height=1, font=(fonteMenor),
                                relief=RAISED, overrelief=RIDGE, fg=cor3, bg=cor5,
                                command=self.getCampoCep)
        buttonConsulta.place(x=55,y=40)

    def getCampoCep(self):
        codigo = self.campoConsulta.get()
        retorno = ConsultaCep()  # objeto de tratamento do cep no API
        endereco = retorno.tratar_cep(codigo)
        justify = 'left'
        fonteMenor = 'Ivy 9 bold'


        #Envio do resultado da pesquisa
        self.labelView['text'] = endereco
        self.labelView['justify'] = justify
        self.labelView['font'] = fonteMenor




