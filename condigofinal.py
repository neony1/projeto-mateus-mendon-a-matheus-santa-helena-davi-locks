import mysql.connector
import customtkinter
from customtkinter import CTkLabel  
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#configuração de banco de dados
conexao_banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)
cursor = conexao_banco.cursor()


#função de verificação de login
def verificar_login():
    senha_correta = "senha123"
    if senha.get() == senha_correta:
        abrir_tela_selecao()
    else:
        erro_label.configure(text="Senha incorreta")

#função para mostrar o relógio
def mostrar_relogio():
    agora = datetime.now()
    horario = agora.strftime("%H:%M:%S")
    relogio_label.configure(text=horario)
    relogio_label.after(1000, mostrar_relogio)

#função para abrir a tela de opções
def abrir_tela_selecao():
    janela.withdraw()

    tela_selecao = customtkinter.CTkToplevel()
    tela_selecao.geometry("500x400")
    tela_selecao.title("Seleção de Gerenciamento")
    tela_selecao.configure(bg="#2a2d2e")

    titulo_label = customtkinter.CTkLabel(tela_selecao, text="Selecione o Gerenciamento", font=("Arial", 24, "bold"))
    titulo_label.pack(pady=50)

    def abrir_gerenciamento_livros():
        tela_selecao.withdraw()
        abrir_tela_gerenciamento_livros(tela_selecao)

    def abrir_gerenciamento_usuarios():
        tela_selecao.withdraw()
        abrir_tela_gerenciamento_usuarios(tela_selecao)

    #botões de seleção
    frame_botoes = customtkinter.CTkFrame(tela_selecao)
    frame_botoes.pack(pady=20)

    botao_livros = customtkinter.CTkButton(frame_botoes, text="Gerenciamento de Livros", command=abrir_gerenciamento_livros)
    botao_usuarios = customtkinter.CTkButton(frame_botoes, text="Gerenciamento de Usuários", command=abrir_gerenciamento_usuarios)

    botao_livros.pack(side="left", padx=10)
    botao_usuarios.pack(side="left", padx=10)

    #relógio no canto superior direito
    global relogio_label
    relogio_label = customtkinter.CTkLabel(tela_selecao, text="", font=("Arial", 12), anchor='ne')
    relogio_label.place(relx=1.0, rely=0.0, x=-50, y=10)
    mostrar_relogio()

#grafíco do usuário
def criar_grafico_usuarios(tela_exibicao):
    cursor.execute("SELECT COUNT(*) FROM usuario")
    total_usuarios = cursor.fetchone()[0]
    
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(['Total de Usuários'], [total_usuarios], color='skyblue')
    ax.set_xlim(0, total_usuarios + 10)
    ax.set_title('Total de Usuários Cadastrados')
    
    canvas = FigureCanvasTkAgg(fig, master=tela_exibicao)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

#grafíco do livro
def criar_grafico_livros(tela_principal):
    cursor.execute("SELECT COUNT(*) FROM livro")
    total_livros = cursor.fetchone()[0]
    
    #criando gráfico de barras
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(['Total de Livros'], [total_livros], color='skyblue')
    ax.set_xlim(0, total_livros + 10)
    ax.set_title('Total de Livros Cadastrados')
    canvas = FigureCanvasTkAgg(fig, master=tela_principal)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

