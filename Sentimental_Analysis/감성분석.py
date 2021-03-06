# -*- coding: utf-8 -*-
"""대응분석과 토픽모델링을 이용한 계층적 감성분석

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LLAFw6Lz2qqxyokf9RRUx8h4Af8eQ-M7

#총선 기사 감성분석
"""

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
dict_0 = pd.read_excel('/content/drive/MyDrive/감성분석_Input_Bing사전.xlsx')
dict_0.head()

#감성 사전 품사 추출하기
from konlpy.tag import * # class  
komoran=Komoran()
index=[]
words=[]
score=[]
text_1=[]
for j in range(0,len(dict_0)):
    ex_pos=komoran.pos(dict_0.iloc[j,0])
    for (text, tclass) in ex_pos : # ('형태소', 'NNG') 
        if tclass == 'VV' or tclass == 'VA' or tclass == 'NNG' or tclass=='XPN' or tclass == 'NNP'or tclass=='VX' or tclass == 'VCP' or tclass == 'VCN' or tclass == 'MAG' or tclass == 'XR': 
            index+=[j]
            words+=[dict_0.iloc[j,0]]
            score+=[dict_0.iloc[j,1]]
            text_1.append(text)
dict_1=pd.DataFrame({'Index':index,'Text':text_1,'Words':words,'Score':score})

#총선 기사 품사 추출하기
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
article_0 = pd.read_excel('/content/drive/MyDrive/감성분석_Input_총선기사.xlsx')

import re
index=[]
paper=[]
text_1=[]
text_2=[]
title=[]
for i in range(0,len(article_0)):
  article_0.iloc[i,0]=re.sub('\n|\r','',article_0.iloc[i,0]) #문장에서 필요없는 문구 삭제
  ex_pos=komoran.pos(article_0.iloc[i,0]) #komoran 품사 태그 적용
  for (text, tclass) in ex_pos : # ('형태소', 'NNG') 
      if tclass == 'VV' or tclass == 'VA' or tclass == 'NNG' or tclass == 'NNP'or tclass=='XPN' or tclass=='VX' or tclass == 'VCP' or tclass == 'VCN' or tclass == 'MAG' or tclass == 'XR': 
          index+=[i]
          paper+=[article_0.iloc[i,3]]
          text_1+=[article_0.iloc[i,0]]
          text_2.append(text)
          title+=[article_0.iloc[i,4]]
article_1=pd.DataFrame({'Index':index,'Text':text_2,'Article':text_1,'Paper':paper,'Title':title})

#감성점수 매기기
article_1.loc[:,'Score']=[0]*len(article_1)
dict_list=list(dict_1.loc[:,'Text'])
article_list=list(article_1.loc[:,'Text'])
for i in range(len(dict_list)):
  equal_list = list(filter(lambda x: (article_list[x]==dict_list[i]) and (len(article_list[x])>=2), range(len(article_list))))
  for j in equal_list:
    article_1.loc[j,'Score']=dict_1.loc[i,'Score']

article_0['Score']=article_1['Score'].groupby(article_1['Index']).sum()
article_0.to_csv('감성분석_Result_총선기사.csv',index=False)

"""#개천절집회 기사 감성분석"""

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
dict_0 = pd.read_excel('/content/drive/MyDrive/감성분석_Input_Bing사전.xlsx')
dict_0.head()

#감성 사전 품사 추출하기
from konlpy.tag import * # class  
komoran=Komoran()
index=[]
words=[]
score=[]
text_1=[]
for j in range(0,len(dict_0)):
    ex_pos=komoran.pos(dict_0.iloc[j,0])
    for (text, tclass) in ex_pos : # ('형태소', 'NNG') 
        if tclass == 'VV' or tclass == 'VA' or tclass == 'NNG' or tclass=='XPN' or tclass == 'NNP'or tclass=='VX' or tclass == 'VCP' or tclass == 'VCN' or tclass == 'MAG' or tclass == 'XR': 
            index+=[j]
            words+=[dict_0.iloc[j,0]]
            score+=[dict_0.iloc[j,1]]
            text_1.append(text)
dict_1=pd.DataFrame({'Index':index,'Text':text_1,'Words':words,'Score':score})

dict_1
#개천절집회 기사 품사 추출하기
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
article_0 = pd.read_excel('/content/drive/MyDrive/감성분석_Input_개천절집회기사.xlsx')
article_0.head()

