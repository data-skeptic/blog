# Graph Query Languages: Gremlin vs. openCypher vs. SPARQL

Graphs have become a powerful tool for modeling complex and interconnected data. Unlike relational databases, they store data as nodes (entities) and edges (relationships that link two entities). There are, however, various graph query languages, each with unique features and syntax. The three most widely used are Gremlin, openCypher, and SPARQL. 

This article will discuss the uniqueness and differences between these graph query languages. All code snippets in this article are run on Amazon Neptune. There could be a few nuances between Amazon Neptune syntax and the native query language syntax.


## Understanding graphs

As mentioned earlier, graphs are represented in nodes and edges. For instance, assume we want to capture a network of friends. 



* Alice is friends with Charlie, Diana, and Eli.
* Charlie is friends with Eli.

The figure below captures the relationship between these four people.

<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image5.png" style="width:4.44in; height:3.36in;">






Each person, Eli, Charlie, Alice, and Diana, is a node. The lines represent the connection between them, in this case, friendship. Nodes and edges can both have properties.

For instance, the properties of a person node include gender, properties, age, etc., while the properties of a friendship edge can be ‘years of friendship’, ‘level of friendship’, etc.

When querying graphs, we specify them in terms of steps from a node to an edge or vice versa. These steps are technically called traversals. In our graph, if we wish to know Diana's friends, we traverse from Diana to any available edge and find the adjacent node.


## Gremlin

Gremlin is a part of the Apache TinkerPop project. It allows us to create powerful graphs using simple syntax. We can download Gremlin Server and Gremlin Console to create and manage a graph database with Gremlin.

Gremlin queries always begin from a traversal source. By convention, this is given the variable `g`. `g` is the traversal that connects to the gremlin server.


### Adding a node

To add a node in Gremlin, we use `g.addV()`. We add the `.property()` method to add properties of the node.

For instance, the code below adds a person node with an ID `1`, whose first name is Diana.


```
g.addV('person').property(id, '1').property('first_name', 'Diana')
```


Let’s add more nodes to the graph.


```
g.addV('person').property(id, '2').property('first_name', 'Charlie').next()
g.addV('person').property(id, '3').property('first_name', 'Alice').next()
g.addV('person').property(id, '4').property('first_name', 'Eli')
```



### Adding an edge

To add an edge, we use `g.addE()`. The `addE()` method follows the following syntax:


```
g.V(<source_node_id>).addE(<edge_name>).to(__.V(<target_node_id>)
```


We can also specify the properties of the edge using the `.property()` method.

The code below adds an edge between Alice and Charlie, with three years of friendship as the edge property.


```
g.V('3').addE('friends_with').to(__.V('2')).property(id, '1').property('years_of_friendship', 3)
```


Let’s add the other edges


```
g.V('3').addE('friends_with').to(__.V('1')).property('years_of_friendship', 2).next()
g.V('3').addE('friends_with').to(__.V('4')).property('years_of_friendship', 4).next()
g.V('2').addE('friends_with').to(__.V('4')).property('years_of_friendship', 5)
```



### Deleting a node/edge

We can delete a node or edge in Gremlin with the `.drop()` method. To delete a node, run.


```
g.V(<node_id>).drop()
```


If the node specified has incoming or outgoing edges, Gremlin automatically deletes these edges.

To delete an edge in Gremlin, we use the syntax


```
g.E(<edge_id>).drop()
```


When we delete an edge, the relationship between the source and target nodes is removed, but the nodes themselves remain.


### Delete the graph

To delete the entire graph, run


```
g.V().drop().iterate()
```


This removes all nodes in the graph. But since Gremlin automatically removes any associated edge alongside, the graph becomes empty once all the nodes are removed.


### Traversing the graph

Traversing a graph means moving from one node to another through an edge. This allows us to write queries to filter relationships we are interested in or find paths between two nodes. To specify a node when the traversal begins, we use the `has()` method to specify the property of the node we are interested in.

The `.has()` method has the syntax:


```
g.V().has(<node_name>, <property_key>, <property_value>)
```


When traversing a graph in Gremlin, we also need to specify the direction of the traversal. There are three possible directions.



* `out()`: The traversal considers only outgoing edges.
* `in()`: The traversal considers only incoming edges.
* `both()`: The traversal considers both outgoing and incoming edges.

Let’s say we want to find Alice's friends; we can traverse from the Alice node outward. The result is any path (edge to node) from Alice's node. The code below returns all the friends of Alice.


```
g.V().has('person', 'first_name', 'Alice').out('friends_with').values('first_name').toList()
```


Output:



<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image3.png" style="width:6.5in; height:auto;">



