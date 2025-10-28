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