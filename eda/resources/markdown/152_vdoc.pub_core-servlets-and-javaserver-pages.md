## Chapter 18 JDBC and Database Connection Pooling

<!-- image -->

## Core Note

JDBC is not an acronym.

Although  a  complete  tutorial  on  database  programming  is  beyond  the scope of  this chapter,  I'll  cover  the  basics  of  using  JDBC  here,  assuming you  are  already  familiar  with  SQL.  For  more  details  on  JDBC,  see http://java.sun.com/products/jdbc/ ,  the  on-line  API  for java.sql , or  the  JDBC  tutorial  at http://java.sun.com/docs/books/tutorial/ jdbc/ .  If  you  don't  already  have  access  to  a  database,  you  might  find mySQL a good choice for practice. It is free for non-Microsoft operating systems as well as for educational or research use on Windows. For details, see http://www.mysql.com/ .

## 18.1 Basic Steps in Using JDBC

There are seven standard steps in querying databases:

- 1. Load the JDBC driver.
- 2. Define the connection URL.
- 3. Establish the connection.
- 4. Create a statement object.
- 5. Execute a query or update.
- 6. Process the results.
- 7. Close the connection.

Here are some details of the process.

## Load the Driver

The driver is the piece of software that knows how to talk to the actual database server. To load the driver, all you need to do is to load the appropriate class; a static block in the class itself automatically makes a driver instance and registers it with the JDBC driver manager. To make your code as flexible as possible, it is best to avoid hard-coding the reference to the class name.

These requirements bring up two interesting questions. First, how do you load a class without making an instance of it? Second, how can you refer to a class  whose  name  isn't  known  when  the  code  is  compiled?  The  answer  to both questions is: use Class.forName . This method takes a string represent-

## 18.1 Basic Steps in Using JDBC

ing a fully qualified class name (i.e., one that includes package names) and loads  the  corresponding  class.  This  call  could  throw  a ClassNotFoundException , so should be inside a try / catch block. Here is an example:

```
try { Class.forName("connect.microsoft.MicrosoftDriver"); Class.forName("oracle.jdbc.driver.OracleDriver"); Class.forName("com.sybase.jdbc.SybDriver"); } catch(ClassNotFoundException cnfe) { System.err.println("Error loading driver: " + cnfe); }
```

One  of  the  beauties  of  the  JDBC  approach  is  that  the  database  server requires no changes whatsoever. Instead, the JDBC driver (which is on the client) translates calls written in the Java programming language into the specific  format  required  by  the  server.  This  approach  means  that  you  have  to obtain a JDBC driver specific to the database you are using; you will need to check its documentation for the fully qualified class name to use. Most database  vendors  supply  free  JDBC  drivers  for  their  databases,  but  there  are many third-party vendors of drivers for  older databases. For  an  up-to-date list,  see http://java.sun.com/products/jdbc/drivers.html .  Many  of these driver vendors supply free trial versions (usually with an expiration date or with some limitations on the number of simultaneous connections), so it is easy to learn JDBC without paying for a driver.

In principle, you can use Class.forName for any class in your CLASSPATH . In  practice,  however,  most  JDBC  driver  vendors  distribute  their  drivers inside  JAR  files.  So,  be  sure  to  include  the  path  to  the  JAR  file  in  your CLASSPATH setting.

## Define the Connection URL

Once you have loaded the JDBC driver, you need to specify the location of the database server. URLs referring to databases use the jdbc: protocol and have  the  server  host,  port,  and  database  name  (or  reference)  embedded within the URL. The exact format will be defined in the documentation that comes with the particular driver, but here are two representative examples:

