## Core Approach

Always set the content type before transmitting the actual document.

## 2.4 Packaging Servlets

<!-- image -->

The second step in writing a servlet that builds an HTML document is to have your println statements output HTML, not plain text. The structure of an HTML document is discussed more in Section 2.5 (Simple HTML-Building Utilities), but it should be familiar to most readers. Listing 2.3 gives an example servlet, with the result shown in Figure 2-2.

## Listing 2.3 HelloWWW.java import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class HelloWWW extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String docType = "&lt;!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " + "Transitional//EN\"&gt;\n"; out.println(docType + "&lt;HTML&gt;\n" + "&lt;HEAD&gt;&lt;TITLE&gt;Hello WWW&lt;/TITLE&gt;&lt;/HEAD&gt;\n" + "&lt;BODY&gt;\n" + "&lt;H1&gt;Hello WWW&lt;/H1&gt;\n" + "&lt;/BODY&gt;&lt;/HTML&gt;"); } }

## 2.4 Packaging Servlets

In  a  production  environment,  multiple  programmers  may  be  developing servlets for the same server. So, placing all the servlets in the top-level servlet directory results in a massive hard-to-manage directory and risks name conflicts when two developers accidentally choose the same servlet name. Packages  are  the  natural  solution  to  this  problem.  Using  packages  results  in changes in the way the servlets are created, the way that they are compiled,

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 2 First Servlets

Figure 2-2 Result of Listing 2.3 ( HelloWWW.java ).

<!-- image -->

and the way they're invoked. Let's take these areas one at a time in the following three subsections. The first two changes are exactly the same as with any other Java class that uses packages; there is nothing specific to servlets.

## Creating Servlets in Packages

Two steps are needed to place servlets in packages:

- 1. Move the files to a subdirectory that matches the intended package name.

For example, I'll use the coreservlets package for most of the rest of the servlets in this book. So, the class files need to go in a subdirectory called coreservlets .

- 2. Insert a package statement in the class file.

For example, to place a class file in a package called somePackage , the first line of the file should read package somePackage;

For example, Listing 2.4 presents a variation of the HelloWWW servlet that  is  in  the coreservlets package.  The  class  file  goes  in install\_dir /webpages/WEB-INF/classes/coreservlets for Tomcat 3.0,  in install\_dir /webpages/WEB-INF/servlets/coreservlets for the JSWDK 1.0.1, and in install\_dir /servlets/coreservlets for the Java Web Server 2.0.

## Listing 2.4 HelloWWW2.java

## package coreservlets;

```
import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class HelloWWW2 extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String docType = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " + "Transitional//EN\">\n"; out.println(docType + "<HTML>\n" + "<HEAD><TITLE>Hello WWW</TITLE></HEAD>\n" + "<BODY>\n" + "<H1>Hello WWW</H1>\n" + "</BODY></HTML>"); } }
```

## Compiling Servlets in Packages

There are two main ways to compile classes that are in packages. The first option is to place your package subdirectory right in the directory where the Web server expects servlets to go. Then, you would set the CLASSPATH variable to point to the directory above the one actually containing your servlets, that is, to the main servlet directory used by the Web server. You can then compile normally from within the package-specific subdirectory. For example, if your base servlet directory is C:\JavaWebServer2.0\servlets and your package name (and thus subdirectory name) is coreservlets , and you are running Windows, you would do:

DOS&gt; set CLASSPATH=C:\JavaWebServer2.0\servlets;%CLASSPATH%

```
DOS> cd C:\JavaWebServer2.0\servlets\coreservlets DOS> javac HelloWorld.java
```

The first part, setting the CLASSPATH , you probably want to do permanently, rather than each time you start a new DOS window. On Windows 95/98 you typically  put  the set CLASSPATH=... statement in your autoexec.bat file somewhere after the line that sets  the CLASSPATH to  point to servlet.jar

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 2.4 Packaging Servlets

## Chapter 2 First Servlets

and the JSP JAR file. On Windows NT or Windows 2000, you go to the Start menu, select Settings, select Control Panel, select System, select Environment, then enter the variable and value. On Unix (C shell), you set the CLASSPATH variable by setenv CLASSPATH / install\_dir /servlets:$CLASSPATH

Put this in your .cshrc file to make it permanent.

If your package were of the form name1.name2.name3 rather than simply name1 as here, the CLASSPATH should still point to the top-level servlet directory, that is, the directory containing name1 .

A second way to compile classes that are in packages is to keep the source code in a location distinct from the class files. First, you put your package directories in any location you find convenient. The CLASSPATH refers to this location. Second, you use the -d option  of javac to  install  the  class  files  in  the directory the Web server expects. An example follows. Again, you will probably want to set the CLASSPATH permanently rather than set it each time.

DOS&gt; cd C:\MyServlets\coreservlets

DOS&gt; set CLASSPATH=C:\MyServlets;%CLASSPATH%

DOS&gt; javac -d C:\tomcat\webpages\WEB-INF\classes HelloWWW2.java

Keeping the source code separate from the class files is the approach I use for my own development. To complicate my life further, I have a number of different CLASSPATH settings  that I  use  for  different  projects,  and  typically use JDK 1.2, not JDK 1.1 as the Java Web Server expects. So, on Windows I find it convenient to automate the servlet compilation process with a batch file servletc.bat , as shown in Listing 2.5 (line breaks in the set CLASSPATH line  inserted  only  for  readability).  I  put  this  batch  file  in C:\Windows\Command or  somewhere  else  in  the  Windows PATH .  After  this,  to compile  the HelloWWW2 servlet  and  install  it  with  the  Java  Web  Server,  I merely go to C:\MyServlets\coreservlets and do ' servletc HelloWWW2.java '.  The  source  code  archive  at http://www.coreservlets.com/ contains variations of servletc.bat for the JSWDK and Tomcat. You can do something similar on Unix with a shell script.

## Invoking Servlets in Packages

To invoke a servlet that is in a package, use the URL

http://host/servlet/packageName.ServletName

instead of

http://host/servlet/ServletName

Thus, if the Web server is running on the local system,

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.