import json
from utils.dictionary import createDictionary
from utils.order import order

#January workouts
with open('files/text/January.txt') as jan_workouts_file:
    
    d = createDictionary(jan_workouts_file)

    with open("files/json/january.json","w") as f:
        json.dump(d,f)

#February workouts
with open('files/text/February.txt') as feb_workouts_file:
    
    d = createDictionary(feb_workouts_file)

    with open("files/json/february.json","w") as f:
        json.dump(d,f)

#March workouts
with open('files/text/March.txt') as mar_workouts_file:
    
    d = createDictionary(mar_workouts_file)

    with open("files/json/march.json","w") as f:
        json.dump(d,f)

#April workouts
with open('files/text/April.txt') as apr_workouts_file:
    
    d = createDictionary(apr_workouts_file)

    with open("files/json/april.json","w") as f:
        json.dump(d,f)

#May workouts
with open('files/text/May.txt') as may_workouts_file:
    
    d = createDictionary(may_workouts_file)

    with open("files/json/may.json","w") as f:
        json.dump(d,f)

#June workouts
with open('files/text/June.txt') as june_workouts_file:
    
    d = createDictionary(june_workouts_file)

    with open("files/json/june.json","w") as f:
        json.dump(d,f) 

#July workouts
with open('files/text/July.txt') as july_workouts_file:
    
    d = createDictionary(july_workouts_file)

    with open("files/json/july.json","w") as f:
        json.dump(d,f)