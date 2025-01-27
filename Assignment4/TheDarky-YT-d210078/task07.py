# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mwjET73SYotcWOeJLGs_FZmjj_7Tj76h

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

q1 = """
SELECT ?Subject WHERE {
  ?Subject rdfs:subClassOf ns:LivingThing
}
"""

for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

q2 = """
SELECT ?Subject WHERE {
  ?Subject rdf:type ?a .
  ?a rdfs:subClassOf* ns:Person
}
"""

for r in g.query(q2):
  print(r)

"""**TASK 7.3: List all individuals of just "Person" or "Animal". You do not need to list the individuals of the subclasses of person (in SPARQL only)**

"""

q3 = """
SELECT ?Subject WHERE {
  { ?Subject rdf:type ns:Person } UNION { ?Subject rdf:type ns:Animal }
}
"""

for r in g.query(q3):
  print(r)

"""**TASK 7.4:  List the name of the persons who know Rocky (in SPARQL only)**"""

q4 = """
SELECT ?name WHERE {
  ?p ns:knows ns:RockySmith.
  ?p vcard:FN ?name
}
"""

for r in g.query(q4):
  print(r)

"""**Task 7.5: List the name of those animals who know at least another animal in the graph (in SPARQL only)**"""

q5 = """
SELECT ?name WHERE {
  ?a rdf:type ns:Animal .
  ?a ns:knows ?otherAnimal .
  ?otherAnimal rdf:type ns:Animal .
  ?a vcard:FN ?name .
  FILTER (?a != ?otherAnimal)
}
"""

for r in g.query(q5):
  print(r)

"""**Task 7.6: List the age of all living things in descending order (in SPARQL only)**"""

q6 = """
SELECT ?age WHERE {
  ?lThing rdf:type ns:LivingThing .
  ?lThing ns:age ?age .
}
ORDER BY DESC(?age)
"""

for r in g.query(q6):
  print(r)