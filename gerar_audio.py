import os
from pydub import AudioSegment

PASTA_DOS_SONS = "audios/"

PASTA_DE_SAIDA = "audios_gerados/"

def criar_palavra(palavra):

    print(f"Gerando a palavra: '{palavra}'...")

    palavra_final = AudioSegment.silent(duration=0)

    
    for letra in palavra:

        nome_do_arquivo = f"{letra}.wav"
        caminho_do_arquivo = os.path.join(PASTA_DOS_SONS, nome_do_arquivo)

        som_da_silaba = AudioSegment.from_file(caminho_do_arquivo)
        palavra_final += som_da_silaba

    caminho_de_saida = os.path.join(PASTA_DE_SAIDA, f"{palavra}.wav")
    palavra_final.export(caminho_de_saida, format="mp3")
    
    print(f"Palavra '{palavra}' salva com sucesso em '{caminho_de_saida}'!\n")



if __name__ == "__main__":
    p = input("digite a palavra: ").strip()
    criar_palavra(p)