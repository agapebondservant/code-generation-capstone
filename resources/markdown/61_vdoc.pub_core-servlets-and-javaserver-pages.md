## 5.2 A Servlet That Shows the CGI Variables

## SERVER\_PROTOCOL

The SERVER\_PROTOCOL variable indicates the protocol name and version used in the request line (e.g., HTTP/1.0 or HTTP/1.1 ). Access it by calling request.getProtocol() .

## SERVER\_SOFTWARE

This variable gives identifying information about the Web server. Access it by means of getServletContext().getServerInfo() .

## 5.2 A Servlet That Shows the CGI Variables

Listing 5.1 presents a servlet that creates a table showing the values of all the CGI variables other than HTTP\_XXX\_YYY , which are just the HTTP request headers  described  in  Chapter  4.  Figure  5-1  shows  the  result  for  a  typical request.

## Listing 5.1 ShowCGIVariables.java package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.util.*; /** Creates a table showing the current value of each *  of the standard CGI variables. */ public class ShowCGIVariables extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String[][] variables = { { "AUTH\_TYPE", request.getAuthType() }, { "CONTENT\_LENGTH", String.valueOf(request.getContentLength()) }, { "CONTENT\_TYPE", request.getContentType() },

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 5 Accessing the Standard CGI Variables

## Listing 5.1 ShowCGIVariables.java (continued)

```
{ "DOCUMENT_ROOT", getServletContext().getRealPath("/") }, { "PATH_INFO", request.getPathInfo() }, { "PATH_TRANSLATED", request.getPathTranslated() }, { "QUERY_STRING", request.getQueryString() }, { "REMOTE_ADDR", request.getRemoteAddr() }, { "REMOTE_HOST", request.getRemoteHost() }, { "REMOTE_USER", request.getRemoteUser() }, { "REQUEST_METHOD", request.getMethod() }, { "SCRIPT_NAME", request.getServletPath() }, { "SERVER_NAME", request.getServerName() }, { "SERVER_PORT", String.valueOf(request.getServerPort()) }, { "SERVER_PROTOCOL", request.getProtocol() }, { "SERVER_SOFTWARE", getServletContext().getServerInfo() } }; String title = "Servlet Example: Showing CGI Variables"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>\n" + "<TABLE BORDER=1 ALIGN=CENTER>\n" + "<TR BGCOLOR=\"#FFAD00\">\n" + "<TH>CGI Variable Name<TH>Value"); for(int i=0; i<variables.length; i++) { String varName = variables[i][0]; String varValue = variables[i][1]; if (varValue == null) varValue = "<I>Not specified</I>"; out.println("<TR><TD>" + varName + "<TD>" + varValue); } out.println("</TABLE></BODY></HTML>"); } /** POST and GET requests handled identically. */ public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } }
```

## 5.2 A Servlet That Shows the CGI Variables

Figure 5-1 The standard CGI variables for a typical request.

<!-- image -->