import re
index=[]
paper=[]
text_1=[]
text_2=[]
title=[]
for i in range(0,len(article_0)):
  article_0.iloc[i,0]=re.sub('\n|\r','',article_0.iloc[i,0]) #문장에서 필요없는 문구 삭제
  ex_pos=komoran.pos(article_0.iloc[i,0]) #komoran 품사 태그 적용
  for (text, tclass) in ex_pos : # ('형태소', 'NNG') 
      if tclass == 'VV' or tclass == 'VA' or tclass == 'NNG' or tclass == 'NNP'or tclass=='XPN' or tclass=='VX' or tclass == 'VCP' or tclass == 'VCN' or tclass == 'MAG' or tclass == 'XR': 
          index+=[i]
          paper+=[article_0.iloc[i,3]]
          text_1+=[article_0.iloc[i,0]]
          text_2.append(text)
          title+=[article_0.iloc[i,4]]
article_1=pd.DataFrame({'Index':index,'Text':text_2,'Article':text_1,'Paper':paper,'Title':title})

article_1
#감성점수 매기기
article_1.loc[:,'Score']=[0]*len(article_1)
dict_list=list(dict_1.loc[:,'Text'])
article_list=list(article_1.loc[:,'Text'])
for i in range(len(dict_list)):
  equal_list = list(filter(lambda x: (article_list[x]==dict_list[i]) and (len(article_list[x])>=2), range(len(article_list))))
  for j in equal_list:
    article_1.loc[j,'Score']=dict_1.loc[i,'Score']

article_0['Score']=article_1['Score'].groupby(article_1['Index']).sum()
article_0.to_csv('개천절집회_감성분석_졸업논문.csv',index=False)

"""#방역 기사 감성분석"""

#필요한 패키지 설치
!apt-get update 
!apt-get install g++ openjdk-8-jdk python-dev python3-dev 
!pip3 install JPype1-py3 
!pip3 install konlpy 
!JAVA_HOME="C:\Users\tyumi\Downloads"

from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
dict_0 = pd.read_excel('/content/drive/MyDrive/감성분석_Input_Bing사전.xlsx')
dict_0.head()

#감성 사전 품사 추출하기
from konlpy.tag import * # class  
komoran=Komoran()
index=[]
words=[]
score=[]
text_1=[]
for j in range(0,len(dict_0)):
    ex_pos=komoran.pos(dict_0.iloc[j,0])
    for (text, tclass) in ex_pos : # ('형태소', 'NNG') 
        if tclass == 'VV' or tclass == 'VA' or tclass == 'NNG' or tclass=='XPN' or tclass == 'NNP'or tclass=='VX' or tclass == 'VCP' or tclass == 'VCN' or tclass == 'MAG' or tclass == 'XR': 
            index+=[j]
            words+=[dict_0.iloc[j,0]]
            score+=[dict_0.iloc[j,1]]
            text_1.append(text)
dict_1=pd.DataFrame({'Index':index,'Text':text_1,'Words':words,'Score':score})

dict_1

#방역기사 품사 추출하기
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
article_0 = pd.read_excel('/content/drive/MyDrive/감성분석_Input_방역기사.xlsx')
article_0.head()

import re
index=[]
paper=[]
text_1=[]
text_2=[]
title=[]
for i in range(0,len(article_0)):
  article_0.iloc[i,0]=re.sub('\n|\r','',article_0.iloc[i,0]) #문장에서 필요없는 문구 삭제
  ex_pos=komoran.pos(article_0.iloc[i,0]) #komoran 품사 태그 적용
  for (text, tclass) in ex_pos : # ('형태소', 'NNG') 
      if tclass == 'VV' or tclass == 'VA' or tclass == 'NNG' or tclass == 'NNP'or tclass=='XPN' or tclass=='VX' or tclass == 'VCP' or tclass == 'VCN' or tclass == 'MAG' or tclass == 'XR': 
          index+=[i]
          paper+=[article_0.iloc[i,3]]
          text_1+=[article_0.iloc[i,0]]
          text_2.append(text)
          title+=[article_0.iloc[i,4]]
article_1=pd.DataFrame({'Index':index,'Text':text_2,'Article':text_1,'Paper':paper,'Title':title})

article_1

#감성점수 매기기
article_1.loc[:,'Score']=[0]*len(article_1)
dict_list=list(dict_1.loc[:,'Text'])
article_list=list(article_1.loc[:,'Text'])
for i in range(len(dict_list)):
  equal_list = list(filter(lambda x: (article_list[x]==dict_list[i]) and (len(article_list[x])>=2), range(len(article_list))))
  for j in equal_list:
    article_1.loc[j,'Score']=dict_1.loc[i,'Score']

article_0['Score']=article_1['Score'].groupby(article_1['Index']).sum()
article_0.to_csv('감성분석_Result_방역기사.csv',index=False)
