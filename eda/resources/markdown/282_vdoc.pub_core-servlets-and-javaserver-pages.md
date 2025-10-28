## Appendix A Servlet and JSP Quick Reference

## · Use execute to perform operation.

statement.execute();

## Steps in Implementing Connection Pooling

If you don't care about implementation details, just use the ConnectionPool class developed in Chapter 18. Otherwise, follow these steps.

## 1. Preallocate the connections.

Perform this task in the class constructor. Call the constructor from servlet's init method. The following code uses vectors to store available idle connections and unavailable, busy connections.

availableConnections = new Vector(initialConnections); busyConnections = new Vector(); for(int i=0; i&lt;initialConnections; i++) {

availableConnections.addElement(makeNewConnection());

}

## 2. Manage available connections.

If a connection is required and an idle connection is available, put it in the list of busy connections and then return it. The busy list is used to check limits on the total number of connections as well as when the pool is instructed to explicitly close all connections. Discarding a connection opens up a slot that can be used by processes that needed a connection when the connection limit had been reached, so use notifyAll to tell all waiting threads to wake up and see if they can proceed.

public synchronized Connection getConnection()

throws SQLException {

- if (!availableConnections.isEmpty()) {

Connection existingConnection =

(Connection)availableConnections.lastElement(); int lastIndex = availableConnections.size() - 1; availableConnections.removeElementAt(lastIndex);

- if (existingConnection.isClosed()) { notifyAll(); // Freed up a spot for anybody waiting. return(getConnection()); // Repeat process.
- } else {

busyConnections.addElement(existingConnection); return(existingConnection);

}

}

## 3. Allocate new connections.

If a connection is required, there is no idle connection available, and the connection limit has not been reached, then start a

}