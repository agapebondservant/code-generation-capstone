## Chapter 2 First Servlets

get confused, especially when your only change is to a lower-level class, not to the top-level servlet class. So, if it appears that changes you make to your servlets are not reflected in the servlet's behavior, try restarting the server. With the JSWDK and Tomcat, you have to do this every time you make a change, since these mini-servers have no support for automatic servlet reloading.

## 2.10 WebClient: Talking to Web Servers Interactively

This section presents the source code for the WebClient program discussed in  Section  2.9  (Debugging  Servlets)  and used in  Section 2.8 (An  Example Using  Servlet  Initialization  and  Page  Modification  Dates)  and  extensively throughout Chapter 16 (Using HTML Forms). As always, the source code can  be  downloaded  from  the  on-line  archive  at http://www.coreservlets.com/ , and there are no restrictions on its use.

## WebClient

This class is the top-level program that you would use. Start it from the command line, then customize the HTTP request line and request headers, then press 'Submit Request.'

```
Listing 2.12 WebClient.java import java.awt.*; import java.util.*; *  A graphical client that lets you interactively connect to
```

```
public class WebClient extends CloseableFrame public static void main(String[] args) { new WebClient("Web Client"); }
```

```
import java.awt.event.*; /** *  Web servers and send custom request lines and *  request headers. */ implements Runnable, Interruptible, ActionListener {
```

## 2.10 WebClient: Talking to Web Servers Interactively

## Listing 2.12 WebClient.java (continued)

