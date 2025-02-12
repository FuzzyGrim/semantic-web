# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k3Il-_ncwo7BuK8zxfjL6bGFfenyRTRS

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

from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDFS

ns = Namespace("http://somewhere#")
#With rdflib:

for s, p, o in g.triples((None, RDFS.subClassOf, ns.LivingThing)):
    print(s)

#with sparql:
q1 = prepareQuery('''
  SELECT ?subclass WHERE {
    ?subclass rdfs:subClassOf ns:LivingThing.
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": ns }
)

for r in g.query(q1):
  print(r)  #r.subclass would be more legible

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

from rdflib.namespace import RDF

#With rdflib:

subclasses_of_person = set()  #we create a set that saves all types: person + subclasses
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    subclasses_of_person.add(s)

subclasses_of_person.add(ns.Person) #we finally add person

for subclass in subclasses_of_person:
    for s, p, o in g.triples((None, RDF.type, subclass)):
        print(s)

#With sparql:

q2 = prepareQuery('''
  SELECT ?individual WHERE {
    {
      ?individual rdf:type ns:Person.
    }
    UNION
    {
      ?subclass rdfs:subClassOf ns:Person.
      ?individual rdf:type ?subclass.
    }
  }
  ''',
  initNs = { "rdf": RDF, "rdfs": RDFS, "ns": ns }
)

for r in g.query(q2):
  print(r)
#We see Persons + Researchers + Professors (which are persons too)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

q3 = prepareQuery('''
  SELECT ?individual WHERE {
    { ?individual rdf:type ns:Person }
    UNION
    { ?individual rdf:type ns:Animal }
  }
  ''',
  initNs = { "rdf": RDF, "ns": ns }
)

for r in g.query(q3):
    print(r.individual)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

from rdflib.namespace import FOAF
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

q4 = prepareQuery('''
  SELECT ?name WHERE {
    {
      ?individual rdf:type ns:Person.
      ?individual foaf:knows ns:RockySmith.
      ?individual vcard:Given ?name.
    }
    UNION
    {
      ?subclass rdfs:subClassOf ns:Person.
      ?individual rdf:type ?subclass.
      ?individual foaf:knows ns:RockySmith.
      ?individual vcard:Given ?name.
    }
  }
''',
initNs = { "rdf": RDF, "rdfs": RDFS, "vcard": VCARD, "ns": ns }
)

for r in g.query(q4):
    print(r.name)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

q5 = prepareQuery('''
  SELECT ?name WHERE {
    {
      ?animal rdf:type ns:Animal.
      ?animal foaf:knows ?otherAnimal.
      ?otherAnimal rdf:type ns:Animal.
      ?animal vcard:Given ?name
    }
  }
''',
initNs = { "rdf": RDF, "foaf": FOAF, "vcard": VCARD, "ns": ns }
)

# Ejecutar la consulta y visualizar los resultados
for r in g.query(q5):
    print(r.name)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

q6 = prepareQuery('''
  SELECT ?age ?name WHERE {
    {
      ?subclass rdfs:subClassOf ns:LivingThing.
      #this includes person and animal
      ?individual rdf:type ?subclass.
      ?individual foaf:age ?age.
      ?individual vcard:Given ?name.
    }
        UNION
    {
      ?subclass rdfs:subClassOf ns:Person.
      #this includes subclasses of person
      ?individual rdf:type ?subclass.
      ?individual foaf:age ?age.
      ?individual vcard:Given ?name.
    }
  }
  ORDER BY DESC(?age)
''',
initNs = { "rdf": RDF, "rdfs": RDFS, "foaf": FOAF, "vcard": VCARD, "ns": ns }
)

for r in g.query(q6):
    print(r.name, r.age)