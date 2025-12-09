## 18.2 Basic JDBC Example

Listing 18.3 presents a simple class called FruitTest that follows the seven steps outlined in the previous section to show a simple table called fruits . It uses  the  command-line  arguments  to  determine  the  host,  port,  database name, and driver type to use, as shown in Listings 18.1 and 18.2. Rather than putting the driver name and the logic for generating an appropriately formatted database URL directly in this class, these two tasks are spun off to a separate  class  called DriverUtilities ,  shown  in  Listing  18.4.  This  separation minimizes the places that changes have to be made when different drivers are used.

This example does not depend on the way in which the database table was actually created, only on its resultant format. So, for example, an interactive database tool could have been used. In fact, however, JDBC was also used to create the tables, as shown in Listing 18.5. For now, just skim quickly over this listing, as it makes use of utilities not discussed until the next section.

Also, a quick reminder to those who are not familiar with packages. Since FruitTest is  in  the coreservlets package,  it  resides  in  a  subdirectory called coreservlets .  Before  compiling  the  file,  I  set  my CLASSPATH to include the directory containing the coreservlets directory (the JAR file containing  the JDBC drivers should be in  the CLASSPATH also,  of  course). With this setup, I compile simply by doing ' javac FruitTest.java ' from within  the coreservlets subdirectory.  But  to  run FruitTest ,  I  need  to refer to the full package name with ' java coreservlets. FruitTest ... '.

## Listing 18.1 FruitTest result (connecting to Oracle on Solaris)

## Prompt&gt; java coreservlets.FruitTest dbhost1.apl.jhu.edu PTE hall xxxx oracle

Database: Oracle

Version: Oracle7 Server Release 7.2.3.0.0 - Production Release PL/SQL Release 2.2.3.0.0 - Production

## Comparing Apples and Oranges

============================

|   QUARTER |   APPLES | APPLESALES   |   ORANGES | ORANGESALES   | TOPSELLER   |
|-----------|----------|--------------|-----------|---------------|-------------|
|         1 |    32248 | $3547.28     |     18459 | $3138.03      | Maria       |
|         2 |    35009 | $3850.99     |     18722 | $3182.74      | Bob         |
|         3 |    39393 | $4333.23     |     18999 | $3229.83      | Joe         |
|         4 |    42001 | $4620.11     |     19333 | $3286.61      | Maria       |

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.2 Basic JDBC Example

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.2 FruitTest result (connecting to Sybase on NT)

## Prompt&gt; java coreservlets.FruitTest dbhost2.apl.jhu.edu 605741 hall xxxx sybase

Database: Adaptive Server Anywhere

Version: 6.0.2.2188

Comparing Apples and Oranges

============================

|   quarter |   apples | applesales   |   oranges | orangesales   | topseller   |
|-----------|----------|--------------|-----------|---------------|-------------|
|         1 |    32248 | $3547.28     |     18459 | $3138.03      | Maria       |
|         2 |    35009 | $3850.99     |     18722 | $3182.74      | Bob         |
|         3 |    39393 | $4333.23     |     18999 | $3229.83      | Joe         |
|         4 |    42001 | $4620.11     |     19333 | $3286.61      | Maria       |

## Listing 18.3 FruitTest.java

package coreservlets;

```
import java.sql.*;
```

/** A JDBC example that connects to either an Oracle or

- *  a Sybase database and prints out the values of
- *  predetermined columns in the "fruits" table.

*/

