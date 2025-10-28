## 17.4 A Query Viewer That Uses Object Serialization and HTTP Tunneling

## 2. Create an ObjectOutputStream .

ObjectOutputStream out = new ObjectOutputStream(response.getOutputStream());

- 3. Write the data structure by using writeObject . Most

built-in data structures can be sent this way. Classes you write, however, must implement the Serializable interface. This is a simple requirement, however, since Serializable defines no methods. Simply declare that your class implements it.

SomeClass value = new SomeClass(...); out.writeObject(value);

- 4. Flush the stream to be sure all content has been sent to the client.

out.flush();

The following section gives an example of this approach.

## 17.4 A Query Viewer That Uses Object Serialization and HTTP Tunneling

Many people are curious about what types of queries are sent to the major search engines. This is partly idle curiosity ('Is it really true that 64 percent of the  queries  at  AltaVista  are  from  employers  looking  for  programmers  that know Java technology?') and partly so that HTML authors can arrange their page  content  to  fit  the  types  of  queries  normally  submitted,  hoping  to improve their site's ranking with the search engines.

This section presents an applet/servlet combination that displays the fictitious super-search-engine.com 'live,'  continually  updating  sample  queries to visitors that load their query viewer page. Listing 17.4 shows the main applet,  which makes  use  of  an  auxiliary  class  (Listing  17.5)  to  retrieve  the queries  in  a  background  thread.  Once  the  user  initiates  the  process,  the applet  places  a  sample  query  in  a  scrolling  text  area  every  half-second,  as shown in Figure 17-3. Finally, Listing 17.6 shows the servlet that generates the queries on the server. It generates a random sampling of actual recent user queries and sends 50 of them to the client for each request.

If you download the applet and servlet source code from http://www.coreservlets.com/ and  try this application yourself,  be aware that it will only work when you load the top-level HTML page by using

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 17 Using Applets As Servlet Front Ends

HTTP (i.e., by  using a URL of the  form http://... to  request  the  page from a Web server). Loading it directly off your disk through a file: URL fails  since  the  applet  connects  back  to  its  home  site  to  contact  the  servlet. Besides, URLConnection fails for non-HTTP applets in general.

## Listing 17.4 ShowQueries.java

```
import java.applet.Applet; import java.awt.*; import java.awt.event.*; import java.net.*;
```

/** Applet reads arrays of strings packaged inside

- *  a QueryCollection and places them in a scrolling
- *  TextArea. The QueryCollection obtains the strings
- *  by means of a serialized object input stream
- *  connected to the QueryGenerator servlet.

*/

public class ShowQueries extends Applet

```
implements ActionListener, Runnable { private TextArea queryArea; private Button startButton, stopButton, clearButton; private QueryCollection currentQueries; private QueryCollection nextQueries; private boolean isRunning = false; private String address = "/servlet/coreservlets.QueryGenerator"; private URL currentPage; public void init() { setBackground(Color.white); setLayout(new BorderLayout()); queryArea = new TextArea(); queryArea.setFont(new Font("Serif", Font.PLAIN, 14)); add(queryArea, BorderLayout.CENTER); Panel buttonPanel = new Panel(); Font buttonFont = new Font("SansSerif", Font.BOLD, 16); startButton = new Button("Start"); startButton.setFont(buttonFont); startButton.addActionListener(this); buttonPanel.add(startButton); stopButton = new Button("Stop"); stopButton.setFont(buttonFont); stopButton.addActionListener(this); buttonPanel.add(stopButton); clearButton = new Button("Clear TextArea");
```

## 17.4 A Query Viewer That Uses Object Serialization and HTTP Tunneling

## Listing 17.4 ShowQueries.java (continued)

```
clearButton.setFont(buttonFont); clearButton.addActionListener(this); buttonPanel.add(clearButton); add(buttonPanel, BorderLayout.SOUTH); currentPage = getCodeBase(); // Request a set of sample queries. They // are loaded in a background thread, and // the applet checks to see if they have finished // loading before trying to extract the strings. currentQueries = new QueryCollection(address, currentPage); nextQueries = new QueryCollection(address, currentPage);
```

}

/** If you press the "Start" button, the system

- *  starts a background thread that displays
- *  the queries in the TextArea. Pressing "Stop"
- *  halts the process, and "Clear" empties the
- *  TextArea.

*/

