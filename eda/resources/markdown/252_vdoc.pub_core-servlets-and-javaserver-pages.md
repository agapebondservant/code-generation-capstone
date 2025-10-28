## A.15 Integrating Servlets and JSP

## Request Forwarding Syntax

```
String url = "/path/presentation1.jsp"; RequestDispatcher dispatcher = getServletContext().getRequestDispatcher(url); dispatcher.forward();
```

## Forwarding to Regular HTML Pages

- · If initial servlet handles GET requests only, no change is necessary.
- · If initial servlet handles POST , then change destination page from SomePage.html to SomePage.jsp so that it, too, can handle POST .

## Setting Up Globally Shared Beans

- · Initial servlet:

Type1 value1 = computeValueFromRequest(request); getServletContext().setAttribute("key1", value1);

- · Final JSP document:

&lt;jsp:useBean id="key1" class="Type1" scope="application" /&gt;

## Setting Up Session Beans

- · Initial servlet:

Type1 value1 = computeValueFromRequest(request); HttpSession session = request.getSession(true); session.putValue("key1", value1);

- · Final JSP document:

&lt;jsp:useBean id="key1" class="Type1" scope="session" /&gt;

## Interpreting Relative URLs in the Destination Page

- · URL of original servlet is used for forwarded requests. Browser does not know real URL, so it will resolve relative URLs with respect to original servlet's URL.

## Getting a RequestDispatcher by Alternative Means (2.2 Only)

- · By name: use getNamedDispatcher method of ServletContext .
- · By path relative to initial servlet's location: use the getRequestDispatcher method of HttpServletRequest rather than the one from ServletContext .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.