## 16.12 A Debugging Web Server

Figure 16-26 In Internet Explorer, repeatedly pressing the TAB key cycles the input focus among the first, third, and second text fields, in that order (as dictated by TABINDEX ). In Netscape, the input focus would cycle among the first, second, and third fields, in that order (based on the order the elements appear on the page).

<!-- image -->

## 16.12 A Debugging Web Server

This section presents a mini 'Web server' that is useful when you are trying to understand the behavior of HTML forms. I used it for many of the examples earlier in the chapter. It simply reads all the HTTP data sent to it by the browser, then returns a Web page with those lines embedded within a PRE element. This server is also extremely useful for debugging servlets. When something goes wrong, the first task is to determine if the problem lies in the way in which you collect data or the way in which you process it. Starting the EchoServer on,  say,  port  8088  of  your  local  machine,  then  changing  your forms to specify http://localhost:8088/ lets you see if the data being collected is in the format you expect.

## EchoServer

Listing 16.9 presents the top-level server code. You typically run it from the command line, specifying a port to listen on or accepting the default of 8088. It  then  accepts  repeated  HTTP requests from clients, packaging all HTTP data sent to it inside a Web page that is returned to the client. In most cases, the server reads until it gets a blank line, indicating the end of GET , HEAD , or most other types of HTTP requests. In the case of POST , however, the server checks  the Content-Length request  header  and  reads  that  many  bytes beyond the blank line.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 424

## Chapter 16 Using HTML Forms

## Listing 16.9 EchoServer.java

```
import java.net.*; import java.io.*;
```

import java.util.StringTokenizer;

/** A simple HTTP server that generates a Web page

- *  showing all the data that it received from
- *  the Web client (usually a browser). To use this,
- *  start it on the system of your choice, supplying
- *  a port number if you want something other than
- *  port 8088. Call this system server.com. Next,
- *  start a Web browser on the same or a different
- *  system, and connect to http://server.com:8088/whatever.
- *  The resultant Web page will show the data that your browser
- *  sent. For debugging in servlet or CGI programming,
- *  specify http://server.com:8088/whatever as the
- *  ACTION of your HTML form. You can send GET
- *  or POST data; either way, the resultant page
- *  will show what your browser sent.

*/