#USUARIO
def abrir_tela_gerenciamento_usuarios(tela_selecao):
    tela_gerenciamento_usuario = customtkinter.CTkToplevel()
    tela_gerenciamento_usuario.geometry("500x600")
    tela_gerenciamento_usuario.title("Gerenciamento de Usuários")
    tela_gerenciamento_usuario.configure(bg="#2a2d2e")

    titulo_label = customtkinter.CTkLabel(tela_gerenciamento_usuario, text="Gerenciamento de Usuários", font=("Arial", 24, "bold"))
    titulo_label.pack(pady=20)

    def abrir_cadastro_usuario():
        tela_gerenciamento_usuario.withdraw()
        tela_cadastro(tela_gerenciamento_usuario)

    def abrir_exibicao_usuario():
        tela_gerenciamento_usuario.withdraw()
        tela_exibicao(tela_gerenciamento_usuario)

    def abrir_exclusao_usuario():
        tela_gerenciamento_usuario.withdraw()
        tela_exclusao(tela_gerenciamento_usuario)

    def abrir_atualizacao_usuario():
        tela_gerenciamento_usuario.withdraw()
        tela_atualizacao(tela_gerenciamento_usuario)

    #botões de seleção
    frame_botoes = customtkinter.CTkFrame(tela_gerenciamento_usuario)
    frame_botoes.pack(pady=20)

    botao_cadastrar = customtkinter.CTkButton(frame_botoes, text="Cadastrar Usuário", command=abrir_cadastro_usuario)
    botao_atualizar = customtkinter.CTkButton(frame_botoes, text="Atualizar Usuário", command=abrir_atualizacao_usuario)
    botao_exibir = customtkinter.CTkButton(frame_botoes, text="Exibir Usuário", command=abrir_exibicao_usuario)
    botao_excluir = customtkinter.CTkButton(frame_botoes, text="Excluir Usuário", command=abrir_exclusao_usuario)

    botao_cadastrar.pack(side="left", padx=10)
    botao_atualizar.pack(side="left", padx=10)
    botao_exibir.pack(side="left", padx=10)
    botao_excluir.pack(side="left", padx=10)

    #voltar para a tela de seleção
    def voltar_tela_selecao():
        tela_gerenciamento_usuario.destroy()
        tela_selecao.deiconify()

    botao_voltar = customtkinter.CTkButton(tela_gerenciamento_usuario, text="Voltar", command=voltar_tela_selecao)
    botao_voltar.pack(pady=10)

#tela de opções do usário
def abrir_tela_principal():
    janela.withdraw()
    
    tela_principal = customtkinter.CTkToplevel()
    tela_principal.geometry("500x600")
    tela_principal.title("Gerenciamento de Usuários")
    tela_principal.configure(bg="#2a2d2e")
    
    titulo_label = customtkinter.CTkLabel(tela_principal, text="Gerenciamento de Usuários", font=("Arial", 28, "bold"))
    titulo_label.pack(pady=20)

    def abrir_cadastro():
        tela_principal.withdraw()  
        tela_cadastro(tela_principal) 

    def abrir_exibicao():
        tela_principal.withdraw() 
        tela_exibicao(tela_principal)  

    def abrir_exclusao():
        tela_principal.withdraw()  
        tela_exclusao(tela_principal)  

    frame_botoes = customtkinter.CTkFrame(tela_principal)
    frame_botoes.pack(pady=10)

    botao_cadastrar = customtkinter.CTkButton(frame_botoes, text="Cadastrar Usuário", command=abrir_cadastro)
    botao_exibir = customtkinter.CTkButton(frame_botoes, text="Exibir Usuários", command=abrir_exibicao)
    botao_excluir = customtkinter.CTkButton(frame_botoes, text="Excluir Usuário", command=abrir_exclusao)

    botao_cadastrar.pack(side="left", padx=10)
    botao_exibir.pack(side="left", padx=10)
    botao_excluir.pack(side="left", padx=10)

    global relogio_label
    relogio_label = customtkinter.CTkLabel(tela_principal, text="", font=("Arial", 12), anchor='ne')
    relogio_label.place(relx=1.0, rely=0.0, x=-50, y=10)  
    mostrar_relogio()

