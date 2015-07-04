__author__ = 'daniel'
import glob
import yaml
import os
import redis
import json
from datetime import datetime
import time

relk = redis.StrictRedis(host='192.168.59.103', port=6379, db=0)

for in_file in glob.glob("data/hist/*.yml"):
    print in_file
    with open(in_file, 'r') as stream:
        result = yaml.load(stream)
        values = result['ClientCurveRet']['PointList']['CurvePointClient']
        #print(values)

        report = {'fid': os.path.basename(in_file).split('.')[0]}
        report['name'] = result['ClientCurveRet']['CurveTitle']
        for value in values:
            report['value'] = float(value['Value'])
            try:
                report['date'] = datetime.strptime(value['Date'], '%Y-%m-%d').isoformat()
            except:
                print value
                next

            relk.rpush('logstash', json.dumps(report))
            print report

