import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, event):
        txtIn, language, modality = self._view._txtSentence.value, self._view._txtLanguage.value, self._view._txtModality.value
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = 'Parole errate: '

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = f'{paroleErrate} {str(parola)}'
                t2 = time.time()
                tempoRichiesto = t2 - t1
                self._view.createListView(paroleErrate, tempoRichiesto)

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = f'{paroleErrate} {str(parola)}'
                t2 = time.time()
                tempoRichiesto = t2 - t1
                self._view.createListView(paroleErrate, tempoRichiesto)

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = f'{paroleErrate} {str(parola)}'
                t2 = time.time()
                tempoRichiesto = t2 - t1
                self._view.createListView(paroleErrate, tempoRichiesto)
            
            case _:
                return None

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
