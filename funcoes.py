import json

def abrirArquivo(arquivo):
    with open(arquivo, encoding='utf-8') as jsonFile:
        dados = json.load(jsonFile)
        return dados

def deletarItem(arquivo, dados,item):
    dados.remove(item)
    with open(arquivo,'w',encoding='utf-8') as jsonFile:
        json.dump(dados, jsonFile,indent=4, ensure_ascii=False)


def acharItemByIdLinearSearch(dados,id,chave):
    for item in dados:
        if item.get(chave) == id :
            return item
        
def acharItemByIdBinarySearch( lista, id, chave):
    inicio = 0
    fim = len(lista) -1
    while(inicio <= fim):
        meio = (inicio + fim)//2
        
        if(lista[meio].get(chave) == id):
            return meio
        if(lista[meio].get(chave) < id):
            inicio = meio + 1
        else:
            fim = meio -1
    return -1
    