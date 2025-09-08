nomes = ["joaquim", "maria" , "ana"]
print("lista inicial:",nomes)

nomes.append("carlos")
print("apos append:",nomes)

nomes.insert(1,"fernanda")
print("apos insert:",nomes)

nomes[2]= "paulo"
print ("apos a modificaçao",nomes)

del nomes[3]
nomes.remove("fernanda")
print("apos remove:",nomes)

removido=nomes.pop(2)
print(f"apos pop (removido ' {removido}')",nomes)

nomes.clear()
print("apos clear:",nomes)