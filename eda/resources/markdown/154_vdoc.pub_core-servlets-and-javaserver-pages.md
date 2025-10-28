## 18.3 Some JDBC Utilities

In many applications, you don't need to process query results a row at a time. For example, in servlets and JSP pages, it is common to simply format the database results (treating all values as strings) and present them to the user in an HTML table (see Sections 18.4 and 18.8), in an Excel spreadsheet (see Section 11.2), or distributed throughout the page. In such a case, it simplifies processing to have methods that retrieve and store an entire ResultSet for later display.

This section presents two classes that provide this basic functionality along with a few formatting, display, and table creation utilities. The core class is DatabaseUtilities ,  which  implements  static  methods  for  four  common tasks:

## 1. getQueryResults

This method connects to a database, executes a query, retrieves all the rows as arrays of strings, and puts them inside a DBResults object (see Listing 18.7). This method also places the database product name, database version, the names of all the columns and the Connection object into the DBResults object. There are two versions of getQueryResults : one that makes a new connection and another that uses an existing connection.

## 2. createTable

Given a table name, a string denoting the column formats, and an array of strings denoting the row values, this method connects to a database, removes any existing versions of the designated table, issues a CREATE TABLE command with the designated format, then sends a series of INSERT INTO commands for each of the rows. Again, there are two versions: one that makes a new connection and another that uses an existing connection.

## 3. printTable

Given a table name, this method connects to the specified database, retrieves all the rows, and prints them on the standard output. It retrieves the results by turning the table name into a query of the form ' SELECT * FROM tableName ' and passing it to getQueryResults .

## 18.3 Some JDBC Utilities

## Chapter 18 JDBC and Database Connection Pooling

## 4. printTableData

Given a DBResults object from a previous query, this method prints it on the standard output. This is the underlying method used by printTable , but it is also useful for debugging arbitrary database results.

Listing 18.6 gives the main code, and Listing 18.7 presents the auxiliary DBResults class  that  stores  the  accumulated  results  and  returns  them  as arrays of strings ( getRow )  or  wrapped up inside an HTML table ( toHTMLTable ). For example, the following two statements perform a database query, retrieve the results, and format them inside an HTML table that uses the column names as headings with a cyan background color.

```
DBResults results = DatabaseUtilities.getQueryResults(driver, url, username, password, query, true); out.println(results.toHTMLTable("CYAN"));
```

Since an HTML table can do double duty as an Excel spreadsheet (see Section  11.2),  the toHTMLTable method  provides  an  extremely  simple method for building tables or spreadsheets from database results.

Remember that the source code for DatabaseUtilities and DBResults , like  all  the  source  code  in  the  book,  can  be  downloaded  from www.coreservlets.com and used or adapted without restriction.

## Listing 18.6 DatabaseUtilities.java

```
package coreservlets; import java.sql.*; public class DatabaseUtilities {
```

- /** Connect to database, execute specified query,
- *  and accumulate results into DBRresults object.
- *  If the database connection is left open (use the
- *  close argument to specify), you can retrieve the
- *  connection with DBResults.getConnection.

*/

```
public static DBResults getQueryResults(String driver, String url, String username, String password, String query, boolean close) {
```

## 18.3 Some JDBC Utilities

## Listing 18.6 DatabaseUtilities.java (continued)

```
try { Class.forName(driver); Connection connection = DriverManager.getConnection(url, username, password); return(getQueryResults(connection, query, close)); } catch(ClassNotFoundException cnfe) { System.err.println("Error loading driver: " + cnfe); return(null); } catch(SQLException sqle) { System.err.println("Error connecting: " + sqle); return(null); } } /** Retrieves results as in previous method but uses *  an existing connection instead of opening a new one. */ public static DBResults getQueryResults(Connection connection, String query, boolean close) { try { DatabaseMetaData dbMetaData = connection.getMetaData(); String productName = dbMetaData.getDatabaseProductName(); String productVersion = dbMetaData.getDatabaseProductVersion(); Statement statement = connection.createStatement(); ResultSet resultSet = statement.executeQuery(query); ResultSetMetaData resultsMetaData = resultSet.getMetaData(); int columnCount = resultsMetaData.getColumnCount(); String[] columnNames = new String[columnCount]; // Column index starts at 1 (a la SQL) not 0 (a la Java). for(int i=1; i<columnCount+1; i++) { columnNames[i-1] = resultsMetaData.getColumnName(i).trim(); } DBResults dbResults = new DBResults(connection, productName, productVersion, columnCount, columnNames); while(resultSet.next()) { String[] row = new String[columnCount]; // Again, ResultSet index starts at 1, not 0. for(int i=1; i<columnCount+1; i++) { String entry = resultSet.getString(i); if (entry != null) { entry = entry.trim();
```

