## 2.2 A Simple Servlet Generating Plain Text

## 2.2 A Simple Servlet Generating Plain T ext

Listing 2.2 shows a simple servlet that just generates plain text, with the output  shown  in  Figure  2-1.  Section  2.3  (A  Servlet  That  Generates  HTML) shows the more usual case where HTML is generated. However, before moving on, it is worth spending some time going through the process of installing, compiling, and running this simple servlet. You'll find this a bit tedious the first time you try it. Be patient; since the process is the same each time, you'll quickly  get  used  to  it,  especially  if  you  partially  automate  the  process  by means of a script file such as that presented in the following section.

## Listing 2.2 HelloWorld.java import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class HelloWorld extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { PrintWriter out = response.getWriter(); out.println("Hello World"); } }

Figure 2-1 Result of Listing 2.2 ( HelloWorld.java ).

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 2 First Servlets

## Compiling and Installing the Servlet

The first thing you need to do is to make sure that your server is configured properly and that your CLASSPATH refers to the JAR files containing the standard servlet classes. Please refer to Section 1.5 (Installation and Setup) for an explanation of this process.

The next step is to decide where to put the servlet classes. This location varies from server to server, so refer to your Web server documentation for definitive directions. However, there are some moderately common conventions. Most servers have three distinct locations for servlet classes, as detailed below.

## 1. A directory for frequently changing servlet classes.

- Servlets in this directory are automatically reloaded when their class file changes, so you should use this directory during development. For example, this is normally install\_dir /servlets with Sun's Java Web Server and IBM's WebSphere and install\_dir /myserver/servletclasses for BEA WebLogic, although most servers let the server administrator specify a different location. Neither Tomcat nor the JSWDK support automatic servlet reloading. Nevertheless, they still have a similar directory in which to place servlets; you just have to stop and restart the mini-server each time you change an existing servlet. With Tomcat 3.0, place servlets in install\_dir /webpages/WEB-INF/classes . With the JSWDK 1.0.1, use

install\_dir /webpages/WEB-INF/servlets .

- 2. A directory for infrequently changing servlet classes. Servlets placed in this location are slightly more efficient since the server doesn't have to keep checking their modification dates. However, changes to class files in this directory require you to restart the server. This option (or Option 3 below) is the one to use for 'production' servlets deployed to a high-volume site. This directory is usually something like install\_dir /classes , which is the default name with Tomcat, the JSWDK, and the Java Web Server. Since Tomcat and the JSWDK do not support automatic servlet reloading, this directory works the same as the one described in Option 1, so most developers stick with that previous option.

## 2.2 A Simple Servlet Generating Plain Text

## 3. A directory for infrequently changing servlets in JAR files.

With the second option above, the class files are placed directly in the classes directory or in subdirectories corresponding to their package name. Here, the class files are packaged in a JAR file, and that file is then placed in the designated directory. With Tomcat, the JSWDK, the Java Web Server, and most other servers, this directory is install\_dir /lib . You must restart the server whenever you change files in this directory.

Once you've configured your server, set your CLASSPATH ,  and placed the servlet  in  the  proper  directory,  simply  do  ' javac  HelloWorld.java '  to compile the servlet. In production environments, however, servlets are frequently placed into packages to avoid name conflicts with servlets written by other  developers.  Using  packages  involves  a  couple  of  extra  steps  that  are covered in Section 2.4 (Packaging Servlets). Also, it is common to use HTML forms as front ends to servlets (see Chapter 16). To use them, you'll need to know where  to  place  regular  HTML  files  to  make  them  accessible  to  the server. This location varies from server to server, but with the JSWDK and Tomcat, you place an HTML file in install\_dir /webpages/path/file.html and then access it via http://localhost/path/file.html (replace localhost with  the  real hostname if running remotely). A JSP page can be installed anywhere that a normal HTML page can be.

## Invoking the Servlet

With different servers, servlet classes can be placed in a variety of different locations, and there is little standardization among servers. To invoke servlets, however, there is a common  convention: use a URL  of the  form http://host/servlet/ServletName .  Note that the URL refers to servlet ,  singular, even if the real directory containing the servlet code is called servlets , plural, or has an unrelated name like classes or lib .

Figure 2-1, shown earlier in this section, gives an example with the Web server running directly on my PC ('localhost' means 'the current machine').

Most servers also let you register names for servlets, so that a servlet can be  invoked  via http://host/any-path/any-file .  The  process  for  doing this is server-specific; check your server's documentation for details.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.