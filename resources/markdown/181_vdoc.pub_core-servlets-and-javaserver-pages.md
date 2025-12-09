## A.2 First Servlets

## Java Web Server 2.0 Standard Directories

- · install\_dir/servlets

Location for frequently changing servlet classes. Auto-reloading.

- · install\_dir/classes

Location for infrequently changing servlet classes.

- · install\_dir/lib

Location for JAR files containing classes.

## A.2 First Servlets

## Simple Servlet

```
HelloWWW.java import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class HelloWWW extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String docType = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 " + "Transitional//EN\">\n"; out.println(docType + "<HTML>\n" + "<HEAD><TITLE>Hello WWW</TITLE></HEAD>\n" + "<BODY>\n" + "<H1>Hello WWW</H1>\n" + "</BODY></HTML>"); } }
```

## Installing Servlets

- · Put in servlet directories shown in Section A.1.
- · Put in subdirectories corresponding to their package.

## Invoking Servlets

- · http://host/servlet/ServletName
- · http://host/servlet/package.ServletName
- · Arbitrary location defined by server-specific customization.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.