#cadastro usuário
def tela_cadastro(tela_principal):
    tela_cadastro = customtkinter.CTkToplevel()
    tela_cadastro.geometry("500x600")
    tela_cadastro.title("Cadastro de Usuário")
    tela_cadastro.configure(bg="#2a2d2e")

    def cadastrar_usuario():
        try:
            id = entry_id_usuario.get()
            if not id: 
                raise ValueError("O ID do usuário não pode estar vazio.")
            id = int(id)  

            cursor.execute(f"SELECT * FROM usuario WHERE idusuario = {id}")
            if cursor.fetchone():
                raise ValueError(f"Já existe um usuário com o ID {id}.")

            nome = entry_nome_usuario.get()
            idade = entry_idade_usuario.get()
            livros = entry_livros_usuario.get()

            if not idade.isdigit():
                raise ValueError("A idade deve ser um número.")

            idade = int(idade)  


            comando_sql = f'INSERT INTO usuario (idusuario, nome, idade, livros) VALUES ({id}, "{nome}", {idade}, "{livros}")'
            cursor.execute(comando_sql)
            conexao_banco.commit()

            mensagem_label.configure(text="Usuário cadastrado com sucesso!", text_color="green")

        except ValueError as e:
            mensagem_label.configure(text=f"Erro: {e}", text_color="red")  

    entry_id_usuario = customtkinter.CTkEntry(tela_cadastro, placeholder_text="ID do Usuário")
    entry_id_usuario.pack(pady=5)

    entry_nome_usuario = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Nome do Usuário")
    entry_nome_usuario.pack(pady=5)

    entry_idade_usuario = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Idade do Usuário")
    entry_idade_usuario.pack(pady=5)

    entry_livros_usuario = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Livros do Usuário")
    entry_livros_usuario.pack(pady=5)

    botao_cadastrar = customtkinter.CTkButton(tela_cadastro, text="Cadastrar", command=cadastrar_usuario)
    botao_cadastrar.pack(pady=10)

    mensagem_label = customtkinter.CTkLabel(tela_cadastro, text="")
    mensagem_label.pack(pady=10)

    def voltar_tela_principal():
        tela_cadastro.destroy()  
        tela_principal.deiconify()  

    botao_voltar = customtkinter.CTkButton(tela_cadastro, text="Voltar", command=voltar_tela_principal)
    botao_voltar.pack(pady=10)

#exibição usuário
def tela_exibicao(tela_principal):
    tela_exibicao = customtkinter.CTkToplevel()
    tela_exibicao.geometry("600x700")
    tela_exibicao.title("Exibir Usuários")
    tela_exibicao.configure(bg="#2a2d2e")

    def exibir_usuarios():
        termo = entry_pesquisa.get()
        filtro = filtro_var.get()

        if filtro == "Nome":
            comando_sql = f'SELECT idusuario, nome, idade, livros FROM usuario WHERE nome LIKE "%{termo}%"'
        elif filtro == "Tudo":
            comando_sql = f'SELECT idusuario, nome, idade, livros FROM usuario'  
        else:
            comando_sql = f'SELECT idusuario, nome, idade, livros FROM usuario WHERE nome LIKE "%{termo}%"'
    
        cursor.execute(comando_sql)
        resultados = cursor.fetchall()

        for widget in frame_resultados.winfo_children():
            widget.destroy()

        for usuario in resultados:
            idusuario, nome, idade, livros = usuario  
            resultado_frame = customtkinter.CTkFrame(frame_resultados)
            resultado_frame.pack(pady=5, fill="x")
            customtkinter.CTkLabel(resultado_frame, text=f"ID: {idusuario}", width=100).pack(side="left", padx=5)
            customtkinter.CTkLabel(resultado_frame, text=f"Nome: {nome}", width=200).pack(side="left", padx=5)
            customtkinter.CTkLabel(resultado_frame, text=f"Idade: {idade}", width=100).pack(side="left", padx=5)
            customtkinter.CTkLabel(resultado_frame, text=f"Livros: {livros}", width=100).pack(side="left", padx=5)
            


    entry_pesquisa = customtkinter.CTkEntry(tela_exibicao, placeholder_text="Pesquisar")
    entry_pesquisa.pack(pady=10, padx=10, fill="x")

    filtro_var = customtkinter.StringVar(value="Nome")
    filtro_menu = customtkinter.CTkOptionMenu(tela_exibicao, variable=filtro_var, values=["Nome", "Idade", "Tudo"])
    filtro_menu.pack(pady=10)

    botao_exibir = customtkinter.CTkButton(tela_exibicao, text="Exibir Usuários", command=exibir_usuarios)
    botao_exibir.pack(pady=10)

    frame_resultados = customtkinter.CTkFrame(tela_exibicao)
    frame_resultados.pack(pady=10, fill="x")


    criar_grafico_usuarios(tela_exibicao)

    def voltar_tela_principal():
        tela_exibicao.destroy()  
        tela_principal.deiconify()  

    botao_voltar = customtkinter.CTkButton(tela_exibicao, text="Voltar", command=voltar_tela_principal)
    botao_voltar.pack(pady=10)

