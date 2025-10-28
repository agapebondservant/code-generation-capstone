## A.11 The JSP page Directive: Structuring Generated Servlets

## Example of Using setContentType

```
ApplesAndOranges.jsp <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <!-- HEAD part removed. --> <BODY><CENTER><H2>Comparing Apples and Oranges</H2> <% String format = request.getParameter("format"); if ((format != null) && (format.equals("excel"))) { response.setContentType("application/vnd.ms-excel"); } %> <TABLE BORDER=1> <TR><TH></TH><TH>Apples<TH>Oranges <TR><TH>First Quarter<TD>2307<TD>4706 <TR><TH>Second Quarter<TD>2982<TD>5104 <TR><TH>Third Quarter<TD>3011<TD>5220 <TR><TH>Fourth Quarter<TD>3055<TD>5287 </TABLE> </CENTER></BODY></HTML>
```

## The isThreadSafe Attribute

- · &lt;%@ page isThreadSafe="true" %&gt; &lt;%!-- Default --%&gt;
- · &lt;%@ page isThreadSafe="false" %&gt;
- · A value of true means that you have made your code threadsafe and that the system can send multiple concurrent requests. A value of false means that the servlet resulting from JSP document will implement SingleThreadModel (see Section 2.6).
- · Non-threadsafe code:
- •

```
<%! private int idNum = 0; %> <% String userID = "userID" + idNum;
```

```
out.println("Your ID is " + userID + "."); idNum = idNum + 1; %> Threadsafe code: <%! private int idNum = 0; %> <% synchronized(this) { String userID = "userID" + idNum; out.println("Your ID is " + userID + "."); idNum = idNum + 1; } %>
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.