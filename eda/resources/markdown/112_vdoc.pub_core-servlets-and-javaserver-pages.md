## Chapter 13 Using JavaBeans with JSP

- · JSWDK 1.0.1:

install\_dir /webpages/WEB-INF/servlets/lima/Fordhook.cl ass

- · Java Web Server 2.o:

install\_dir /classes/lima/Fordhook.class

The JSP files that use bean classes don't need to be installed anywhere special, however. As is usual with JSP files on a JSP-capable server, they can be placed anywhere that normal Web pages can be.

## 13.2 Example: StringBean

Listing 13.1 presents a simple class called StringBean that is in the coreservlets package. Because the class has no public instance variables (fields) and has a zero-argument constructor since it doesn't declare any explicit constructors, it satisfies the basic criteria for being a bean. Since StringBean has a  method  called getMessage that  returns  a String and  another  method called setMessage that takes a String as an argument, in beans terminology the class is said to have a String parameter called message .

Listing  13.2  shows  a  JSP  file  that  uses  the StringBean class.  First,  an instance of StringBean is created with the jsp:useBean action as follows:

&lt;jsp:useBean id="stringBean" class="coreservlets.StringBean" /&gt;

After this, the message property can be inserted into the page in either of the following two ways:

&lt;jsp:getProperty name="stringBean" property="message" /&gt;

```
<%= stringBean.getMessage() %>
```

The message property can be modified in either of the following two ways:

```
<jsp:setProperty name="stringBean" property="message" value="some message" /> <% stringBean.setMessage("some message"); %>
```

Figure 13-1 shows the result.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Listing 13.1

```
StringBean.java
```

```
package coreservlets; /** A simple bean that has a single String property *  called message. */ public class StringBean { private String message = "No message specified"; public String getMessage () { return(message); } public void setMessage (String message) { this.message = message; } }
```

## 13.2 Example: StringBean

<!-- image -->

## Chapter 13 Using JavaBeans with JSP

```
Listing 13.2 StringBean.jsp <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Using JavaBeans with JSP</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <TABLE BORDER=5 ALIGN="CENTER"> <TR><TH CLASS="TITLE"> Using JavaBeans with JSP</TABLE> <jsp:useBean id="stringBean" class="coreservlets.StringBean" /> <OL> <LI>Initial value (getProperty): <I> <jsp:getProperty name="stringBean" property="message" /> </I> <LI>Initial value (JSP expression): <I> <%= stringBean.getMessage() %> </I> <LI> <jsp:setProperty name="stringBean" property="message" value="Best string bean: Fortex" /> Value after setting property with setProperty: <I> <jsp:getProperty name="stringBean" property="message" /> </I> <LI> <% stringBean.setMessage("My favorite: Kentucky Wonder"); %> Value after setting property with scriptlet: <I> <%= stringBean.getMessage() %> </I> </OL> </BODY> </HTML>
```