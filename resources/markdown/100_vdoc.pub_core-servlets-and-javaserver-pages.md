## 11.9 The errorPage Attribute

## 11.9 The errorPage Attribute

The errorPage attribute specifies a JSP page that should process any exceptions (i.e., something of type Throwable ) thrown but not caught in the current page. It is used as follows:

&lt;%@ page errorPage=" Relative URL " %&gt;

The  exception  thrown  will  be  automatically  available  to  the  designated error page by means of the exception variable. See Listings 11.5 and 11.6 for examples.

## 11.10 The isErrorPage Attribute

The isErrorPage attribute indicates whether or not the current page can act as the error page for another JSP page. Use of isErrorPage takes one of the following two forms:

```
<%@ page isErrorPage="true" %> <%@ page isErrorPage="false" %> <%!-- Default --%>
```

For example, Listing 11.5 shows a JSP page to compute speed based upon distance and time parameters. The page neglects to check if the input parameters are missing or malformed, so an error could easily occur at run time. However, the page designated SpeedErrors.jsp (Listing 11.6) as the page to  handle  errors  that  occur  in ComputeSpeed.jsp ,  so  the  user  does  not receive the typical terse JSP error messages. Figures 11-9 and 11-10 show results when good and bad input parameters are received, respectively.

## Listing 11.5 ComputeSpeed.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

```
<HTML> <HEAD> <TITLE>Computing Speed</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD>
```

&lt;BODY&gt;

&lt;%@ page errorPage="SpeedErrors.jsp" %&gt;

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 11 The JSP page Directive: Structuring Generated Servlets

## Listing 11.5 ComputeSpeed.jsp (continued)

```
<TABLE BORDER=5 ALIGN="CENTER"> <TR><TH CLASS="TITLE"> Computing Speed</TABLE> <%! // Note lack of try/catch for NumberFormatException if // value is null or malformed. private double toDouble(String value) { return(Double.valueOf(value).doubleValue()); } %> <% double furlongs = toDouble(request.getParameter("furlongs")); double fortnights = toDouble(request.getParameter("fortnights")); double speed = furlongs/fortnights; %> <UL> <LI>Distance: <%= furlongs %> furlongs. <LI>Time: <%= fortnights %> fortnights. <LI>Speed: <%= speed %> furlongs per fortnight. </UL> </BODY> </HTML>
```

## Listing 11.6 SpeedErrors.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Error Computing Speed</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD>
```

&lt;BODY&gt;

## &lt;%@ page isErrorPage="true" %&gt;

&lt;TABLE BORDER=5 ALIGN="CENTER"&gt;

## 11.10 The isErrorPage Attribute

## Listing 11.6 SpeedErrors.jsp (continued)

&lt;TR&gt;&lt;TH CLASS="TITLE"&gt;

Error Computing Speed&lt;/TABLE&gt;

&lt;P&gt;

ComputeSpeed.jsp reported the following error:

exception

&lt;I&gt;&lt;%=

%&gt;&lt;/I&gt;. This problem occurred in the following place:

&lt;PRE&gt;

exception

&lt;%

&lt;/PRE&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

Figure 11-9 ComputeSpeed.jsp when it receives legal values.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

.printStackTrace(new PrintWriter(out)); %&gt;