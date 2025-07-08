import json
import os


if __name__ == "__main__":

    if os.path.exists("dicionario.json") and os.path.getsize("dicionario.json") > 0:
        with open("dicionario.json", "r", encoding="utf-8") as f:
            dic = json.load(f)
    else:
        dic = {}

    aberto = True

    while aberto == True:
        acao = input(f'Qual ação vc deseja fazer: (digite help) \n')
        if acao == 'fechar':
            aberto = False
        elif acao == 'ad palavra':
            a = input('palavra:')
            b = input('significado:')
            if a not in dic:
                dic[a] = b
            else:
                print(f'erro, a palavra já existe significa:{dic[a]}')
        elif acao == 'significado':
            pl = input('palavra:')
            try:
                print(dic[pl])
            except:
                print('essa palavra não existe')
        elif acao == 'pesquisa':
            pla = input('significado da palavra que vc quer:')
            for i in dic:
                if i == pla:
                    print(f'a palavra {i} possue o significado: {pla}')
        elif acao == 'help':
            print('significado - traduz uma palavra de solkratilis para portugues ')
            print('ad palavra - adiciona palavra para ao lexico')
            print('fechar - fecha o programa e salva o dicionario')
            print('pesquisa - verifica que existe alguma palavra com tal significado na língua')
            print('contagem - quantos morfemas tem no dic')
        elif acao == 'contagem':
            print(len(dic))


    with open("dicionario.json", "w", encoding="utf-8") as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)


