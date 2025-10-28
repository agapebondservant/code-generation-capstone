## Appendix A Servlet and JSP Quick Reference

- 2. Create an ObjectOutputStream.

ObjectOutputStream out =

new ObjectOutputStream(response.getOutputStream());

- 3. Write the data structure by using writeObject . Most built-in data structures can be sent this way. Classes you write, however, must implement the Serializable interface. SomeClass value = new SomeClass(...); out.writeObject(value);
- 4. Flush the stream to be sure all content has been sent to the client.

out.flush();

## Sending Data by POST and Processing the Results Directly (HTTP Tunneling)

- 1. Create a URL object referring to the applet's home host. It is best to specify a URL suffix and construct the rest of the URL automatically.

URL currentPage = getCodeBase(); String protocol = currentPage.getProtocol(); String host = currentPage.getHost(); int port = currentPage.getPort(); String urlSuffix = "/servlet/SomeServlet"; URL dataURL =

new URL(protocol, host, port, urlSuffix);

- 2. Create a URLConnection object.

URLConnection connection = dataURL.openConnection();

- 3. Instruct the browser not to cache the results. connection.setUseCaches(false);
- 4. Tell the system to permit you to send data, not just read it.

connection.setDoOutput(true);

- 5. Create a ByteArrayOutputStream to buffer the data that will be sent to the server. The purpose of the ByteArrayOutputStream here is the same as it is with the persistent (keep-alive) HTTP connections shown in Section 7.4 - to determine the size of the output so that the Content-Length header can be set.

ByteArrayOutputStream byteStream = new ByteArrayOutputStream(512);

- 6. Attach an output stream to the ByteArrayOutputStream . Use a PrintWriter to send normal form data. To send serialized data structures, use an ObjectOutputStream instead. PrintWriter out = new PrintWriter(byteStream, true);