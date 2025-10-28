## Listing 2.5 servletc.bat

```
@echo off
```

```
rem This is the version for the Java Web Server. rem See http://www.coreservlets.com/ for other versions. set CLASSPATH=C:\JavaWebServer2.0\lib\servlet.jar; C:\JavaWebServer2.0\lib\jsp.jar; C:\MyServlets C:\JDK1.1.8\bin\javac -d C:\JavaWebServer2.0\servlets %1%
```

http://localhost/servlet/coreservlets.HelloWWW2

would invoke the HelloWWW2 servlet, as illustrated in Figure 2-3.

Figure 2-3 Invoking a servlet in a package via

<!-- image -->

http://hostname/servlet/packagename.servletName .

## 2.5 Simple HTML-Building Utilities

An HTML document is structured as follows:

```
<!DOCTYPE ...> <HTML> <HEAD><TITLE>...</TITLE>...</HEAD> <BODY ...> ... </BODY> </HTML>
```

You might be tempted to omit part of this structure, especially the DOCTYPE line, noting that virtually all major browsers ignore it, even though the

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 2.5 Simple HTML-Building Utilities

## Chapter 2 First Servlets

HTML 3.2 and 4.0 specifications require it. I strongly discourage this practice.  The  advantage  of  the DOCTYPE line  is  that  it  tells  HTML  validators which version of HTML you are using, so they know which specification to check your document against. These validators are very valuable debugging services, helping you catch HTML syntax errors that your browser guesses well on, but that other browsers will have trouble displaying. The two most popular on-line validators are the ones from the World Wide Web Consortium  ( http://validator.w3.org/ )  and  from  the  Web  Design  Group ( http://www.htmlhelp.com/tools/validator/ ).  They  let  you  submit  a URL, then they retrieve the page, check the syntax against the formal HTML specification,  and  report  any  errors  to  you.  Since  a  servlet  that  generates HTML looks like a regular Web page to visitors, it can be validated in the normal manner unless it requires POST data to return its result. Remember that GET data is attached to the URL, so you can submit a URL that includes GET data to the validators.

<!-- image -->

## Core Approach

Use an HTML validator to check the syntax of pages that your servlets generate.

Admittedly it is a bit cumbersome to generate HTML with println statements, especially long tedious lines like the DOCTYPE declaration. Some people address this  problem by  writing  detailed HTML generation  utilities  in  Java, then use them throughout their servlets. I'm skeptical of the utility of an extensive  library  for  this.  First  and  foremost,  the  inconvenience  of  generating HTML programmatically is one of the main problems addressed by JavaServer Pages (discussed in the second part of this book). JSP is a better solution, so don't  waste  effort  building  a  complex  HTML  generation  package.  Second, HTML generation routines can be cumbersome and tend not to support the full range of HTML attributes ( CLASS and ID for style sheets, JavaScript event handlers, table cell background colors, and so forth). Despite the questionable value of a full-blown HTML generation library, if you find you're repeating the same constructs many times, you might as well create a simple utility file that simplifies  those  constructs.  For  standard  servlets,  there  are  two  parts  of  the Web page ( DOCTYPE and HEAD ) that are unlikely to change and thus could benefit from being incorporated into a simple utility file. These are shown in List-

## 2.5 Simple HTML-Building Utilities

ing 2.6, with Listing 2.7 showing a variation of HelloWWW2 that makes use of this utility. I'll add a few more utilities throughout the book.

```
Listing 2.6 ServletUtilities.java package coreservlets; import javax.servlet.*; import javax.servlet.http.*; public class ServletUtilities { public static final String DOCTYPE = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " + "Transitional//EN\">"; public static String headWithTitle(String title) { return(DOCTYPE + "\n" + "<HTML>\n" + "<HEAD><TITLE>" + title + "</TITLE></HEAD>\n"); } ... } Listing 2.7 HelloWWW3.java
```

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class HelloWWW3 extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); out.println( ServletUtilities.headWithTitle("Hello WWW") + "<BODY>\n" + "<H1>Hello WWW</H1>\n" + "</BODY></HTML>"); } }
```