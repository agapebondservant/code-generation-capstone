## Chapter 12 Including Files and Applets in JSP Documents

## 12.1 Including Files at Page Translation Time

You use the include directive to include a file in the main JSP document at the time the document is translated into a servlet (which is typically the first time it is accessed). The syntax is as follows:

&lt;%@ include file=" Relative URL " %&gt;

There are two ramifications of the fact that the included file is inserted at page  translation  time,  not  at  request  time  as  with jsp:include (Section 12.2).

First, you include the actual file itself, unlike with jsp:include ,  where the server runs the page and inserts its output . This approach means that the included  file  can  contain  JSP  constructs  (such  as  field  or  method  declarations) that affect the main page as a whole.

Second, if the included file changes, all the JSP files that use it need to be updated.  Unfortunately,  although  servers  are allowed to  support  a  mechanism for detecting when an included file has changed (and then recompiling the servlet), they are not required to do so. In practice, few servers support this capability. Furthermore, there is not a simple and portable 'retranslate this JSP page now' command. Instead, you have to update the modification date of the JSP page. Some operating systems have commands that update the  modification  date  without  your  actually  editing  the  file  (e.g.,  the  Unix touch command), but a simple portable alternative is to include a JSP comment in the top-level page. Update the comment whenever the included file changes. For example, you might put the modification date of the included file in the comment, as below.

&lt;%-- Navbar.jsp modified 3/1/00 --%&gt;

&lt;%@ include file="Navbar.jsp" %&gt;

## Core Warning

If you change an included JSP file, you must update the modification dates of all JSP files that use it.

<!-- image -->

For example, Listing 12.1 shows a page fragment that gives corporate contact  information  and  some  per-page  access  statistics  appropriate  to  be included at the bottom of multiple pages within a site. Listing 12.2 shows a page that makes use of it, and Figure 12-1 shows the result.

## 12.1 Including Files at Page Translation Time

## Listing 12.1 ContactSection.jsp

```
<%@ page import="java.util.Date" %> <%-- The following become fields in each servlet that results from a JSP page that includes this file. --%> <%! private int accessCount = 0; private Date accessDate = new Date(); private String accessHost = "<I>No previous access</I>"; %> <P> <HR> This page &copy; 2000 <A HREF="http//www.my-company.com/">my-company.com</A>. This page has been accessed <%= ++accessCount %> times since server reboot. It was last accessed from <%= accessHost %> at <%= accessDate %>. <% accessHost = request.getRemoteHost(); %> <% accessDate = new Date(); %>
```

## Listing 12.2 SomeRandomPage.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;Some Random Page&lt;/TITLE&gt; &lt;META NAME="author" CONTENT="J. Random Hacker"&gt; &lt;META NAME="keywords" CONTENT="foo,bar,baz,quux"&gt; &lt;META NAME="description" CONTENT="Some random Web page."&gt; &lt;LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;TABLE BORDER=5 ALIGN="CENTER"&gt; &lt;TR&gt;&lt;TH CLASS="TITLE"&gt; Some Random Page&lt;/TABLE&gt; &lt;P&gt; Information about our products and services. &lt;P&gt; Blah, blah, blah. &lt;P&gt; Yadda, yadda, yadda. &lt;%@ include file="ContactSection.jsp" %&gt; &lt;/BODY&gt; &lt;/HTML&gt;

<!-- image -->