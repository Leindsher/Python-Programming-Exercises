#Usar o sistema do script 'codigo base' para um sistema de xcadastro de livros, com os seguintes campos: titulo, autor, genero, numero de paginas e um resumo em caixa frame com text box.
#O sistema deve ter uma tela principal com um título "Cadastro de Livros" e dois botões: "Cadastrar Livro" e "Listar Livros". 
#O sistema deve permitir cadastrar novos livros e listar os livros cadastrados.

import sqlite3
import customtkinter as ctk
from tkinter import messagebox

# CONFIGURAÇÕES
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# BANCO DE DADOS
conexao = sqlite3.connect("livros.db")
cursor = conexao.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    genero TEXT NOT NULL,
    paginas INTEGER NOT NULL,
    resumo TEXT
)
""")
conexao.commit()

# CLASSE PRINCIPAL
class SistemaLivros:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Livros")
        self.root.geometry("400x250")
        titulo = ctk.CTkLabel(root,text="Sistema de Livros", font=("Arial", 24, "bold"))
        titulo.pack(pady=30)

        btn_cadastrar = ctk.CTkButton(root,text="Cadastrar Livro", width=220, command=self.abrir_cadastro)
        btn_cadastrar.pack(pady=10)

        btn_listar = ctk.CTkButton( root, text="Listar Livros",  width=220, command=self.abrir_listagem)
        btn_listar.pack(pady=10)

    # CADASTRO
    def abrir_cadastro(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Cadastro")
        janela.geometry("600x600")
        janela.grab_set()
        ctk.CTkLabel(janela,text="Cadastrar Livro",font=("Arial", 20, "bold")
        ).pack(pady=15)
        titulo = ctk.CTkEntry(janela, placeholder_text="Título")
        titulo.pack(pady=5, padx=20, fill="x")
        autor = ctk.CTkEntry(janela,placeholder_text="Autor")
        autor.pack(pady=5, padx=20, fill="x")
        genero = ctk.CTkEntry( janela,placeholder_text="Gênero")
        genero.pack(pady=5, padx=20, fill="x")
        paginas = ctk.CTkEntry(janela,placeholder_text="Número de Páginas")
        paginas.pack(pady=5, padx=20, fill="x")
        resumo = ctk.CTkTextbox(janela, height=300)
        resumo.pack(pady=5, padx=20, fill="x")
        resumo.insert("end", "Digite um resumo do livro aqui...")

        def salvar():
            if (not titulo.get() or not autor.get()
                or not genero.get()or not paginas.get()):
                messagebox.showwarning("Atenção", "Preencha todos os campos!")
                return
            cursor.execute("""
            INSERT INTO livros
            (titulo, autor, genero, paginas, resumo)
            VALUES (?, ?, ?, ?, ?)
            """, (titulo.get(),autor.get(), genero.get(), paginas.get(), resumo.get("1.0", "end").strip() ))
            conexao.commit()
            messagebox.showinfo("Sucesso","Livro cadastrado!")
            janela.destroy()
            
        ctk.CTkButton(janela,text="Salvar", command=salvar).pack(pady=20)


    # LISTAGEM
    def abrir_listagem(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Livros Cadastrados")
        janela.geometry("850x500")
        janela.grab_set()
        frame_scroll = ctk.CTkScrollableFrame(janela)
        frame_scroll.pack(fill="both",expand=True,padx=10,pady=10)

        def carregar_dados():
            for widget in frame_scroll.winfo_children():
                widget.destroy()
            cursor.execute("""
            SELECT * FROM livros
            ORDER BY id DESC
            """)
            registros = cursor.fetchall()
            cabecalho = ctk.CTkFrame(frame_scroll)
            cabecalho.pack(fill="x", pady=3)
            ctk.CTkLabel(cabecalho, text="Ações", width=180).grid(row=0, column=0)
            ctk.CTkLabel(cabecalho, text="Título",width=100).grid(row=0, column=2)
            ctk.CTkLabel(cabecalho, text="Autor", width=180).grid(row=0, column=3)
            ctk.CTkLabel(cabecalho, text="Gênero", width=120).grid(row=0, column=4)
            ctk.CTkLabel(cabecalho, text="Páginas", width=120).grid(row=0, column=5)            
            ctk.CTkLabel(cabecalho, text="Resumo", width=200).grid(row=0, column=6)

            for registro in registros:
                id_livro = registro[0]
                linha = ctk.CTkFrame(frame_scroll)
                linha.pack(fill="x", pady=2)
                ctk.CTkLabel(linha, text=registro[1],justify='center', width=100).grid(row=0, column=2)
                ctk.CTkLabel(linha, text=registro[2],justify='center', width=180).grid(row=0, column=3)
                ctk.CTkLabel(linha, text=registro[3],justify='center', width=120).grid(row=0, column=4)
                ctk.CTkLabel(linha, text=registro[4],justify='center', width=120).grid(row=0, column=5)
                ctk.CTkLabel(linha, text=registro[5],justify='center', width=200).grid(row=0, column=6)

                btn_editar = ctk.CTkButton(linha, text="Alterar", width=70, command=lambda i=id_livro: self.alterar_livro( i,carregar_dados))
                btn_editar.grid(row=0, column=0, padx=5)
                btn_excluir = ctk.CTkButton(linha, text="Excluir", width=70, fg_color="red", hover_color="#aa0000", command=lambda i=id_livro:self.excluir_livro(i,carregar_dados))
                btn_excluir.grid(row=0,column=1,padx=5)
        carregar_dados()

    # ALTERAÇÃO
    def alterar_livro(self, id_livro, atualizar_lista):
        cursor.execute("""
        SELECT * FROM livros
        WHERE id=?
        """, (id_livro,))
        livro = cursor.fetchone()
        janela = ctk.CTkToplevel(self.root)
        janela.title("Alterar Livro")
        janela.geometry("600x600")
        janela.grab_set()
        titulo = ctk.CTkEntry(janela)
        titulo.insert(0, livro[1])
        titulo.pack(pady=10, padx=20, fill="x")
        autor = ctk.CTkEntry(janela)
        autor.insert(0, livro[2])
        autor.pack(pady=10, padx=20, fill="x")
        genero = ctk.CTkEntry(janela)
        genero.insert(0, livro[3])
        genero.pack(pady=10, padx=20, fill="x")
        paginas = ctk.CTkEntry(janela)
        paginas.insert(0, livro[4])
        paginas.pack(pady=10, padx=20, fill="x")
        resumo = ctk.CTkTextbox(janela, height=300)
        resumo.insert("1.0", livro[5])
        resumo.pack(pady=10, padx=20, fill="x")

        def salvar():
            cursor.execute("""
            UPDATE livros
            SET titulo=?,
                autor=?,
                genero=?,
                paginas=?,
                resumo=?
            WHERE id=?
            """,
            (titulo.get(), autor.get(), genero.get(), paginas.get(), resumo.get(), id_livro))
            conexao.commit()

            messagebox.showinfo("Sucesso", "Registro atualizado!" )
            atualizar_lista()
            janela.destroy()

        ctk.CTkButton(janela, text="Salvar Alterações", command=salvar).pack(pady=20)


    # EXCLUSÃO
    def excluir_livro(self, id_livro, atualizar_lista):
        resposta = messagebox.askyesno("Confirmar", "Deseja excluir este livro?")

        if resposta:
            cursor.execute("""
            DELETE FROM livros
            WHERE id=?
            """, (id_livro,))
            conexao.commit()
            atualizar_lista()


# EXECUÇÃO
root = ctk.CTk()
app = SistemaLivros(root)
root.mainloop()