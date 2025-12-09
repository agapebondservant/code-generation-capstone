}

## Connection pool timing results

| Condition                                                                                               | Average Time   |
|---------------------------------------------------------------------------------------------------------|----------------|
| Slow modem connection to database, 10 initial connections, 50 max connections ( ConnectionPoolServlet ) | 11 seconds     |
| Slow modem connection to database, recycling a single connection ( ConnectionPoolServlet2 )             | 22 seconds     |

## A.18 JDBC and Database Connection Pooling

background thread to allocate a new connection. Then, wait for the first available connection, whether or not it is the newly allocated one.

- if ((totalConnections() &lt; maxConnections) &amp;&amp;

!connectionPending) { // Pending = connecting in bg makeBackgroundConnection();

try {

wait(); // Give up lock and suspend self.

- } catch(InterruptedException ie) {}

return(getConnection()); // Try again.

## 4. Wait for a connection to become available.

This situation occurs when there is no idle connection and you've reached the limit on the number of connections. This waiting should be accomplished without continual polling. It is best to use the wait method, which gives up the thread synchronization lock and suspends the thread until notify or notifyAll is called.

try {

wait();

- } catch(InterruptedException ie) {}

return(getConnection());

## 5. Close connections when required.

Note that connections are closed when they are garbage collected, so you don't always have to close them explicitly. But, you sometimes want more explicit control over the process.

public synchronized void closeAllConnections() {

// The closeConnections method loops down Vector, calling

// close and ignoring any exceptions thrown.

closeConnections(availableConnections);

availableConnections = new Vector();

closeConnections(busyConnections);

busyConnections = new Vector();