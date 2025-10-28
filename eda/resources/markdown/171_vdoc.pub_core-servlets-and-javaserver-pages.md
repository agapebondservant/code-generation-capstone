## 18.8 Connection Pooling: A Case Study

## Table 18.1  Connection pool timing results

Fast LAN connection to database,

10 initial connections, 50 max connections

( ConnectionPoolServlet )

1.8 seconds

Fast LAN connection to database,

recycling a single connection

( ConnectionPoolServlet2 )

2.0 seconds

Fast LAN connection to database, no connection pooling ( ConnectionPoolServlet3 )

2.8 seconds

## Condition

Average Time

## Listing 18.20 ConnectionPoolServlet.java

package coreservlets;

import java.io.*;

import javax.servlet.*;

import javax.servlet.http.*;

import java.sql.*;

/** A servlet that reads information from a database and

- *  presents it in an HTML table. It uses connection
- *  pooling to optimize the database retrieval. A good
- *  test case is ConnectionPool.html, which loads many
- *  copies of this servlet into different frame cells.

*/

public class ConnectionPoolServlet extends HttpServlet { private ConnectionPool connectionPool; public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { String table; try { String query = "SELECT firstname, lastname " + " FROM employees WHERE salary &gt; 70000"; Connection connection = connectionPool.getConnection(); DBResults results = DatabaseUtilities.getQueryResults(connection, query, false); connectionPool.free(connection);

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.20 ConnectionPoolServlet.java (continued)

```
table = results.toHTMLTable("#FFAD00"); } catch(Exception e) { table = "Error: " + e; } response.setContentType("text/html"); // Prevent the browser from caching the response. See // Section 7.2 of Core Servlets and JSP for details. response.setHeader("Pragma", "no-cache"); // HTTP 1.0 response.setHeader("Cache-Control", "no-cache"); // HTTP 1.1 PrintWriter out = response.getWriter(); String title = "Connection Pool Test"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<CENTER>\n" + table + "\n" + "</CENTER>\n</BODY></HTML>");
```

}

- /** Initialize the connection pool when servlet is
- *  initialized. To avoid a delay on first access, load
- *  the servlet ahead of time yourself or have the
- *  server automatically load it after reboot.

*/

```
public void init() { int vendor = DriverUtilities.SYBASE; String driver = DriverUtilities.getDriver(vendor); String host = "dbhost2.apl.jhu.edu"; String dbName = "605741"; String url = DriverUtilities.makeURL(host, dbName, vendor); String username = "hall"; String password = "xxxx"; // Changed :-) try {
```

```
connectionPool = new ConnectionPool(driver, url, username, password, initialConnections(), maxConnections(), true); } catch(SQLException sqle) { System.err.println("Error making pool: " + sqle); getServletContext().log("Error making pool: " + sqle); connectionPool = null; } } public void destroy() { connectionPool.closeAllConnections(); }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.8 Connection Pooling: A Case Study

## Listing 18.20 ConnectionPoolServlet.java (continued)

```
/** Override this in subclass to change number of initial *  connections. */ protected int initialConnections() { return(10); } /** Override this in subclass to change maximum number of *  connections. */ protected int maxConnections() { return(50); } }
```

## Listing 18.21 ConnectionPool.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Frameset//EN"> <HTML> <HEAD><TITLE>Servlet Connection Pooling: A Test</TITLE></HEAD> <!-- Causes 25 near simultaneous requests for same servlet. --> <FRAMESET ROWS="*,*,*,*,*" BORDER=0 FRAMEBORDER=0 FRAMESPACING=0> <FRAMESET COLS="*,*,*,*,*"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> </FRAMESET> <FRAMESET COLS="*,*,*,*,*"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> </FRAMESET> <FRAMESET COLS="*,*,*,*,*"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet">
```

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.21 ConnectionPool.html (continued)

```
<FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> </FRAMESET> <FRAMESET COLS="*,*,*,*,*"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> </FRAMESET> <FRAMESET COLS="*,*,*,*,*"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> <FRAME SRC="/servlet/coreservlets.ConnectionPoolServlet"> </FRAMESET>
```

&lt;/FRAMESET&gt;

&lt;/HTML&gt;

Figure 18-6 A framed document that forces 25 nearly simultaneous requests for the same servlet.

<!-- image -->

| Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   | Servlet Connection Pooling: A Test Netscape   |               |
|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|---------------|
| Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               | Ede Edit Yiew Communicator Help               |               |
| Bookmarks                                     | Bookmarks                                     | Bookmarks                                     | Bookmarks                                     | Bookmarks                                     | Bookmarks                                     | Bookmarks                                     | Bookmarks                                     | Bookmarks                                     | Bookmarks                                     |               |
| fustuame                                      | lastname                                      | fustuname                                     |                                               |                                               | lastname                                      | fustname                                      | lastname                                      |                                               | lastname                                      |               |
| Justin                                        | Time ompler                                   | Justin                                        | Imecompler                                    | Justin                                        | Imecompler                                    | Justin                                        | Time ompler                                   | Justin                                        | Imecompler                                    |               |
|                                               | Vlet                                          | Srr                                           | Vlet                                          |                                               | Vlet                                          |                                               | Vlet                                          | Srr                                           | Vlet                                          |               |
| Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          |               |
| fustname                                      | lastname                                      | Iustamne                                      | lastname                                      | Iustame                                       | lastname                                      | fustame                                       | lastame                                       | fustname                                      | lastnamne                                     |               |
| Justin                                        | Time                                          | Justin                                        | Tmecompler                                    | Justin                                        | Tmecompiler                                   | Justin                                        | Time                                          | Justin                                        | Tmecompler                                    |               |
| Srr                                           | Vlet                                          | Sr                                            | Vlet                                          | Sir                                           | Vlet                                          | Sir                                           | Vlet                                          | Sir                                           | Vlet                                          |               |
| Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           |                                               | Jay                                           | Espy                                          | Jay                                           | Espy                                          |               |
| fustname                                      | lastname                                      | furstname                                     | lastname                                      | fustname                                      | lastname                                      | fustname                                      | lastname                                      | furstname                                     | lastname                                      |               |
| Justin                                        | Tmmecompier                                   | Justin                                        | Tmnecompiler                                  | Justin                                        | Tmecompiler                                   | Justin                                        | ompder                                        | Justin                                        | Tmecompiler                                   |               |
| Srr                                           | Vlet                                          | Sir                                           | Vlet                                          | Sir                                           | Vlet                                          | Sir                                           | Vlet                                          | Sir                                           | Vlet                                          |               |
| Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          |               |
| fustuame                                      | lastname                                      | fustname                                      | lastname                                      | fustname                                      | lastname                                      | fustuame                                      | lastname                                      | fustname                                      | lastname                                      |               |
| Justin                                        | Immecompler                                   | Justin                                        | Imecompier                                    | Justin                                        | Tmecompiler                                   | Justin                                        |                                               | Justin                                        | Imecompler                                    |               |
| Sr                                            | Vlet                                          | Sr                                            | Vlet                                          | Sir                                           | Vlet                                          | Srr                                           | Vlet                                          |                                               | Vlet                                          |               |
| Jay                                           | Espy                                          | Jay                                           | Espy                                          |                                               | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          |               |
|                                               | lastname                                      | fustame                                       | lastname                                      | fustname                                      | lastname                                      | fustame                                       | lastname                                      | fustame                                       | lastname                                      |               |
| Justin                                        | Tmecompiler                                   | Justin                                        | Imecompiler                                   |                                               | Tmecompiler                                   | Justu                                         | Tmecompier                                    | Justin                                        | Imecompler                                    |               |
| Srr                                           | Vlet                                          |                                               | Vlet                                          | Srr                                           | Vlet                                          | Srr                                           | Vlet                                          |                                               | Vlet                                          |               |
| Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          | Jay                                           | Espy                                          |               |
| Document Done                                 | Document Done                                 | Document Done                                 | Document Done                                 | Document Done                                 | Document Done                                 | Document Done                                 | Document Done                                 | Document Done                                 | Document Done                                 | Document Done |

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.8 Connection Pooling: A Case Study

## Listing 18.22 ConnectionPoolServlet2.java

package coreservlets;

```
/** A variation of ConnectionPoolServlet that uses only *  a single connection, queueing up all requests to it. *  Used to compare timing results. */ public class ConnectionPoolServlet2 extends ConnectionPoolServlet { protected int initialConnections() { return(1); } protected int maxConnections() { return(1); } }
```

## Listing 18.23 ConnectionPoolServlet3.java package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.sql.*; /** A variation of ConnectionPoolServlet that does NOT *  use connection pooling. Used to compare timing *  benefits of connection pooling. */ public class ConnectionPoolServlet3 extends HttpServlet { private String url, username, password; public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { String table; String query = "SELECT firstname, lastname " + " FROM employees WHERE salary &gt; 70000"; try { Connection connection = DriverManager.getConnection(url, username, password);

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 18 JDBC and Database Connection Pooling

## response.setHeader("Cache-Control", "no-cache"); // HTTP 1.1 Listing 18.23 ConnectionPoolServlet3.java (continued)

```
DBResults results = DatabaseUtilities.getQueryResults(connection, query, true); table = results.toHTMLTable("#FFAD00"); } catch(Exception e) { table = "Exception: " + e; } response.setContentType("text/html"); // Prevent the browser from caching the response. See // Section 7.2 of Core Servlets and JSP for details. response.setHeader("Pragma", "no-cache"); // HTTP 1.0 PrintWriter out = response.getWriter(); String title = "Connection Pool Test (*No* Pooling)"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<CENTER>\n" + table + "\n" + "</CENTER>\n</BODY></HTML>"); } public void init() { try { int vendor = DriverUtilities.SYBASE; String driver = DriverUtilities.getDriver(vendor); Class.forName(driver); String host = "dbhost2.apl.jhu.edu"; String dbName = "605741"; url = DriverUtilities.makeURL(host, dbName, vendor); username = "hall"; password = "xxxx"; // Changed :-) } catch(ClassNotFoundException e) { System.err.println("Error initializing: " + e); getServletContext().log("Error initializing: " + e); } } }
```

## 18.9 Sharing Connection Pools

## 18.9 Sharing Connection Pools

In  the  previous  example,  each  servlet  had  its  own  connection  pool.  This approach makes sense when different servlets perform substantially different tasks and thus talk to different databases. However, it is also quite common for some or all of the servlets on a server to talk to the same database and thus to share a connection pool. There are two main approaches to sharing pools: using the servlet context (a servlet-specific technique) and using static methods or singleton classes (a general Java technique).

## Using the Servlet Context to Share Connection Pools

You can call the servlet getServletContext method to get an object of type ServletContext that is shared by all servlets on the server (or within a Web application if your server supports Web applications). This ServletContext object has a setAttribute method that takes a String and an Object and stores  the Object in  a  table  with  the String as  a  key.  You  can  obtain  the Object at  a  later  time  by  calling getAttribute with  the String (this method returns null if there is no value associated with the key).

So, for example, a group of servlets that all use the books database could share pools by having each servlet perform the following steps:

```
ServletContext context = getServletContext(); ConnectionPool bookPool = (ConnectionPool)context.getAttribute("book-pool"); if (bookPool == null) { bookPool = new ConnectionPool(...); context.setAttribute("book-pool", bookPool);
```

}

