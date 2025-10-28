## Chapter 17 Using Applets As Servlet Front Ends

## Listing 17.6 QueryGenerator.java (continued)

```
// The real, honest-to-goodness queries people have sent :-) private String randomQuery() { String[] locations = { "Where ", "How " }; String[] actions = { "can I look for ", "can I find ", "can I get " }; String[] sources = { "information ", "resources ", "data ", "references " }; String[] prepositions = { "on ", "about ", "concerning " }; String[] subjects = { "the book Core Servlets and JavaServer Pages", "the text Core Servlets and JavaServer Pages", "Core Servlets and JavaServer Pages", "Core Servlets and JSP", "the book Core Web Programming (Java 2 Edition)", "Core Web Programming (Java 2 Edition)", "servlet programming", "JavaServer Pages", "JSP", "Java alternatives to CGI", "server-side Java" }; String[] endings = { "?", "?", "?", "?!", "?!!!?" }; String[][] sentenceTemplates = { locations, actions, sources, prepositions, subjects, endings }; String query = ""; for(int i=0; i<sentenceTemplates.length; i++) { query = query + randomEntry(sentenceTemplates[i]); } return(query); } private String randomEntry(String[] strings) { int index = (int)(Math.random()*strings.length); return(strings[index]); } }
```

## 17.5 Sending Data by POST and Processing the Results Directly (HTTP Tunneling)

With GET data, an applet has two options for the results of a submission: tell the browser  to display the  results (construct a URL object  and  call getAppletContext().showDocument )  or  process  the  results  itself  (construct  a URL object,  get  a URLConnection ,  open  an  input  stream,  and  read  the

## 17.5 Sending Data by POST and Processing the Results Directly

results). These two options are discussed in Sections 17.1 and 17.3, respectively. With POST data, however, only the second option is available since the URL constructor has no method to let you associate POST data with it. Sending POST data  has  some  of  the  same  advantages  and  disadvantages  as  when applets send GET data. The two main disadvantages are that the server-side program must be on the host from which the applet was loaded, and that the applet is required to display all the results itself: it cannot pass HTML to the browser in a portable manner. On the plus side, the server-side program can be simpler (not needing to wrap the results in HTML) and the applet can update its display without requiring the page to be reloaded. Furthermore, applets that communicate using POST can use serialized data streams to send data to a servlet, in addition to reading serialized data from servlets. This is quite  an  advantage,  since  serialized  data  simplifies  communication  and HTTP tunneling lets you piggyback on existing connections through firewalls even when direct socket connections are prohibited. Applets using GET can read serialized data (see Section 17.4) but are unable to send it since it is not legal to append arbitrary binary data to URLs.

Thirteen steps are required for the applet to send POST data to the server and  read  the  results,  as  shown  below.  Although  there  are  many  required steps,  each  step  is  relatively  simple.  The  code  is  slightly  simplified  by  the omission of try / catch blocks around the statements.

## 1. Create a URL object referring to the applet's home host.

As before, since the URL must refer to the host the applet came from, it makes the most sense to specify a URL suffix and construct the rest of the URL automatically.

URL currentPage = getCodeBase(); String protocol = currentPage.getProtocol(); String host = currentPage.getHost(); int port = currentPage.getPort(); String urlSuffix = "/servlet/SomeServlet"; URL dataURL = new URL(protocol, host, port, urlSuffix);

- 2. Create a URLConnection object. This object will be used to obtain input and output streams that connect to the server.

URLConnection connection = dataURL.openConnection();

- 3. Instruct the browser not to cache the results.

connection.setUseCaches(false);

- 4. Tell the system to permit you to send data, not just read it.

connection.setDoOutput(true);

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 17 Using Applets As Servlet Front Ends

- 5. Create a ByteArrayOutputStream to buffer the data that will be sent to the server. The purpose of the ByteArrayOutputStream here is the same as it is with the persistent (keep-alive) HTTP connections shown in Section 7.4 - to determine the size of the output so that the Content-Length header can be set. The ByteArrayOutputStream constructor specifies an initial buffer size, but this value is not critical since the buffer will grow automatically if necessary.

ByteArrayOutputStream byteStream = new ByteArrayOutputStream(512);

- 6. Attach an output stream to the ByteArrayOutputStream . to send normal form data. To send serial-

Use a PrintWriter ized data structures, use an ObjectOutputStream instead.

PrintWriter out = new PrintWriter(byteStream, true);

- 7. Put the data into the buffer. For form data, use print . For high-level serialized objects, use writeObject .
- 8. Set the Content-Length header. This header is required for POST data, even though it is unused with GET requests. connection.setRequestProperty ("Content-Length", String.valueOf(byteStream.size()));
- 9. Set the Content-Type header. Netscape uses multipart/form-data by default, but regular form data requires a setting of application/x-www-form-urlencoded , which is the default with Internet Explorer. So, for portability you should set this value explicitly when sending regular form data. The value is irrelevant when sending serialized data.

```
String val1 = URLEncoder.encode(someVal1); String val2 = URLEncoder.encode(someVal2); String data = "param1=" + val1 + "&param2=" + val2; // Note '&' out.print(data); // Note print, not println out.flush(); // Necessary since no println used
```

connection.setRequestProperty

("Content-Type", "application/x-www-form-urlencoded");