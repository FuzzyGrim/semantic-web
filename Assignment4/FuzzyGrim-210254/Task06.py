# **Task 06: Modifying RDF(s)**
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind("ns", Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind(
    "vcard", Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False
)
g.parse(github_storage + "/rdf/example5.rdf", format="xml")

# Create a new class named Researcher
ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
    print(s, p, o)

# **TASK 6.1: Create a new class named "University"**
g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

# **TASK 6.2: Add "Researcher" as a subclass of "Person"**
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

# **TASK 6.3: Create a new individual of Researcher named "Jane Smithers"**
g.add((ns.JaneSmithers, RDF.type, ns.Researcher))
# Visualize the results
for s, p, o in g:
    print(s, p, o)

# **TASK 6.4: Add to the individual JaneSmithers the email address, fullName, given and family names. Use the https://schema.org vocabulary**
schema = Namespace("https://schema.org/")
g.add((ns.JaneSmithers, schema.email, Literal("jane.smithers@example.com")))
g.add((ns.JaneSmithers, schema.fullName, Literal("Jane Smithers")))
g.add((ns.JaneSmithers, schema.givenName, Literal("Jane")))
g.add((ns.JaneSmithers, schema.familyName, Literal("Smithers")))

# Visualize the results
for s, p, o in g:
    print(s, p, o)

# **TASK 6.5: Add UPM as the university where John Smith works. Use the "https://example.org/ namespace**
ex = Namespace("https://example.org/")
g.add((ns.JohnSmith, ex.worksAt, ns.UPM))
g.add((ns.UPM, RDF.type, ns.University))

# Visualize the results
for s, p, o in g:
    print(s, p, o)

# **Task 6.6: Add that Jown knows Jane using the FOAF vocabulary. Make sure the relationship exists.**
from rdflib.namespace import FOAF
g.add((ns.JohnSmith, FOAF.knows, ns.JaneSmithers))

# Visualize the results
for s, p, o in g:
    print(s, p, o)