#atualização usuário
def tela_atualizacao(tela_principal):
    tela_atualizacao = customtkinter.CTkToplevel()
    tela_atualizacao.geometry("500x600")
    tela_atualizacao.title("Atualizar Usuário")
    tela_atualizacao.configure(bg="#2a2d2e")

    def atualizar_usuario():
        try:
            id_usuario = entry_id_usuario.get()
            if not id_usuario:
                raise ValueError("O ID do usuário não pode estar vazio.")

            id_usuario = int(id_usuario)

            cursor.execute(f"SELECT * FROM usuario WHERE idusuario = {id_usuario}")
            if not cursor.fetchone():
                raise ValueError("Usuário não encontrado.")

            novo_nome = entry_nome_usuario.get()
            nova_idade = entry_idade_usuario.get()
            novos_livros = entry_livros_usuario.get()

            if not nova_idade.isdigit():
                raise ValueError("A idade deve ser um número.")
            nova_idade = int(nova_idade)

            cursor.execute(f"""
                UPDATE usuario 
                SET nome = '{novo_nome}', idade = {nova_idade}, livros = '{novos_livros}'
                WHERE idusuario = {id_usuario}
            """)
            conexao_banco.commit()

            mensagem_label.configure(text="Usuário atualizado com sucesso!", text_color="green")

        except ValueError as e:
            mensagem_label.configure(text=f"Erro: {e}", text_color="red")

    entry_id_usuario = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="ID do Usuário")
    entry_id_usuario.pack(pady=5)

    entry_nome_usuario = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Novo Nome")
    entry_nome_usuario.pack(pady=5)

    entry_idade_usuario = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Nova Idade")
    entry_idade_usuario.pack(pady=5)

    entry_livros_usuario = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Novos Livros")
    entry_livros_usuario.pack(pady=5)

    botao_atualizar = customtkinter.CTkButton(tela_atualizacao, text="Atualizar", command=atualizar_usuario)
    botao_atualizar.pack(pady=10)

    mensagem_label = customtkinter.CTkLabel(tela_atualizacao, text="")
    mensagem_label.pack(pady=10)

    def voltar_tela_principal():
        tela_atualizacao.destroy()
        tela_principal.deiconify()

    botao_voltar = customtkinter.CTkButton(tela_atualizacao, text="Voltar", command=voltar_tela_principal)
    botao_voltar.pack(pady=10)


