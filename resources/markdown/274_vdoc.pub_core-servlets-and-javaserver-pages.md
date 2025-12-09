## Appendix A Servlet and JSP Quick Reference

## Sending Data with GET and Processing the Results Directly (HTTP Tunneling)

- 1. Create a URL object referring to applet's home host. You usually build a URL based upon the hostname from which the applet was loaded.

URL currentPage = getCodeBase(); String protocol = currentPage.getProtocol(); String host = currentPage.getHost(); int port = currentPage.getPort(); String urlSuffix = "/servlet/SomeServlet"; URL dataURL = new URL(protocol, host, port, urlSuffix);

- 2. Create a URLConnection object. The openConnection method of URL returns a URLConnection object. This object will be used to obtain streams with which to communicate. URLConnection connection = dataURL.openConnection();
- 3. Instruct the browser not to cache the URL data. connection.setUseCaches(false);
- 4. Set any desired HTTP headers. If you want to set HTTP request headers (see Chapter 4), you can use setRequestProperty to do so.

connection.setRequestProperty("header", "value");

- 5. Create an input stream. There are several appropriate streams, but a common one is BufferedReader . It is at the point where you create the input stream that the connection to the Web server is actually established behind the scenes.

BufferedReader in =

new BufferedReader(new InputStreamReader(

connection.getInputStream()));

- 6. Read each line of the document. Simply read until you get

```
null . String line; while ((line = in.readLine()) != null) { doSomethingWith(line);
```

}

- 7. Close the input stream.

in.close();