from burp import IBurpExtender
from burp import IContextMenuFactory

from javax.swing import JMenuItem
from java,util import List,ArrayList
from java.net import URL

import re
from datetime import datetime
from HTMLParser import HTMLParser

class TagStripper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.page_text=[]

    def handle_data(self, data):
        self.page_text.append(data)

    def handle_comment(self,data):
        delf.hander_data(data)
        return ''.join(self.page_text)
    def strip(self,html):
        self.feed(html)
        return ''.join(self.page_text)

class BurpExtender(IBurpExtender,IContextMenuFactory):
    def registerExtenderCallbacks(self,callbacks):
        self._callbacks=callbacks
        self._helpers=callbacks.getHelpers()
        self.context=None
        self.hosts=set()
        self.wordlist=set(['password'])
        callbacks.setExtensionName('BHP Wordlist')
        callbacks.registrContextMenuFactory(self)
        return

    def createMenuItems(self,contexte_menu):
        self.context=contexte_menu
        menu_list=ArrayList()
        menu_list.add(JMenuItem('create Wordlist',actionPerformed=self.wordlist_menu))
        return menu_list
