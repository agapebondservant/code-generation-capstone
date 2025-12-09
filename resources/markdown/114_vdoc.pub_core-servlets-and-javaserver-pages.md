## Chapter 13 Using JavaBeans with JSP

## Listing 13.6 SaleEntry3.jsp (continued)

&lt;TABLE BORDER=5 ALIGN="CENTER"&gt; &lt;TR&gt;&lt;TH CLASS="TITLE"&gt; Using jsp:setProperty&lt;/TABLE&gt;

&lt;jsp:useBean id="entry" class="coreservlets.SaleEntry" /&gt; &lt;%-- WARNING! Both the JSWDK 1.0.1 and the Java Web Server have a bug that makes them fail on automatic type conversions to double values.

--%&gt;

## &lt;jsp:setProperty name="entry" property="*" /&gt;

&lt;BR&gt; &lt;TABLE ALIGN="CENTER" BORDER=1&gt; &lt;TR CLASS="COLORED"&gt; &lt;TH&gt;Item ID&lt;TH&gt;Unit Price&lt;TH&gt;Number Ordered&lt;TH&gt;Total Price &lt;TR ALIGN="RIGHT"&gt; &lt;TD&gt;&lt;jsp:getProperty name="entry" property="itemID" /&gt; &lt;TD&gt;$&lt;jsp:getProperty name="entry" property="itemCost" /&gt; &lt;TD&gt;&lt;jsp:getProperty name="entry" property="numItems" /&gt; &lt;TD&gt;$&lt;jsp:getProperty name="entry" property="totalCost" /&gt; &lt;/TABLE&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## 13.4 Sharing Beans

Up to this point, I have treated the objects that were created with jsp:useBean as though they were simply bound to local variables in the \_jspService method (which is called by the service method of the servlet that is generated from the page). Although the beans are indeed bound to local variables, that is not the only behavior. They are also stored in one of four  different  locations,  depending  on  the  value  of  the  optional scope attribute of jsp:useBean . The scope attribute has the following possible values:

## · page

This is the default value. It indicates that, in addition to being bound to a local variable, the bean object should be placed in the PageContext object for the duration of the current request. In principle, storing the object there means that servlet code can access it by calling getAttribute on the predefined pageContext variable. In practice, beans created with page scope are almost always accessed by jsp:getProperty , jsp:setProperty , scriptlets, or expressions later in the same page.

## · application

This very useful value means that, in addition to being bound to a local variable, the bean will be stored in the shared ServletContext available through the predefined application variable or by a call to getServletContext() . The ServletContext is shared by all servlets in the same Web application (or all servlets in the same server or servlet engine if no explicit Web applications are defined). Values in the ServletContext can be retrieved by the getAttribute method. This sharing has a couple of ramifications.

First, it provides a simple mechanism for multiple servlets and JSP pages to access the same object. See the following subsection (Conditional Bean Creation) for details and an example.

Second, it lets a servlet create a bean that will be used in JSP pages, not just access one that was previously created. This approach lets a servlet handle complex user requests by setting up beans, storing them in the ServletContext , then forwarding the request to one of several possible JSP pages to present results appropriate to the request data. For details on this approach, see Chapter 15 (Integrating Servlets and JSP).

## · session

This value means that, in addition to being bound to a local variable, the bean will be stored in the HttpSession object associated with the current request, where it can be retrieved with getValue . Attempting to use scope="session" causes an

## 13.4 Sharing Beans

## Chapter 13 Using JavaBeans with JSP

error at page translation time when the page directive stipulates that the current page is not participating in sessions. (See Section 11.4, 'The session Attribute.')

## · request

This value signifies that, in addition to being bound to a local variable, the bean object should be placed in the ServletRequest object for the duration of the current request, where it is available by means of the getAttribute method. This value is only a slight variation of the per-request scope provided by scope="page" (or by default when no scope is specified).

## Conditional Bean Creation

To  make  bean  sharing  more  convenient,  there  are  two  situations  where bean-related elements are evaluated conditionally.

First,  a jsp:useBean element  results  in  a  new  bean  being  instantiated only if no bean with the same id and scope can be found. If a bean with the same id and scope is found, the preexisting bean is simply bound to the variable referenced by id . A typecast is performed if the preexisting bean is of a more specific type than the bean being declared, and a ClassCastException results if this typecast is illegal.

Second, instead of

```
<jsp:useBean ... /> you can use <jsp:useBean ...> statements </jsp:useBean>
```

The point  of  using  the  second  form  is  that  the  statements  between  the jsp:useBean start and end tags are executed only if a new bean is created, not if  an  existing  bean is used. This conditional execution is convenient for setting  initial  bean  properties  for  beans  that  are  shared  by  multiple  pages. Since you don't know which page will be accessed first, you don't know which page should contain the initialization code. No problem: they can all contain the code, but only the page first accessed actually executes it. For example, Listing  13.7  shows  a  simple  bean  that  can  be  used  to  record  cumulative access counts to any of a set of related pages. It also stores the name of the first page that was accessed. Since there is no way to predict which page in a set will be accessed first, each page that uses the shared counter has statements like the following:

## 13.4 Sharing Beans

```
<jsp:useBean id="counter" class="coreservlets.AccessCountBean" scope="application"> <jsp:setProperty name="counter" property="firstPage" value="Current Page Name" /> </jsp:useBean> Collectively, the pages using the counter have been accessed
```

&lt;jsp:getProperty name="counter" property="accessCount" /&gt; times.

Listing  13.8  shows  the  first  of  three  pages  that  use  this  approach.  The source code archive at http://www.coreservlets.com/ contains the other two nearly identical pages. Figure 13-3 shows a typical result.

## Listing 13.7 AccessCountBean.java

```
package coreservlets;
```

```
/** Simple bean to illustrate sharing beans through *  use of the scope attribute of jsp:useBean. */ public void setFirstPage(String firstPage) {
```

```
public class AccessCountBean { private String firstPage; private int accessCount = 1; public String getFirstPage() { return(firstPage); } this.firstPage = firstPage; } public int getAccessCount() { return(accessCount++); } }
```

<!-- image -->

## Chapter 13 Using JavaBeans with JSP

## Listing 13.8 SharedCounts1.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Shared Access Counts: Page 1</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <TABLE BORDER=5 ALIGN="CENTER"> <TR><TH CLASS="TITLE"> Shared Access Counts: Page 1</TABLE> <P> <jsp:useBean id="counter" class="coreservlets.AccessCountBean" scope="application" > <jsp:setProperty name="counter" property="firstPage" value="SharedCounts1.jsp" /> </jsp:useBean> Of SharedCounts1.jsp (this page), <A HREF="SharedCounts2.jsp">SharedCounts2.jsp</A>, and <A HREF="SharedCounts3.jsp">SharedCounts3.jsp</A>, <jsp:getProperty name="counter" property="firstPage" /> was the first page accessed. <P> Collectively, the three pages have been accessed <jsp:getProperty name="counter" property="accessCount" /> times. </BODY> </HTML>
```

## 13.4 Sharing Beans

Figure 13-3 Result of a user visiting SharedCounts3.jsp . The first page visited by any user was SharedCounts2.jsp . SharedCounts1.jsp , SharedCounts2.jsp , and SharedCounts3.jsp were collectively visited a total

<!-- image -->

of twelve times after the server was last started but prior to the visit shown in this figure.

<!-- image -->