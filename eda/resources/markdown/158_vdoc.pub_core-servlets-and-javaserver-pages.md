## 18.7 Connection Pooling

## Listing 18.18 PreparedStatements.java (continued)

```
private static void printUsage() { System.out.println("Usage: PreparedStatements host " + "dbName username password " + "oracle|sybase [print]."); } }
```

## 18.7 Connection Pooling

Opening a connection to a database is a time-consuming process. For short queries, it can take much longer to open the connection than to perform the actual database retrieval. Consequently, it makes sense to reuse Connection objects  in  applications  that  connect  repeatedly  to  the  same  database.  This section presents a class for connection pooling :  preallocating  database  connections and recycling them as clients connect. Servlets and JSP pages can benefit  significantly  from  this  class  since  the  database  to  which  any  given servlet or JSP page connects is typically known in advance (e.g., specified in the init method). For example, the servlet shown in Section 18.8 shows a sevenfold performance gain by making use of this connection pool class.

A connection pool class should be able to perform the following tasks:

- 1. Preallocate the connections.
- 2. Manage available connections.
- 3. Allocate new connections.
- 4. Wait for a connection to become available.
- 5. Close connections when required.

I'll sketch out the approach to each of these steps here. The full code for the ConnectionPool class is shown in Listing 18.19. As with all classes in the book,  you  can  download  the  source  code  from http://www.coreservlets.com/ .

## 1. Preallocate the connections.

Perform this task in the class constructor. Allocating more connections in advance speeds things up if there will be many concurrent requests later but causes an initial delay. As a result, a servlet that preallocates very many connections should build the

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 18 JDBC and Database Connection Pooling

connection pool from its init method, and you should be sure that the servlet is initialized prior to a 'real' client request. The following code uses vectors to store available idle connections and unavailable, busy connections. Assume that makeNewConnection uses a URL, username, and password stored previously, then simply calls the getConnection method of DriverManager .

```
availableConnections = new Vector(initialConnections); busyConnections = new Vector(); for(int i=0; i<initialConnections; i++) { availableConnections.addElement(makeNewConnection()); }
```

## 2. Manage available connections.

If a connection is required and an idle connection is available, put it in the list of busy connections and then return it. The busy list is used to check limits on the total number of connections as well as when the pool is instructed to explicitly close all connections. One caveat: connections can time out, so before returning the connection, confirm that it is still open. If not, discard the connection and repeat the process. Discarding a connection opens up a slot that can be used by processes that needed a connection when the connection limit had been reached, so use notifyAll to tell all waiting threads to wake up and see if they can proceed (e.g., by allocating a new connection).

```
public synchronized Connection getConnection() throws SQLException { if (!availableConnections.isEmpty()) { Connection existingConnection = (Connection)availableConnections.lastElement(); int lastIndex = availableConnections.size() - 1; availableConnections.removeElementAt(lastIndex); if (existingConnection.isClosed()) { notifyAll(); // Freed up a spot for anybody waiting. return(getConnection()); // Repeat process. } else { busyConnections.addElement(existingConnection); return(existingConnection); } } }
```

## 3. Allocate new connections.

If a connection is required, there is no idle connection available, and the connection limit has not been reached, then start a background thread to allocate a new connection. Then, wait for the first available connection, whether or not it is the newly allocated one.

```
if ((totalConnections() < maxConnections) && !connectionPending) { // Pending = connecting in bg makeBackgroundConnection(); } try { wait(); // Give up lock and suspend self. } catch(InterruptedException ie) {} return(getConnection()); // Try again.
```

## 4. Wait for a connection to become available.

This situation occurs when there is no idle connection and you've reached the limit on the number of connections. This waiting should be accomplished without continual polling. The natural approach is to use the wait method, which gives up the thread synchronization lock and suspends the thread until notify or notifyAll is called. Since notifyAll could stem from several possible sources, threads that wake up still need to test to see if they can proceed. In this case, the simplest way to accomplish this task is to recursively repeat the process of trying to obtain a connection.

```
try { wait(); } catch(InterruptedException ie) {} return(getConnection());
```

It may be that you don't want to let clients wait and would rather throw an exception when no connections are available and the connection limit has been reached. In such a case, do the following instead:

throw new SQLException("Connection limit reached");

## 5. Close connections when required.

Note that connections are closed when they are garbage collected, so you don't always have to close them explicitly. But, you sometimes want more explicit control over the process.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.7 Connection Pooling

## Chapter 18 JDBC and Database Connection Pooling

```
public synchronized void closeAllConnections() { // The closeConnections method loops down Vector, calling // close and ignoring any exceptions thrown. closeConnections(availableConnections); availableConnections = new Vector(); closeConnections(busyConnections); busyConnections = new Vector(); }
```

The full class follows.

## Listing 18.19 ConnectionPool.java

