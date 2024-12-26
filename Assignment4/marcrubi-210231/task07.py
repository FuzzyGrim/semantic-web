# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yPniC8cCIRK0ofpUQK_h0bcNOa4CroCF

**Task 07: Querying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""First let's read the RDF file"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "LivingThing" with RDFLib and SPARQL**"""

# TO DO
q1 = """
    SELECT ?subClass WHERE {
        ?subClass rdfs:subClassOf <http://somewhere#LivingThing>
    }
"""
# Visualize the results
for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = """
    SELECT ?individual WHERE {
        ?individual rdf:type/rdfs:subClassOf* <http://somewhere#Person>
    }
"""
# Visualize the results
for r in g.query(q2):
    print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

# TO DO
q3 = """
    SELECT ?individual WHERE {
        { ?individual rdf:type <http://somewhere#Person> }
        UNION
        { ?individual rdf:type <http://somewhere#Animal> }
    }
"""
# Visualize the results
for r in g.query(q3):
    print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

# TO DO
q4 = """
    SELECT ?name WHERE {
        ?person rdf:type <http://somewhere#Person> .
        ?person <http://xmlns.com/foaf/0.1/knows> <http://somewhere#Rocky> .
        ?person <http://www.w3.org/2001/vcard-rdf/3.0#FN> ?name .
    }
"""

# Visualize the results
for r in g.query(q4):
    print(r)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

# TO DO
q5 = """
    SELECT ?animalName WHERE {
        ?animal rdf:type <http://somewhere#Animal> .
        ?animal <http://xmlns.com/foaf/0.1/knows> ?otherAnimal .
        ?otherAnimal rdf:type <http://somewhere#Animal> .
        ?animal <http://www.w3.org/2001/vcard-rdf/3.0#FN> ?animalName .
    }
"""

# Visualize the results
for r in g.query(q5):
    print(r)


"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

# TO DO
q6 = """
    SELECT ?name ?age WHERE {
        ?living rdf:type <http://somewhere#LivingThing> .
        ?living <http://www.w3.org/2001/vcard-rdf/3.0#FN> ?name .
        ?living <http://somewhere#age> ?age .
    }
    ORDER BY DESC(?age)
"""
# Visualize the results
for r in g.query(q6):
    print(r)