```
public void actionPerformed(ActionEvent event) { if (event.getSource() == startButton) { if (!isRunning) { Thread queryDisplayer = new Thread(this); isRunning = true; queryArea.setText(""); queryDisplayer.start(); showStatus("Started display thread..."); } else { showStatus("Display thread already running..."); } } else if (event.getSource() == stopButton) { isRunning = false; showStatus("Stopped display thread..."); } else if (event.getSource() == clearButton) { queryArea.setText(""); } }
```

/** The background thread takes the currentQueries

- *  object and every half-second places one of the queries
- *  the object holds into the bottom of the TextArea. When
- *  all of the queries have been shown, the thread copies
- *  the value of the nextQueries object into
- *  currentQueries, sends a new request to the server
- *  in order to repopulate nextQueries, and repeats
- *  the process.

*/

445

## Chapter 17 Using Applets As Servlet Front Ends

## Listing 17.4 ShowQueries.java (continued)

```
public void run() { while(isRunning) { showQueries(currentQueries); currentQueries = nextQueries; nextQueries = new QueryCollection(address, currentPage); } } private void showQueries(QueryCollection queryEntry) { // If request has been sent to server but the result // isn't back yet, poll every second. This should // happen rarely but is possible with a slow network // connection or an overloaded server. while(!queryEntry.isDone()) { showStatus("Waiting for data from server..."); pause(1); } showStatus("Received data from server..."); String[] queries = queryEntry.getQueries(); String linefeed = "\n"; // Put a string into TextArea every half-second. for(int i=0; i<queries.length; i++) { if (!isRunning) { return; } queryArea.append(queries[i]); queryArea.append(linefeed); pause(0.5); } } public void pause(double seconds) { try { Thread.sleep((long)(seconds*1000)); } catch(InterruptedException ie) {} } }
```

## 17.4 A Query Viewer That Uses Object Serialization and HTTP Tunneling

## Listing 17.5 QueryCollection.java

```
import java.net.*; import java.io.*;
```

/** When this class is built, it returns a value

- *  immediately, but this value returns false for isDone
- *  and null for getQueries. Meanwhile, it starts a Thread
- *  to request an array of query strings from the server,
- *  reading them in one fell swoop by means of an
- *  ObjectInputStream. Once they've all arrived, they
- *  are placed in the location getQueries returns,
- *  and the isDone flag is switched to true.
- *  Used by the ShowQueries applet.

*/

public class QueryCollection implements Runnable {

```
private String[] queries; private String[] tempQueries; private boolean isDone = false; private URL dataURL; public QueryCollection(String urlSuffix, URL currentPage) { try { // Only the URL suffix need be supplied, since // the rest of the URL is derived from the current page. String protocol = currentPage.getProtocol(); String host = currentPage.getHost(); int port = currentPage.getPort(); dataURL = new URL(protocol, host, port, urlSuffix); Thread queryRetriever = new Thread(this); queryRetriever.start(); } catch(MalformedURLException mfe) { isDone = true; } } public void run() { try { tempQueries = retrieveQueries(); queries = tempQueries; } catch(IOException ioe) { tempQueries = null; queries = null; } isDone = true; } public String[] getQueries() { return(queries); } public boolean isDone() { return(isDone); }
```

## Chapter 17 Using Applets As Servlet Front Ends

Figure 17-3 The ShowQueries applet in action.

<!-- image -->

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 17.4 A Query Viewer That Uses Object Serialization and HTTP Tunneling

```
Listing 17.6 QueryGenerator.java package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; /** Servlet that generates an array of strings and *  sends them via an ObjectOutputStream to applet *  or other Java client. */ public class QueryGenerator extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { boolean useNumbering = true; String useNumberingFlag = request.getParameter("useNumbering"); if ((useNumberingFlag == null) || useNumberingFlag.equals("false")) { useNumbering = false; } String contentType = "application/x-java-serialized-object"; response.setContentType(contentType); ObjectOutputStream out = new ObjectOutputStream(response.getOutputStream()); String[] queries = getQueries(useNumbering); // If you send a nonstandard data structure, be // sure it is defined with "implements Serializable". out.writeObject(queries); out.flush(); } public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } private String[] getQueries(boolean useNumbering) { String[] queries = new String[50]; for(int i=0; i<queries.length; i++) { queries[i] = randomQuery(); if (useNumbering) { queries[i] = "" + (i+1) + ": " + queries[i]; } } return(queries); }
```