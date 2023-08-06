from abc import ABC
import mwparserfromhell
import pendulum
'''定义一些功能特化的基类'''
class WikiSectionDict(ABC):
    '''用于get_section()方法的字典类
    覆写了dict.index()方法，输出可直接用于edit(section)的值'''
    def __init__(wd):
        self.wd = wd
    def index(num:str)->str:
        return int(self.wd.index(num)+1)
    
class gen_wikitext():
    def __init__(self):
        self.txt:str = """"""
    def add_title(self,po:int,title:str):
        self.txt += "="*po + title + "="*po
        
class gen_tem():
    def __init__(self,title):
        self.txt = mwparserfromhell.parse("{{"+title+"}}")
