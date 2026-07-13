ld=[
    {
        "eid":1,
        "ename":"martin",
        "salary":12300,
        "skills":["java","python"]
    },
    {
        "eid":2,
        "ename":"jack",
        "salary":25000,
        "skills":["SAP","python","selenium"]
    },
    {
        "eid":3,
        "ename":"sean",
        "salary":75000,
        "skills":["tableau","python","PowerBi"]
    },
    {
        "eid":1,
        "ename":"james",
        "salary":60000,
        "skills":["js","python"]
    }
]

for d in ld:
    if d["salary"] > 53000:
        d["skills"].append("gen ai")
        print(d["skills"])

# if "SAP" in d["skills"]:
#     d["salary"] += 5000
# print(ld)

# if d["salary"] < 75000 and d["salary"] > 60000:
#     print(d["ename"])
