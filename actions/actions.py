# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

#----------------------------------------------------------------------------------
from html import entities
import rdflib
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities= tracker.latest_message['entities']
        print(entities)
        print("Entitie Es un =", type(entities))
        print("el primer elemto es: "," y tipo ",(entities[0], type(entities[0])))
        print("imprimiento value ", entities[0]['value'])

        
        dispatcher.utter_message(text="Escribe tu pregunta:")

        return []

class ActionConsulta(Action):

    def name(self) -> Text:
        return "action_consulta"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities= tracker.latest_message['entities']
        var = str(entities[0]['value'])
        var=var.title()
        var= var.replace(" ","_") 
        print("URI's:")
        g= rdflib.Graph()        
        #result= g.parse('http://dbpedia.org/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2FSteve_Jobs')
                 
        link= 'http://dbpedia.org/describe/?uri=http%3A%2F%2Fdbpedia.org%2Fresource%2F'+var
        print(link)
        result= g.parse(str(link))
        
        print("Graph URIs : ",len(result))

        print(g.serialize(format="turtle"))
        from rdflib.namespace import RDF, RDFS, FOAF
        for person in g.subjects(RDF.type, FOAF.Person):
            for ent in g.objects(person, RDFS.label):
                if(ent.language == "es"):
                    print(ent)

        db = rdflib.Namespace('http://dbpedia.org/ontology/')
        for person in g.subjects(RDF.type, FOAF.Person):
            for ent in g.objects(person, db['abstract']):
                if(ent.language == "es"):
                    print(ent)   
                    dispatcher.utter_message(text="RESPUESTA \n"+str(ent))         

        #dispatcher.utter_message(text="RESPUESTA \n"+ent)

        return []



class ActionDefinicion(Action):

    def name(self) -> Text:
        return "action_definicion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        #Lista de dicionarios con entidades
        entities= tracker.latest_message['entities']
        print(entities)
        print("Entitie Es un =", type(entities))
        print("el primer elemto es: "," y tipo ",(entities[0], type(entities[0])))
        print("imprimiento value ", entities[0]['value'])

        
        dispatcher.utter_message(text="Escribe tu pregunta:")

        return []