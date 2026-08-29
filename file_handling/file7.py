import json

with open("file_handling/demo6.txt","w+") as f:
    json_str=json.dumps([10,20,30,40]) #serialisation
    f.write(json_str)
    f.seek(0)
    data=f.read() #reatds and return string
    object=json.loads(data)
    print(object,type(object))