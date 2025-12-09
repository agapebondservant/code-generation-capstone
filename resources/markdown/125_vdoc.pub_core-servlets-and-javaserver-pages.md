## Chapter 15 Integrating Servlets and JSP

partially process the data, set up beans, then forward the results to one of a number of different JSP pages, depending on the circumstances. In early JSP specifications,  this  approach  was  known  as  the model  2 approach  to  JSP. Rather than completely forwarding the request, the servlet can generate part of  the  output  itself,  then  include  the  output  of  one  or  more  JSP  pages  to obtain the final result.

## 15.1 Forwarding Requests

The key to letting servlets forward requests or include external content is to use a RequestDispatcher . You obtain a RequestDispatcher by calling the getRequestDispatcher method of ServletContext , supplying a URL relative to the server root. For example, to obtain a RequestDispatcher associated with http://yourhost/presentations/presentation1.jsp ,  you would do the following:

```
String url = "/presentations/presentation1.jsp"; RequestDispatcher dispatcher =
```

getServletContext().getRequestDispatcher(url);

Once  you  have  a RequestDispatcher ,  you  use forward to  completely transfer control to the associated URL and use include to output the associated URL's content. In both cases, you supply the HttpServletRequest and HttpServletResponse as arguments. Both methods throw ServletException and IOException . For example, Listing 15.1 shows a portion of a servlet that forwards the request to one of three different JSP pages, depending on the value of the operation parameter. To avoid repeating the getRequestDispatcher call, I use a utility method called gotoPage that takes the URL,  the HttpServletRequest and  the HttpServletResponse ;  gets  a RequestDispatcher ; and then calls forward on it.

## Using Static Resources

In most cases, you forward requests to a JSP page or another servlet. In some cases, however, you might want to send the request to a static HTML page. In an e-commerce site, for example, requests that indicate that the user does not have a valid account name might be forwarded to an account application page that uses HTML forms to gather the requisite information. With GET requests, forwarding requests to a static HTML page is perfectly legal and requires no special syntax; just supply the address of the HTML page as the

## Listing 15.1 Request Forwarding Example

```
public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { String operation = request.getParameter("operation"); if (operation == null) { operation = "unknown"; } if (operation.equals("operation1")) { gotoPage("/operations/presentation1.jsp", request, response); } else if (operation.equals("operation2")) { gotoPage("/operations/presentation2.jsp", request, response); } else { gotoPage("/operations/unknownRequestHandler.jsp", request, response); } } private void gotoPage(String address, HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { RequestDispatcher dispatcher = getServletContext().getRequestDispatcher(address); dispatcher.forward(request, response); }
```

argument  to getRequestDispatcher .  However,  since  forwarded  requests use the same request method as the original request, POST requests cannot be forwarded to normal HTML pages. The solution to this problem is to simply  rename  the  HTML  page  to  have  a .jsp extension.  Renaming somefile.html to somefile.jsp does  not  change  its  output  for GET requests, but somefile.html cannot  handle POST requests,  whereas somefile.jsp gives an identical response for both GET and POST .

## Supplying Information to the Destination Pages

To  forward  the  request  to  a  JSP  page,  a  servlet  merely  needs  to  obtain  a RequestDispatcher by  calling  the getRequestDispatcher method  of ServletContext ,  then  call forward on  the  result,  supplying  the HttpServletRequest and HttpServletResponse as  arguments.  That's  fine  as far  as  it  goes,  but  this  approach  requires  the  destination  page  to  read  the

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 15.1 Forwarding Requests

## Chapter 15 Integrating Servlets and JSP

information it needs out of the HttpServletRequest . There are two reasons why it might not be a good idea to have the destination page look up and process all the data itself. First, complicated programming is easier in a servlet than in a JSP page. Second, multiple JSP pages may require the same data, so it would be wasteful for each JSP page to have to set up the same data. A better approach is for the original servlet to set up the information that the destination pages need, then store it somewhere that the destination pages can easily access.

There are two main places for the servlet to store the data that the JSP pages will use: in the HttpServletRequest and as a bean in the location specific to the scope attribute of jsp:useBean (see Section 13.4, 'Sharing Beans' ).

The originating servlet would store arbitrary objects in the HttpServletRequest by using request.setAttribute("key1", value1);

The destination page would access the value by using a JSP scripting element to call

Type1 value1 = (Type1)request.getAttribute("key1");

For complex values, an even better approach is to represent the value as a bean and store it in the location used by jsp:useBean for shared beans. For example,  a scope of application means  that  the  value  is  stored  in  the ServletContext , and ServletContext uses setAttribute to store values. Thus, to make a bean accessible to all servlets or JSP pages in the server or Web application, the originating servlet would do the following:

Type1 value1 = computeValueFromRequest(request); getServletContext().setAttribute("key1", value1);

The  destination  JSP  page  would  normally  access  the  previously  stored value by using jsp:useBean as follows:

&lt;jsp:useBean id="key1" class="Type1" scope="application" /&gt;

Alternatively, the destination page could use a scripting element to explicitly call application.getAttribute("key1") and cast the result to Type1 .

For a servlet to make data specific to a user session rather than globally accessible, the servlet would store the value in the HttpSession in the normal manner, as below:

Type1 value1 = computeValueFromRequest(request); HttpSession session = request.getSession(true); session.putValue("key1", value1);

The destination page would then access the value by means of

&lt;jsp:useBean id="key1" class="Type1" scope="session" /&gt;

## 15.1 Forwarding Requests

The Servlet 2.2 specification adds a third way to send data to the destination  page  when  using GET requests:  simply  append  the  query  data  to  the URL. For example,

```
String address = "/path/resource.jsp?newParam=value"; RequestDispatcher dispatcher = getServletContext().getRequestDispatcher(address); dispatcher.forward(request, response);
```

This  technique  results  in  an additional request  parameter  of newParam (with a value of value ) being added to whatever request parameters already existed. The new parameter is added to the beginning of the query data so that it will replace existing values if the destination page uses getParameter (use  the  first  occurrence  of  the  named  parameter)  rather  than getParameterValues (use all occurrences of the named parameter).

## Interpreting Relative URLs in the Destination Page

Although a servlet can forward the request to arbitrary locations on the same server,  the  process  is  quite  different  from  that  of using  the sendRedirect method of HttpServletResponse (see  Section  6.1).  First, sendRedirect requires the client to reconnect to the new resource, whereas the forward method of RequestDispatcher is  handled  completely  on  the  server.  Second, sendRedirect does not automatically preserve all of the request data; forward does.  Third, sendRedirect results  in  a  different  final  URL, whereas with forward, the URL of the original servlet is maintained.

This final point means that, if the destination page uses relative URLs for images or style sheets, it needs to make them relative to the server root, not to the destination page's actual location. For example, consider the following style sheet entry:

```
<LINK REL=STYLESHEET HREF="my-styles.css" TYPE="text/css">
```

If the JSP page containing this entry is accessed by means of a forwarded request, my-styles.css will be interpreted relative to the URL of the originating servlet, not relative to the JSP page itself, almost certainly resulting in an error. The solution is to give the full server path to the style sheet file, as follows:

```
<LINK REL=STYLESHEET HREF="/path/my-styles.css" TYPE="text/css">
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.