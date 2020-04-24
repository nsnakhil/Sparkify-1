

import json
import glob
import pymongo

#import all .json files from log data into MongoDB.

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["events&songs"]
mycollection = mydb["logs"]


all_events = []
for f in glob.glob("*.json"):
    for line in open(f,'r'):
        all_events.append(json.loads(line))

mycollection.insert_many(all_events)

# Segregating data in terms of 'weeks' 

#week 1
mycollection = mydb["week_1"]

fileslist_1 = ['2018-11-01-events.json','2018-11-02-events.json','2018-11-03-events.json','2018-11-04-events.json']
weekone_events = []
               
for f in fileslist_1:
    for line in open(f,'r'):
        weekone_events.append(json.loads(line))

mycollection.insert_many(weekone_events)

#week2
mycollection = mydb["week_2"]

fileslist_2 = ['2018-11-05-events.json','2018-11-06-events.json','2018-11-07-events.json','2018-11-08-events.json','2018-11-09-events.json','2018-11-10-events.json','2018-11-11-events.json']
weektwo_events = []
               
for f in fileslist_2:
    for line in open(f,'r'):
        weektwo_events.append(json.loads(line))

mycollection.insert_many(weektwo_events)

#week3
mycollection = mydb["week_3"]

fileslist_3 = ['2018-11-12-events.json','2018-11-13-events.json','2018-11-14-events.json','2018-11-15-events.json','2018-11-16-events.json','2018-11-17-events.json','2018-11-18-events.json']
weekthree_events = []
               
for f in fileslist_3:
    for line in open(f,'r'):
        weekthree_events.append(json.loads(line))

mycollection.insert_many(weekthree_events)

#week4
mycollection = mydb["week_4"]

fileslist_4 = ['2018-11-19-events.json','2018-11-20-events.json','2018-11-21-events.json','2018-11-22-events.json','2018-11-23-events.json','2018-11-24-events.json','2018-11-25-events.json']
weekfour_events = []
               
for f in fileslist_4:
    for line in open(f,'r'):
        weekfour_events.append(json.loads(line))

mycollection.insert_many(weekfour_events)

#week 5

mycollection = mydb["week_5"]

fileslist_5 = ['2018-11-26-events.json','2018-11-27-events.json','2018-11-28-events.json','2018-11-29-events.json','2018-11-30-events.json']
weekfive_events = []
               
for f in fileslist_5:
    for line in open(f,'r'):
        weekfive_events.append(json.loads(line))

mycollection.insert_many(weekfive_events)


myclient.close()

