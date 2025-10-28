## Chapter 18 JDBC and Database Connection Pooling

## for(int col=0; col&lt;getColumnCount(); col++) { Listing 18.7 DBResults.java (continued)

```
} for(int row=0; row<getRowCount(); row++) { buffer.append("\n  <TR>\n    "); String[] rowData = getRow(row); buffer.append("<TD>" + rowData[col]); } } buffer.append("\n</TABLE>"); return(buffer.toString()); } }
```

## 18.4 Applying the Database Utilities

Now,  let's  see  how  the  database  utilities  of  Section  18.3  can  simplify  the retrieval and display of database results. Listing 18.8 presents a class that connects to the database specified on the command line and prints out all entries in the employees table. Listings 18.9 and 18.10 show the results when connecting to Oracle and Sybase databases, respectively. Listing 18.11 shows a similar class that performs the same database lookup but formats the results in  an  HTML table.  Listing  18.12  shows  the  raw  HTML  result.  I'll put  an HTML table like this in a real Web page in Section 18.8 (Connection Pooling: A Case Study).

Listing 18.13 shows the JDBC code used to create the employees table.

## 18.4 Applying the Database Utilities

```
Listing 18.8 EmployeeTest.java
```

```
package coreservlets; import java.sql.*; /** Connect to Oracle or Sybase and print "employees" table. */ public class EmployeeTest { public static void main(String[] args) { if (args.length < 5) { printUsage(); return; } String vendorName = args[4]; int vendor = DriverUtilities.getVendor(vendorName); if (vendor == DriverUtilities.UNKNOWN) { printUsage(); return; } String driver = DriverUtilities.getDriver(vendor); String host = args[0]; String dbName = args[1]; String url = DriverUtilities.makeURL(host, dbName, vendor); String username = args[2]; String password = args[3]; DatabaseUtilities.printTable(driver, url, username, password, "employees", 12, true); } private static void printUsage() { System.out.println("Usage: EmployeeTest host dbName " + "username password oracle|sybase."); } }
```

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.9 EmployeeTest result (connecting to Oracle on Solaris)

## Prompt&gt; java coreservlets.EmployeeTest dbhost1.apl.jhu.edu PTE hall xxxx oracle

Database: Oracle

Version: Oracle7 Server Release 7.2.3.0.0 - Production Release PL/SQL Release 2.2.3.0.0 - Production

## employees:

==========

|   ID | FIRSTNAME |   | LASTNAME |      | LANGUAGE |    |   SALARY |
|------|---------------|-----------------|---------------|----------|
|    1 | Wye |         | Tukay |         | COBOL |       |    42500 |
|    2 | Britt |       | Tell |          | C++ |         |    62000 |
|    3 | Max |         | Manager |       | none |        |    15500 |
|    4 | Polly |       | Morphic |       | Smalltalk |   |    51500 |
|    5 | Frank         | | Function |    | Common Lisp | |    51500 |
|    6 | Justin        | |Timecompiler | | Java |        |    98000 |
|    7 | Sir |         | Vlet |          | Java |        |   114750 |
|    8 | Jay |         | Espy |          | Java |        |   128500 |

## Listing 18.10 EmployeeTest result (connecting to Sybase on NT)

## Prompt&gt; java coreservlets.EmployeeTest dbhost2.apl.jhu.edu 605741 hall xxxx sybase

Database: Adaptive Server Anywhere

Version: 6.0.2.2188

## employees:

==========

|   id | firstname |   | lastname |      | language |    |   salary |
|------|---------------|-----------------|---------------|----------|
|    1 | Wye |         | Tukay |         | COBOL |       |    42500 |
|    2 | Britt |       | Tell |          | C++ |         |    62000 |
|    3 | Max |         | Manager |       | none |        |    15500 |
|    4 | Polly |       | Morphic |       | Smalltalk |   |    51500 |
|    5 | Frank         | | Function |    | Common Lisp | |    51500 |
|    6 | Justin        | |Timecompiler | | Java |        |    98000 |
|    7 | Sir |         | Vlet |          | Java |        |   114750 |
|    8 | Jay |         | Espy |          | Java |        |   128500 |

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.4 Applying the Database Utilities

## Listing 18.11 EmployeeTest2.java

```
package coreservlets; import java.sql.*; /** Connect to Oracle or Sybase and print "employees" table *  as an HTML table. */ public class EmployeeTest2 { public static void main(String[] args) { if (args.length < 5) { printUsage(); return; } String vendorName = args[4]; int vendor = DriverUtilities.getVendor(vendorName); if (vendor == DriverUtilities.UNKNOWN) { printUsage(); return; } String driver = DriverUtilities.getDriver(vendor); String host = args[0]; String dbName = args[1]; String url = DriverUtilities.makeURL(host, dbName, vendor); String username = args[2]; String password = args[3]; String query = "SELECT * FROM employees"; DBResults results = DatabaseUtilities.getQueryResults(driver, url, username, password, query, true); System.out.println(results.toHTMLTable("CYAN")); } private static void printUsage() { System.out.println("Usage: EmployeeTest2 host dbName " + "username password oracle|sybase."); } }
```

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.12 EmployeeTest2 result (connecting to Sybase on NT)

```
Prompt> java coreservlets.EmployeeTest2 dbhost2 605741 hall xxxx sybase <TABLE BORDER=1> <TR BGCOLOR="CYAN"> <TH>id<TH>firstname<TH>lastname<TH>language<TH>salary <TR> <TD>1<TD>Wye<TD>Tukay<TD>COBOL<TD>42500.0 <TR> <TD>2<TD>Britt<TD>Tell<TD>C++<TD>62000.0 <TR> <TD>3<TD>Max<TD>Manager<TD>none<TD>15500.0 <TR> <TD>4<TD>Polly<TD>Morphic<TD>Smalltalk<TD>51500.0 <TR> <TD>5<TD>Frank<TD>Function<TD>Common Lisp<TD>51500.0 <TR> <TD>6<TD>Justin<TD>Timecompiler<TD>Java<TD>98000.0 <TR> <TD>7<TD>Sir<TD>Vlet<TD>Java<TD>114750.0 <TR> <TD>8<TD>Jay<TD>Espy<TD>Java<TD>128500.0 </TABLE>
```

## Listing 18.13 EmployeeCreation.java

```
package coreservlets; import java.sql.*; /** Make a simple "employees" table using DatabaseUtilities. */ public class EmployeeCreation { public static Connection createEmployees(String driver, String url, String username, String password, boolean close) { String format = "(id int, firstname varchar(32), lastname varchar(32), " + "language varchar(16), salary float)"; String[] employees = {"(1, 'Wye', 'Tukay', 'COBOL', 42500)", "(2, 'Britt', 'Tell',   'C++',   62000)", "(3, 'Max',  'Manager', 'none',  15500)", "(4, 'Polly', 'Morphic', 'Smalltalk', 51500)",
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.