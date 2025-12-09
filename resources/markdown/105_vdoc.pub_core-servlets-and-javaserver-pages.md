Chapter 12 Including Files and Applets in JSP Documents

Figure 12-1 Result of SomeRandomPage.jsp .

<!-- image -->

## 12.2 Including Files at Request Time

The include directive (Section 12.1) lets you include documents that contain JSP code into multiple different pages. Including JSP content is a useful capability, but the include directive requires you to update the modification date of the page whenever the included file changes, which is a significant inconvenience. The jsp:include action includes files at the time of the client request and thus does not require you to update the main file when an included file changes. On the other hand, the page has already been translated into a servlet by request time, so the included files cannot contain JSP.

<!-- image -->

## Core Approach

Use the include Otherwise, use jsp:include .

directive if included files will use JSP constructs.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 12.2 Including Files at Request Time

Although the included files cannot contain JSP , they can be the result of resources that use JSP to create the output. That is, the URL that refers to the included resource is interpreted in the normal manner by the server and thus  can  be  a  servlet  or  JSP  page.  This  is  precisely  the  behavior  of  the include method  of  the RequestDispatcher class,  which  is  what  servlets use if they want to do this type of file inclusion. See Section 15.3 (Including Static or Dynamic Content) for details.

The jsp:include element has two required attributes, as shown in the sample below: page (a relative URL referencing the file to be included) and flush (which must have the value true ).

&lt;jsp:include page=" Relative URL " flush="true" /&gt;

Although you typically include HTML or plain text documents, there is no requirement that the included files have any particular file extension. However, the Java Web Server 2.0 has a bug that causes it to terminate page processing  when it  tries  to  include  a  file  that  does  not  have  a .html or .htm extension (e.g., somefile.txt ). Tomcat, the JSWDK, and most commercial servers have no such restrictions.

## Core Warning

Due to a bug, you must use .html or .htm extensions for included files used with the Java Web Server.

<!-- image -->

As an example, consider the simple news summary page shown in Listing 12.3.  Page  developers  can  change  the  news items in the  files Item1.html through Item4.html (Listings 12.4 through 12.7) without having to update the main news page. Figure 12-2 shows the result.

## Listing 12.3 WhatsNew.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

```
<HTML> <HEAD> <TITLE>What's New</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css">
```

&lt;/HEAD&gt;

&lt;BODY&gt;

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 12 Including Files and Applets in JSP Documents

## Listing 12.3 WhatsNew.jsp (continued)

```
<CENTER> <TABLE BORDER=5> <TR><TH CLASS="TITLE"> What's New at JspNews.com</TABLE> </CENTER> <P> Here is a summary of our four most recent news stories: <OL> <LI> <jsp:include page="news/Item1.html" flush="true" /> <LI> <jsp:include page="news/Item2.html" flush="true" /> <LI> <jsp:include page="news/Item3.html" flush="true" /> <LI> <jsp:include page="news/Item4.html" flush="true" /> </OL> </BODY> </HTML>
```

## Listing 12.4 Item1.html

&lt;B&gt;Bill Gates acts humble.&lt;/B&gt; In a startling and unexpected development, Microsoft big wig Bill Gates put on an open act of humility yesterday.

&lt;A HREF="http://www.microsoft.com/Never.html"&gt;More details...&lt;/A&gt;

## Listing 12.5 Item2.html

&lt;B&gt;Scott McNealy acts serious.&lt;/B&gt; In an unexpected twist, wisecracking Sun head Scott McNealy was sober and subdued at yesterday's meeting.

&lt;A HREF="http://www.sun.com/Imposter.html"&gt;More details...&lt;/A&gt;

## Listing 12.6 Item3.html

&lt;B&gt;Larry Ellison acts conciliatory.&lt;/B&gt; Catching his competitors off guard yesterday, Oracle prez Larry Ellison referred to his rivals in friendly and respectful terms.

&lt;A HREF="http://www.oracle.com/Mistake.html"&gt;More details...&lt;/A&gt;

## Listing 12.7 Item4.html

&lt;B&gt;Sportscaster uses "literally" correctly.&lt;/B&gt; In an apparent slip of the tongue, a popular television commentator was heard to use the word "literally" when he did &lt;I&gt;not&lt;/I&gt; mean "figuratively."

&lt;A HREF="http://www.espn.com/Slip.html"&gt;More details...&lt;/A&gt;

Figure 12-2 Result of WhatsNew.jsp .

<!-- image -->

## 12.2 Including Files at Request Time