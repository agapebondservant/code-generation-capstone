## 14.5 Optionally Including the Tag Body

Figure 14-4 The custom csajsp:heading element gives you much more control over heading format than does the standard H1 through H6 elements in HTML.

<!-- image -->

## 14.5 Optionally Including the Tag Body

Most tags either never make use of body content or always do so. This section shows you how to use request time information to decide whether or not to include the tag body. Although the body can contain JSP that is interpreted at page translation time, the result of that translation is servlet code that can be invoked or ignored at request time.

## The Tag Handler Class

Optionally including the tag body is a trivial exercise: just return EVAL\_BODY\_INCLUDE or SKIP\_BODY depending  on  the  value  of  some request  time expression. The important thing to know is how to discover that  request  time  information,  since doStartTag does  not  have HttpServletRequest and HttpServletResponse arguments  as  do service ,

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 14 Creating Custom JSP Tag Libraries

\_jspService , doGet ,  and doPost .  The  solution  to  this  dilemma  is to  use getRequest to  obtain  the HttpServletRequest from  the  automatically defined pageContext field  of TagSupport .  Strictly  speaking,  the  return type  of getRequest is ServletRequest ,  so  you  have  to  do  a  typecast  to HttpServletRequest if  you  want  to  call  a  method  that  is  not  inherited from ServletRequest . However, in this case I just use getParameter , so no typecast is required.

Listing  14.13  defines  a  tag  that  ignores  its  body  unless  a  request  time debug parameter is supplied. Such a tag provides a useful capability whereby you embed debugging information directly in the JSP page during development, but activate it only when a problem occurs.

```
Listing 14.13 DebugTag.java
```

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import javax.servlet.*; /** A tag that includes the body content only if *  the "debug" request parameter is set. */ public class DebugTag extends TagSupport { public int doStartTag() { ServletRequest request = pageContext.getRequest(); String debugFlag = request.getParameter("debug"); if ((debugFlag != null) && (!debugFlag.equalsIgnoreCase("false"))) { return(EVAL_BODY_INCLUDE); } else { return(SKIP_BODY); } } }
```

## 14.5 Optionally Including the Tag Body

## The Tag Library Descriptor File

If your tag ever makes use of its body, you must provide the value JSP inside the bodycontent element. Other than that, all the elements within tag are used in the same way as described previously. Listing 14.14 shows the entries needed for DebugTag .

## Listing 14.14 csajsp-taglib.tld

```
<?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" --> <tlibversion>1.0</tlibversion> <jspversion>1.1</jspversion> <shortname>csajsp</shortname> <urn></urn> <info> A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. </info> <!-- Other tags defined earlier... --> <tag> <name>debug</name> <tagclass>coreservlets.tags.DebugTag</tagclass> <info>Includes body only if debug param is set.</info> <bodycontent>JSP</bodycontent> </tag> </taglib>
```

## Chapter 14 Creating Custom JSP Tag Libraries

## The JSP File

Listing  14.15  shows  a  page  that  encloses  debugging  information  between &lt;csajsp:debug&gt; and &lt;/csajsp:debug&gt; .  Figures 14-5 and 14-6 show the normal result and the result when a request time debug parameter is supplied, respectively.

```
Listing 14.15 DebugExample.jsp <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Using the Debug Tag</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <H1>Using the Debug Tag</H1> <%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %> Top of regular page. Blah, blah, blah. Yadda, yadda, yadda. <P> <csajsp:debug> <B>Debug:</B> <UL> <LI>Current time: <%= new java.util.Date() %> <LI>Requesting hostname: <%= request.getRemoteHost() %> <LI>Session ID: <%= session.getId() %> </UL> </csajsp:debug> <P> Bottom of regular page. Blah, blah, blah. Yadda, yadda, yadda. </BODY> </HTML>
```

## 14.5 Optionally Including the Tag Body

<!-- image -->

Figure 14-5 The body of the csajsp:debug element is normally ignored.

<!-- image -->

Figure 14-6 The body of the csajsp:debug element is included when a debug request parameter is supplied.

<!-- image -->