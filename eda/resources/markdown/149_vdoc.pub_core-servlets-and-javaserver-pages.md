## 10. Send the real data.

byteStream.writeTo(connection.getOutputStream());

- 11. Open an input stream. You typically use a BufferedReader for ASCII or binary data and an ObjectInputStream for serialized Java objects.

```
BufferedReader in =
```

new BufferedReader(new InputStreamReader

```
(connection.getInputStream()));
```

## 12. Read the result.

The specific details will depend on what type of data the server sends. Here is an example that does something with each line sent by the server:

```
String line; while((line = in.readLine()) != null) { doSomethingWith(line); }
```

- 13. Pat yourself on the back. Yes, the procedure for handling POST is long and tedious. Fortunately, it is a relatively rote process. Besides, you can always download an example from www.coreservlets.com and use it as a starting point.

The next section gives an example of an applet that performs these steps.

## 17.6 An Applet That Sends POST Data

Listing 17.7 presents an applet that follows the approach outlined in the previous  section.  The  applet  uses  a URLConnection and  an  attached ByteArrayOutputStream to  send POST data  to  a  URL  the  user  specifies.  The applet also makes use of the LabeledTextField class, shown previously in Listing 2.2 and available for  download from http://www.coreservlets.com/ .

Figures  17-4  and  17-5  show  the  results  of  submitting  the  data  to  the ShowParameters servlet and EchoServer HTTP server, respectively.

## 17.6 An Applet That Sends POST Data

## Chapter 17 Using Applets As Servlet Front Ends

## Listing 17.7 SendPost.java

```
import java.applet.Applet; import java.awt.*; import java.awt.event.*; import java.net.*; import java.io.*;
```

/** Applet that reads firstName, lastName, and

- *  emailAddress parameters and sends them via
- *  POST to the host, port, and URI specified.

*/

public class SendPost extends Applet

```
implements ActionListener { private LabeledTextField firstNameField, lastNameField, emailAddressField, hostField, portField, uriField; private Button sendButton; private TextArea resultsArea; URL currentPage; public void init() { setBackground(Color.white); setLayout(new BorderLayout()); Panel inputPanel = new Panel(); inputPanel.setLayout(new GridLayout(9, 1)); inputPanel.setFont(new Font("Serif", Font.BOLD, 14)); firstNameField = new LabeledTextField("First Name:", 15); inputPanel.add(firstNameField); lastNameField = new LabeledTextField("Last Name:", 15); inputPanel.add(lastNameField); emailAddressField = new LabeledTextField("Email Address:", 25); inputPanel.add(emailAddressField); Canvas separator1 = new Canvas(); inputPanel.add(separator1); hostField = new LabeledTextField("Host:", 15); // Applets loaded over the network can only connect // to the server from which they were loaded. hostField.getTextField().setEditable(false); currentPage = getCodeBase(); // getHost returns empty string for applets from local disk. String host = currentPage.getHost(); String resultsMessage = "Results will be shown here..."; if (host.length() == 0) { resultsMessage = "Error: you must load this applet\n" +
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 17.6 An Applet That Sends POST Data

## Listing 17.7 SendPost.java (continued)

}

```
"from a real Web server via HTTP,\n" + "not from the local disk using\n" + "a 'file:' URL. It is fine,\n" + "however, if the Web server is\n" + "running on your local system."; setEnabled(false); } hostField.getTextField().setText(host); inputPanel.add(hostField); portField = new LabeledTextField("Port (-1 means default):", 4); String portString = String.valueOf(currentPage.getPort()); portField.getTextField().setText(portString); inputPanel.add(portField); uriField = new LabeledTextField("URI:", 40); String defaultURI = "/servlet/coreservlets.ShowParameters"; uriField.getTextField().setText(defaultURI); inputPanel.add(uriField); Canvas separator2 = new Canvas(); inputPanel.add(separator2); sendButton = new Button("Submit Data"); sendButton.addActionListener(this); Panel buttonPanel = new Panel(); buttonPanel.add(sendButton); inputPanel.add(buttonPanel); add(inputPanel, BorderLayout.NORTH); resultsArea = new TextArea(); resultsArea.setFont(new Font("Monospaced", Font.PLAIN, 14)); resultsArea.setText(resultsMessage); add(resultsArea, BorderLayout.CENTER); public void actionPerformed(ActionEvent event) { try { String protocol = currentPage.getProtocol(); String host = hostField.getTextField().getText(); String portString = portField.getTextField().getText(); int port; try { port = Integer.parseInt(portString); } catch(NumberFormatException nfe) { port = -1; // I.e., default port of 80 } String uri = uriField.getTextField().getText(); URL dataURL = new URL(protocol, host, port, uri); URLConnection connection = dataURL.openConnection(); // Make sure browser doesn't cache this URL.
```

connection.setUseCaches(false);

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 17 Using Applets As Servlet Front Ends

## Listing 17.7 SendPost.java (continued)

```
// Tell browser to allow me to send data to server. connection.setDoOutput(true); ByteArrayOutputStream byteStream = new ByteArrayOutputStream(512); // Grows if necessary // Stream that writes into buffer PrintWriter out = new PrintWriter(byteStream, true); String postData = "firstName=" + encodedValue(firstNameField) + "&lastName=" + encodedValue(lastNameField) + "&emailAddress=" + encodedValue(emailAddressField); // Write POST data into local buffer out.print(postData); out.flush(); // Flush since above used print, not println // POST requests are required to have Content-Length String lengthString = String.valueOf(byteStream.size()); connection.setRequestProperty ("Content-Length", lengthString); // Netscape sets the Content-Type to multipart/form-data // by default. So, if you want to send regular form data, // you need to set it to // application/x-www-form-urlencoded, which is the // default for Internet Explorer. If you send // serialized POST data with an ObjectOutputStream, // the Content-Type is irrelevant, so you could // omit this step. connection.setRequestProperty ("Content-Type", "application/x-www-form-urlencoded"); // Write POST data to real output stream byteStream.writeTo(connection.getOutputStream());
```

```
BufferedReader in = new BufferedReader(new InputStreamReader (connection.getInputStream())); String line; String linefeed = "\n"; resultsArea.setText(""); while((line = in.readLine()) != null) { resultsArea.append(line); resultsArea.append(linefeed); } } catch(IOException ioe) { // Print debug info in Java Console System.out.println("IOException: " + ioe); } }
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 17.6 An Applet That Sends POST Data

## Listing 17.7 SendPost.java (continued)

- // LabeledTextField is really a Panel with a Label and
- // TextField inside it. This extracts the TextField part,
- // gets the text inside it, URL-encodes it, and
- // returns the result.

private String encodedValue(LabeledTextField field) { String rawValue = field.getTextField().getText(); return(URLEncoder.encode(rawValue));

}

}

Figure 17-4 Result of using SendPost to send POST data to the ShowParameters servlet, which is presented in Section 3.4 (Example: Reading All Parameters).

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

Chapter 17 Using Applets As Servlet Front Ends

Figure 17-5 Result of using SendPost to send POST data to the EchoServer HTTP server, which is presented in Section 16.12 (A Debugging Web Server).

<!-- image -->