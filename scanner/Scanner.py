from pathlib import Path
from datetime import datetime, timedelta

class Arquivo:
    def __init__(self, nome_arquivo, tipo_arquivo, tamanho_arquivo, modificacao_arquivo, arquivo, categoria):
        self.nome_arquivo = nome_arquivo 
        self.tipo_arquivo = tipo_arquivo
        self.tamanho_arquivo = tamanho_arquivo
        self.modificacao_arquivo = modificacao_arquivo
        self.arquivo = arquivo
        self.categoria = categoria



class Scanner:

    pasta_pessoal = [ "Área de trabalho",
    "Documentos",
    "Downloads",
    "Imagens",
    "Músicas",
    "Vídeos",
    "Modelos",
    "Público"]

    pasta_ignorada = [ ".cache",
        ".npm",
        ".nvm",
        ".steam",
        ".dotnet",
        ".gemini"]

    def formatar_tamanho(self, tamanho):

        unidades = ["B", "KB", "MB", "GB"]

        for unidade in unidades:

            if tamanho < 1024:
                return f"{tamanho:.2f} {unidade}"

            tamanho = tamanho / 1024

    def deve_analisar(self, arquivo):
        for pasta in arquivo.parts:
            if pasta in self.pasta_ignorada:
                return False

        return True

    def e_pessoal(self, arquivo):

        for pasta in arquivo.parts:
            if pasta in self.pasta_pessoal:
                return True

        return False

    def analisar(self):
        now = datetime.now()
        pasta = Path.home()

        lista = []

        for arquivo in pasta.rglob("*"):
             
             if not self.deve_analisar(arquivo):
                continue
             
             if arquivo.is_file():

                if self.e_pessoal(arquivo):
                    print("arquivo pessoal:", arquivo)
                    categoria = "Pessoal"
                else:
                    categoria = "Outros"

                nome_arquivo = arquivo.name

                tipo_arquivo = arquivo.suffix

                tamanho_arquivo = arquivo.stat().st_size
                tamanho_arquivo = self.formatar_tamanho(tamanho_arquivo)

                modificacao_arquivo = now - (datetime.fromtimestamp(arquivo.stat().st_mtime))

                tempo = ""

                if modificacao_arquivo.days <= 5:
                    tempo = "recente"
                elif modificacao_arquivo.days <= 40:
                    tempo = "antigo"
                else:
                    tempo = "muito antigo"

                guardar = Arquivo(nome_arquivo, tipo_arquivo, tamanho_arquivo, modificacao_arquivo, arquivo, categoria)

                lista.append(guardar)


        return lista   