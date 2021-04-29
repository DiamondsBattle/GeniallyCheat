from re import findall
from requests import get


def getAnswers(a):
    return findall(pattern=r'(var solution = \["[a-z]*[A-Z]*[0-9]*[^\]]*"])', string=a)

def transformAnswer(a):
    a = a[15:]
    a = a.replace('["', '').replace('"]', '').replace('"', '')
    a = a.split('|')[0]
    a = a.replace(',', ', ')
    return a

def getPage():
    # example : https://view.genial.ly/606dc8487ba6360d7147bc1c/interactive-content-scratch-debranche
    return get(input('Entrez le lien vers la page Genial.ly : ')).text


if __name__ == '__main__':
    page = getPage()
    print('Chargement des réponses...')
    rep = getAnswers(page)
    for i in range(len(rep)):
        print(f'Réponse {i + 1} : {transformAnswer(rep[i])}')
