## 2.7 An Example Using Initialization Parameters

in  languages (such as ones named after letters of the alphabet) where it is easy to read or write off the ends of arrays, make illegal typecasts, or have dangling  pointers  due  to  memory  reclamation  errors.  Besides,  even  Java technology won't prevent someone from tripping over the power cable running to the computer. So, don't count on destroy as the only mechanism for saving state to disk. Activities like hit counting or accumulating lists of cookie values that indicate special access should also proactively write their state to disk periodically.

## 2.7 An Example Using Initialization Parameters

Listing 2.8 shows a servlet that reads the message and repeats initialization parameters when initialized. Figure 2-5 shows the result when message is Shibboleth , repeats is 5 ,  and  the  servlet  is  registered  under  the  name ShowMsg .  Remember that, although servlets read init  parameters in a standard way, developers set init parameters in a server-specific manner. Please refer to your server documentation for authoritative details. Listing 2.9 shows the configuration file used with Tomcat to obtain the result of Figure 2-5, Listing 2.10 shows the configuration file used with the JSWDK, and Figures 2-6 and 2-7 show how to set the parameters interactively with the Java Web Server. The result is identical to Figure 2-5 in all three cases.

Because the process of setting init parameters is server-specific, it is a good idea to minimize the number of separate initialization entries that have to be specified. This will limit the work you need to do when moving servlets that use init parameters from one server to another. If you need to read a large amount of data, I recommend that the init parameter itself merely give the location of a parameter file, and that the real data go in that file. An example of  this  approach is given  in  Section  4.5  (Restricting Access  to  Web  Pages), where the initialization parameter specifies nothing more than the location of the password file.

## Core Approach

For complex initializations, store the data in a separate file and use the init parameters to give the location of that file.

<!-- image -->

## Chapter 2 First Servlets

## Listing 2.8 ShowMessage.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; /** Example using servlet initialization. Here, the message *  to print and the number of times the message should be *  repeated is taken from the init parameters. */ public class ShowMessage extends HttpServlet { private String message; private String defaultMessage = "No message."; private int repeats = 1; public void init(ServletConfig config) throws ServletException { // Always call super.init super.init(config); message = config.getInitParameter("message"); if (message == null) { message = defaultMessage; } try { String repeatString = config.getInitParameter("repeats"); repeats = Integer.parseInt(repeatString); } catch(NumberFormatException nfe) { // NumberFormatException handles case where repeatString // is null *and* case where it is something in an // illegal format. Either way, do nothing in catch, // as the previous value (1) for the repeats field will // remain valid because the Integer.parseInt throws // the exception *before* the value gets assigned // to repeats. } } public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "The ShowMessage Servlet"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>");
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 2.7 An Example Using Initialization Parameters

## Listing 2.8 ShowMessage.java (continued)

```
for(int i=0; i<repeats; i++) { out.println(message + "<BR>"); } out.println("</BODY></HTML>"); } }
```

Figure 2-5 The ShowMessage servlet with server-specific initialization parameters.

<!-- image -->

Listing 2.9 shows the setup file used to supply initialization parameters to servlets used with Tomcat 3.0. The idea is that you first associate a name with the servlet class file, then associate initialization parameters with that name (not with the actual class file). The setup file is located in install\_dir /webpages/WEB-INF . Rather than recreating a similar version by  hand,  you  might  want  to  download  this  file  from http://www.coreservlets.com/ , modify it, and copy it to install\_dir /webpages/WEB-INF .

Listing 2.10 shows the properties file used to supply initialization parameters  to  servlets  in  the  JSWDK.  As  with  Tomcat,  you  first  associate  a  name with  the  servlet  class,  then  associate  the  initialization  parameters  with  the name. The properties file is located in install\_dir /webpages/WEB-INF .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 42 Chapter 2 First Servlets

## Listing 2.9 web.xml (for T omcat)

```
<?xml version="1.0" encoding="ISO-8859-1"?> <!DOCTYPE web-app PUBLIC "-//Sun Microsystems, Inc.//DTD Web Application 2.2//EN" "http://java.sun.com/j2ee/dtds/web-app_2.2.dtd"> <web-app> <servlet> <servlet-name> ShowMsg </servlet-name> <servlet-class> coreservlets.ShowMessage </servlet-class> <init-param> <param-name> message </param-name> <param-value> Shibboleth </param-value> </init-param> <init-param> <param-name> repeats </param-name> <param-value> 5 </param-value> </init-param> </servlet> </web-app>
```

## 2.7 An Example Using Initialization Parameters

## Listing 2.10 servlets.properties

- # servlets.properties used with the JSWDK
- # Register servlet via servletName.code=servletClassFile
- # You access it via http://host/examples/servlet/servletName

ShowMsg.code=coreservlets.ShowMessage

- # Set init params via
- #   servletName.initparams=param1=val1,param2=val2,...

ShowMsg.initparams=message=Shibboleth,repeats=5

- # Standard setting
- jsp.code=com.sun.jsp.runtime.JspServlet
- # Set this to keep servlet source code built from JSP jsp.initparams=keepgenerated=true

Figure 2-6 Registering a name for a servlet with the Java Web Server. Servlets that use initialization parameters must first be registered this way.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->