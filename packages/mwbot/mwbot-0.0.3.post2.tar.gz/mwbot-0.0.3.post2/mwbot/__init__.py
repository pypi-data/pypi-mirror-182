'''用于编辑/获取mediawiki文本的库'''
import requests
import ujson as json
from loguru import logger
import os
import schedule
# import lib.model as model
import aiohttp
import mwbot.prototype as pt

class Bot():
    '''[https://www.mediawiki.wikimirror.org/wiki/API:Main_page/zh]
    现阶段要求api，index，username，password四个参数'''

    # 成员变量
    def __init__(self, sitename, api, index, username, password):
        '''初始化参数sitename, api, index, username, password'''
        self.sitename = sitename
        self.api = api
        self.index = index
        self.username = username
        self.password = password
        self.S = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}
        # 懒狗式自动登录
        self.login()
        # 防过期 10min登一次
        def login_schedule():
            self.login(output_bool=False)
        schedule.every(10).minutes.do(login_schedule)

    def fetch_token(self, type: str):
        '''fetch_token(type=STRING)
        根据不同的type类型返回对应的token'''
        PARAMS = {
            'action': "query",
            'meta': "tokens",
            'type': str(type),
            'format': "json"
        }
        token = self.S.post(url=self.api, data=PARAMS)
        token = token.json()
        location = str(type) + "token"
        return token['query']['tokens'][location]

    def login(self,output_bool=True):
        '''登录'''
        login_PARAMS = {
            'action': "login",
            'lgname': self.username,
            'lgpassword': self.password,
            'lgtoken': self.fetch_token(type="login"),
            'format': "json"
        }
        login = self.S.post(url=self.api, data=login_PARAMS,headers=self.headers)
        login = login.json()
        if login['login']['result'] == "Success":
            if output_bool==True:
                logger.info(f'Welcome to {self.sitename}, {login["login"]["lgusername"]}!')
            else:...

    def get_data(self, page_name: str):
        '''
        input:y = x.get_data(page_name="xxx")
        output:list with dict:
        {   'pageid': 155, 
                'ns': 0, 
                'title': 'Test', 
                'revisions': [
                        {'slots': 
                                {'main': 
                                        {'contentmodel': 'wikitext', 
                                        'contentformat': 'text/x-wiki', 
                                        'content': 'Test'}
                                }
                        }
                ]
        }'''
        PARAMS = {
            "action": "query",
            "prop": "revisions",
            "titles": page_name,
            "rvslots": "*",
            "rvprop": "content",
            "formatversion": 2,
            "format": "json"
        }
        text = self.S.post(url=self.api, data=PARAMS, headers=self.headers)
        text = text.json()
        text = text["query"]["pages"][0]
        #logger.info(f'Get info of [[{text["title"]}]] successfully.\n{text}')
        return text

    def get_page_text(self, page_name, section=''):
        '''获取页面中的文本'''
        # PARAMS = {
        #     "title=": page_name,
        #     "action": "raw",
        #     "section": section
        # }
        # act = self.S.post(url=self.index, data=PARAMS, headers=self.headers)
        act = self.S.post(url=f"{self.index}?action=raw&title={page_name}&section={section}", headers=self.headers)
        if act.status_code == 404:
            logger.warning(f"请检查get_page_text传入的页面是否在{self.sitename}存在。")
            return None
        #logger.info(f'The text of [[{page_name}]]:\n{data}')
        else:
            return str(act.text)

    def edit_page(self, title:str, text:str, summary="", **kwargs):
        '''编辑一个页面。常用参数：title,text,summary.'''
        PARAMS = {
            "action": "edit",
            "minor": True,
            "bot": True,
            "format": "json",
            "title": title,
            "text": text,
            "summary":summary
        }
        for key, value in kwargs.items():
            key = str(key)
            value = str(value)
            PARAMS[key] = value
        PARAMS["token"] = self.fetch_token(type="csrf")
        PARAMS["summary"] += " //Edit by Bot."
        act = self.S.post(url=self.api, data=PARAMS, headers=self.headers)
        act = act.json()
        if act['edit']['result'] == "Success":
            logger.info(f'Edit [[{PARAMS["title"]}]] successfully.')
        else:
            logger.debug(act)

    def upload_local(self, local_name, local_path, web_name, text="", **kwargs):
        '''从本地上传一个文件.'''
        PARAMS = {
            "action": "upload",
            "filename": web_name,
            "format": "json",
            "token": self.fetch_token(type="csrf"),
            "ignorewarnings": True,
            "watchlist" :"nochange"
        }
        for key, value in kwargs.items():
            key = str(key)
            value = str(value)
            PARAMS[key] = value
        FILE = {'file': (local_name, open(local_path, 'rb'), 'multipart/form-data')}
        act = self.S.post(url=self.api, data=PARAMS,headers=self.headers, files=FILE)
        act = act.json()
        # logger.info(f'Upload {local_name}=>[[File:{web_name}]] successfully.')
        print(act)

    def purge(title, **kwargs):
        '''刷新页面'''
        PARAMS = {
            "action": "purge",
            "titles": str(title),
            "format": "json"
        }
        for key, value in kwargs.items():
            key = str(key)
            value = str(value)
            PARAMS[key] = value
        PARAMS["summary"] += " //Upload by Bot."
        act = self.S.post(url=self.api, data=PARAMS,headers=self.headers)
        act = act.json()
        if act["upload"]["result"] == "Success":
            logger.info(f"Purge [[{title}]] Successfully.")
        else:
            logger.debug(act)

    def parse(self, page_name, **kwargs):
        '''https://prts.wiki/api.php?action=help&modules=parse'''
        PARAMS = {
            "format": "json",
            "page": page_name,
            "action": "parse"
        }
        for key, value in kwargs.items():
            key = str(key)
            value = str(value)
            PARAMS[key] = value
        act = self.S.post(url=self.api, data=PARAMS, headers=self.headers)
        return act.json()

    def get_section(self, page_name):
        result = self.parse(page_name=page_name, prop='sections')
        result = result['parse']['sections']
        result_list = []
        for i in result:
            result_list.append(i['line'])
        if result_list:
            return pt.WikiSectionDict(result_list)
        else:
            logger.info(f'页面{page_name}没有任何章节！')
    def create_page(self,title,text,summary):
        '''创建页面'''
        deal = self.get_data(page_name=title)
        if "missing" in deal:
            self.edit_page(title=title,text=text,summary=summary)
            return False
        else:
            logger.info(f"Skip Create [[{title}]].")
            return True
    def deal_flow(self,title,cotmoderationState,cotreason="标记"):
        PARAMS = {
            "action": "flow",
            "page": str(title),
            "submodule":"lock-topic", 
            "cotmoderationState":cotmoderationState,
            "cotreason":cotreason,
            "format": "json",
            "token":self.fetch_token(type="csrf")
        }
        act = self.S.post(url=self.api, data=PARAMS, headers=self.headers).json()
        logger.info(f"{cotmoderationState} the flow {title} successfully.({cotreason})")
    def reply_flow(self,title,content):
        PARAMS = {
            "action": "flow",
            "submodule":"reply",
            "page":title,
            "repreplyTo": str(title),
            "repcontent":str(content),
            "repformat":"wikitext",
            "format": "json",
            "token":self.fetch_token(type="csrf")
        }
        act = self.S.post(url=self.api, data=PARAMS, headers=self.headers).json()
        logger.info(f"Reply the flow {title} successfully.")
    def rc(self,namespace):
        ...