We can also specify a starting node using the node ID rather than its property.


```
g.V('3').out('friends_with').values('first_name').toList()
```



### Recursive traversals

Sometimes, we may need to traverse a graph multiple times or until a condition is met. This is called recursive traversal. When performing recursive traversals in Gremlin, we use the `repeat(<a_traversal>)` step to instruct that a loop is repeated until a condition to stop is met. There are two ways of stopping a `repeat()` step.



* `times(<an_integer>)`: This is used after a `repeat()` step to specify the number of times the traversal within the `repeat()` step is done.
* `until(<a_traversal>)`: This specifies a traversal condition that must be met before the repeat loops stop. For instance, a traversal is repeated until a node ID of 1 is reached. Note that the `until()` step should be used carefully, because if the condition is not met, all possible paths will be explored. This can cause performance issues in large graphs.

Assume the graph was undirected, and we wish to return the friends of Diana's friends. This means we need to traverse the graph twice from Diana. We use the code:


```
g.V('1').
repeat(both()).
times(2).
valueMap()
```


Output:


<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image8.png" style="width:6.5in; height:auto;">




So the friends of friends of Diana are Charlie and Eli.

We often use the `until()` and `repeat()` steps when returning a path between two nodes.


### Returning a Path

When we traverse a graph, we can filter nodes or edges of interest to return the paths between two nodes. A path is a unique property of graphs, allowing us to understand the possible connections between two nodes. We can return the paths in Gremlin using the `path()` step.

For instance, Alice can get to Eli in our friends network in two ways.



* Directly to Eli since she is friends with him
* Through Charlie, since she is friends with Charlie and Charlie is friends with Eli.

We do this in Gremlin using the following syntax.


```
g.V(<source_node_id>)
  .repeat(out(<relationship>))
  .until(hasId(<target_node_id>))
  .path()
  .by(<node_property_to_return>)
  .toList()
```


The code below returns all possible paths between Alice and Eli.


```
g.V('3')
  .repeat(out('friends_with'))
  .until(hasId('4'))
  .path()
  .by('first_name')
  .toList()
```


Output: 

<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image9.png" style="width:6.5in; height:auto;">





But when we use `path()`, Gremlin considers all possible paths in the graph, including repeated paths. If there are repeated paths, we run into a cycle where the path becomes unending. This is similar to having an infinite loop in Python.

To ensure we do not run into cycles in Gremlin, we add the `simplePath()` step within the `repeat()` step. This way, Gremlin considers only linear paths and discards cycles.

A safer way to run the earlier code is:


```
g.V('3')
  .repeat(out('friends_with').simplePath())
  .until(hasId('4'))
  .path()
  .by('first_name')
  .toList()
```


This returns the same result, and this way, we are certain Gremlin will not run into cycles.


## openCypher

openCypher is popularly known for its SQL-like syntax. It was developed by Neo4j and has gained acceptance due to its similarity with SQL.


### Adding a node

To add a node in openCypher, we use the `CREATE` keyword. The `CREATE` keyword follows the syntax below.


```
CREATE (n:<node_name> {<property_key>:<property>})
```


For instance, to add the Diana node, we run


```
CREATE (n:person {name: 'Diana'})
```


We can add the other nodes in a similar fashion.


### Adding an edge

To add an edge, we first define the source and target nodes using the `MATCH` clause. For instance, we match Alice and Charlie in this fashion.


```
MATCH (a:person {name: 'Alice'}), (c:person {name: 'Charlie'})
```


Notice that Alice was mapped to `a` and Charlie to `c`. 

Next, we can create an edge from node a to c, using the syntax below.


```
CREATE (a)-[]->(c)
```


We specify the property of the edge in the square bracket. The code below defines an edge from Alice to Charlie with three years of friendship.


```
MATCH (a:person {name: 'Alice'}), (c:person {name: 'Charlie'})
CREATE (a)-[:friends_with {years_of_friendship: 3}]->(c)
```



### Deleting a node

We can delete a node or edge in openCypher. We first use the `MATCH` clause to specify the node of interest and use the `DELETE` clause to delete it. We follow the syntax below.


```
MATCH (n: <node_properties>)
DELETE n
```


For instance, to delete Diana, we can run:


```
MATCH (n:person {name: 'Diana'})
DELETE n
```


Note that openCypher only deletes a node if it has no edges. When edges are associated with the node, we must detach them before deleting them using the `DETACH DELETE` clause.

Thus, since Diana has an edge, we use the code below to delete the Diana node and the associated edge.


```
MATCH (n:person {name: 'Diana'})
DETACH DELETE n
```



### Deleting an edge

