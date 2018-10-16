Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> from urllib.request import Request, urlopen
>>> link = Request('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',headers={'User-Agent': 'Mozilla/5.0'})
pagina = urlopen(link).read().decode('utf-8', 'ignore')
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> from urllib.request import Request, urlopen

link = Request('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',
               headers={'User-Agent': 'Mozilla/5.0'})
pagina = urlopen(link).read().decode('utf-8', 'ignore')

from bs4 import BeautifulSoup

soup = BeautifulSoup(pagina, "lxml")
texto = soup.find(id="noticia").text

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentencas = sent_tokenize(texto)
palavras = word_tokenize(texto.lower())

from nltk.corpus import stopwords
from string import punctuation

stopwords = set(stopwords.words('portuguese') + list(punctuation))
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

from nltk.probability import FreqDist

frequencia = FreqDist(palavras_sem_stopwords)

from collections import defaultdict

sentencas_importantes = defaultdict(int)

for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

from heapq import nlargest

idx_sentencas_importantes = nlargest(4, sentencas_importantes, sentencas_importantes.get)

for i in sorted(idx_sentencas_importantes):
    print(sentencas[i])
    
SyntaxError: multiple statements found while compiling a single statement
>>> import urllib as urlib
>>> 
=============================== RESTART: Shell ===============================
>>> import urllib as urllib
>>> urllib.request import Request, urlopen
SyntaxError: invalid syntax
>>> from urllib.request import Request, urlopen
>>> link = Rquest('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',headers={'User-Agent' :'Google Chrome/67'})
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    link = Rquest('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',headers={'User-Agent' :'Google Chrome/67'})
NameError: name 'Rquest' is not defined
>>> link = Request('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',headers={'User-Agent' :'Google Chrome/67'})
>>> pagina = urlopen(link) .read() .decode('utf-8', 'ignore')
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup (pagina, "lxml")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    soup = BeautifulSoup (pagina, "lxml")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
>>> yes
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    yes
NameError: name 'yes' is not defined
>>> soup = BeautifulSoup(pagina, "lmxl")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    soup = BeautifulSoup(pagina, "lmxl")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lmxl. Do you need to install a parser library?
>>> soup = BeautifulSoup(pagina, 'lxml')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    soup = BeautifulSoup(pagina, 'lxml')
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
>>> soup = BeautifulSoup(pagina)

Warning (from warnings module):
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "html.parser")

>>> soup = BeautifulSoup
>>> texto = soup.find(id="noticia").text
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    texto = soup.find(id="noticia").text
TypeError: find() missing 1 required positional argument: 'self'
>>> soup = BeautifulSoup (pagina,"lxml")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    soup = BeautifulSoup (pagina,"lxml")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
>>> soup = BeautifulSoup (pagina,"lxml")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    soup = BeautifulSoup (pagina,"lxml")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
>>> soup = BeautifulSoup (pagina,"xml")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    soup = BeautifulSoup (pagina,"xml")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: xml. Do you need to install a parser library?
>>> import parser
>>> soup = BeautifulSoup (pagina,"lxml")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    soup = BeautifulSoup (pagina,"lxml")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
>>> import lxml
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import lxml
ModuleNotFoundError: No module named 'lxml'
>>> soup = BeautifulSoup (pagina,"lxml")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    soup = BeautifulSoup (pagina,"lxml")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
>>> soup = BeautifulSoup (pagina,"lxml")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    soup = BeautifulSoup (pagina,"lxml")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
>>> soup = BeautifulSoup(pagina, "html5lib")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    soup = BeautifulSoup(pagina, "html5lib")
  File "C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\site-packages\bs4\__init__.py", line 165, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html5lib. Do you need to install a parser library?
>>> soup = BeautifulSoup(pagina, "html.parser")
>>> texto = soup.find(id="noticia").text
>>> from nltk.tokenize import word_tokenize
>>> from nltk.tokenize import sent_tokenize
>>> sentencas = sent_tokenize(texto)
>>> palavras = word_tokenize(texto.lower())
>>> from nltk.corpus import stopwords
>>> from string import punctuation
>>> stopwords = set(stopwords.words('portuguese') + list(punctuation))palavras_sem_stopwords = [palavra for palavra if palavra not in stopwords]
SyntaxError: invalid syntax
>>> stopwords = set(stopwords.words('portuguese') + list(punctuation))
>>> palavras_sem_stopwords = [palavra for palavra if palavra not in stopwords]
SyntaxError: invalid syntax
>>> palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]
>>> from nltk.probability import FreqDist
>>> frequencia = FreqDist(palavras_sem_stopwords)
>>> from collections import defaultdict
>>> sentencas_importantes = defaultdict(int)
>>> for i, sentenca in enumerate(sentencas):
	for palavra in word_tokenize(sentenca.lower()):
		if palavra in frequencia:
			sentenca_importantes[i] += frequencia [palavra]

			
Traceback (most recent call last):
  File "<pyshell#50>", line 4, in <module>
    sentenca_importantes[i] += frequencia [palavra]
NameError: name 'sentenca_importantes' is not defined
>>> for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]

            
>>> from heapq import nlargerst
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    from heapq import nlargerst
ImportError: cannot import name 'nlargerst' from 'heapq' (C:\Users\Wesley Calazans\AppData\Local\Programs\Python\Python37-32\lib\heapq.py)
>>> from heapq import nlargest
>>> idx_sentencas_importantes = nlargest(4, sentencas_importantes,sentencas_importantes.get)
>>> for i in sorted(idx_sentencas_importantes):
	print(sentencas[i])

	

 


 Lúcio Bernardo Junior/Câmara dos Deputados - 19.4.17
Deputados discutem na Comissão da Reforma da Previdência; com gravata roxa, o presidente do colegiado, Carlos Marun


A comissão especial que analisa a proposta de reforma da Previdência na Câmara dos Deputados inicia na tarde desta terça-feira (25) a discussão do                   relatório apresentado na semana passada pelo relator
, deputado Arthur Maia (PPS-BA).
Depois de fechar acordo com parlamentares da oposição, que tentavam obstruir a sessão de leitura do parecer do relator, o presidente da comissão da                   reforma da Previdência
, deputado Carlos Marun (PMDB-MS), designou que todas as reuniões desta semana sejam para discutir o relatório e apresentar pedido de vista.
O relatório de Arthur Maia fixa a idade mínima de aposentadoria em 62 anos para as mulheres e em 65 anos para os homens após um período de transição de 20 anos.
Para se tornar lei, a proposta de reforma da Previdência precisa, após ser aprovada na comissão especial, também passar por votação em dois turnos no plenário da Câmara e depois receber o aval do Senado.
>>> 
