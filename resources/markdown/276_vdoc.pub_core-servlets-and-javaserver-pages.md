## A.17 Using Applets As Servlet Front Ends

## Sending Serialized Data: The Applet Code

- 1. Create a URL object referring to the applet's home host. It is best to specify a URL suffix and construct the rest of the URL automatically.

URL currentPage = getCodeBase(); String protocol = currentPage.getProtocol(); String host = currentPage.getHost(); int port = currentPage.getPort(); String urlSuffix = "/servlet/SomeServlet"; URL dataURL = new URL(protocol, host, port, urlSuffix);

- 2. Create a URLConnection object. The openConnection method of URL returns a URLConnection object. This object will be used to obtain streams with which to communicate. URLConnection connection = dataURL.openConnection();
- 3. Instruct the browser not to cache the URL data. connection.setUseCaches(false);
- 4. Set any desired HTTP headers. connection.setRequestProperty("header", "value");
- 5. Create an ObjectInputStream . The constructor for this class simply takes the raw input stream from the URLConnection . ObjectInputStream in = new ObjectInputStream(connection.getInputStream());
- 6. Read the data structure with readObject . The return type of readObject is Object , so you need to make a typecast to whatever more specific type the server actually sent. SomeClass value = (SomeClass)in.readObject(); doSomethingWith(value);
- 7. Close the input stream.

in.close();

## Sending Serialized Data: The Servlet Code

- 1. Specify that binary content is being sent. To do so, designate application/x-java-serialized-object as the MIME type of the response. This is the standard MIME type for objects encoded with an ObjectOutputStream , although in practice, since the applet (not the browser) is reading the result, the MIME type is not very important. See the discussion of Content-Type in Section 7.2 for more information on MIME types.
- String contentType = "application/x-java-serialized-object"; response.setContentType(contentType);