```
package coreservlets; import java.sql.*; import java.util.*; /** A class for preallocating, recycling, and managing *  JDBC connections. */ public class ConnectionPool implements Runnable { private String driver, url, username, password; private int maxConnections; private boolean waitIfBusy; private Vector availableConnections, busyConnections; private boolean connectionPending = false; public ConnectionPool(String driver, String url, String username, String password, int initialConnections, int maxConnections, boolean waitIfBusy) throws SQLException { this.driver = driver; this.url = url; this.username = username; this.password = password; this.maxConnections = maxConnections; this.waitIfBusy = waitIfBusy; if (initialConnections > maxConnections) { initialConnections = maxConnections; } availableConnections = new Vector(initialConnections); busyConnections = new Vector(); for(int i=0; i<initialConnections; i++) { availableConnections.addElement(makeNewConnection()); } }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.7 Connection Pooling

## Listing 18.19 ConnectionPool.java (continued)

```
public synchronized Connection getConnection() throws SQLException { if (!availableConnections.isEmpty()) { Connection existingConnection = (Connection)availableConnections.lastElement(); int lastIndex = availableConnections.size() - 1; availableConnections.removeElementAt(lastIndex); // If connection on available list is closed (e.g., // it timed out), then remove it from available list // and repeat the process of obtaining a connection. // Also wake up threads that were waiting for a if (existingConnection.isClosed()) { notifyAll(); // Freed up a spot for anybody waiting return(getConnection()); } else { busyConnections.addElement(existingConnection); return(existingConnection); }
```

```
// connection because maxConnection limit was reached. } else { // Three possible cases: // 1) You haven't reached maxConnections limit. So //    establish one in the background if there isn't //    already one pending, then wait for //    the next available connection (whether or not //    it was the newly established one). // 2) You reached maxConnections limit and waitIfBusy //    flag is false. Throw SQLException in such a case. // 3) You reached maxConnections limit and waitIfBusy //    flag is true. Then do the same thing as in second //    part of step 1: wait for next available connection. if ((totalConnections() < maxConnections) && !connectionPending) { makeBackgroundConnection(); } else if (!waitIfBusy) { throw new SQLException("Connection limit reached"); } // Wait for either a new connection to be established // (if you called makeBackgroundConnection) or for // an existing connection to be freed up. try { wait(); } catch(InterruptedException ie) {} // Someone freed up a connection, so try again. return(getConnection()); } }
```

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.19 ConnectionPool.java (continued)

```
// You can't just make a new connection in the foreground // when none are available, since this can take several // seconds with a slow network connection. Instead, // start a thread that establishes a new connection, // then wait. You get woken up either when the new connection // is established or if someone finishes with an existing // connection. private void makeBackgroundConnection() { connectionPending = true; try { Thread connectThread = new Thread(this); connectThread.start(); } catch(OutOfMemoryError oome) { // Give up on new connection } } public void run() { try { Connection connection = makeNewConnection(); synchronized(this) { availableConnections.addElement(connection); connectionPending = false; notifyAll(); } } catch(Exception e) { // SQLException or OutOfMemory // Give up on new connection and wait for existing one // to free up. } } // This explicitly makes a new connection. Called in // the foreground when initializing the ConnectionPool, // and called in the background when running. private Connection makeNewConnection() throws SQLException { try { // Load database driver if not already loaded Class.forName(driver); // Establish network connection to database Connection connection = DriverManager.getConnection(url, username, password); return(connection); } catch(ClassNotFoundException cnfe) { // Simplify try/catch blocks of people using this by // throwing only one exception type. throw new SQLException("Can't find class for driver: " + driver); } }
```

## 18.7 Connection Pooling

## public synchronized void free(Connection connection) { busyConnections.removeElement(connection); availableConnections.addElement(connection); // Wake up threads that are waiting for a connection notifyAll(); } public synchronized int totalConnections() { return(availableConnections.size() + busyConnections.size()); } /** Close all the connections. Use with caution: *  be sure no connections are in use before *  calling. Note that you are not &lt;I&gt;required&lt;/I&gt; to *  call this when done with a ConnectionPool, since *  connections are guaranteed to be closed when *  garbage collected. But this method gives more control *  regarding when the connections are closed. */ public synchronized void closeAllConnections() { closeConnections(availableConnections); availableConnections = new Vector(); closeConnections(busyConnections); busyConnections = new Vector(); } private void closeConnections(Vector connections) { try { for(int i=0; i&lt;connections.size(); i++) { Connection connection = (Connection)connections.elementAt(i); if (!connection.isClosed()) { connection.close(); } } } catch(SQLException sqle) { // Ignore errors; garbage collect anyhow } } public synchronized String toString() { String info = "ConnectionPool(" + url + "," + username + ")" + ", available=" + availableConnections.size() + ", busy=" + busyConnections.size() + ", max=" + maxConnections; return(info); } } Listing 18.19 ConnectionPool.java (continued)

<!-- image -->