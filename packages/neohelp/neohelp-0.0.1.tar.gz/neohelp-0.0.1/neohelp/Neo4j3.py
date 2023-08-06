print("1")
"""
*Library-->
a) List all readers who have recommended either book “…” or “……..” or “……..”
MATCH (a:Reader)-[r:RECOMMENDED]->(b:Book)
WHERE b.title="Tinker Tailor Soldier Spy" or b.title="Our Man in Havana"
RETURN a



 b) List the readers who haven’t recommended any book 

match (a:Reader) where not (a:Reader)-[:RECOMMENDED]->(:Book) return a



c) List the authors who have written a book that has been read / issued by maximum number of readers.

MATCH (b:Book)-[r:ISSUED_BY]->(a:Reader)
RETURN b.title,COUNT(b)

MATCH (b:Book)-[r:ISSUED_BY]->(a:Reader)
where max(count(b))
RETURN b.title, COUNT(b)


d) List the names of books recommended by “……….” And read by at least one reader

MATCH (a:Reader{name:"Lan"})-[r:RECOMMENDED]->(b:Book)
WHERE count(r)>0
RETURN b


MATCH (a:Reader{name:"Lan" })-[r:RECOMMENDED]->(b:Book)-[rr:ISSUED_BY]->(rd:Reader)
RETURN a,r,rd,rr,b



e) List the names of books recommended by “………” and read by maximum number of readers. 





f) List the names of publishers who haven’t published any books written by authors from Pune and Mumbai.



g) List the names of voracious readers in our library 
[Voracious means the reader who haven't issued any book]

MATCH (a:Reader)
WHERE NOT (:Book)-[:ISSUED_BY]->(a:Reader)
RETURN a.name


*Employee-->
a) List the name of employees in department" IT".
-->


match (e:Employee)-[:Works_in]->(:Department{Name:"IT"})  
return  e.Name


b) List the projects controlled by a department “IT.”  and have employees of the 
same department working in it. 
--->
match  (d:Department{Name:'IT'})<-[:Controlled_by]-(p:Projects)<-[:Assigned_to]-(e:Employee),
(e:Employee)-[:Works_in]->(d:Department)
return d,p,e


c) List the names of the projects belonging to departments managed by employee “…….” 
--->

match (e:Employee{Name:'Harry'})-[:Project_manager]->(p:Projects)-[:Controlled_by]->(d:Department)
return e,p,d

d)List the names of employees having the same skills as employee “………..” 
--->
match(e:Employee{Name:'Harry'})--(s:Skillset)--(ee:Employee) return ee,s
"""