To delete an edge in openCypher, we use the `MATCH` clause to specify the edge of interest and then `DELETE` clause to remove the edge. It follows the syntax:


```
MATCH (a)-[e]->(b)
DELETE e
```


Notice that we have defined the edge as ‘e’ in the `MATCH` step, and then we use the DELETE clause to remove it. To remove the `friends_with` edge between Alice and Charlie, we run:


```
MATCH (a:person {name: 'Alice'})-[e:friends_with]->(c:person {name: 'Charlie'})
DELETE e
```



### Deleting the graph

To delete the entire graph, run:


```
MATCH (n)
DETACH DELETE n
```



### Traversing the graph

To traverse the graph, we use the `MATCH` clause to specify the pattern we desire in the graph and the `RETURN` keyword to return the result.

For instance, if we wish to return all direct friends of Alice, we run:


```
MATCH (a:person {name: 'Alice'})-[:friends_with*1]->(friends)
RETURN friends.name as FirstName
```


Output:



<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image6.png" style="width:6.5in; height:auto;">




There are a few things to notice here.



* The `MATCH` clause followed the pattern `(a)-[:b]->(c)`: This means that the graph would traverse outward from a, find an edge named b, and return the resulting nodes (called c).
* `*1` when specifying the edge: The graph should be traversed once from a.

To traverse twice, we use `*2`.

To traverse to the root of all possible paths, we use `*`

To traverse and return any of the paths within a range, say all nodes between the third and fifth traversal, we use `*3..5`.

For instance, we can return the friends of friends of Alice assuming an undirected graph using:


```
MATCH (a:person {name: 'Alice'})-[:friends_with*2]-(friends)
RETURN friends.name AS FirstName
```


Output:


<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image4.png" style="width:6.5in; height:auto;">





Notice that the structure of the `MATCH` step is `(a)-[]-(c)`. When we use `(a)-[]-(c)`, the traversal is undirected, meaning both incoming and outgoing edges are considered. If we use `(a)<-[]-(c)`, only incoming nodes from node a will be considered.


### Returning paths

Similar to other approaches, we use the `MATCH` clause to specify the start and end nodes. The `RETURN` clause is then used to return all the paths. For instance, to return the paths between Alice and Eli:


```
MATCH path = (a:person {name: 'Alice'})-[:friends_with*]->(e:person {name: 'Eli'})
RETURN path
```


This returns a list of all the paths. The list contains the node labels, including its id. To return just the name, we use a list comprehension in the `RETURN` step.


```
MATCH path = (a:person {name: 'Alice'})-[:friends_with*]->(e:person {name: 'Eli'})
RETURN [node IN nodes(path) | node.name] AS FirstName
```


Output:


<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image10.png" style="width:6.5in; height:auto;">




## SPARQL

SPARQL (SPARQL Protocol and RDF Query Language) is a query language for querying and manipulating data stored in an RDF (Resource Description Framework) format. RDF is a standard model for data interchange on the web where data is represented in the format: subject-predicate-object, called triplets.

Subjects and objects are entities in an RDF graph. They are technically called resources (not nodes) identified with a URI (Uniform Resource Identifier). In other words, subjects and objects are URIs. The predicate defines the relationship between the subject and the object.


### Adding a resource

To add a resource, we use the `INSERT DATA` operation. The code below adds the resource and specifies that the resource is of class `Person`.


```
PREFIX ex: <http://example.com/>
INSERT DATA {
  ex:Alice a ex:Person .}
```


As mentioned earlier, resources are URI. In the code snippet, we defined a new resource within the URI `<[http://example.com/](http://example.com/)>`. But to avoid writing this URI when creating a resource, we use the `PREFIX` keyword to set the URI to ex. This means that the URI prefix can be written as ex.

Queries in SPARQL are always written in the form object predicate subject (a triple).

It appears that in:


```
INSERT DATA {
  ex:Alice a ex:Person .}
```


The subject is `Alice`, a is a special keyword in Turtle syntax meaning is `of type`, and the object is `Person`. Therefore, the query above can be read as insert Alice, who is of type Person.

When we do not wish to specify the type of a subject, we replace a with the name of the relationship in the form `<prefix:subject prefix:relationship prefix:object>` .

Adding resources with edges

We can add edges by using the `INSERT DATA` with the triple syntax: 


```
<prefix:subject prefix:relationship prefix:object> .
```


For example, we can specify that Charlie is friends with Eli with:


```
PREFIX ex: <http://example.com/>
INSERT DATA {
  ex:Charlie ex:friendsWith ex:Eli .
}  
```


This creates the `nodes` Charlie and Eli and their relationship `friendsWith`, all in one sweep.