## Chapter 18 JDBC and Database Connection Pooling

## Using Singleton Classes to Share Connection Pools

Rather than using the ServletContext to  share connection pools, you can use normal static methods. For example, you could write a BookPool class with  static getPool and setPool methods  and  have  each  servlet  check BookPool.getPool to see if the value is non-null, instantiating a new ConnectionPool if necessary. However, each servlet has to repeat similar code, and  a  servlet  could  accidentally  overwrite  the  shared  pool  that BookPool.getPool returns.

A  better  approach  is  to  use  a singleton  class to  encapsulate  the  desired behavior. A singleton class is simply a class for which only a single instance can be created, enforced through use of a private constructor. The instance is retrieved  through a static method  that  checks  if  there  is  already  an  object allocated, returning it if so and allocating and returning a new one if not. For example, here is the outline of a singleton BookPool class. Each servlet that used it would obtain the connection pool by simply calling BookPool.getInstance() .

## 18.9 Sharing Connection Pools

```
public class BookPool extends ConnectionPool { private static BookPool pool = null; private BookPool(...) { super(...); // Call parent constructor ... } public static synchronized BookPool getInstance() { if (pool == null) { pool = new BookPool(...); } return(pool); } }
```

<!-- image -->

' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter Servlet and JSP Quick Reference

<!-- image -->