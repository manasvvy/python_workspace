

dl={"eid":[2,4,11,48],
    "enames":["amy","baby","caby","dabby"],
    "salary":[90000,12000,24000,54000],
    "dept":["hr","sales","development","testing"],
    "skills":["mba","comms","cs","selenium"]
    }

#print(dl.keys())
for key,values in dl.items(): #for l in dl:
    print(values[0])          #print([l][0])

print("---------------------------------")    

'''for key,values in dl.items():
    if key=="skills":  #diff solutions try
        print(values[2])'''

for i in range(len(dl["enames"])):
    if "caby"==dl["enames"][i]:
        print(dl["skills"][i])

# dl["skills"][dl["enames"].index("caby")]