```
}
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 18 JDBC and Database Connection Pooling

## row[i-1] = entry; } dbResults.addRow(row); } if (close) { connection.close(); } return(dbResults); } catch(SQLException sqle) { System.err.println("Error connecting: " + sqle); return(null); } } /** Build a table with the specified format and rows. */ public static Connection createTable(String driver, String url, String username, String password, String tableName, String tableFormat, String[] tableRows, boolean close) { try { Class.forName(driver); Connection connection = DriverManager.getConnection(url, username, password); return(createTable(connection, username, password, tableName, tableFormat, tableRows, close)); } catch(ClassNotFoundException cnfe) { System.err.println("Error loading driver: " + cnfe); return(null); } catch(SQLException sqle) { System.err.println("Error connecting: " + sqle); return(null); } } /** Like the previous method, but uses existing connection. */ public static Connection createTable(Connection connection, String username, String password, String tableName, String tableFormat, String[] tableRows, Listing 18.6 DatabaseUtilities.java (continued)

```
boolean close) {
```

## 18.3 Some JDBC Utilities

## Listing 18.6 DatabaseUtilities.java (continued)

```
try { Statement statement = connection.createStatement(); // Drop previous table if it exists, but don't get // error if it doesn't. Thus the separate try/catch here. try { statement.execute("DROP TABLE " + tableName); } catch(SQLException sqle) {} String createCommand = "CREATE TABLE " + tableName + " " + tableFormat; statement.execute(createCommand); String insertPrefix = "INSERT INTO " + tableName + " VALUES"; for(int i=0; i<tableRows.length; i++) { statement.execute(insertPrefix + tableRows[i]); } if (close) { connection.close(); return(null); } else { return(connection); } } catch(SQLException sqle) { System.err.println("Error creating table: " + sqle); return(null); } } public static void printTable(String driver, String url, String username, String password, String tableName, int entryWidth, boolean close) { String query = "SELECT * FROM " + tableName; DBResults results = getQueryResults(driver, url, username, password, query, close); printTableData(tableName, results, entryWidth, true); }
```

/** Prints out all entries in a table. Each entry will

- *  be printed in a column that is entryWidth characters
- *  wide, so be sure to provide a value at least as big
- *  as the widest result.

*/

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.6 DatabaseUtilities.java (continued)

```
public static void printTable(Connection connection, String tableName, int entryWidth, boolean close) { String query = "SELECT * FROM " + tableName; DBResults results = getQueryResults(connection, query, close); printTableData(tableName, results, entryWidth, true); } public static void printTableData(String tableName, DBResults results, int entryWidth, boolean printMetaData) { if (results == null) { return; } if (printMetaData) { System.out.println("Database: " + results.getProductName()); System.out.println("Version: " + results.getProductVersion()); System.out.println(); } System.out.println(tableName + ":"); String underline = padString("", tableName.length()+1, "="); System.out.println(underline); int columnCount = results.getColumnCount(); String separator = makeSeparator(entryWidth, columnCount); System.out.println(separator); String row = makeRow(results.getColumnNames(), entryWidth); System.out.println(row); System.out.println(separator); int rowCount = results.getRowCount(); for(int i=0; i<rowCount; i++) { row = makeRow(results.getRow(i), entryWidth); System.out.println(row); } System.out.println(separator); }
```

## 18.3 Some JDBC Utilities

## Listing 18.6 DatabaseUtilities.java (continued)

```
// A String of the form "|  xxx |  xxx |  xxx |" private static String makeRow(String[] entries, int entryWidth) { String row = "|"; for(int i=0; i<entries.length; i++) { row = row + padString(entries[i], entryWidth, " "); row = row + " |"; } return(row); } // A String of the form "+------+------+------+" private static String makeSeparator(int entryWidth, int columnCount) { String entry = padString("", entryWidth+1, "-"); String separator = "+"; for(int i=0; i<columnCount; i++) { separator = separator + entry + "+"; } return(separator); } private static String padString(String orig, int size, String padChar) { if (orig == null) { orig = "<null>"; } // Use StringBuffer, not just repeated String concatenation // to avoid creating too many temporary Strings. StringBuffer buffer = new StringBuffer(""); int extraChars = size - orig.length(); for(int i=0; i<extraChars; i++) { buffer.append(padChar); } buffer.append(orig); return(buffer.toString()); } }
```

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.7 DBResults.java

```
package coreservlets; import java.sql.*; import java.util.*; /** Class to store completed results of a JDBC Query. *  Differs from a ResultSet in several ways: *  <UL> *    <LI>ResultSet doesn't necessarily have all the data; *        reconnection to database occurs as you ask for *        later rows. *    <LI>This class stores results as strings, in arrays. *    <LI>This class includes DatabaseMetaData (database product *        name and version) and ResultSetMetaData *        (the column names). *    <LI>This class has a toHTMLTable method that turns *        the results into a long string corresponding to *        an HTML table. *  </UL> */ public class DBResults { private Connection connection; private String productName; private String productVersion; private int columnCount; private String[] columnNames; private Vector queryResults; String[] rowData; public DBResults(Connection connection, String productName, String productVersion, int columnCount, String[] columnNames) { this.connection = connection; this.productName = productName; this.productVersion = productVersion; this.columnCount = columnCount; this.columnNames = columnNames; rowData = new String[columnCount]; queryResults = new Vector(); } public Connection getConnection() { return(connection); }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.3 Some JDBC Utilities

## public String getProductName() { return(productName); } public String getProductVersion() { return(productVersion); } public int getColumnCount() { return(columnCount); } public String[] getColumnNames() { return(columnNames); } public int getRowCount() { return(queryResults.size()); } public String[] getRow(int index) { return((String[])queryResults.elementAt(index)); } public void addRow(String[] row) { queryResults.addElement(row); } /** Output the results as an HTML table, with *  the column names as headings and the rest of *  the results filling regular data cells. */ public String toHTMLTable(String headingColor) { StringBuffer buffer = new StringBuffer("&lt;TABLE BORDER=1&gt;\n"); if (headingColor != null) { buffer.append("  &lt;TR BGCOLOR=\"" + headingColor + "\"&gt;\n    "); } else { buffer.append("  &lt;TR&gt;\n    "); } for(int col=0; col&lt;getColumnCount(); col++) { buffer.append("&lt;TH&gt;" + columnNames[col]); Listing 18.7 DBResults.java (continued)

<!-- image -->