To view the edges in the RDF graph, we use:


```
SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
}
```


Output:



<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image1.png" style="width:6.5in; height:auto;">





If we wish to insert multiple predicates and objects from one subject, we use ; to separate the insertions. We do not repeat the subject after the first data insertion. For instance, the code below inserts a relationship between Alice to Charlie, Diana, and Eli.


```
PREFIX ex: <http://example.com/>
INSERT DATA {

  ex:Alice ex:friendsWith ex:Charlie ;
            ex:friendsWith ex:Diana ;
            ex:friendsWith ex:Eli .
}  
```



### Traversing the graph

We can traverse the graph to return objects of connecting relationships. We use the `SELECT` clause to specify what to return and the `WHERE` clause to define the triplet. The object is defined using a variable with a preceding `?` character. For instance, to return friends of Alice, we can use:


```
PREFIX ex: <http://example.com/>

SELECT ?friend
WHERE {
  ex:Alice ex:friendsWith ?friend .
}
```


Output:



<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image7.png" style="width:6.5in; height:auto;">





We can also traverse the graph multiple times. If we want to return the friends of friends of Alice, the predicate in the triplet is written twice and separated with `/`.


```
PREFIX ex: <http://example.com/>

SELECT ?friendOfFriend
WHERE {
  ex:Alice ex:friendsWith/ex:friendsWith ?friendOfFriend .
}
```


Output:



<img src="https://feaas-staging.s3.us-east-1.amazonaws.com/user/david@dataskeptic.com/imdb_images/image2.png" style="width:6.5in; height:auto;">





Comparing Gremlin, openCypher and SPARQL

Having explored all three popular graph query languages, the table below shows the differences between the three of them.


<table>
  <tr>
   <td><strong>Feature/Aspect</strong>
   </td>
   <td><strong>SPARQL</strong>
   </td>
   <td><strong>openCypher</strong>
   </td>
   <td><strong>Gremlin</strong>
   </td>
  </tr>
  <tr>
   <td><strong>Graph model</strong>
   </td>
   <td>Triple-based (subject-predicate-object)
   </td>
   <td>Nodes and relationships with properties
   </td>
   <td>Vertices and edges with properties
   </td>
  </tr>
  <tr>
   <td><strong>Creating node and edge</strong>
   </td>
   <td>RDF describes nodes and edges simultaneously as triples
   </td>
   <td>Nodes must exist before creating edges (except when using the MERGE keyword)
   </td>
   <td>Nodes and edges can be created in any order
   </td>
  </tr>
  <tr>
   <td><strong>Deleting node and edge</strong>
   </td>
   <td>Must explicitly delete edges or use CASCADE in some stores
   </td>
   <td>Must use DETACH DELETE to remove node and edges
   </td>
   <td>Automatically deletes edges when a node is removed
   </td>
  </tr>
  <tr>
   <td><strong>Label types</strong>
   </td>
   <td>RDF Types (resources and properties as URIs)
   </td>
   <td>Labels for nodes and relationships
   </td>
   <td>Labels for vertices and edges
   </td>
  </tr>
  <tr>
   <td><strong>Query Type</strong>
   </td>
   <td>Declarative, focused on pattern matching
   </td>
   <td>Declarative, SQL-like syntax
   </td>
   <td>Declarative and imperative, fluent API
   </td>
  </tr>
  <tr>
   <td><strong>Updating node and edge</strong>
   </td>
   <td>INSERT, DELETE WHERE
   </td>
   <td>CREATE, MERGE, DELETE
   </td>
   <td>addV(), addE(), drop()
   </td>
  </tr>
  <tr>
   <td><strong>Learning curve</strong>
   </td>
   <td>Steep for those unfamiliar with semantic web concepts
   </td>
   <td>Moderate, similar to SQL
   </td>
   <td>Moderate to steep. Although intuitive, it needs an understanding of a new syntax
   </td>
  </tr>
  <tr>
   <td><strong>Use cases</strong>
   </td>
   <td>Semantic web applications, knowledge graphs
   </td>
   <td>Social networks, recommendation systems
   </td>
   <td>Real-time analytics, complex network problems
   </td>
  </tr>
</table>


## Wrapping up

We have seen the differences between using SPARQL, openCypher and Gremlin. There are multiple factors to consider when deciding what to learn. openCypher may be more familiar because of its syntax similarity to SQL. Its use in Neo4j graphs also makes it more popular. Gremlin is also a good choice and can be quite easy to learn. SPARQL has a bit more specifics and it is best for linked data on the web.

If you ask me, I will rank openCypher as my favorite, Gremlin comes a close second and SPARQL will be third.