```
String host = "dbhost.yourcompany.com"; String dbName = "someName"; int port = 1234; String oracleURL = "jdbc:oracle:thin:@" + host + ":" + port + ":" + dbName; String sybaseURL = "jdbc:sybase:Tds:" + host  + ":" + port + ":" + "?SERVICENAME=" + dbName;
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 18 JDBC and Database Connection Pooling

JDBC is most often used from servlets or regular desktop applications but is also sometimes employed from applets. If you use JDBC from an applet, remember that, to prevent hostile applets from browsing behind corporate firewalls,  browsers  prevent  applets  from  making  network  connections  anywhere except to the server from which they were loaded. Consequently, to use  JDBC from applets, either the  database  server  needs to  reside  on  the same machine as the HTTP server or you need to use a proxy server that reroutes database requests to the actual server.

## Establish the Connection

To make the actual network connection, pass the URL, the database username,  and  the  password  to  the getConnection method  of  the DriverManager class, as illustrated in the following example. Note that getConnection throws an SQLException ,  so you need to use a try / catch block. I'm omitting this block from the following example since the methods in the following steps throw the same exception, and thus you typically use a single try / catch block for all of them.

```
String username = "jay_debesee"; String password = "secret"; Connection connection = DriverManager.getConnection(oracleURL, username, password);
```

An optional part of this step is to look up information about the database by using the getMetaData method of Connection .  This  method returns a DatabaseMetaData object which has methods to let you discover the name and  version  of  the  database  itself  ( getDatabaseProductName , getDatabaseProductVersion )  or  of  the  JDBC  driver  ( getDriverName , getDriverVersion ). Here is an example:

```
DatabaseMetaData dbMetaData = connection.getMetaData(); String productName = dbMetaData.getDatabaseProductName(); System.out.println("Database: " + productName); String productVersion = dbMetaData.getDatabaseProductVersion(); System.out.println("Version: " + productVersion);
```

Other useful  methods in the Connection class  include prepareStatement (create  a PreparedStatement ;  discussed  in  Section  18.6), prepareCall (create a CallableStatement ), rollback (undo statements since last commit ), commit (finalize  operations  since  last commit ), close (terminate connection),  and isClosed (has  the  connection  either  timed  out  or  been explicitly closed?).

## Create a Statement

A Statement object is used to send queries and commands to the database and is created from the Connection as follows:

Statement statement = connection.createStatement();

## Execute a Query

Once you have a Statement object, you can use it to send SQL queries by using the executeQuery method, which returns an object of type ResultSet . Here is an example:

String query = "SELECT col1, col2, col3 FROM sometable"; ResultSet resultSet = statement.executeQuery(query);

To  modify  the  database,  use executeUpdate instead  of executeQuery , and supply a string that uses UPDATE , INSERT , or DELETE . Other useful methods in the Statement class include execute (execute an arbitrary command) and setQueryTimeout (set  a  maximum delay  to  wait  for  results).  You  can also  create  parameterized  queries  where  values  are  supplied  to  a  precompiled fixed-format query. See Section 18.6 for details.

## Process the Results

The simplest way to handle the results is to process them one row at a time, using the ResultSet ' s next method to move through the table a row at a time. Within a row, ResultSet provides various get Xxx methods that take a column index or column name as an argument and return the result as a variety of different Java types. For instance, use getInt if the value should be an integer, getString for a String , and so on for most other data types. If you just  want  to  display  the  results,  you  can  use getString regardless  of  the actual  column  type.  However,  if  you  use  the  version  that  takes  a  column index, note that columns are indexed starting at 1 (following the SQL convention), not at 0 as with arrays, vectors, and most other data structures in the Java programming language.

## Core Warning

The first column in a ResultSet row has index 1, not 0.

<!-- image -->

Here is an example that prints the values of the first three columns in all rows of a ResultSet .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.1 Basic Steps in Using JDBC

## Chapter 18 JDBC and Database Connection Pooling

```
while(resultSet.next()) { System.out.println(results.getString(1) + " " + results.getString(2) + " " + results.getString(3)); }
```

In addition to the get Xxx and next methods, other useful methods in the ResultSet class include findColumn (get the index of the named column), wasNull (was the last get Xxx result SQL NULL ? Alternatively, for strings you can simply compare the return value to null ),  and getMetaData (retrieve information about the ResultSet in a ResultSetMetaData object).

The getMetaData method is particularly useful. Given only a ResultSet , you have to know about the name, number, and type of the columns to be able to process the table properly. For most fixed-format queries, this is a reasonable expectation. For ad hoc queries, however, it is useful to be able to dynamically discover high-level information about the result. That is the role of the ResultSetMetaData class: it lets you determine the number, names, and  types  of  the  columns  in  the ResultSet .  Useful ResultSetMetaData methods include getColumnCount (the  number  of  columns), getColumnName(colNumber) (a column name, indexed starting at 1), getColumnType (an int to  compare  against  entries  in java.sql.Types ), isReadOnly (is entry a read-only value?), isSearchable (can it be used in a WHERE clause?), isNullable (is a null value permitted?), and several others that give details on  the  type  and  precision  of  the  column. ResultSetMetaData does not include the number of rows, however; the only way to determine that is to repeatedly call next on the ResultSet until it returns false .

## Close the Connection

To close the connection explicitly, you would do:

connection.close();

You should postpone this step if you expect to perform additional database operations, since the overhead of opening a connection is usually large. In fact, reusing existing connections is such an important optimization that Section 18.7 develops a library just for that purpose and Section 18.8 shows some typical timing results.