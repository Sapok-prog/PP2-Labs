import json 

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print(80*"=")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for i in range(3):
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"], "                            ", data["imdata"][i]["l1PhysIf"]["attributes"]["fecMode"], " ", data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])