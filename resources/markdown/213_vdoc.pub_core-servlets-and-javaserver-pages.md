## Appendix A Servlet and JSP Quick Reference

- · response : the HttpServletResponse associated with response to client.
- · out : the JspWriter ( PrintWriter subclass) used to send output to the client.
- · session : the HttpSession object associated with request. See Chapter 9.
- · application : the ServletContext as obtained by getServletConfig().getContext() . Shared by all servlets and JSP pages on server or in Web application. See Section 15.1.
- · config : the ServletConfig object for this page.
- · pageContext : the PageContext object associated with current page. See Section 13.4 for a discussion of its use.
- · page : synonym for this (current servlet instance); not very useful now. Placeholder for future.

## A.11 The JSP page Directive: Structuring Generated Servlets

## The import Attribute

- · &lt;%@ page import="package.class" %&gt;
- · &lt;%@ page import="package.class1,...,package.classN" %&gt;

## The contentType Attribute

- · &lt;%@ page contentType="MIME-Type" %&gt;
- · &lt;%@ page contentType="MIME-Type; charset=Character-Set" %&gt;
- •
- Cannot be invoked conditionally. Use &lt;% response.setContentType("..."); %&gt;

## Example of Using contentType

## Excel.jsp

```
<%@ page contentType="application/vnd.ms-excel" %> <%-- Note that there are tabs, not spaces, between columns. --%> 1997 1998 1999 2000 2001 (Anticipated) 12.3 13.4 14.5 15.6 16.7
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

- for that.