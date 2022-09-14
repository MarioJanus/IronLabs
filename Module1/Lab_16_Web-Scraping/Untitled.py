#!/usr/bin/env python
# coding: utf-8

# In[59]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://github.com/trending/developers'
html = requests.get(url).content

soup=BeautifulSoup(html, "lxml")
tags=['text']
soup
text=[element.text for element in soup.find_all(tags)]
print('\n'.join(text))


# In[71]:


import requests
from bs4 import BeautifulSoup
from bs4.element import CData

import pandas as pd

url = 'https://github.com/trending/developers'
html = requests.get(url).content

soup.get_text()


# In[ ]:




