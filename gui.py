import customtkinter as ctk
import base64
import tkinter as tk
from b64imagens import *



class Formulario_Pessoa_Fisica:
    def __init__(self):
        self.formulario_pf = ctk.CTkToplevel()
        self.formulario_pf.geometry('700x720+650+100')
        self.formulario_pf.title('BRASBANK - Janela de Formulário para Cadastro!')
        self.formulario_pf.resizable(False, False)
        self.formulario_widgets()
        self.formulario_pf.grab_set()
        self.formulario_pf.focus_force()
        self.formulario_pf.mainloop()


    def formulario_widgets(self):
        self.nome_entry = ctk.CTkEntry(master=self.formulario_pf)
        self.cpf = ctk.CTkEntry(master=self.formulario_pf)
        self.data_nascimentos = ctk.CTkEntry(master=self.formulario_pf)
        self.endereço = ctk.CTkEntry(master=self.formulario_pf)








class Cadastro_de_Conta:
    def cadastrar(self):
        self.janela_cadastro = ctk.CTkToplevel()
        self.janela_cadastro.title('BRASBANK - Bem vindo ao sistema de cadastro! V: 1.0 Made By: FelRFDev!')
        self.janela_cadastro.geometry('700x720+650+100')
        self.janela_cadastro.resizable(False, False)
        self.widgets_de_cadastro()
        self.janela_cadastro.grab_set()
        self.janela_cadastro.focus_force()
        self.janela_cadastro.mainloop()

    def selecionar_classe_pessoa(self, escolha):
        self.escolha = escolha


    def realizar_cadastro(self):
        if self.escolha == 'Pessoa Física':
            Formulario_Pessoa_Fisica()

        
    def widgets_de_cadastro(self):
        self.moedas_imagem = tk.PhotoImage(master=self.janela_cadastro, data=moedas)
        self.moedas_painel = tk.Canvas(master=self.janela_cadastro, width=720, height=720)
        self.moedas_painel.create_image((self.moedas_imagem.width() / 2, self.moedas_imagem.height() / 2),
                                        image=self.moedas_imagem)

        self.painel_barra = tk.Canvas(master=self.janela_cadastro, width=720, height=60, background='#727272')

        self.painel_dp_menu = ctk.CTkFrame(master=self.janela_cadastro, width=400, height=400, fg_color='#708090')
        self.drop_menu = ctk.CTkOptionMenu(master=self.janela_cadastro,
                                           bg_color='#708090', 
                                           values=['Pessoa Física','Pessoa Jurídica'], command=self.selecionar_classe_pessoa)
        
        self.botao_cadastrar_escolha = ctk.CTkButton(master=self.janela_cadastro, text='Cadastrar', bg_color='#708090', command=self.realizar_cadastro)

        
        
        self.painel_barra.place(x=-2, y=0)
        self.painel_dp_menu.place(x=160, y=150)
        self.drop_menu.place(x=290, y=290)
        self.botao_cadastrar_escolha.place(x=290, y=390)
        self.moedas_painel.place(x=0, y=0)




class Janela_Principal(Cadastro_de_Conta, Formulario_Pessoa_Fisica):
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('699x720+650+100')
        self.root.title('BRASBANK - Caixa Eletrônico! - Seja bem vindo! V: 1.0 Made By: FelRFDev!')
        self.root.resizable(False, False)
        self.root._set_appearance_mode('dark')
        self.widgets()
        self.root.mainloop()
    
    def widgets(self):
        # -=-===-== Criando os Widgets =-=-=-=-=-=
        self.painel1 = tk.Canvas(master=self.root, width=240, height=840, background='#727272', highlightthickness=0)
        self.criar_conta = ctk.CTkButton(master=self.root, text='Criar Conta', width=120, font=('Impact',20),  height=100, bg_color='#727272', command=self.cadastrar)
        self.ver_saldo = ctk.CTkButton(master=self.root, text='Ver Saldo', font=('Impact',20), width=120, height=100, bg_color='#727272')
        self.fazer_deposito = ctk.CTkButton(master=self.root, text='Realizar\nDepósito', font=('Impact',20), width=120, height=100, bg_color='#727272')
        self.fazer_saque = ctk.CTkButton(master=self.root, text='Realizar\nSaque', width=120, font=('Impact',20), height=100, bg_color='#727272')

        self.banner2 = tk.PhotoImage(master=self.root, data=banner_inicial)
        self.banner2_canvas = tk.Canvas(master=self.root, width=500, height=500, highlightthickness=1)
        self.banner2_canvas.create_image((self.banner2.width()/2, self.banner2.height()/2),image=self.banner2)

        self.banner_banco=tk.PhotoImage(master=self.root, data=banner_do_banco)
        self.banner_banco_canvas = tk.Canvas(master=self.root, width=710, height=233, highlightthickness=1)
        self.banner_banco_canvas.create_image((self.banner_banco.width()/2, self.banner_banco.height()/2), image=self.banner_banco)
        

        # -=-===-== Posicionando os Widgets =-=-=-=-=-=
        
        self.banner_banco_canvas.place(x=-1, y=-10)
        self.banner2_canvas.place(x=200, y=220)
        self.criar_conta.place(x=30, y=240)
        self.ver_saldo.place(x=30, y=360)
        self.fazer_deposito.place(x=30, y=480)
        self.fazer_saque.place(x=30, y=600)
        self.painel1.place(x=0, y=0)


janela1 = Janela_Principal()

