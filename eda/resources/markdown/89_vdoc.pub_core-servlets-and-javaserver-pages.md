## Chapter 10 JSP Scripting Elements

## Special Declaration Syntax

As  with scriptlets,  if  you  want  to  use  the  characters %&gt; ,  enter %\&gt; instead. Finally, note that the XML equivalent of &lt;%! Code %&gt; is

&lt;jsp:declaration&gt; Code

&lt;/jsp:declaration&gt;

## 10.5 Predefined Variables

To simplify code in JSP expressions and scriptlets, you are supplied with eight automatically defined variables, sometimes called implicit objects . Since JSP declarations  (see  Section  10.4)  result  in  code  that  appears  outside  of  the \_jspService method, these variables are not accessible in declarations. The available  variables  are request , response , out , session , application , config , pageContext , and page . Details for each are given below.

## request

This variable is the HttpServletRequest associated with the request; it gives you access to the request parameters, the request type (e.g., GET or POST ), and the incoming HTTP headers (e.g., cookies). Strictly speaking, if the protocol in the request is something other than HTTP, request is allowed to be a subclass of ServletRequest other than HttpServletRequest . However, few, if any, JSP servers currently support non-HTTP servlets.

## response

This variable is the HttpServletResponse associated with the response to the client. Note that since the output stream (see out ) is normally buffered, it is legal to set HTTP status codes and response headers in JSP pages, even though the setting of headers or status codes is not permitted in servlets once any output has been sent to the client.

## out

This is the PrintWriter used to send output to the client. However, to make the response object useful, this is a buffered version of PrintWriter called JspWriter . You can adjust the buffer size through use of the buffer attribute of the page directive (see Section 11.5). Also note

## 10.5 Predefined Variables

that out is used almost exclusively in scriptlets, since JSP expressions are automatically placed in the output stream and thus rarely need to refer to out explicitly.

## session

This variable is the HttpSession object associated with the request. Recall that sessions are created automatically, so this variable is bound even if there is no incoming session reference. The one exception is if you use the session attribute of the page directive (see Section 11.4) to turn sessions off. In that case, attempts to reference the session variable cause errors at the time the JSP page is translated into a servlet.

## application

This variable is the ServletContext as obtained via getServletConfig().getContext() . Servlets and JSP pages can store persistent data in the ServletContext object rather than in instance variables. ServletContext has setAttribute and getAttribute methods that let you store arbitrary data associated with specified keys. The difference between storing data in instance variables and storing it in the ServletContext is that the ServletContext is shared by all servlets in the servlet engine (or in the Web application, if your server supports such a capability). For more information on the use of the ServletContext , see Section 13.4 (Sharing Beans) and Chapter 15 (Integrating Servlets and JSP).

## config

This variable is the ServletConfig object for this page.

## pageContext

JSP introduced a new class called PageContext to give a single point of access to many of the page attributes and to provide a convenient place to store shared data. The pageContext variable stores the value of the PageContext object associated with the current page. See Section 13.4 (Sharing Beans) for a discussion of its use.

## page

This variable is simply a synonym for this and is not very useful in the Java programming language. It was created as a place holder for the time when the scripting language could be something other than Java.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.