#exclusão usuário
def tela_exclusao(tela_principal):
    tela_exclusao = customtkinter.CTkToplevel()
    tela_exclusao.geometry("500x600")
    tela_exclusao.title("Excluir Usuário")
    tela_exclusao.configure(bg="#2a2d2e")

    def excluir_usuario():
        try:
            id_usuario = entry_id_exclusao.get()
            if not id_usuario:
                raise ValueError("O ID do usuário não pode estar vazio.")

            id_usuario = int(id_usuario)

            cursor.execute(f"SELECT * FROM usuario WHERE idusuario = {id_usuario}")
            if not cursor.fetchone():
                raise ValueError("Usuário não encontrado.")

            cursor.execute(f"DELETE FROM usuario WHERE idusuario = {id_usuario}")
            conexao_banco.commit()

            mensagem_label.configure(text="Usuário excluído com sucesso!", text_color="green")
        except ValueError as e:
            mensagem_label.configure(text=f"Erro: {e}", text_color="red")

    entry_id_exclusao = customtkinter.CTkEntry(tela_exclusao, placeholder_text="ID do Usuário")
    entry_id_exclusao.pack(pady=20)

    botao_excluir = customtkinter.CTkButton(tela_exclusao, text="Excluir", command=excluir_usuario)
    botao_excluir.pack(pady=10)

    mensagem_label = customtkinter.CTkLabel(tela_exclusao, text="")
    mensagem_label.pack(pady=10)

    def voltar_tela_principal():
        tela_exclusao.destroy()  
        tela_principal.deiconify()  

    botao_voltar = customtkinter.CTkButton(tela_exclusao, text="Voltar", command=voltar_tela_principal)
    botao_voltar.pack(pady=10)


#LIVROS
def abrir_tela_gerenciamento_livros(tela_selecao):
    tela_gerenciamento_livros = customtkinter.CTkToplevel()
    tela_gerenciamento_livros.geometry("500x600")
    tela_gerenciamento_livros.title("Gerenciamento de Livros")
    tela_gerenciamento_livros.configure(bg="#2a2d2e")

    titulo_label = customtkinter.CTkLabel(tela_gerenciamento_livros, text="Gerenciamento de Livros", font=("Arial", 24, "bold"))
    titulo_label.pack(pady=20)

    def abrir_cadastro_livro():
        tela_gerenciamento_livros.withdraw()
        tela_cadastro_livro(tela_gerenciamento_livros)

    def abrir_exibicao_livros():
        tela_gerenciamento_livros.withdraw()
        tela_exibicao_livros(tela_gerenciamento_livros)

    def abrir_exclusao_livros():
        tela_gerenciamento_livros.withdraw()
        tela_exclusao_livros(tela_gerenciamento_livros)
    
    def abrir_atualizacao_livro():
        tela_gerenciamento_livros.withdraw()
        tela_atualizacao_livro(tela_gerenciamento_livros)

    

    #botões de seleção
    frame_botoes = customtkinter.CTkFrame(tela_gerenciamento_livros)
    frame_botoes.pack(pady=20)

    #botões de seleção
    botao_cadastrar = customtkinter.CTkButton(frame_botoes, text="Cadastrar Livro", command=abrir_cadastro_livro)
    botao_atualizar = customtkinter.CTkButton(frame_botoes, text="Atualizar Livro", command=abrir_atualizacao_livro)
    botao_exibir = customtkinter.CTkButton(frame_botoes, text="Exibir Livros", command=abrir_exibicao_livros)
    botao_excluir = customtkinter.CTkButton(frame_botoes, text="Excluir Livro", command=abrir_exclusao_livros)

    botao_cadastrar.pack(side="left", padx=10)
    botao_atualizar.pack(side="left", padx=10)
    botao_exibir.pack(side="left", padx=10)
    botao_excluir.pack(side="left", padx=10)

    #voltar para a tela de seleção
    def voltar_tela_selecao():
        tela_gerenciamento_livros.destroy()
        tela_selecao.deiconify()

    botao_voltar = customtkinter.CTkButton(tela_gerenciamento_livros, text="Voltar", command=voltar_tela_selecao)
    botao_voltar.pack(pady=10)

