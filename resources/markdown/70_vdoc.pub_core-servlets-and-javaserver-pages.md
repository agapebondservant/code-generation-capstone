## 7.4 Using Persistent HTTP Connections

## Listing 7.5 ServletUtilities.java

```
package coreservlets; import javax.servlet.*; import javax.servlet.http.*; public class ServletUtilities { // ... Other utilities shown earlier
```

```
/** Read a parameter with the specified name, convert it *  to an int, and return it. Return the designated default *  value if the parameter doesn't exist or if it is an *  illegal integer format. */ public static int getIntParameter(HttpServletRequest request,
```

```
String paramName, int defaultValue) { String paramString = request.getParameter(paramName); int paramValue; try { paramValue = Integer.parseInt(paramString); } catch(NumberFormatException nfe) { // null or bad format paramValue = defaultValue; } return(paramValue); } // ... }
```

## 7.4 Using Persistent HTTP Connections

One of the problems with HTTP 1.0 was that it required a separate socket connection for each request. When a Web page that includes lots of small images or many applet classes is retrieved, the overhead of establishing all the connections could be significant compared to the actual download time of the documents. Many browsers and servers supported the 'keep-alive' extension to address this problem. With this extension, the server tells the browser how many bytes are contained in the response, then leaves the connection open for a certain period of time after returning the document. The client detects

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 7 Generating the Server Response: HTTP Response Headers

that the document has finished loading by monitoring the number of bytes received, and reconnects on the same socket for further transactions. Persistent connections of this type became standard in HTTP 1.1, and compliant servers are supposed to use persistent connections unless the client explicitly instructs them not to (either by a ' Connection: close ' request header or indirectly by sending a request that specifies HTTP/1.0 instead of HTTP/1.1 and does not also stipulate ' Connection: keep-alive ').

Servlets  can  take  advantage  of  persistent  connections  if  the  servlets  are embedded in servers that support them. The server should handle most of the process, but it has no way to determine how large the returned document is.  So  the  servlet  needs  to  set  the Content-Length response  header  by means of response.setContentLength . A servlet can determine the size of the returned document by buffering the output by means of a ByteArrayOutputStream ,  retrieving the number of bytes with the byte stream's size method, then sending the buffered output to the client by passing the servlet's output stream to the byte stream's writeTo method.

Using persistent connections is likely to pay off only for servlets that load a large number of small objects, where those objects are also servlet-generated and would thus not otherwise take advantage of the server's support for persistent connections. Even so, the advantage gained varies greatly from Web server to Web server and even from Web browser to Web browser. For example, the default configuration for Sun's Java Web Server is to permit only five connections on a single HTTP socket: a value that is too low for many applications. Those who use this server can raise the limit by going to the administration console, selecting 'Web Service' then 'Service Tuning,' then entering a value in the 'Connection Persistence' window.

Listing 7.6 shows a servlet that generates a page with 100 IMG tags  (see Figure  7-4  for  the  result).  Each  of  the IMG tags  refers  to  another  servlet ( ImageRetriever , shown in Listing 7.7) that reads a GIF file from the server system and returns it to the client. Both the original servlet and the ImageRetriever servlet use persistent connections unless instructed not to do so by means of a parameter in the form data named usePersistence with  a value of no . With Netscape 4.7 and a 28.8K dialup connection to talk to the Solaris version of Java Web Server 2.0 (with the connection limit raised above 100), the use of persistent connections reduced the average download time between 15 and 20 percent.

## 7.4 Using Persistent HTTP Connections

## Listing 7.6 PersistentConnection.java

package coreservlets;

```
import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.util.*;
```

/** Illustrates the value of persistent HTTP connections for

- *  pages that include many images, applet classes, or
- *  other auxiliary content that would otherwise require
- *  a separate connection to retrieve.

*/

```
public class PersistentConnection extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); ByteArrayOutputStream byteStream = new ByteArrayOutputStream(7000); PrintWriter out = new PrintWriter(byteStream, true); String persistenceFlag = request.getParameter("usePersistence"); boolean usePersistence = ((persistenceFlag == null) || (!persistenceFlag.equals("no"))); String title; if (usePersistence) { title = "Using Persistent Connection"; } else { title = "Not Using Persistent Connection"; } out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=\"CENTER\">" + title + "</H1>"); int numImages = 100; for(int i=0; i<numImages; i++) { out.println(makeImage(i, usePersistence)); } out.println("</BODY></HTML>"); if (usePersistence) { response.setContentLength(byteStream.size()); } byteStream.writeTo(response.getOutputStream()); } private String makeImage(int n, boolean usePersistence) { String file = "/servlet/coreservlets.ImageRetriever?gifLocation=" + "/bullets/bullet" + n + ".gif"; if (!usePersistence)
```

## Chapter 7 Generating the Server Response: HTTP Response Headers

## HttpServletResponse response) Listing 7.6 PersistentConnection.java (continued)

```
file = file + "&usePersistence=no"; return("<IMG SRC=\"" + file + "\"\n" + "     WIDTH=6 HEIGHT=6 ALT=\"\">"); } public void doPost(HttpServletRequest request, throws ServletException, IOException { doGet(request, response); } }
```

## Listing 7.7 ImageRetriever.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*;
```

/** A servlet that reads a GIF file off the local system

- *  and sends it to the client with the appropriate MIME type.
- *  Includes the Content-Length header to support the
- *  use of persistent HTTP connections unless explicitly
- *  instructed not to through "usePersistence=no".
- *  Used by the PersistentConnection servlet.

*/

```
public class ImageRetriever extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { String gifLocation = request.getParameter("gifLocation"); if ((gifLocation == null) || (gifLocation.length() == 0)) { reportError(response, "Image File Not Specified"); return; } String file = getServletContext().getRealPath(gifLocation); try { BufferedInputStream in = new BufferedInputStream(new FileInputStream(file)); ByteArrayOutputStream byteStream = new ByteArrayOutputStream(512); int imageByte;
```

## 7.4 Using Persistent HTTP Connections

```
while((imageByte = in.read()) != -1) { byteStream.write(imageByte); } in.close(); String persistenceFlag = request.getParameter("usePersistence"); boolean usePersistence = ((persistenceFlag == null) || (!persistenceFlag.equals("no"))); response.setContentType("image/gif"); if (usePersistence) { response.setContentLength(byteStream.size()); } byteStream.writeTo(response.getOutputStream()); } catch(IOException ioe) { reportError(response, "Error: " + ioe); } } public void reportError(HttpServletResponse response, String message) throws IOException { response.sendError(response.SC_NOT_FOUND, message); } } Listing 7.7 ImageRetriever.java (continued)
```

<!-- image -->

Figure 7-4 Result of the PersistentConnection servlet.

<!-- image -->