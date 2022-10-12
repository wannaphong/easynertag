# -*- coding: utf-8 -*-
from typing import List
from nltk.tokenize import RegexpTokenizer
import re


def white_space_split(text: str)->List[str]:
    return text.split(" ")


class Engine:
    def __init__(self,word_tokenize=white_space_split,pos_tag=None) -> None:
        """
        word_tokenize: function for do word tokenize (default is white_space_split)
        pos_tag: function for do part of speech tagging
        """
        self.pattern = r'\[(.*?)\](.*?)\[\/(.*?)\]'
        self.tokenizer = RegexpTokenizer(self.pattern) # [TIME]8.00[/TIME] -> ('TIME','ไง','TIME')
        self.word_tokenize = word_tokenize
        self.pos_tag = pos_tag

    def _toolner_to_tag(self, text:str)->str:
        text=re.sub("<[^>]*>","",text)
        text=re.sub("(\[\/(.*?)\])","\\1***",text) # for processing non-tag
        text=re.sub("(\[\w+\])","***\\1",text)
        text2=[]
        for i in text.split('***'):
            if "[" in i:
                text2.append(i)
            else:
                text2.append("[word]"+i+"[/word]")
        text="".join(text2)
        return text.replace("[word][/word]","")

    def _pos_tag(self,text:str,output:str="str")->str:
        listtxt=[i for i in text.split('\n') if i!='']
        list_word=[]
        for data in listtxt:
            list_word.append(data.split('\t')[0])
        list_word=self.pos_tag(list_word)
        _text=[]
        i=0
        for data in listtxt:
            _text.append(data.split('\t')[0]+'\t'+list_word[i][1]+'\t'+data.split('\t')[1])
            i+=1
        if output=="list":
            return _text
        return '\n'.join(_text)

    def text2conll2002(self, text:str,pos=False)->str:
        """
        make the dataset
        """
        text=self._toolner_to_tag(text)
        text=text.replace("''",'"')
        text=text.replace("’",'"').replace("‘",'"')#.replace('"',"")
        tag=self.tokenizer.tokenize(text)
        j=0
        conll2002=""
        for tagopen,text,tagclose in tag:
            word_cut=self.word_tokenize(text)
            i=0
            txt5=""
            while i<len(word_cut):
                if word_cut[i]=="''" or word_cut[i]=='"':pass
                elif i==0 and tagopen!='word':
                    txt5+=word_cut[i]
                    txt5+='\t'+'B-'+tagopen
                elif tagopen!='word':
                    txt5+=word_cut[i]
                    txt5+='\t'+'I-'+tagopen
                else:
                    txt5+=word_cut[i]
                    txt5+='\t'+'O'
                txt5+='\n'
                i+=1
            conll2002+=txt5
        if pos==False:
            return conll2002
        return self._pos_tag(conll2002)
