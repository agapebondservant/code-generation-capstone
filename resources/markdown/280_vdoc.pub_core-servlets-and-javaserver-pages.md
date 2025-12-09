## A.18 JDBC and Database Connection Pooling

## Database Utilities

These are static methods in the DatabaseUtilities class (Listing 18.6).

## · getQueryResults

Connects to a database, executes a query, retrieves all the rows as arrays of strings, and puts them inside a DBResults object (see Listing 18.7). Also places the database product name, database version, the names of all the columns and the Connection object into the DBResults object. There are two versions of getQueryResults : one makes a new connection, the other uses an existing connection. DBResults has a simple toHTMLTable method that outputs result in HTML, which can be used as either a real HTML table or as an Excel spreadsheet (see Section 11.2).

## · createTable

Given a table name, a string denoting the column formats, and an array of strings denoting the row values, this method connects to a database, removes any existing versions of the designated table, issues a CREATE TABLE command with the designated format, then sends a series of INSERT INTO commands for each of the rows. Again, there are two versions: one makes a new connection, and the other uses an existing connection.

## · printTable

Given a table name, this method connects to the specified database, retrieves all the rows, and prints them on the standard output. It retrieves the results by turning the table name into a query of the form ' SELECT * FROM tableName ' and passing it to getQueryResults .

## · printTableData

Given a DBResults object from a previous query, this method prints it on the standard output. This is the underlying method used by printTable , but it is also useful for debugging arbitrary database results.

## Prepared Statements (Precompiled Queries)

- · Use connection.prepareStatement to make precompiled form. Mark parameters with question marks.

String template =

"UPDATE employees SET salary = ? WHERE id = ?";

PreparedStatement statement =

connection.prepareStatement(template);

## · Use statement.set Xxx to specify parameters to query.

```
statement.setFloat(1, 1.234); statement.setInt(2, 5);
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.