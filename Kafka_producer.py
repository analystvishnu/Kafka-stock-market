#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json


# In[ ]:


producer = KafkaProducer(bootstrap_servers = ['54.179.175.167:9092'],
                        value_serializer = lambda x:
                        dumps(x).encode('utf-8'))


# In[ ]:


df = pd.read_csv('indexProcessed.csv')


# In[ ]:


# df.sample(1).to_dict(orient = "records")

while True:
    dict_stock = df.sample(1).to_dict(orient = "records")[0]
    producer.send('demo_test', value =dict_stock)
    sleep(1)


# In[ ]:


# producer.flush()


# In[ ]:




