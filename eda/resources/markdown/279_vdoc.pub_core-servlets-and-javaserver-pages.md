## Appendix A Servlet and JSP Quick Reference

## A.18 JDBC and Database Connection Pooling Basic Steps in Using JDBC

- 1. Load the JDBC driver. See http://java.sun.com/products/jdbc/drivers.html for available drivers. Example:

Class.forName(" package.DriverClass "); Class.forName("oracle.jdbc.driver.OracleDriver");

- 2. Define the connection URL. The exact format will be defined in the documentation that comes with the particular driver.

```
String host = "dbhost.yourcompany.com"; String dbName = "someName"; int port = 1234; String oracleURL = "jdbc:oracle:thin:@" + host + ":" + port + ":" + dbName; String sybaseURL = "jdbc:sybase:Tds:" + host  + ":" + port + ":" + "?SERVICENAME=" + dbName;
```

## 3. Establish the connection.

String username = "jay\_debesee";

String password = "secret";

Connection connection =

DriverManager.getConnection(oracleURL, username, password)

An optional part of this step is to look up information about the database by using the getMetaData method of Connection . This method returns a DatabaseMetaData object which has methods to let you discover the name and version of the database itself ( getDatabaseProductName , getDatabaseProductVersion ) or of the JDBC driver ( getDriverName , getDriverVersion ).

- 4. Create a statement object.

Statement statement = connection.createStatement();

- 5.
- Execute a query or update.

String query = "SELECT col1, col2, col3 FROM sometable"; ResultSet resultSet = statement.executeQuery(query);

- 6. Process the results. Use next to get a new row. Use

getXxx(index) or getXxx(columnName) to extract values from a row. First column has index 1, not 0.

while(resultSet.next()) {

System.out.println(results.getString(1) + " " +

results.getString(2) + " " +

results.getString(3));

}

## 7. Close the connection.

connection.close();

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.