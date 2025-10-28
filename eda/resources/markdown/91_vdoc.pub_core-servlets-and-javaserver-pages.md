## Chapter 11 The JSP page Directive: Structuring Generated Servlets

markup tags; it is discussed in Chapter 14 (Creating Custom JSP Tag Libraries).

The page directive lets you define one or more of the following case-sensitive  attributes: import , contentType , isThreadSafe , session , buffer , autoflush , extends , info , errorPage , isErrorPage ,  and language . These attributes are explained in the following sections.

## 11.1 The import Attribute

The import attribute of the page directive lets you specify the packages that should be imported by the servlet into which the JSP page gets translated. If you  don't  explicitly specify any  classes  to import,  the  servlet  imports java.lang.* , javax.servlet.* , javax.servlet.jsp.* , javax.servlet.http.* ,  and  possibly  some  number  of  server-specific  entries.  Never write JSP code that relies on any server-specific classes being imported automatically. Use of the import attribute takes one of the following two forms:

```
<%@ page import="package.class" %> <%@ page import="package.class1,...,package.classN" %>
```

For  example,  the  following  directive  signifies  that  all  classes  in  the java.util package should be available to use without explicit package identifiers.

&lt;%@ page import="java.util.*" %&gt;

The import attribute is the only page attribute that is allowed to appear multiple  times  within  the  same  document.  Although page directives  can appear anywhere within the document, it is traditional to place import statements either near the top of the document or just before the first place that the referenced package is used.

## Directories for Custom Classes

If you  import  classes that are not in any of the standard java or javax.servlet packages, you need to be sure that those classes have been properly  installed  on  your  server.  In  particular,  most  servers  that  support automatic servlet reloading do not permit classes that are in the auto-reloading directories to be referenced by JSP pages. The particular locations used for  servlet  classes  vary  from  server  to  server,  so  you  should  consult  your server's documentation for definitive guidance. The locations used by Apache Tomcat 3.0, the JSWDK 1.0.1, and the Java Web Server 2.0 are summarized

## 11.1 The import Attribute

in Table 11.1. All three of these servers also make use of JAR files in the lib subdirectory, and in all three cases you must restart the server whenever you change files in this directory.

## Table 11.1  Class Installation Directories

| Server              | Location Relative to Installation Directory   | Use                                                  | Automatically Reloaded When Class Changes?   | Availab le from JSP Pages?   |
|---------------------|-----------------------------------------------|------------------------------------------------------|----------------------------------------------|------------------------------|
| Tomcat 3.0          | webpages/WEB-INF/ classes                     | Standardlocation for servlet classes                 | No                                           | Yes                          |
| Tomcat 3.0          | classes                                       | Alternative loca- tion for servlet classes           | No                                           | Yes                          |
| JSWDK 1.0.1         | webpages/WEB-INF/ servlets                    | Standardlocation for servlet classes                 | No                                           | Yes                          |
| JSWDK 1.0.1         | classes                                       | Alternative loca- tion for servlet classes           | No                                           | Yes                          |
| Java Web Server 2.0 | servlets                                      | Location for fre- quently chang- ing servlet classes | Yes                                          | No                           |
| Java Web Server 2.0 | classes                                       | Location for infrequently changing servlet classes   | No                                           | Yes                          |

## Example

Listing 11.1 presents a page that uses three classes not in the standard JSP import list: java.util.Date , coreservlets.ServletUtilities (see Listing 8.3), and coreservlets.LongLivedCookie (see Listing 8.4). To simplify references to these classes, the JSP page uses

&lt;%@ page import="java.util.*,coreservlets.*" %&gt;

Figures 11-1 and 11-2 show some typical results.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 11 The JSP page Directive: Structuring Generated Servlets

## Listing 11.1 ImportAttribute.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>The import Attribute</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <H2>The import Attribute</H2> <%-- JSP page directive --%> <%@ page import="java.util.*,coreservlets.*" %> <%-- JSP Declaration (see Section 10.4) --%> <%! private String randomID() { int num = (int)(Math.random()*10000000.0); return("id" + num); } private final String NO_VALUE = "<I>No Value</I>"; %> <%-- JSP Scriptlet (see Section 10.3) --%> <% Cookie[] cookies = request.getCookies(); String oldID = ServletUtilities.getCookieValue(cookies, "userID", NO_VALUE); String newID; if (oldID.equals(NO_VALUE)) { newID = randomID(); } else { newID = oldID; } LongLivedCookie cookie = new LongLivedCookie("userID", newID); response.addCookie(cookie); %> <%-- JSP Expressions (see Section 10.2) --%> This page was accessed at <%= new Date() %> with a userID cookie of <%= oldID %>. </BODY> </HTML>
```