#cadastro livros
def tela_cadastro_livro(tela_gerenciamento_livros):
    tela_cadastro = customtkinter.CTkToplevel()
    tela_cadastro.geometry("500x600")
    tela_cadastro.title("Cadastro de Livro")
    tela_cadastro.configure(bg="#2a2d2e")

    def cadastrar_livro():
        try:
            id = entry_id_livro.get()
            if not id:
                raise ValueError("O ID do livro não pode estar vazio.")
            id = int(id)

            cursor.execute(f"SELECT * FROM livro WHERE idlivro = {id}")
            if cursor.fetchone():
                raise ValueError(f"Já existe um livro com o ID {id}.")

            nome = entry_nome_livro.get()
            autor = entry_autor_livro.get()
            genero = entry_genero_livro.get()
            editora = entry_editora_livro.get()
            lancamento = entry_lancamento_livro.get()
            quantidade = entry_quantidade_livro.get()

            if not quantidade.isdigit():
                raise ValueError("A quantidade deve ser um número.")

            quantidade = int(quantidade)

            comando_sql = f'INSERT INTO livro (idlivro, nomelivro, autor, genero, editora, lancamento, quantidade) VALUES ({id}, "{nome}", "{autor}", "{genero}", "{editora}", "{lancamento}", {quantidade})'
            cursor.execute(comando_sql)
            conexao_banco.commit()

            mensagem_label.configure(text="Livro cadastrado com sucesso!", text_color="green")

        except ValueError as e:
            mensagem_label.configure(text=f"Erro: {e}", text_color="red")

    entry_id_livro = customtkinter.CTkEntry(tela_cadastro, placeholder_text="ID do Livro")
    entry_id_livro.pack(pady=5)

    entry_nome_livro = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Nome do Livro")
    entry_nome_livro.pack(pady=5)

    entry_autor_livro = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Autor do Livro")
    entry_autor_livro.pack(pady=5)

    entry_genero_livro = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Gênero do Livro")
    entry_genero_livro.pack(pady=5)

    entry_editora_livro = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Editora do Livro")
    entry_editora_livro.pack(pady=5)

    entry_lancamento_livro = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Data de Lançamento")
    entry_lancamento_livro.pack(pady=5)

    entry_quantidade_livro = customtkinter.CTkEntry(tela_cadastro, placeholder_text="Quantidade")
    entry_quantidade_livro.pack(pady=5)

    botao_cadastrar = customtkinter.CTkButton(tela_cadastro, text="Cadastrar", command=cadastrar_livro)
    botao_cadastrar.pack(pady=10)

    mensagem_label = customtkinter.CTkLabel(tela_cadastro, text="")
    mensagem_label.pack(pady=10)

    def voltar_tela_gerenciamento_livros():
        tela_cadastro.destroy()
        tela_gerenciamento_livros.deiconify()

    botao_voltar = customtkinter.CTkButton(tela_cadastro, text="Voltar", command=voltar_tela_gerenciamento_livros)
    botao_voltar.pack(pady=10)

