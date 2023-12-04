import customtkinter as ctk
import base64
import tkinter as tk
from b64imagens import *
from dio import *
from tkinter import messagebox
from random import randint

clientes = []

class Janela_Ver_Saldo:
    def __init__(self):
        self.janela_vs = ctk.CTkToplevel()
        self.janela_vs.geometry("700x720+500+100")
        self.janela_vs.title('BRASBANK - Consulta de Saldo !')
        self.janela_vs.resizable(False, False)
        self.janela_vs.widgets()
        self.janela_vs.mainloop()

    def widgets(self):
        pass







class Formulario_Pesssoa_Juridica:
    """Classe para a janela de cadastro de pessoa Jurídica"""
    def __init__(self):
        self.formulario_pj = ctk.CTkToplevel()
        self.formulario_pj.geometry("700x720+500+100")
        self.formulario_pj.title('BRASBANK - Janela de Formulário para Cadastro !')
        self.formulario_pj.resizable(False, False)
        self.formulario_widgets_pj()
        self.formulario_pj.grab_set()
        self.formulario_pj.focus_force()
        self.formulario_pj.mainloop()

    def realizar_cadastro_pf(self):
        if (not self.nome_entry_pj.get() or not self.cnpj.get() or not self.data_nascimento_pj.get()
                or not self.endereco_pj.get() or not self.senha_pj.get()):
            tk.messagebox.showerror('Erro!', 'Você precisa preencher todos os dados!')
        else:
            cliente = Cliente(self.endereco_pj.get())
            cliente.classificacao = Pessoa_Juridica(self.nome_entry_pj.get(), self.cnpj.get(), self.data_nascimento_pj.get())
            conta = Conta_Corrente.gerar_conta(numero=randint(1, 10000), senha=self.senha_pj.get(), cliente=cliente)
            cliente.adicionar_conta(conta)
            clientes.append(cliente)
            print(clientes)
            tk.messagebox.showinfo("Sucesso", 'Cadastro realizado com sucesso!')



    def formulario_widgets_pj(self):
        # -=-=-=-=-=-= Widgets Visuais =-=-=-=-=-=-=-=-=-=

        self.nome_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.nome_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='Nome', font=('Impact', 14), bg_color='#708090',
                                          text_color='white')
        self.cnpj_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.cnpj_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='CNPJ', font=('Impact', 14), bg_color='#708090',
                                          text_color='white')

        self.dt_nascimento_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.dt_nascimento_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='DT Nascimento', font=('Impact', 10),
                                                   bg_color='#708090',
                                                   text_color='white')

        self.endereco_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.endereco_texto_pj= ctk.CTkLabel(master=self.formulario_pj, text='Endereço', font=('Impact', 14),
                                             bg_color='#708090',
                                             text_color='white')

        self.senha_painel_pj = ctk.CTkFrame(master=self.formulario_pj, width=68, height=28, fg_color='#708090')
        self.senha_texto_pj = ctk.CTkLabel(master=self.formulario_pj, text='Senha', font=('Impact', 14),
                                           bg_color='#708090',
                                           text_color='white')


        # =-=-=-=-=-= Places =-=-==-=-=-=-=-=-
        self.nome_painel_pj.place(x=82, y=160)
        self.nome_texto_pj.place(x=92, y=160)
        self.cnpj_painel_pj.place(x=82, y=230)
        self.cnpj_texto_pj.place(x=92, y=230)
        self.dt_nascimento_painel_pj.place(x=336, y=229)
        self.dt_nascimento_texto_pj.place(x=340, y=229)
        self.endereco_painel_pj.place(x=82, y=330)
        self.endereco_texto_pj.place(x=92, y=330)
        self.senha_painel_pj.place(x=165, y=420)
        self.senha_texto_pj.place(x=180, y=420)

        # -=-=-=-=-=-=-=-=-= Widgets Cadastrais -=-=-=-=-=-=-=-=-=
        self.nome_entry_pj = ctk.CTkEntry(master=self.formulario_pj, width=400)
        self.cnpj= ctk.CTkEntry(master=self.formulario_pj)
        self.data_nascimento_pj = ctk.CTkEntry(master=self.formulario_pj)
        self.endereco_pj = ctk.CTkEntry(master=self.formulario_pj, width=400)
        self.senha_pj = ctk.CTkEntry(master=self.formulario_pj, width=220)
        self.botao_confirmar_cadastro_pj = ctk.CTkButton(master=self.formulario_pj, text='Cadastrar',
                                                      command=self.realizar_cadastro_pf)

        # -=-=-=-=-=-=-=-=-= Places -=-=-=-=-=-=-=-=-=
        self.nome_entry_pj.place(x=170, y=160)
        self.cnpj.place(x=170, y=230)
        self.data_nascimento_pj.place(x=430, y=230)
        self.endereco_pj.place(x=170, y=330)
        self.senha_pj.place(x=250, y=420)
        self.botao_confirmar_cadastro_pj.place(x=284, y=520)



