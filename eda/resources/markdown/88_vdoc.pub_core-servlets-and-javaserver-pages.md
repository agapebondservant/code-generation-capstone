## Chapter 10 JSP Scripting Elements

When converted to a servlet by the JSP engine, this fragment will result in something similar to the following.

- if (Math.random() &lt; 0.5) {

```
out.println("Have a <B>nice</B> day!"); } else { out.println("Have a <B>lousy</B> day!");
```

}

## Special Scriptlet Syntax

There are two special constructs you should take note of. First, if you want to use the characters %&gt; inside a scriptlet, enter %\&gt; instead. Second, the XML equivalent of &lt;% Code %&gt; is

```
<jsp:scriptlet> Code </jsp:scriptlet>
```

The two forms are treated identically by JSP engines.

## 10.4 JSP Declarations

A JSP declaration lets you define methods or fields that get inserted into the main  body  of  the  servlet  class  ( outside of  the \_jspService method  that  is called by service to process the request). A declaration has the following form:

&lt;%! Java Code %&gt;

Since declarations do not generate any output, they are normally used in conjunction  with  JSP  expressions  or  scriptlets.  For  example,  here  is  a  JSP fragment  that  prints  the  number  of  times  the  current  page  has  been requested since the server was booted (or the servlet class was changed and reloaded). Recall that multiple client requests to the same servlet result only in multiple threads calling the service method of a single servlet instance. They do not result in the creation of multiple servlet instances except possibly when the servlet implements SingleThreadModel . For a discussion of SingleThreadModel , see Section 2.6 (The Servlet Life Cycle) and Section 11.3 (The isThreadSafe Attribute). Thus, instance variables (fields) of a servlet are shared by multiple requests and accessCount does not have to be declared static below.

&lt;%! private int accessCount = 0; %&gt; Accesses to page since server reboot: &lt;%= ++accessCount %&gt;

## 10.4 JSP Declarations

Listing 10.3 shows the full JSP page; Figure 10-5 shows a representative result.

## Listing 10.3 AccessCounts.jsp &lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;JSP Declarations&lt;/TITLE&gt; &lt;META NAME="author" CONTENT="Marty Hall"&gt; &lt;META NAME="keywords" CONTENT="JSP,declarations,JavaServer,Pages,servlets"&gt; &lt;META NAME="description" CONTENT="A quick example of JSP declarations."&gt; &lt;LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;H1&gt;JSP Declarations&lt;/H1&gt; &lt;%! private int accessCount = 0; %&gt; &lt;H2&gt;Accesses to page since server reboot: &lt;%= ++accessCount %&gt;&lt;/H2&gt; &lt;/BODY&gt; &lt;/HTML&gt;

Figure 10-5 Visiting AccessCounts.jsp after it has been requested 15 times by

<!-- image -->

the same or different clients.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.