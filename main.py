from re import findall
from requests import get

class UserInput:
    def __init__(self, page):
        self.rep = self.getAnswers(page)
        print('Si plusieurs réponses sont attendues, elles seront séparées par une virgule.')
        for i in range(len(self.rep)):
            print(f'Réponse {i + 1} : {self.transformAnswer(self.rep[i])}')

    def getAnswers(self, a):
        return findall(pattern=r'(var solution = \["[a-z]*[A-Z]*[0-9]*[^\]]*"])', string=a)

    def transformAnswer(self, a):
        a = a[15:].replace('["', '').replace('"]', '').replace('"', '').split('|')[0].replace(',', ', ')
        return a

    @staticmethod
    def getDesc():
        return 'Texte entré par l\'utilisateur'


class DragDrop():
    def __init__(self, page):
        pass

    @staticmethod
    def getDesc():
        return 'Glisser-Déposer'


def getPage():
    # example : https://view.genial.ly/606dc8487ba6360d7147bc1c/interactive-content-scratch-debranche
    return get(input('Entrez le lien vers la page Genial.ly : ')).text


if __name__ == '__main__':
    page = getPage()
    modes = {
        '1': UserInput
    }
    for i in modes:
        print(f'{i} : {modes[i].getDesc()}')

    valid = False
    while not valid:
        type = input('Veuillez choisir un numéro d\'exercices :')
        try:
            modes[type](page)
            valid = True
        except:
            print('Numéro invalide !')
    print('Chargement des réponses...')