class Formulario_Pessoa_Fisica:
    """Classe para a janela de cadastro de pessoa Física"""
    def __init__(self):
        self.formulario_pf = ctk.CTkToplevel()
        self.formulario_pf.geometry('700x720+650+100')
        self.formulario_pf.title('BRASBANK - Janela de Formulário para Cadastro!')
        self.formulario_pf.resizable(False, False)
        self.formulario_widgets()
        self.formulario_pf.grab_set()
        self.formulario_pf.focus_force()
        self.formulario_pf.mainloop()

    def realizar_cadastro(self):
        if (not self.nome_entry.get() or not self.cpf.get() or not self.data_nascimento.get() or not self.endereco.get()
                or not self.senha.get()):
            tk.messagebox.showerror('Erro!', 'Você precisa preencher todos os dados!')
        else:
            # -=-=-=-=-=- Cadastrando Cliente Pessoa Física e Conta Bancária -=-=-=-=-=-
            cliente = Cliente(self.endereco.get())
            cliente.classificacao = Pessoa_Fisica(self.nome_entry.get(), self.cpf.get(), self.data_nascimento.get())
            conta = Conta_Corrente.gerar_conta(numero=randint(1,10000), senha=self.senha.get(), cliente=cliente)
            cliente.adicionar_conta(conta)
            clientes.append(cliente)
            print(clientes)
            tk.messagebox.showinfo("Sucesso", 'Cadastro realizado com sucesso!')


    def formulario_widgets(self):

        #-=-=-=-=-=-= Widgets Visuais =-=-=-=-=-=-=-=-=-=

        self.nome_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.nome_texto = ctk.CTkLabel(master=self.formulario_pf, text='Nome', font=('Impact', 14), bg_color='#708090',
                                       text_color='white')
        self.cpf_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.cpf_texto = ctk.CTkLabel(master=self.formulario_pf, text='CPF', font=('Impact', 14), bg_color='#708090',
                                       text_color='white')

        self.dt_nascimento_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.dt_nascimento_texto = ctk.CTkLabel(master=self.formulario_pf, text='DT Nascimento', font=('Impact', 10),
                                                bg_color='#708090',
                                                text_color='white')

        self.endereco_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.endereco_texto= ctk.CTkLabel(master=self.formulario_pf, text='Endereço', font=('Impact', 14),
                                         bg_color='#708090',
                                         text_color='white')

        self.senha_painel = ctk.CTkFrame(master=self.formulario_pf, width=68, height=28, fg_color='#708090')
        self.senha_texto = ctk.CTkLabel(master=self.formulario_pf, text='Senha', font=('Impact', 14),
                                         bg_color='#708090',
                                         text_color='white')

        # =-=-=-=-=-= Places =-=-==-=-=-=-=-=-
        self.nome_painel.place(x=82, y=160)
        self.nome_texto.place(x=92, y=160)
        self.cpf_painel.place(x=82, y=230)
        self.cpf_texto.place(x=92, y=230)
        self.dt_nascimento_painel.place(x=336, y=229)
        self.dt_nascimento_texto.place(x=340, y=229)
        self.endereco_painel.place(x=82, y=330)
        self.endereco_texto.place(x=92, y=330)
        self.senha_painel.place(x=165, y=420)
        self.senha_texto.place(x=180, y=420)


        # -=-=-=-=-=-=-=-=-= Widgets Cadastrais -=-=-=-=-=-=-=-=-=
        self.nome_entry = ctk.CTkEntry(master=self.formulario_pf, width=400)
        self.cpf = ctk.CTkEntry(master=self.formulario_pf)
        self.data_nascimento = ctk.CTkEntry(master=self.formulario_pf)
        self.endereco = ctk.CTkEntry(master=self.formulario_pf, width=400)
        self.senha = ctk.CTkEntry(master=self.formulario_pf, width=220)
        self.botao_confirmar_cadastro = ctk.CTkButton(master=self.formulario_pf, text='Cadastrar',
                                                      command=self.realizar_cadastro)


        # -=-=-=-=-=-=-=-=-= Places -=-=-=-=-=-=-=-=-=
        self.nome_entry.place(x=170, y=160)
        self.cpf.place(x=170, y=230)
        self.data_nascimento.place(x=430, y=230)
        self.endereco.place(x=170, y=330)
        self.senha.place(x=250, y=420)
        self.botao_confirmar_cadastro.place(x=284, y=520)






