print("1")
"""
********************** Assignment 2 *********************

# 1. Library Database : 
a) List all people, who have issued a book “Our Man in Havana”.
-->
MATCH (b:Book)-[r:ISSUED_BY]->(rd:Reader)
WHERE b.title='Our Man in Havana'
RETURN b,r,rd


b) Count the number of people who have read “Tinker Tailor Soldier Spy” .
-->
[Note : Count this query doesn't give output for both conditions Issued_by and 
RECOMMENDED (i.e. both are readers)]

MATCH (a:Reader)-[r:RECOMMENDED]->(b:Book)
WHERE b.title="Tinker Tailor Soldier Spy"
RETURN COUNT(a)

MATCH (a:Reader)-[r:ISSUED_BY]->(b:Book)
WHERE b.title="Our Man in Havana"
RETURN COUNT(a)

c) Add a property “Number of books issued" for "Mr. Clay" and set its value as the count  
-->
[Note: These query is not running.]

MATCH (clay:Reader{name:'Clay'})
SET clay.No_of_Issued=4
RETURN clay



d) List the names of publishers from pune city. 
-->
match(p:Publisher{city:'Pune'})
return p.name


_________________________________________________________________________________________

# 2.Song Database: 
a) List the names of songs written by “:Emiway Bantai” 
-->
Match(s:Song)-[r:WRITTEN_BY]->(a:Song_Author) 
where a.Name='Emiway Bantai' 
return s.Name



b) List the names of record companies who have financed for the song “Kar Gayi Chull” .
-->
Match(rec:Recording_company)-[r:Finances]->(s:Song) 
where s.Name='Kar Gayi Chull' 
return rec,s,r


c) List the names of artist  performing the song “Bohot Hard” .
-->
MATCH (a:Artist)-[r:PERFORMS]->(s:Song)
WHERE s.Name='Bohot Hard'
RETURN a, s,r



d) Name the songs recorded by the studio “ …….” 	
-->

MATCH (s:Song)-[r:RECORDED_IN]->(rec:Recoding_studio)
WHERE rec.Name='Zee Studio'
RETURN s,rec,r




___________________________________________________________________________________________

# 3. Employee Database:

a) List the name of employees in department" IT".
-->
match (e:Employee)-[:Works_in]->(:Department{Name:"IT"})  
return  e.Name


b) List the projects along with their properties, controlled by department “IT” 
-->

match  (d:Department{Name:'IT'})<-[:Controlled_by]-(p:Projects)
return d,p


c) List the departments along with the count of employees in it 
-->

[Note : Not solved yet]
match (:Employee)-[:Works_in]->(d:Department)--((e:Employee))
return d,COUNT(e)



d) List the skillset for an employee “Harry” 
-->
MATCH (e:Employee{Name:"Harry"})-[:Has_acquired]->(s:Skillset)
return s,e
___________________________________________________________________________________________



# 4. Movie Database:
a) Find all actors who have acted in a movie “The Matrix” .
-->
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
where m.title='The Matrix'
return p.name

b) Find all reviewer pairs, one following the other and 
both reviewing the same movie, and return entire subgraphs. 
-->
match (p:Person)-[:REVIEWED]->(m:Movie),  (:Movie)<-[:REVIEWED]-(p) return p.name,m.title

c) Find all actors that acted in a movie together after 2000 
and return the actor names and movie node .
-->
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE m.released>1998
RETURN p.name, m.title

d) Find all movies produced by “ Joel Silver".
-->
MATCH (p:Person)-[:PRODUCED]->(m:Movie)
where p.name='Joel Silver'
Return m.title

___________________________________________________________________________________________
"""
