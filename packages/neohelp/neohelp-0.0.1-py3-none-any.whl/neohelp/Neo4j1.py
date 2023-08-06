print("1")
"""
 Assignment 1 
I ]  --> Create the following databases as graph models. 
Visualize the models after creation, Return properties
 of nodes, Return the nodes labels, Return the 
relationships with its properties.  NB: You may assume 
and add more labels , relationships, properties  to the 
graphs 

There are  individual books, readers, and authors 
that are present in the library data model.. 
A minimal set of labels are as follows: 
Book: This label includes all the books 
Person: This label includes authors, translators, 
reviewers, Readers, Suppliers and so on 
Publisher: This label includes the publishers 
of books in the database   

A set of basic relationships are as follows: 
PublishedBy: This relationship is used to 
specify that a book was published by a publisher 
Votes: This relationship describes the relation 
between a user and a book, for example, how a book 
was rated by a user. 
ReviewedBy : This relationship is used to specify that
 a book was reviewed and remarked by a user. 
TranslatedBy: This relationship is used to specify that 
a book was translated to a language by a user. 
IssuedBy:  This relationship is used to specify that a 
book was issued  by a user. 
ReturnedBy:  This relationship is used to specify that 
a book was returned by a user 
 
Every book has the following properties: 
Title: This is the title of the book in string format
Tags: This is an array of string tags useful for searching 
through the database based on topic, arguments, geographic 
regions, languages, and so on 
Status: the book status , specifying whether its issued or 
in library. 
Condition: book condition, new or old 
Cost : Cost of book Type: book is a Novel, Journal, 
suspense thriller etc  


--> 

CREATE (john:Author{name:'John Le Carre', born:'19-10-1932'})

CREATE (tinker:Book{title:"Tinker Tailor Soldier Spy",
tag:['English', 'Japanies'], status:'not Issued', condition:'New' 
,published:1974,cost:350, type:'Novel'})

CREATE (graham:Author{name:'Graham Greene',born:'02-10-1904',died:'02-04-1991'})

CREATE (our:Book{title:'Our Man in Havana',tag:['Ameriaca','English','Korian'],status:'Issued',condition:'new', published:1958, cost:250, type:'suspense thriller'})

CREATE (lan:Reader:Author{name:'Lan'})
CREATE (alan:Reader{name:'Alan'})


CREATE  (john)-[:WROTE]->(tinker),
	(alan)-[:RECOMMENDED{date:'05-07-2011'}]->(tinker),
	(lan)-[:RECOMMENDED{date:'09-09-2011'}]->(tinker),
	(lan)-[:RECOMMENDED{date:'03-02-2011'}]->(our),
	(graham)-[:WROTE]->(our)




#View All nodes, labels, Relationships etc.
---> match (n) return n

#Delete All nodes, labels, Relationships etc.
---> MATCH (n) DETACH DELETE n

@CREATE (tinker:Book{title:'Bayari',tag: [ 'Social Issues','Maharashtra'],
 published:1988,cost:550, type:'Novel'})

#Delete All nodes, labels, Relationships where Book="Bayari"
--->
match (n:Book{title:'Bayari'}) Detach delete n

 


***>        [---OR---]


CREATE(pk:Publisher{name:'PK',city:'Pune'})

CREATE (john:Author{name:'John Le Carre', born:'19-10-1932'})
CREATE (graham:Author{name:'Graham Greene',born:'02-10-1904',died:'02-04-1991'})

CREATE (tinker:Book{title:"Tinker Tailor Soldier Spy",
tag:['English', 'Japanies'], status:'not Issued', condition:'New', published:1974, cost:350, type:'Novel'})
CREATE (our:Book{title:'Our Man in Havana',
tag:['Ameriaca','English','Korian'], status:'Issued',condition:'new',
published:1958, cost:250, type:'suspense thriller'})

CREATE (lan:Reader:Author{name:'Lan'})
CREATE (alan:Reader{name:'Alan'})
CREATE(clay:Reader{name:'Clay'})
CREATE(han:Reader{name:'Hanahha Baker'})

CREATE(Jassica:Auther{name:'Jassica'})

CREATE  (our)-[:PUBLISHED_BY]->(pk),
	(Jassica)<-[:TRANSLATED_BY]-(tinker),
	(our)-[:ISSUED_BY]->(clay),
	(tinker)-[:REVIEWED_BY]->(pk),
	(han)-[:VOTES{stars:4}]->(our),
	(tinker)-[:PUBLISHED_BY]->(pk),
	(john)-[:WROTE]->(tinker),
	(alan)-[:RECOMMENDED{date:'05-07-2011'}]->(tinker),
	(lan)-[:RECOMMENDED{date:'09-09-2011'}]->(tinker),
	(lan)-[:RECOMMENDED{date:'03-02-2011'}]->(our),
	(graham)-[:WROTE]->(our)

CREATE(b:Book{title:"Bayari",
tag:['English', 'Marathi'], status:'not Issued', condition:'New', published:1999, cost:333, type:'Novel'})
match (lan:Reader{name:'Lan'})
create (b)-[:RECOMMENDED]->(lan)
return b,lan

match (:Reader{Name:"Lan"})-[r:RECOMMENDED]->(:Book{title="Tinker Tailor Soldier Spy"})
detach delete r

match (b:Book),(r:Reader)
where b.title="Our Man in Havana" and r.name="Hanahha Baker"
create(b)-[i:ISSUED_BY]->(r)
return b,r

match (b:Book),(r:Reader)
where b.title="Tinker Tailor Soldier Spy" and r.name:"Clay"
create(b)-[i:ISSUED_BY]->(r)
return b,r

CREATE (sane:Author{name:'sane guruji', born:'09-10-1942', city :"Satara"})
 
match(b:Book),(a:Author)
where b.title="Bayari" and a.name="sane guruji"
create (a)-[:WROTE]->(b)
return a,b


match (p:Publisher)<-[r:PUBLISHED_BY]-(b:Book)<-[rr:WROTE]-(a:Author)
return r,rr




____________________________________________________________________________



II ] --> Consider a Song database, with labels as Artists,
Song, Recording_company, Recoding_studio, song author etc.
Relationships can be as follows
Artist -> [Performs] -> Song ->[Written by] -> Song_author. 
Song -> [Recorded in ] -> Recording Studio ->[managed by] 
-> Recording Company Recording Company -> [Finances]
-> Song You may add more labels and relationship and their properties, 
as per assumptions


CREATE(pk:Artist:Song_Author{Name:'PK', Age:20, followers:'50M'})
CREATE(bantai:Artist:Song_Author{Name:'Emiway Bantai', Age:26, followers:'5M'})
CREATE(guru:Artist:Song_Author{Name:'Guru', Age:27, followers:'12M'})
CREATE(raf:Artist:Song_Author{Name:'Raftaar', Age:30, followers:'4M'})
CREATE(divine:Artist:Song_Author{Name:'Divine', Age:31, followers:'14M'})
CREATE(neha:Artist:Song_Author{Name:'Neha Kakkar', Age:29, followers:'3M'})

CREATE(hard:Song{Name:'Bohot Hard', likes:'40M'})
CREATE(gully:Song{Name:'Mere Gully Main', likes:'12M'})
CREATE(azadi:Song{Name:'Azadi', likes:'7M'})
CREATE(asli:Song{Name:'Asli',likes:'8M'})
CREATE(gabru:Song{Name:'High Rated Gabru', likes:'10M'})
CREATE(ladki:Song{Name:'Ladki Marwake Marke Maneggii', likes:'2.5M'})
CREATE(machayenge:Song{Name:'Machayenge', likes:'8M'})
CREATE(chull:Song{Name:'Kar Gayi Chull', likes:'5M'})

CREATE(arijit:Song_Author{Name:'Arijit Singh',No_songs:50})
CREATE(tony:Song_Author{Name:'Tony Kakkar',No_songs:112})

CREATE(coke:Recording_company{Name:'Coke Studio'})
CREATE(zee:Recording_company:Recoding_studio{Name:'Zee Studio'})

CREATE  (pk)-[:PERFORMS]->(hard),
	(gabru)-[:WRITTEN_BY]->(bantai),
	(bantai)-[:PERFORMS]->(machayenge)-[:WRITTEN_BY]->(bantai),
	(guru)-[:PERFORMS]->(gabru)-[:WRITTEN_BY]->(arijit),
	(raf)-[:PERFORMS]->(ladki)-[:WRITTEN_BY]->(raf),
	(divine)-[:PERFORMS]->(gully)-[:WRITTEN_BY]->(divine),
	(divine)-[:PERFORMS]->(azadi)-[:WRITTEN_BY]->(divine),
	(neha)-[:PERFORMS]->(chull),
	(asli)-[:RECORDED_IN]->(zee)-[:MANAGED_BY]->(zee)-[:Finances]->(hard),
	(gabru)-[:RECORDED_IN]->(coke)-[:MANAGED_BY]->(zee),
	(ladki)-[:RECORDED_IN]->(zee)-[:MANAGED_BY]->(coke)-[:Finances]->(chull),
	(azadi)-[:RECORDED_IN]->(coke)-[:MANAGED_BY]->(coke),
	(neha)-[:FOLLOWS]->(arijit)-[:FOLLOWS]->(guru)-[:FOLLOWS]->(raf)-[:FOLLOWS]->(tony)-[:FOLLOWS]->(pk)
	
__________________________________________________________________________________

3. Consider an Employee database, with a minimal set of labels as follows:
Employee: denotes a person as an employee of the organization          
Department: denotes the different departments, in which employees work.           
Skillset: A list of skills acquired by an employee          
Projects: A list of projects in which an employee works. 

A minimal set of relationships can be as follows:           
Works_in : employee works in a department           
Has_acquired: employee has acquired a skill            
Assigned_to : employee assigned to a project          
Controlled_by: A project is controlled by a department          
Project_manager : Employee is a project_manager of a Project
-->

CREATE(harry:Employee {Name:'Harry', age:29, Qualification:['MCS','BCS'], Experience:8})
CREATE(pashya:Employee {Name:'Pashya', age:30, Qualification:['MCA','BCA','MSCIT'],Experience:8})
CREATE(bablu:Employee {Name:'Bablu', age:28, Qualification:['B.Tech','MSCIT'],Experience:5})
CREATE(monu:Employee {Name:'Monu', age:26, Qualification:['B.Tech','M.Tech'],Experience:3})
CREATE(babu:Employee {Name:'Babu', age:32, Qualification:['M.Tech','B.Tech','MSCIT','MCS','BCS'],Experience:10})
CREATE(nandu:Employee {Name:'Nandu', age:34, Qualification:['B.Tech','BCS','MSCIT'],Experience:4})

CREATE(it:Department{Name:'IT',no_of_Emp:5})
CREATE(bpo:Department{Name:'BPO',no_of_Emp:5})
CREATE(cbo:Department{Name:'CBO',no_of_Emp:5})
CREATE(cmn:Department{Name:'TeleCommunication',no_of_Emp:5})

CREATE(vgd:Skillset{skills:['Fluent Communication','Leadership Qualities','Optimistic']})
CREATE(bet:Skillset{skills:['Good Communication','Java Devloper']})
CREATE(gd:Skillset{skills:['Leadership Qualities','Optimistic','Finnance Matser']})
CREATE(av:Skillset{skills:['Fluent Communication']})

CREATE(sg:Projects{Name:'SG Website Design', TimeSpan:'30day', clinet:'SG Architecture'})
CREATE(food:Projects{Name:'Food Deliver app', TimeSpan:'35day', clinet:'Hydrabaad Biryanni'})
CREATE(location:Projects{Name:'Location Finder', TimeSpan:'45day', clinet:'AI Location Developer'})
CREATE(ecom:Projects{Name:'Ecommerce Website Design', TimeSpan:'50day', clinet:'Eco-market'})
CREATE(tata:Projects{Name:'Tata Sky', TimeSpan:'20day', clinet:'SkyVoice India'})
CREATE(out:Projects{Name:'Out Bound Process', TimeSpan:'90day', clinet:'Ruby Max'})


CREATE  (harry)-[:Works_in]->(it),
	(pashya)-[:Works_in]->(bpo),
	(bablu)-[:Works_in]->(cbo),
	(monu)-[:Works_in]->(cmn),
	(nandu)-[:Works_in]->(it),
	(harry)-[:Has_acquired]->(vgd),
	(pashya)-[:Has_acquired]->(bet),
	(bablu)-[:Has_acquired]->(gd),
	(monu)-[:Has_acquired]->(vgd),
	(nandu)-[:Has_acquired]->(bet),
 		(harry)-[:Has_acquired]->(av),
	(harry)-[:Assigned_to]->(sg),
	(nandu)-[:Assigned_to]->(food),
	(bablu)-[:Assigned_to]->(ecom),
	(monu)-[:Assigned_to]->(sg),
	(pashya)-[:Assigned_to]->(location),
	(harry)-[:Assigned_to]->(out),
	(bablu)-[:Assigned_to]->(out),
	(out)-[:Controlled_by]->(it),
	(location)-[:Controlled_by]->(cbo),
	(sg)-[:Controlled_by]->(it),
	(ecom)-[:Controlled_by]->(bpo),
	(food)-[:Controlled_by]->(cmn),
	(nandu)-[:Project_manager]->(sg),
	(bablu)-[:Project_manager]->(food),
	(monu)-[:Project_manager]->(ecom),
	(pashya)-[:Project_manager]->(location),
	(babu)-[:Project_manager]->(tata),
	(harry)-[:Project_manager]->(out)


__________________________________________________________________________________



IV]  -->Consider a movie database, with nodes as Actors, Movies, Roles, 
Producer, Financier, Director. Assume appropriate relationships between the nodes, 
include properties for nodes and relationships



CREATE (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
CREATE (Carrie:Person {name:'Carrie-Anne Moss', born:1967})
CREATE (Laurence:Person {name:'Laurence Fishburne', born:1961})
CREATE (Hugo:Person {name:'Hugo Weaving', born:1960})
CREATE (LillyW:Person {name:'Lilly Wachowski', born:1967})
CREATE (LanaW:Director{name:'Lana Wachowski', born:1965})
CREATE (JoelS {name:'Joel Silver', born:1952})
CREATE
  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix),
  (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrix),
  (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrix),
  (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrix),
  (LillyW)-[:DIRECTED]->(TheMatrix),
  (LanaW)-[:DIRECTED]->(TheMatrix),
  (JoelS)-[:PRODUCED]->(TheMatrix)

CREATE (Emil:Person {name:"Emil Eifrem", born:1978})
CREATE (Emil)-[:ACTED_IN {roles:["Emil"]}]->(TheMatrix)

CREATE (TheMatrixReloaded:Movie {title:'The Matrix Reloaded', released:2003, tagline:'Free your mind'})
CREATE
  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixReloaded),
  (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixReloaded),
  (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixReloaded),
  (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixReloaded),
  (LillyW)-[:DIRECTED]->(TheMatrixReloaded),
  (LanaW)-[:DIRECTED]->(TheMatrixReloaded),
  (JoelS)-[:PRODUCED]->(TheMatrixReloaded)

CREATE (AngelaScope:Person {name:'Angela Scope'})
CREATE (JessicaThompson:Person {name:'Jessica Thompson'})



CREATE
  (JessicaThompson)-[:REVIEWED {summary:'An amazing journey', rating:95}]->(TheMatrixReloaded),
  (JessicaThompson)-[:REVIEWED {summary:'Silly, but fun', rating:65}]->(TheMatrix),
  (AngelaScope)-[:REVIEWED {summary:'Pretty funny at times', rating:62}]->(TheMatrixReloaded)

  Match (n) detach delete n




******************************** Thank You ***************************
"""