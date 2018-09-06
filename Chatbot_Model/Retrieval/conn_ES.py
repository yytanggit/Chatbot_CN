# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     conn_ES.py
   Description :   py连接es
   Author :       charl
   date：          2018/9/4
-------------------------------------------------
   Change Activity: 2018/9/4:
-------------------------------------------------
"""

import sys
import json

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host':'test.npacn.com', 'port':9200}])

# 创建索引
es.indices.create(index='zhizhuxia')

# 插入数据
es.index(index='zhizhuxia', doc_type='test_type', id='01', body={'any': '张三是一个好人', 'timestamp': datetime.now()})

# 查询数据 get 和 search 两种方式
res = es.get(index='zhizhuxia', doc_type='test_type', id='01')
print(res)
print(res['_source'])

