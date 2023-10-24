# -*-coding:GBK -*-
from kafka import KafkaConsumer
import json
# import pymysql
# import time

# topic_name = 'tc_radar_event'
# topic_name = 'bigdata_event'
# topic_name = "ms_strategy_sync"
# topic_name = "ms_access_relation"
# topic_name = "headquarters-change-stream"
topic_name = "youguang_test"

consumer = KafkaConsumer(topic_name,
                         group_id='test',                   # 同名组多个消费者消费同一个topic
                         # enable_auto_commit=True,
                         # auto_commit_interval_ms=2,
                         sasl_mechanism="PLAIN",
                         security_protocol='SASL_PLAINTEXT',
                         sasl_plain_username="qingteng",
                         sasl_plain_password="zfCjJKQrro2lPJqn",
                         # bootstrap_servers=['172.16.13.30:9092'],
                         bootstrap_servers=['10.106.110.78:9092'],
                         auto_offset_reset="latest"
                         )

# conn = pymysql.connect(host="172.16.4.81", user="root", password="Qingteng@qt2019", database="kafka", charset="utf8")

import chardet


for msg in consumer:
    result = json.loads(msg.value.decode("utf8"))
    print(result)
    # print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value.decode("utf8")))
    # print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))
    # comId = result["comid"]
    # agent_id = result["agent_id"]
    # if comId == "696448443735544c4d67":
    #     print(result)
    #     print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value.decode("utf8")))






