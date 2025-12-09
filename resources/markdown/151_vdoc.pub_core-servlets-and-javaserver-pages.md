' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

<!-- image -->

<!-- image -->

## Topics in This Chapter

- · The seven basic steps in connecting to databases
- · Simple database retrieval example
- · Some utilities that simplify JDBC usage
- · Formatting a database result as plain text or HTML
- · An interactive graphical query viewer
- · Precompiled queries
- · A connection pool library
- · A comparison of servlet performance with and without connection pooling
- · Sharing connection pools

Home page for this book: http://www.coreservlets.com.

Home page for sequel: http://www.moreservlets.com.

Servlet and JSP training courses: http://courses.coreservlets.com.

<!-- image -->

DBC  provides  a  standard  library  for  accessing  relational  databases. Using the JDBC API, you can access a wide variety of different SQL databases with exactly the same Java syntax. It is important to note that although  JDBC  standardizes  the  mechanism  for  connecting  to  databases, the syntax for sending queries and committing transactions, and the data structure  representing the result,  it does not attempt to standardize the SQL syntax. So, you can use any SQL extensions your database vendor supports. However, since most queries follow standard SQL syntax, using JDBC lets  you  change  database  hosts,  ports,  and  even  database  vendors with minimal changes in your code. J

DILBERT reprinted by permission of United Syndicate, Inc.

<!-- image -->

Officially, JDBC is not an acronym and thus does not stand for anything. Unofficially, 'Java Database Connectivity' is commonly used as the long form of the name.