```
private LabeledTextField hostField, portField, requestLineField; private TextArea requestHeadersArea, resultArea; private String host, requestLine; private int port; private String[] requestHeaders = new String[30]; private Button submitButton, interruptButton; private boolean isInterrupted = false; public WebClient(String title) { super(title); setBackground(Color.lightGray); setLayout(new BorderLayout(5, 30)); int fontSize = 14; Font labelFont = new Font("Serif", Font.BOLD, fontSize); Font headingFont = new Font("SansSerif", Font.BOLD, fontSize+4); Font textFont = new Font("Monospaced", Font.BOLD, fontSize-2); Panel inputPanel = new Panel(); inputPanel.setLayout(new BorderLayout()); Panel labelPanel = new Panel(); labelPanel.setLayout(new GridLayout(4,1)); hostField = new LabeledTextField("Host:", labelFont, 30, textFont); portField = new LabeledTextField("Port:", labelFont, "80", 5, textFont); // Use HTTP 1.0 for compatibility with the most servers. // If you switch this to 1.1, you *must* supply a // Host: request header. requestLineField = new LabeledTextField("Request Line:", labelFont, "GET / HTTP/1.0", 50, textFont); labelPanel.add(hostField); labelPanel.add(portField); labelPanel.add(requestLineField); Label requestHeadersLabel = new Label("Request Headers:"); requestHeadersLabel.setFont(labelFont); labelPanel.add(requestHeadersLabel); inputPanel.add(labelPanel, BorderLayout.NORTH); requestHeadersArea = new TextArea(5, 80); requestHeadersArea.setFont(textFont); inputPanel.add(requestHeadersArea, BorderLayout.CENTER); Panel buttonPanel = new Panel(); submitButton = new Button("Submit Request"); submitButton.addActionListener(this); submitButton.setFont(labelFont); buttonPanel.add(submitButton);
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 54

## Chapter 2 First Servlets

## Listing 2.12 WebClient.java (continued)

```
inputPanel.add(buttonPanel, BorderLayout.SOUTH); add(inputPanel, BorderLayout.NORTH); Panel resultPanel = new Panel(); resultPanel.setLayout(new BorderLayout()); Label resultLabel = new Label("Results", Label.CENTER); resultLabel.setFont(headingFont); resultPanel.add(resultLabel, BorderLayout.NORTH); resultArea = new TextArea(); resultArea.setFont(textFont); resultPanel.add(resultArea, BorderLayout.CENTER); Panel interruptPanel = new Panel(); interruptButton = new Button("Interrupt Download"); interruptButton.addActionListener(this); interruptButton.setFont(labelFont); interruptPanel.add(interruptButton); resultPanel.add(interruptPanel, BorderLayout.SOUTH); add(resultPanel, BorderLayout.CENTER); setSize(600, 700); setVisible(true); } public void actionPerformed(ActionEvent event) { if (event.getSource() == submitButton) { Thread downloader = new Thread(this); downloader.start(); } else if (event.getSource() == interruptButton) { isInterrupted = true; } } public void run() { isInterrupted = false; if (hasLegalArgs()) new HttpClient(host, port, requestLine, requestHeaders, resultArea, this); } public boolean isInterrupted() { return(isInterrupted); } private boolean hasLegalArgs() { host = hostField.getTextField().getText(); if (host.length() == 0) { report("Missing hostname"); return(false); }
```

## 2.10 WebClient: Talking to Web Servers Interactively

## Listing 2.12 WebClient.java (continued)

```
String portString = portField.getTextField().getText(); if (portString.length() == 0) { report("Missing port number"); return(false); } try { port = Integer.parseInt(portString); } catch(NumberFormatException nfe) { report("Illegal port number: " + portString); return(false); } requestLine = requestLineField.getTextField().getText(); if (requestLine.length() == 0) { report("Missing request line"); return(false); } getRequestHeaders(); return(true); } private void report(String s) { resultArea.setText(s); } private void getRequestHeaders() { for(int i=0; i<requestHeaders.length; i++) requestHeaders[i] = null; int headerNum = 0; String header = requestHeadersArea.getText(); StringTokenizer tok = new StringTokenizer(header, "\r\n"); while (tok.hasMoreTokens()) requestHeaders[headerNum++] = tok.nextToken(); } }
```

## HttpClient

The HttpClient class does the real network communication. It simply sends the  designated  request  line  and  request  headers  to  the  Web  server,  then reads the lines that come back one at a time, placing them into a TextArea until  either  the  server  closes  the  connection  or  the HttpClient is  interrupted by means of the isInterrupted flag.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 2 First Servlets

## Listing 2.13 HttpClient.java

```
import java.awt.*; import java.net.*; import java.io.*; /** *  The underlying network client used by WebClient. */ public class HttpClient extends NetworkClient { private String requestLine; private String[] requestHeaders; private TextArea outputArea; private Interruptible app; public HttpClient(String host, int port, String requestLine, String[] requestHeaders, TextArea outputArea, Interruptible app) { super(host, port); this.requestLine = requestLine; this.requestHeaders = requestHeaders; this.outputArea = outputArea; this.app = app; if (checkHost(host)) connect(); } protected void handleConnection(Socket uriSocket) throws IOException { try { PrintWriter out = SocketUtil.getWriter(uriSocket); BufferedReader in = SocketUtil.getReader(uriSocket); outputArea.setText(""); out.println(requestLine); for(int i=0; i<requestHeaders.length; i++) { if (requestHeaders[i] == null) break; else out.println(requestHeaders[i]); } out.println(); String line; while ((line = in.readLine()) != null && !app.isInterrupted()) outputArea.append(line + "\n"); if (app.isInterrupted()) outputArea.append("---- Download Interrupted ----"); } catch(Exception e) { outputArea.setText("Error: " + e); } }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 2.10 WebClient: Talking to Web Servers Interactively

## outputArea.setText("Bogus host: " + host); Listing 2.13 HttpClient.java (continued)

```
private boolean checkHost(String host) { try { InetAddress.getByName(host); return(true); } catch(UnknownHostException uhe) { return(false); } } }
```

## NetworkClient

The NetworkClient class is a generic starting point for network clients and is extended by HttpClient .

## Listing 2.14 NetworkClient.java

```
import java.net.*; import java.io.*; /** A starting point for network clients. You'll need to *  override handleConnection, but in many cases *  connect can remain unchanged. It uses *  SocketUtil to simplify the creation of the *  PrintWriter and BufferedReader. * * @see SocketUtil */ public class NetworkClient { protected String host; protected int port; /** Register host and port. The connection won't *  actually be established until you call *  connect. * * @see #connect */ public NetworkClient(String host, int port) { this.host = host; this.port = port;
```

```
}
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 2 First Servlets

## Listing 2.14 NetworkClient.java (continued)

```
/** Establishes the connection, then passes the socket *  to handleConnection. * * @see #handleConnection */ public void connect() { try { Socket client = new Socket(host, port); handleConnection(client); } catch(UnknownHostException uhe) { System.out.println("Unknown host: " + host); uhe.printStackTrace(); } catch(IOException ioe) { System.out.println("IOException: " + ioe); ioe.printStackTrace(); } } /** This is the method you will override when *  making a network client for your task. *  The default version sends a single line *  ("Generic Network Client") to the server, *  reads one line of response, prints it, then exits. */ protected void handleConnection(Socket client) throws IOException { PrintWriter out = SocketUtil.getWriter(client); BufferedReader in = SocketUtil.getReader(client); out.println("Generic Network Client"); System.out.println ("Generic Network Client:\n" + "Made connection to " + host + " and got '" + in.readLine() + "' in response"); client.close(); } /** The hostname of the server we're contacting. */ public String getHost() { return(host); } /** The port connection will be made on. */ public int getPort() { return(port); } }
```

## SocketUtil

SocketUtil is  a  simple  utility  class  that  simplifies  creating  some  of  the streams  used  in  network  programming.  It  is  used  by NetworkClient and HttpClient .

## Listing 2.15 SocketUtil.java import java.net.*; import java.io.*; /** A shorthand way to create BufferedReaders and *  PrintWriters associated with a Socket. */ public class SocketUtil { /** Make a BufferedReader to get incoming data. */ public static BufferedReader getReader(Socket s) throws IOException { return(new BufferedReader( new InputStreamReader(s.getInputStream()))); } /** Make a PrintWriter to send outgoing data. *  This PrintWriter will automatically flush stream *  when println is called. */ public static PrintWriter getWriter(Socket s) throws IOException { // 2nd argument of true means autoflush return(new PrintWriter(s.getOutputStream(), true)); } }

## 2.10 WebClient: Talking to Web Servers Interactively

## Chapter 2 First Servlets

## CloseableFrame

CloseableFrame is an extension of the standard Frame class, with the addition that user requests to quit the frame are honored. This is the top-level window on which WebClient is built.

```
Listing 2.16 CloseableFrame.java
```

```
import java.awt.*;
```

```
import java.awt.event.*; /** A Frame that you can actually quit. Used as *  the starting point for most Java 1.1 graphical *  applications. */ public class CloseableFrame extends Frame { public CloseableFrame(String title) { super(title); enableEvents(AWTEvent.WINDOW_EVENT_MASK); } /** Since we are doing something permanent, we need *  to call super.processWindowEvent <B>first</B>. */ public void processWindowEvent(WindowEvent event) { super.processWindowEvent(event); // Handle listeners if (event.getID() == WindowEvent.WINDOW_CLOSING) System.exit(0); } }
```

## 2.10 WebClient: Talking to Web Servers Interactively

## LabeledTextField

The LabeledTextField class is a simple combination of a TextField and a Label and is used in WebClient .

## Listing 2.17 LabeledTextField.java

```
import java.awt.*; /** A TextField with an associated Label. */ public class LabeledTextField extends Panel { private Label label; private TextField textField; public LabeledTextField(String labelString, Font labelFont, int textFieldSize, Font textFont) { setLayout(new FlowLayout(FlowLayout.LEFT)); label = new Label(labelString, Label.RIGHT); if (labelFont != null) label.setFont(labelFont); add(label); textField = new TextField(textFieldSize); if (textFont != null) textField.setFont(textFont); add(textField); } public LabeledTextField(String labelString, String textFieldString) { this(labelString, null, textFieldString, textFieldString.length(), null); } public LabeledTextField(String labelString, int textFieldSize) { this(labelString, null, textFieldSize, null); } public LabeledTextField(String labelString, Font labelFont, String textFieldString, int textFieldSize, Font textFont) { this(labelString, labelFont, textFieldSize, textFont); textField.setText(textFieldString); }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

61

## 62 Chapter 2 First Servlets

## Listing 2.17 LabeledTextField.java (continued)

```
/** The Label at the left side of the LabeledTextField. *  To manipulate the Label, do: *  <PRE> *    LabeledTextField ltf = new LabeledTextField(...); *    ltf.getLabel().someLabelMethod(...); *  </PRE> * * @see #getTextField */ public Label getLabel() { return(label); } /** The TextField at the right side of the *  LabeledTextField. * * @see #getLabel */ public TextField getTextField() { return(textField); } }
```

## 2.10 WebClient: Talking to Web Servers Interactively

## Interruptible

Interruptible is  a  simple  interface  used  to  identify  classes  that  have  an isInterrupted method. It is used by HttpClient to poll WebClient to see if the user has interrupted it.

## Listing 2.18 Interruptible.java

/**

- *  An interface for classes that can be polled to see
- *  if they've been interrupted. Used by HttpClient
- *  and WebClient to allow the user to interrupt a network
- *  download.

*/

```
public interface Interruptible { public boolean isInterrupted(); }
```

63