## 15.4 Example: Showing Raw Servlet and JSP Output

Also note that this type of file inclusion differs from that supported by the  JSP include directive  discussed  in  Section  12.1  (Including  Files  at Page  Translation  Time).  There,  the  actual source  code of  JSP  files  was included in the page by use of the include directive, whereas the include method  of RequestDispatcher just  includes  the result of  the  specified resource. On the other hand, the jsp:include action discussed in Section 12.2 (Including Files at Request Time) has behavior similar to that of the include method,  except  that jsp:include is  available  only  from  JSP pages, not from servlets.

## 15.4 Example: Showing Raw Servlet and JSP Output

When you are debugging servlets or JSP pages, it is often useful to see the raw HTML they generate. To do this, you can choose 'View Source' from the  browser  menu  after  seeing  the  result.  Alternatively,  to  set  HTTP request headers and see the HTTP response headers in addition to HTML source,  use  the WebClient program  shown  in  Section  2.10  (WebClient: Talking to Web Servers Interactively). For quick debugging, another option is available: create a servlet that takes a URL as input and creates an output page showing the HTML source code. Accomplishing this task relies on the fact  that  the  HTML TEXTAREA element  ignores  all  HTML  markup  other than the &lt;/TEXTAREA&gt; tag.  So,  the  original  servlet  generates  the  top  of  a Web page, up to a &lt;TEXTAREA&gt; tag. Then, it includes the output of whatever URL was specified in the query data. Next, it continues with the Web page, starting with a &lt;/TEXTAREA&gt; tag.  Of course, the servlet will fail if it tries to display a resource that contains the &lt;/TEXTAREA&gt; tag, but the point here is the process of including files.

Listing  15.10  shows  the  servlet  that  accomplishes  this  task,  and  Listing 15.11 shows an HTML form that gathers input and sends it to the servlet. Figures  15-3  and  15-4  show  the  results  of  the  HTML  form  and  servlet, respectively.

## Chapter 15 Integrating Servlets and JSP

## Listing 15.10 ShowPage.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; /** Example of the include method of RequestDispatcher. *  Given a URI on the same system as this servlet, the *  servlet shows you its raw HTML output. */ public class ShowPage extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String url = request.getParameter("url"); out.println(ServletUtilities.headWithTitle(url) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + url + "</H1>\n" + "<FORM><CENTER>\n" + "<TEXTAREA ROWS=30 COLS=70>"); if ((url == null) || (url.length() == 0)) { out.println("No URL specified."); } else { // Attaching data works only in version 2.2. String data = request.getParameter("data"); if ((data != null) && (data.length() > 0)) { url = url + "?" + data; } RequestDispatcher dispatcher = getServletContext().getRequestDispatcher(url); dispatcher.include(request, response); } out.println("</TEXTAREA>\n" + "</CENTER></FORM>\n" + "</BODY></HTML>"); } /** Handle GET and POST identically. */ public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } }
```

## 15.4 Example: Showing Raw Servlet and JSP Output

Figure 15-3 Front end to ShowPage servlet. See Listing 15.11 for the HTML source.

<!-- image -->

Figure 15-4 Result of ShowPage servlet when given a URL referring to

<!-- image -->

Expressions.jsp (see Listing 10.1 in Section 10.2).

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->