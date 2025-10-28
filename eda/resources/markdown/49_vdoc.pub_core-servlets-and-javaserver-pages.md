## Core Warning

The values supplied to getParameter and getParameterValues are case sensitive.

## 3.3 Example: Reading Three Explicit Parameters

<!-- image -->

Finally,  although  most  real  servlets  look  for  a  specific  set  of  parameter names, for debugging purposes it is sometimes useful to get a full list. Use getParameterNames to get this list in the form of an Enumeration , each entry of which can be cast to a String and used in a getParameter or getParameterValues call.  Just  note  that  the HttpServletRequest API does not specify the order in which the names appear within that Enumeration .

## Core Warning

Don't count on getParameterNames returning the names in any particular order.

<!-- image -->

## 3.3 Example: Reading Three Explicit Parameters

Listing  3.1  presents  a  simple  servlet  called ThreeParams that  reads  form data parameters named param1 , param2 , and param3 and places their values  in  a  bulleted  list.  Listing  3.2  shows  an  HTML  form  that  collects  user input and sends it to this servlet. By use of an ACTION of /servlet/coreservlets.ThreeParams , the form can be installed anywhere on the system running the servlet; there need not be any particular association between the directory  containing  the  form  and  the  servlet  installation  directory.  Recall that  the  specific  locations  for  installing  HTML  files  vary  from  server  to server.  With  the  JSWDK  1.0.1  and  Tomcat  3.0,  HTML  pages  are  placed somewhere in install\_dir /webpages and are accessed via http://host/path/file.html . For example, if the form shown in Listing 3.2 is placed in install\_dir /webpages/forms/ThreeParamsForm.html and the server is accessed from the same host that it is running on, the form would be accessed by a URL of http://localhost/forms/ThreeParamsForm.html .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 3 Handling the Client Request: Form Data

Figures 3-1 and 3-2 show the result of the HTML front end and the servlet, respectively.

## Listing 3.1 ThreeParams.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class ThreeParams extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Reading Three Request Parameters"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>\n" + "<UL>\n" + "  <LI><B>param1</B>: " + request.getParameter("param1") + "\n" + "  <LI><B>param2</B>: " + request.getParameter("param2") + "\n" + "  <LI><B>param3</B>: " + request.getParameter("param3") + "\n" + "</UL>\n" + "</BODY></HTML>"); } }
```

Although you are required to specify response settings (see Chapters 6 and 7) before beginning to generate the content, there is no requirement that you read the request parameters at any particular time.

If  you're  accustomed  to  the  traditional  CGI  approach  where  you  read POST data through the standard input, you should note that you can do the same thing with servlets by calling getReader or getInputStream on the HttpServletRequest and then using that stream to obtain the raw input. This is a bad idea for regular parameters since the input is neither parsed (separated  into  entries  specific  to  each  parameter)  nor  URL-decoded (translated so that plus signs become spaces and % XX gets replaced by the

## 3.3 Example: Reading Three Explicit Parameters

ASCII or ISO Latin-1 character corresponding to the hex value XX ). However, reading the raw input might be of use for uploaded files or POST data being sent by custom clients rather than by HTML forms. Note, however, that if you read the POST data in this manner, it might no longer be found by getParameter .

## Listing 3.2 ThreeParamsForm.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Collecting Three Parameters</TITLE> </HEAD> <BODY BGCOLOR="#FDF5E6"> <H1 ALIGN="CENTER">Collecting Three Parameters</H1> <FORM ACTION="/servlet/coreservlets.ThreeParams" > First Parameter:  <INPUT TYPE="TEXT" NAME="param1" ><BR> Second Parameter: <INPUT TYPE="TEXT" NAME="param2" ><BR> Third Parameter:  <INPUT TYPE="TEXT" NAME="param3" ><BR> <CENTER> <INPUT TYPE="SUBMIT"> </CENTER> </FORM> </BODY> </HTML>
```

<!-- image -->

Figure 3-1 HTML front end resulting from ThreeParamsForm.html .

<!-- image -->