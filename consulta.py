import rdflib
g= rdflib.Graph()
#result= g.parse('http://dbpedia.org/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2FSteve_Jobs')
var= input("Ingrese lo que se desee saber: ")
var=var.title()
var= var.replace(" ","_")
link= 'http://dbpedia.org/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2F'+var
print(link)
result= g.parse(str(link))
#print("Grafo dice : ", len(resp))

#result = g.parse('http://dbpedia.org/describe/?url=http%3A%2F%2Fdbpedia.org%2Fresource%2FAlbert_Einstein&distinct=1&p=1&sid=104977&lp=38&op=-1&next=&gp=1')
print("Graph URIs : ",len(result))

print(g.serialize(format="turtle"))



