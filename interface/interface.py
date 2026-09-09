import tkinter as tk
from datetime import datetime
from pathlib import Path
import zipfile


class Interface:

    def __init__(self, scanner):
        self.scanner = scanner
        self.selecionados = {}
        self.arquivos_selecionados = {}
        self.frames_arquivos = {}

    def mostrar(self):
        self.tipos = {}
        self.selecionados = {}
        self.arquivos_selecionados = {}
        self.frames_arquivos = {}

        for arquivo in self.arquivos:

            if arquivo.categoria != "Pessoal":
                continue

            tipo = arquivo.tipo_arquivo

            if tipo == "":
                tipo = "sem extensão"

            if tipo not in self.tipos:
                self.tipos[tipo] = []

            self.tipos[tipo].append(arquivo)

        coluna = 0
        linha = 0

        for tipo in self.tipos:

            frame_tipo = tk.Frame(self.area_tipos)
            frame_tipo.grid(
                row=linha,
                column=coluna,
                sticky="w",
                padx=10,
                pady=3
            )

            frame_arquivos = tk.Frame(frame_tipo)

            self.frames_arquivos[tipo] = frame_arquivos

            selecionado = tk.BooleanVar(value=False)

            self.selecionados[tipo] = selecionado

            self.arquivos_selecionados[tipo] = []

            seta = tk.Button(
                frame_tipo,
                text="▶",
                width=2,
                command=lambda t=tipo: self.mostrar_arquivos(t)
            )

            seta.pack(side="left")

            caixa = tk.Checkbutton(
                frame_tipo,
                text=f"{tipo} ({len(self.tipos[tipo])} arquivos)",
                variable=selecionado,
                command=lambda t=tipo: self.selecionar_tipo(t)
            )

            caixa.pack(side="left")

            for arquivo in self.tipos[tipo]:

                variavel_arquivo = tk.BooleanVar(value=False)

                self.arquivos_selecionados[tipo].append(
                    (arquivo, variavel_arquivo)
                )

            linha += 1

            if linha >= 30:
                linha = 0
                coluna += 1

    def mostrar_arquivos(self, tipo):

        frame = self.frames_arquivos[tipo]

        if frame.winfo_ismapped():
            frame.pack_forget()
            return

        for widget in frame.winfo_children():
            widget.destroy()

        for arquivo, variavel in self.arquivos_selecionados[tipo]:

            data_modificacao = datetime.fromtimestamp(
                arquivo.arquivo.stat().st_mtime
            ).strftime("%d/%m/%Y %H:%M")

            caixa = tk.Checkbutton(
                frame,
                text=(
                    f"{arquivo.nome_arquivo} | "
                    f"{arquivo.tamanho_arquivo} | "
                    f"{data_modificacao}"
                ),
                variable=variavel,
                command=lambda t=tipo: self.atualizar_tipo(t)
            )

            caixa.pack(
                anchor="w",
                padx=35,
                pady=2
            )

        frame.pack(anchor="w")

    def selecionar_tipo(self, tipo):

        valor = self.selecionados[tipo].get()

        for arquivo, variavel in self.arquivos_selecionados[tipo]:
            variavel.set(valor)

    def atualizar_tipo(self, tipo):

        arquivos = self.arquivos_selecionados[tipo]

        todos_selecionados = all(
            variavel.get()
            for arquivo, variavel in arquivos
        )

        self.selecionados[tipo].set(todos_selecionados)

    def fazer_backup(self):

        selecionados = []

        for tipo in self.arquivos_selecionados:

            for arquivo, variavel in self.arquivos_selecionados[tipo]:

                if variavel.get():
                    selecionados.append(arquivo)

        if not selecionados:
            print("Nenhum arquivo selecionado.")
            return

        pasta_backup = Path("backup")
        pasta_backup.mkdir(exist_ok=True)

        nome_backup = pasta_backup / "backup.backup"

        with zipfile.ZipFile(
            nome_backup,
            "w",
            zipfile.ZIP_DEFLATED
        ) as backup:

            for arquivo in selecionados:

                caminho = arquivo.arquivo

                backup.write(
                    caminho,
                    arcname=caminho.name
                )

        print("Backup criado com sucesso!")
        print("Arquivo:", nome_backup)
        print("Total selecionado:", len(selecionados))

    def iniciar(self):

        janela = tk.Tk()

        janela.title("Backup")
        janela.geometry("1000x800")

        botao = tk.Button(
            janela,
            text="Iniciar análise",
            command=self.iniciar_analise
        )

        botao.pack(pady=10)

        container = tk.Frame(janela)
        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        canvas = tk.Canvas(container)

        barra = tk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview
        )

        self.area_tipos = tk.Frame(canvas)

        self.area_tipos.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=self.area_tipos,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=barra.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        barra.pack(
            side="right",
            fill="y"
        )

        botao_backup = tk.Button(
            janela,
            text="Criar Backup",
            command=self.fazer_backup
        )

        botao_backup.pack(pady=20)

        janela.mainloop()

    def iniciar_analise(self):

        self.arquivos = self.scanner.analisar()

        print("Total de arquivos analisados:", len(self.arquivos))

        self.mostrar()