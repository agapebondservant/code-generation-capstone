## Chapter 15 Integrating Servlets and JSP

## Listing 15.11 ShowPage.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;Viewing JSP and Servlet Output&lt;/TITLE&gt; &lt;/HEAD&gt;

&lt;BODY BGCOLOR="#FDF5E6"&gt;

&lt;H1 ALIGN="CENTER"&gt;Viewing JSP and Servlet Output&lt;/H1&gt; Enter a relative URL of the form /path/name and, optionally, any attached GET data you want to send. The raw HTML output of the specified URL (usually a JSP page or servlet) will be shown. Caveats: the URL specified cannot contain the string &lt;CODE&gt;&amp;lt;/TEXTAREA&amp;gt;&lt;/CODE&gt;, and attached GET data works only with servlet engines that support version 2.2.

## &lt;FORM ACTION="/servlet/coreservlets.ShowPage" &gt;

&lt;CENTER&gt;

URL:

&lt;INPUT TYPE="TEXT" NAME="url" SIZE=50 VALUE="/"&gt;&lt;BR&gt; GET Data:

&lt;INPUT TYPE="TEXT" NAME="data" SIZE=50&gt;&lt;BR&gt;&lt;BR&gt;

&lt;Input TYPE="SUBMIT" VALUE="Show Output"&gt;

&lt;/CENTER&gt;

&lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## 15.5 Forwarding Requests From JSP Pages

The most common request forwarding scenario is that the request first comes to a servlet and the servlet forwards the request to a JSP page. The reason a servlet usually handles the original request is that checking request parameters and setting up beans requires a lot of programming, and it is more convenient to do this programming in a servlet than in a JSP document. The reason that the destination page is usually a JSP document is that JSP simplifies the process of creating the HTML content.

However, just because this is the usual approach doesn't mean that it is the only way of doing things. It is certainly possible for the destination page to be a servlet. Similarly, it is quite possible for a JSP page to forward requests else-

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 15.5 Forwarding Requests From JSP Pages

where. For example, a request might go to a JSP page that normally presents results of a certain type and that forwards the request elsewhere only when it receives unexpected values.

Sending  requests  to  servlets  instead  of  JSP  pages  requires  no  changes whatsoever in the use of the RequestDispatcher . However, there is special syntactic  support  for  forwarding  requests  from  JSP  pages.  In  JSP,  the jsp:forward action is simpler and easier to use than wrapping up RequestDispatcher code in a scriptlet. This action takes the following form:

&lt;jsp:forward page="Relative URL" /&gt;

The page attribute is allowed to contain JSP expressions so that the destination can be computed at request time. For example, the following sends about half the visitors to http://host/examples/page1.jsp and the others to http://host/examples/page2.jsp .

```
<% String destination; if (Math.random() > 0.5) { destination = "/examples/page1.jsp"; } else { destination = "/examples/page2.jsp"; }
```

%&gt;

&lt;jsp:forward page="&lt;%= destination %&gt;" /&gt;

<!-- image -->

## Supporting Technologies

<!-- image -->

Chapter 16 Chapter 17

Using HTML Forms, 384 Using Applets As Servlet Front Ends, 432 JDBC and Database Connection Pooling, 460

Chapter 18