class Cadastro_de_Conta:
    """Classe  com a janela para escolha de pessoa física ou jurídica"""
    def cadastrar(self):
        self.janela_cadastro = ctk.CTkToplevel()
        self.janela_cadastro.title('BRASBANK - Bem vindo ao sistema de cadastro! V: 1.0 Made By: FelRFDev!')
        self.janela_cadastro.geometry('700x720+650+100')
        self.janela_cadastro.resizable(False, False)
        self.widgets_de_cadastro()
        self.janela_cadastro.grab_set()
        self.janela_cadastro.focus_force()
        self.janela_cadastro.mainloop()

    def realizar_cadastro(self):
        if self.drop_menu.get() == 'Pessoa Física':
            Formulario_Pessoa_Fisica()
        elif self.drop_menu.get() == 'Pessoa Jurídica':
            Formulario_Pesssoa_Juridica()
        
    def widgets_de_cadastro(self):
        self.escolha = ''
        self.moedas_imagem = tk.PhotoImage(master=self.janela_cadastro, data=moedas)
        self.moedas_painel = tk.Canvas(master=self.janela_cadastro, width=720, height=720)
        self.moedas_painel.create_image((self.moedas_imagem.width() / 2, self.moedas_imagem.height() / 2),
                                        image=self.moedas_imagem)

        self.painel_barra = tk.Canvas(master=self.janela_cadastro, width=720, height=60, background='#727272')

        self.painel_dp_menu = ctk.CTkFrame(master=self.janela_cadastro, width=400, height=400, fg_color='#708090')
        self.drop_menu = ctk.CTkOptionMenu(master=self.janela_cadastro,
                                           bg_color='#708090', 
                                           values=['Pessoa Física', 'Pessoa Jurídica'])
        
        self.botao_cadastrar_escolha = ctk.CTkButton(master=self.janela_cadastro, text='Cadastrar', bg_color='#708090',
                                                     command=self.realizar_cadastro)

        
        
        self.painel_barra.place(x=-2, y=0)
        self.painel_dp_menu.place(x=160, y=150)
        self.drop_menu.place(x=290, y=290)
        self.botao_cadastrar_escolha.place(x=290, y=390)
        self.moedas_painel.place(x=0, y=0)




class Janela_Principal(Cadastro_de_Conta, Formulario_Pessoa_Fisica):
    """Classe que origina a janela principal"""
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



