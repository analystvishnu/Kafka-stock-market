#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem


# In[ ]:


consumer = KafkaConsumer(
                        'demo_test',
                        bootstrap_servers = ['54.179.175.167:9092'],
                        value_deserializer = lambda x:
                        loads(x.decode('utf-8'))
                        )


# In[ ]:


s3 = S3FileSystem()


# In[ ]:


for count,i in enumerate(consumer):
    with s3.open("s3://kafka-vis-demo/stock_market_{}.json".format(count),'w') as file:
        json.dump(i.value, file)