#exibição livros
def tela_atualizacao_livro(tela_gerenciamento_livros):
    tela_atualizacao = customtkinter.CTkToplevel()
    tela_atualizacao.geometry("500x600")
    tela_atualizacao.title("Atualizar Livro")
    tela_atualizacao.configure(bg="#2a2d2e")

    def atualizar_livro():
        try:
            id = entry_id_livro.get()
            if not id:
                raise ValueError("O ID do livro não pode estar vazio.")
            id = int(id)

            cursor.execute(f"SELECT * FROM livro WHERE idlivro = {id}")
            if not cursor.fetchone():
                raise ValueError("Livro não encontrado.")

            nome = entry_nome_livro.get()
            autor = entry_autor_livro.get()
            genero = entry_genero_livro.get()
            editora = entry_editora_livro.get()
            lancamento = entry_lancamento_livro.get()
            quantidade = entry_quantidade_livro.get()

            if not quantidade.isdigit():
                raise ValueError("A quantidade deve ser um número.")
            quantidade = int(quantidade)

            comando_sql = f'''
            UPDATE livro 
            SET nomelivro="{nome}", autor="{autor}", genero="{genero}", editora="{editora}", lancamento="{lancamento}", quantidade={quantidade}
            WHERE idlivro={id}
            '''
            cursor.execute(comando_sql)
            conexao_banco.commit()

            mensagem_label.configure(text="Livro atualizado com sucesso!", text_color="green")

        except ValueError as e:
            mensagem_label.configure(text=f"Erro: {e}", text_color="red")

    entry_id_livro = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="ID do Livro")
    entry_id_livro.pack(pady=5)

    entry_nome_livro = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Nome do Livro")
    entry_nome_livro.pack(pady=5)

    entry_autor_livro = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Autor do Livro")
    entry_autor_livro.pack(pady=5)

    entry_genero_livro = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Gênero do Livro")
    entry_genero_livro.pack(pady=5)

    entry_editora_livro = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Editora do Livro")
    entry_editora_livro.pack(pady=5)

    entry_lancamento_livro = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Data de Lançamento")
    entry_lancamento_livro.pack(pady=5)

    entry_quantidade_livro = customtkinter.CTkEntry(tela_atualizacao, placeholder_text="Quantidade")
    entry_quantidade_livro.pack(pady=5)

    botao_atualizar = customtkinter.CTkButton(tela_atualizacao, text="Atualizar", command=atualizar_livro)
    botao_atualizar.pack(pady=10)

    mensagem_label = customtkinter.CTkLabel(tela_atualizacao, text="")
    mensagem_label.pack(pady=10)

    def voltar_tela_gerenciamento_livros():
        tela_atualizacao.destroy()
        tela_gerenciamento_livros.deiconify()

    botao_voltar = customtkinter.CTkButton(tela_atualizacao, text="Voltar", command=voltar_tela_gerenciamento_livros)
    botao_voltar.pack(pady=10)


#exibição livros
def tela_exibicao_livros(tela_gerenciamento_livros):
    tela_exibicao = customtkinter.CTkToplevel()
    tela_exibicao.geometry("600x700")
    tela_exibicao.title("Exibir Livros")
    tela_exibicao.configure(bg="#2a2d2e")

    
    def exibir_livros():
        termo = entry_pesquisa.get()
        filtro = filtro_var.get()
        
        
        if filtro == "Nome":
            comando_sql = f'SELECT * FROM livro WHERE nomelivro LIKE "%{termo}%"'
        elif filtro == "Autor":
            comando_sql = f'SELECT * FROM livro WHERE autor LIKE "%{termo}%"'
        elif filtro == "Gênero":
            comando_sql = f'SELECT * FROM livro WHERE genero LIKE "%{termo}%"'
        else:
            comando_sql = f'SELECT * FROM livro WHERE nomelivro LIKE "%{termo}%" OR autor LIKE "%{termo}%" OR genero LIKE "%{termo}%"'
        
        cursor.execute(comando_sql)
        resultados = cursor.fetchall()
        
       
        for widget in frame_resultados.winfo_children():
            widget.destroy()  
        
        for livro in resultados:
            idlivro, nomelivro, autor, genero, editora, lancamento, quantidade = livro
            resultado_frame = customtkinter.CTkFrame(frame_resultados)
            resultado_frame.pack(pady=5, fill="x")
            customtkinter.CTkLabel(resultado_frame, text=f"ID: {idlivro}", width=100).pack(side="left", padx=5)
            customtkinter.CTkLabel(resultado_frame, text=f"Nome: {nomelivro}", width=200).pack(side="left", padx=5)
            customtkinter.CTkLabel(resultado_frame, text=f"Autor: {autor}", width=150).pack(side="left", padx=5)
            customtkinter.CTkLabel(resultado_frame, text=f"Gênero: {genero}", width=100).pack(side="left", padx=5)
            customtkinter.CTkLabel(resultado_frame, text=f"Qtd: {quantidade}", width=100).pack(side="left", padx=5)
            
            
            def excluir_livro(idlivro):
                comando_sql = f'DELETE FROM livro WHERE idlivro = {idlivro}'
                cursor.execute(comando_sql)
                conexao_banco.commit()
                exibir_livros()  
                mensagem_label.configure(text="Livro excluído com sucesso!", text_color="green")
            
            
            botao_excluir = customtkinter.CTkButton(resultado_frame, text="Excluir", command=lambda idlivro=idlivro: excluir_livro(idlivro))
            botao_excluir.pack(side="left", padx=10)

    
    entry_pesquisa = customtkinter.CTkEntry(tela_exibicao, placeholder_text="Pesquisar por Nome, Autor ou Gênero")
    entry_pesquisa.pack(pady=10)

    
    filtro_var = customtkinter.StringVar(value="Nome")
    filtro_menu = customtkinter.CTkOptionMenu(tela_exibicao, variable=filtro_var, values=["Nome", "Autor", "Gênero", "Todos"])
    filtro_menu.pack(pady=10)

    
    botao_pesquisar = customtkinter.CTkButton(tela_exibicao, text="Pesquisar", command=exibir_livros)
    botao_pesquisar.pack(pady=10)

    
    frame_resultados = customtkinter.CTkFrame(tela_exibicao)
    frame_resultados.pack(pady=10, fill="both", expand=True)

    
    mensagem_label = customtkinter.CTkLabel(tela_exibicao, text="")
    mensagem_label.pack(pady=10)

    #Gráfico
    criar_grafico_livros(tela_exibicao)
    #
    def voltar_tela_gerenciamento_livros():
        tela_exibicao.destroy()
        tela_gerenciamento_livros.deiconify()

    botao_voltar = customtkinter.CTkButton(tela_exibicao, text="Voltar", command=voltar_tela_gerenciamento_livros)
    botao_voltar.pack(pady=10)

#exclusão livros
def tela_exclusao_livros(tela_gerenciamento_livros):
    tela_exclusao = customtkinter.CTkToplevel()
    tela_exclusao.geometry("500x400")
    tela_exclusao.title("Exclusão de Livros")
    tela_exclusao.configure(bg="#2a2d2e")

    def excluir_livro():
        try:
            id = entry_id_exclusao_livro.get()
            if not id:
                raise ValueError("O ID do livro não pode estar vazio.")
            id = int(id)

            cursor.execute(f"SELECT * FROM livro WHERE idlivro = {id}")
            livro = cursor.fetchone()
            if livro is None:
                raise ValueError("Livro não encontrado.")

            cursor.execute(f"DELETE FROM livro WHERE idlivro = {id}")
            conexao_banco.commit()

            mensagem_label.configure(text="Livro excluído com sucesso!", text_color="green")

        except ValueError as e:
            mensagem_label.configure(text=f"Erro: {e}", text_color="red")

    entry_id_exclusao_livro = customtkinter.CTkEntry(tela_exclusao, placeholder_text="ID do Livro")
    entry_id_exclusao_livro.pack(pady=5)

    botao_excluir = customtkinter.CTkButton(tela_exclusao, text="Excluir", command=excluir_livro)
    botao_excluir.pack(pady=10)

    mensagem_label = customtkinter.CTkLabel(tela_exclusao, text="")
    mensagem_label.pack(pady=10)

    def voltar_tela_gerenciamento_livros():
        tela_exclusao.destroy()
        tela_gerenciamento_livros.deiconify()

    botao_voltar = customtkinter.CTkButton(tela_exclusao, text="Voltar", command=voltar_tela_gerenciamento_livros)
    botao_voltar.pack(pady=10)

#função para a tela de login
janela = customtkinter.CTk()
janela.geometry("400x400")
janela.title("Tela de Login")
janela.configure(bg="#2a2d2e")

senha_label = customtkinter.CTkLabel(janela, text="Digite a senha de administrador", font=("Arial", 18))
senha_label.pack(pady=20)

senha = customtkinter.CTkEntry(janela, show="*")
senha.pack(pady=10)

botao_entrar = customtkinter.CTkButton(janela, text="Entrar", command=verificar_login)
botao_entrar.pack(pady=20)

erro_label = customtkinter.CTkLabel(janela, text="", text_color="red")
erro_label.pack(pady=10)

janela.mainloop()