public class EchoServer extends NetworkServer {

protected int maxRequestLines = 50; protected String serverName = "EchoServer";

```
/** Supply a port number as a command-line *  argument. Otherwise port 8088 will be used. */ public static void main(String[] args) { int port = 8088; if (args.length > 0) { try { port = Integer.parseInt(args[0]); } catch(NumberFormatException nfe) {} } new EchoServer(port, 0); } public EchoServer(int port, int maxConnections) { super(port, maxConnections); listen(); }
```

/** Overrides the NetworkServer handleConnection

- *  method to read each line of data received, save it
- *  into an array of strings, then send it
- *  back embedded inside a PRE element in an
- *  HTML page.

*/

## 16.12 A Debugging Web Server

## public void handleConnection(Socket server) throws IOException{ System.out.println (serverName + ": got connection from " + server.getInetAddress().getHostName()); BufferedReader in = SocketUtil.getReader(server); PrintWriter out = SocketUtil.getWriter(server); String[] inputLines = new String[maxRequestLines]; int i; for (i=0; i&lt;maxRequestLines; i++) { inputLines[i] = in.readLine(); if (inputLines[i] == null) // Client closed connection break; if (inputLines[i].length() == 0) { // Blank line if (usingPost(inputLines)) { readPostData(inputLines, i, in); i = i + 2; } break; } } printHeader(out); for (int j=0; j&lt;i; j++) { out.println(inputLines[j]); } printTrailer(out); server.close(); } // Send standard HTTP response and top of a standard Web page. // Use HTTP 1.0 for compatibility with all clients. private void printHeader(PrintWriter out) { out.println ("HTTP/1.0 200 OK\r\n" + "Server: " + serverName + "\r\n" + "Content-Type: text/html\r\n" + "\r\n" + "&lt;!DOCTYPE HTML PUBLIC " + "\"-//W3C//DTD HTML 4.0 Transitional//EN\"&gt;\n" + "&lt;HTML&gt;\n" + "&lt;HEAD&gt;\n" + "  &lt;TITLE&gt;" + serverName + " Results&lt;/TITLE&gt;\n" + "&lt;/HEAD&gt;\n" + "\n" + "&lt;BODY BGCOLOR=\"#FDF5E6\"&gt;\n" + "&lt;H1 ALIGN=\"CENTER\"&gt;" + serverName + " Results&lt;/H1&gt;\n" + Listing 16.9 EchoServer.java (continued)

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 16 Using HTML Forms

## Listing 16.9 EchoServer.java (continued)

```
"Here is the request line and request headers\n" + "sent by your browser:\n" + "<PRE>"); } // Print bottom of a standard Web page. private void printTrailer(PrintWriter out) { out.println ("</PRE>\n" + "</BODY>\n" + "</HTML>\n"); } // Normal Web page requests use GET, so this // server can simply read a line at a time. // However, HTML forms can also use POST, in which // case we have to determine the number of POST bytes // that are sent so we know how much extra data // to read after the standard HTTP headers. private boolean usingPost(String[] inputs) { return(inputs[0].toUpperCase().startsWith("POST")); } private void readPostData(String[] inputs, int i, BufferedReader in) throws IOException { int contentLength = contentLength(inputs); char[] postData = new char[contentLength]; in.read(postData, 0, contentLength); inputs[++i] = new String(postData, 0, contentLength); } // Given a line that starts with Content-Length, // this returns the integer value specified. private int contentLength(String[] inputs) { String input; for (int i=0; i<inputs.length; i++) { if (inputs[i].length() == 0) break; input = inputs[i].toUpperCase(); if (input.startsWith("CONTENT-LENGTH")) return(getLength(input)); } return(0); }
```

## 16.12 A Debugging Web Server

## Listing 16.9 EchoServer.java (continued)

```
private int getLength(String length) { StringTokenizer tok = new StringTokenizer(length); tok.nextToken(); return(Integer.parseInt(tok.nextToken())); } }
```

## ThreadedEchoServer

Listing 16.10 presents a multithreaded variation of the EchoServer ,  useful when your server needs to accept multiple simultaneous client requests.

## Listing 16.10 ThreadedEchoServer.java

```
import java.net.*; import java.io.*; /** A multithreaded variation of EchoServer. */ public class ThreadedEchoServer extends EchoServer implements Runnable { public static void main(String[] args) { int port = 8088; if (args.length > 0) { try { port = Integer.parseInt(args[0]); } catch(NumberFormatException nfe) {} } ThreadedEchoServer echoServer = new ThreadedEchoServer(port, 0); echoServer.serverName = "Threaded Echo Server"; } public ThreadedEchoServer(int port, int connections) { super(port, connections); }
```

/** The new version of handleConnection starts

- *  a thread. This new thread will call back to the
- *  &lt;I&gt;old&lt;/I&gt; version of handleConnection, resulting
- *  in the same server behavior in a multithreaded
- *  version. The thread stores the Socket instance
- *  since run doesn't take any arguments, and since
- *  storing the socket in an instance variable risks
- *  having it overwritten if the next thread starts

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 16 Using HTML Forms

## Listing 16.10 ThreadedEchoServer.java (continued)

```
*  before the run method gets a chance to *  copy the socket reference. */ public void handleConnection(Socket server) { Connection connectionThread = new Connection(this, server); connectionThread.start(); } public void run() { Connection currentThread = (Connection)Thread.currentThread(); try { super.handleConnection(currentThread.serverSocket); } catch(IOException ioe) { System.out.println("IOException: " + ioe); ioe.printStackTrace(); } } } /** This is just a Thread with a field to store a *  Socket object. Used as a thread-safe means to pass *  the Socket from handleConnection to run. */ class Connection extends Thread { protected Socket serverSocket; public Connection(Runnable serverObject, Socket serverSocket) { super(serverObject); this.serverSocket = serverSocket; } }
```

## NetworkServer

Listings 16.11 and 16.12 present some utilities classes that simplify networking. The EchoServer is built on top of them.

## 16.12 A Debugging Web Server

## Listing 16.11 NetworkServer.java

```
import java.net.*; import java.io.*;
```

/** A starting point for network servers. You'll need to

- *  override handleConnection, but in many cases
- *  listen can remain unchanged. NetworkServer uses
- *  SocketUtil to simplify the creation of the
- *  PrintWriter and BufferedReader.
- *  @see SocketUtil

*/

```
public class NetworkServer { private int port, maxConnections;
```

/** Build a server on specified port. It will continue

- *  to accept connections, passing each to
- *  handleConnection, until an explicit exit
- *  command is sent (e.g., System.exit) or the
- *  maximum number of connections is reached. Specify
- *  0 for maxConnections if you want the server
- *  to run indefinitely.

*/

public NetworkServer(int port, int maxConnections) { setPort(port);

setMaxConnections(maxConnections);

}

/** Monitor a port for connections. Each time one

- *  is established, pass resulting Socket to
- *  handleConnection.

*/

```
public void listen() { int i=0; try { ServerSocket listener = new ServerSocket(port); Socket server; while((i++ < maxConnections) || (maxConnections == 0)) { server = listener.accept(); handleConnection(server); } } catch (IOException ioe) { System.out.println("IOException: " + ioe); ioe.printStackTrace(); } }
```

<!-- image -->

## Chapter 16 Using HTML Forms

## Listing 16.11 NetworkServer.java (continued)

/** This is the method that provides the behavior

- *  to the server, since it determines what is
- *  done with the resulting socket. &lt;B&gt;Override this
- *  method in servers you write.&lt;/B&gt;
- *  &lt;P&gt;
- *  This generic version simply reports the host
- *  that made the connection, shows the first line
- *  the client sent, and sends a single line
- *  in response.

*/

```
protected void handleConnection(Socket server) throws IOException{ BufferedReader in = SocketUtil.getReader(server); PrintWriter out = SocketUtil.getWriter(server); System.out.println ("Generic Network Server: got connection from " + server.getInetAddress().getHostName() + "\n" + "with first line '" + in.readLine() + "'"); out.println("Generic Network Server"); server.close(); }
```

/** Gets the max connections server will handle before

- *  exiting. A value of 0 indicates that server
- *  should run until explicitly killed.

*/

```
public int getMaxConnections() { return(maxConnections);
```

}

/** Sets max connections. A value of 0 indicates that

*  server should run indefinitely (until explicitly *  killed).

*/

```
public void setMaxConnections(int maxConnections) { this.maxConnections = maxConnections; } /** Gets port on which server is listening. */ public int getPort() { return(port); }
```

## 16.12 A Debugging Web Server

## Listing 16.11 NetworkServer.java (continued)

```
/** Sets port. <B>You can only do before "connect" *  is called.</B> That usually happens in the constructor. */ protected void setPort(int port) { this.port = port; } }
```

## Listing 16.12

```
SocketUtil.java
```

```
import java.net.*; import java.io.*; /** A shorthand way to create BufferedReaders and *  PrintWriters associated with a Socket. */ public class SocketUtil { /** Make a BufferedReader to get incoming data. */ public static BufferedReader getReader(Socket s) throws IOException { return(new BufferedReader( new InputStreamReader(s.getInputStream()))); } /** Make a PrintWriter to send outgoing data. *  This PrintWriter will automatically flush stream *  when println is called. */ public static PrintWriter getWriter(Socket s) throws IOException { // 2nd argument of true means autoflush return(new PrintWriter(s.getOutputStream(), true)); } }
```