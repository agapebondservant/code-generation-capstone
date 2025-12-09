## Chapter 4 Handling the Client Request: HTTP Request Headers

should usually check getProtocol before specifying response headers (Chapter 7) that are specific to HTTP 1.1.

## 4.2 Printing All Headers

Listing  4.1  shows  a  servlet  that  simply  creates  a  table  of  all  the  headers  it receives, along with their associated values. It also prints out the three components of the main request line (method, URI, and protocol). Figures 4-1 and 4-2 show typical results with Netscape and Internet Explorer.

## Listing 4.1 ShowRequestHeaders.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.util.*; /** Shows all the request headers sent on this *  particular request. */ public class ShowRequestHeaders extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Servlet Example: Showing Request Headers"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>\n" + "<B>Request Method: </B>" + request.getMethod() + "<BR>\n" + "<B>Request URI: </B>" + request.getRequestURI() + "<BR>\n" + "<B>Request Protocol: </B>" + request.getProtocol() + "<BR><BR>\n" +
```

## 4.2 Printing All Headers

## Listing 4.1 ShowRequestHeaders.java (continued)

```
"<TABLE BORDER=1 ALIGN=CENTER>\n" + "<TR BGCOLOR=\"#FFAD00\">\n" + "<TH>Header Name<TH>Header Value"); Enumeration headerNames = request.getHeaderNames() ; while(headerNames.hasMoreElements()) { String headerName = (String)headerNames.nextElement(); out.println("<TR><TD>" + headerName); out.println("    <TD>" + request.getHeader(headerName) ); } out.println("</TABLE>\n</BODY></HTML>"); } /** Let the same servlet handle both GET and POST. */ public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } }
```

Figure 4-1 Request headers sent by Netscape 4.7 on Windows 98.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.