public class FruitTest {

/** Reads the hostname, database name, username, password,

- *  and vendor identifier from the command line. It
- *  uses the vendor identifier to determine which
- *  driver to load and how to format the URL. The
- *  driver, URL, username, host, and password are then
- *  passed to the showFruitTable method.

*/

```
public static void main(String[] args) { if (args.length < 5) { printUsage(); return; } String vendorName = args[4]; int vendor = DriverUtilities.getVendor(vendorName); if (vendor == DriverUtilities.UNKNOWN) { printUsage(); return; }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.2 Basic JDBC Example

## String driver = DriverUtilities.getDriver(vendor); String host = args[0]; String dbName = args[1]; String url = DriverUtilities.makeURL(host, dbName, vendor); String username = args[2]; String password = args[3]; showFruitTable(driver, url, username, password); } /** Get the table and print all the values. */ public static void showFruitTable(String driver, String url, String username, String password) { try { // Load database driver if not already loaded. Class.forName(driver); // Establish network connection to database. Connection connection = DriverManager.getConnection(url, username, password); // Look up info about the database as a whole. DatabaseMetaData dbMetaData = connection.getMetaData(); String productName = dbMetaData.getDatabaseProductName(); System.out.println("Database: " + productName); String productVersion = dbMetaData.getDatabaseProductVersion(); System.out.println("Version: " + productVersion + "\n"); System.out.println("Comparing Apples and Oranges\n" + "============================"); Statement statement = connection.createStatement(); String query = "SELECT * FROM fruits"; // Send query to database and store results. ResultSet resultSet = statement.executeQuery(query); // Look up information about a particular table. ResultSetMetaData resultsMetaData = resultSet.getMetaData(); int columnCount = resultsMetaData.getColumnCount(); // Column index starts at 1 (a la SQL) not 0 (a la Java). for(int i=1; i&lt;columnCount+1; i++) { System.out.print(resultsMetaData.getColumnName(i) + "  "); } System.out.println(); // Print results. while(resultSet.next()) { Listing 18.3 FruitTest.java (continued)

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 18 JDBC and Database Connection Pooling

```
// Quarter System.out.print("    " + resultSet.getInt(1)); // Number of Apples System.out.print("     " + resultSet.getInt(2)); // Apple Sales System.out.print("   $" + resultSet.getFloat(3)); // Number of Oranges System.out.print("    " + resultSet.getInt(4)); // Orange Sales System.out.print("    $" + resultSet.getFloat(5)); // Top Salesman System.out.println("      " + resultSet.getString(6)); } } catch(ClassNotFoundException cnfe) { System.err.println("Error loading driver: " + cnfe); } catch(SQLException sqle) { System.err.println("Error connecting: " + sqle); } } private static void printUsage() { System.out.println("Usage: FruitTest host dbName " + "username password oracle|sybase."); } } Listing 18.3 FruitTest.java (continued)
```

## Listing 18.4 DriverUtilities.java

package coreservlets;

```
/** Some simple utilities for building Oracle and Sybase *  JDBC connections. This is <I>not</I> general-purpose *  code -- it is specific to my local setup. */ public class DriverUtilities { public static final int ORACLE = 1; public static final int SYBASE = 2; public static final int UNKNOWN = -1;
```

## 18.2 Basic JDBC Example

## Listing 18.4 DriverUtilities.java (continued)

```
/** Build a URL in the format needed by the *  Oracle and Sybase drivers I am using. */ public static String makeURL(String host, String dbName, int vendor) { if (vendor == ORACLE) { return("jdbc:oracle:thin:@" + host + ":1521:" + dbName); } else if (vendor == SYBASE) { return("jdbc:sybase:Tds:" + host  + ":1521" + "?SERVICENAME=" + dbName); } else { return(null); } } /** Get the fully qualified name of a driver. */ public static String getDriver(int vendor) { if (vendor == ORACLE) { return("oracle.jdbc.driver.OracleDriver"); } else if (vendor == SYBASE) { return("com.sybase.jdbc.SybDriver"); } else { return(null); } } /** Map name to int value. */ public static int getVendor(String vendorName) { if (vendorName.equalsIgnoreCase("oracle")) { return(ORACLE); } else if (vendorName.equalsIgnoreCase("sybase")) { return(SYBASE); } else { return(UNKNOWN); } } }
```

<!-- image -->

## 472

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.5 FruitCreation.java

```
package coreservlets; import java.sql.*; /** Creates a simple table named "fruits" in either *  an Oracle or a Sybase database. */ public class FruitCreation { public static void main(String[] args) { if (args.length < 5) { printUsage(); return; } String vendorName = args[4]; int vendor = DriverUtilities.getVendor(vendorName); if (vendor == DriverUtilities.UNKNOWN) { printUsage(); return; } String driver = DriverUtilities.getDriver(vendor); String host = args[0]; String dbName = args[1]; String url = DriverUtilities.makeURL(host, dbName, vendor); String username = args[2]; String password = args[3]; String format = "(quarter int, " + "apples int, applesales float, " + "oranges int, orangesales float, " + "topseller varchar(16))"; String[] rows = { "(1, 32248, 3547.28, 18459, 3138.03, 'Maria')", "(2, 35009, 3850.99, 18722, 3182.74, 'Bob')", "(3, 39393, 4333.23, 18999, 3229.83, 'Joe')", "(4, 42001, 4620.11, 19333, 3286.61, 'Maria')" }; Connection connection = DatabaseUtilities.createTable(driver, url, username, password, "fruits", format, rows, false); // Test to verify table was created properly. Reuse // old connection for efficiency. DatabaseUtilities.printTable(connection, "fruits", 11, true); } private static void printUsage() { System.out.println("Usage: FruitCreation host dbName " + "username password oracle|sybase."); } }
```