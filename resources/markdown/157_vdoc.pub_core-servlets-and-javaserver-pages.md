## 18.6 Prepared Statements (Precompiled Queries)

```
Listing 18.17 ExitListener.java /** A listener that you attach to the top-level Frame
```

```
package coreservlets; import java.awt.*; import java.awt.event.*; *  or JFrame of your application, so quitting the *  frame exits the application. */ public class ExitListener extends WindowAdapter { public void windowClosing(WindowEvent event) { System.exit(0); } }
```

## 18.6 Prepared Statements (Precompiled Queries)

If  you  are  going  to  execute  similar  SQL  statements  multiple  times,  using 'prepared' statements can be more efficient than executing a raw query each time. The idea is to create a parameterized statement in a standard form that is sent to the database for compilation before actually being used. You use a question mark to indicate the places where a value will be substituted into the statement. Each time you use the prepared statement, you simply replace some of the marked parameters, using a set Xxx call  corresponding  to  the entry you want to set (using 1-based indexing) and the type of the parameter (e.g., setInt , setString , and so forth). You then use executeQuery (if you want  a ResultSet back)  or execute / executeUpdate (for  side  effects)  as with normal statements. For instance, if you were going to give raises to all the personnel in the employees database, you might do something like the following:

```
Connection connection = DriverManager.getConnection(url, user, password); String template = "UPDATE employees SET salary = ? WHERE id = ?"; PreparedStatement statement = connection.prepareStatement(template); float[] newSalaries = getNewSalaries();
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

```
int[] employeeIDs = getIDs(); statement.setFloat(1, newSalaries[i]); statement.setInt(2, employeeIDs[i]); statement.execute();
```

```
for(int i=0; i<employeeIDs.length; i++) { }
```

The performance advantages of prepared statements can vary significantly, depending on how well the server supports precompiled queries and how efficiently the driver handles raw queries. For example, Listing 18.18 presents a class that sends 40 different queries to a database using prepared statements, then repeats the same 40 queries using regular statements. With a PC and a 28.8K modem connection to the Internet to talk to an Oracle database, prepared statements took only half the time of raw queries, averaging 17.5 seconds for the 40 queries as compared with an average of 35 seconds for the raw queries. Using a fast LAN connection to the same Oracle database, prepared statements  took  only  about  70  percent  of  the  time  required  by  raw  queries, averaging 0.22 seconds for the 40 queries as compared with an average of 0.31 seconds  for  the  regular  statements.  With  Sybase,  prepared  statement  times were virtually identical to times for raw queries both with the modem connection and with the fast LAN connection. To get performance numbers for your setup, download DriverUtilities .java from http://www.coreservlets.com/ , add information about your drivers to it, then run the PreparedStatements program yourself.

## Listing 18.18 PreparedStatements.java

```
package coreservlets; import java.sql.*; /** An example to test the timing differences resulting *  from repeated raw queries vs. repeated calls to *  prepared statements. These results will vary dramatically *  among database servers and drivers. */ public class PreparedStatements { public static void main(String[] args) { if (args.length < 5) { printUsage(); return; } String vendorName = args[4]; int vendor = DriverUtilities.getVendor(vendorName);
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.6 Prepared Statements (Precompiled Queries)

```
if (vendor == DriverUtilities.UNKNOWN) { printUsage(); return; } String driver = DriverUtilities.getDriver(vendor); String host = args[0]; String dbName = args[1]; String url = DriverUtilities.makeURL(host, dbName, vendor); String username = args[2]; String password = args[3]; // Use "print" only to confirm it works properly, // not when getting timing results. boolean print = false; if ((args.length > 5) && (args[5].equals("print"))) { print = true; } Connection connection = getConnection(driver, url, username, password); if (connection != null) { doPreparedStatements(connection, print); doRawQueries(connection, print); } } private static void doPreparedStatements(Connection conn, boolean print) { try { String queryFormat = "SELECT lastname FROM employees WHERE salary > ?"; PreparedStatement statement = conn.prepareStatement(queryFormat); long startTime = System.currentTimeMillis(); for(int i=0; i<40; i++) { statement.setFloat(1, i*5000); ResultSet results = statement.executeQuery(); if (print) { showResults(results); } } long stopTime = System.currentTimeMillis(); double elapsedTime = (stopTime - startTime)/1000.0; System.out.println("Executing prepared statement " + "40 times took " + elapsedTime + " seconds."); } catch(SQLException sqle) { System.out.println("Error executing statement: " + sqle); } } Listing 18.18 PreparedStatements.java (continued)
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.18 PreparedStatements.java (continued)

```
public static void doRawQueries(Connection conn, boolean print) { try { String queryFormat = "SELECT lastname FROM employees WHERE salary > "; Statement statement = conn.createStatement(); long startTime = System.currentTimeMillis(); for(int i=0; i<40; i++) { ResultSet results = statement.executeQuery(queryFormat + (i*5000)); if (print) { showResults(results); } } long stopTime = System.currentTimeMillis(); double elapsedTime = (stopTime - startTime)/1000.0; System.out.println("Executing raw query " + "40 times took " + elapsedTime + " seconds."); } catch(SQLException sqle) { System.out.println("Error executing query: " + sqle); } } private static void showResults(ResultSet results) throws SQLException { while(results.next()) { System.out.print(results.getString(1) + " "); } System.out.println(); } private static Connection getConnection(String driver, String url, String username, String password) { try { Class.forName(driver); Connection connection = DriverManager.getConnection(url, username, password); return(connection); } catch(ClassNotFoundException cnfe) { System.err.println("Error loading driver: " + cnfe); return(null); } catch(SQLException sqle) { System.err.println("Error connecting: " + sqle); return(null); } }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.