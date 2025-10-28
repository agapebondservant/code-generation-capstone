' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter JSP Scripting Elements

<!-- image -->

## Topics in This Chapter

- · The purpose of JSP
- · How JSP pages are invoked
- · Using JSP expressions to insert dynamic results directly into the output page
- · Using JSP scriptlets to insert Java code into the method that handles requests for the page
- · Using JSP declarations to add methods and field declarations to the servlet that corresponds to the JSP page
- · Predefined variables that can be used within expressions and scriptlets

Home page for this book: http://www.coreservlets.com. Home page for sequel: http://www.moreservlets.com. Servlet and JSP training courses: http://courses.coreservlets.com.

' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

<!-- image -->

avaServer  Pages  (JSP)  technology  enables  you  to  mix  regular,  static HTML with dynamically generated content from servlets. You simply write  the  regular  HTML  in  the  normal  manner,  using  familiar Web-page-building tools. You then enclose the code for the dynamic parts  in  special  tags,  most  of  which  start  with &lt;% and  end  with %&gt; .  For example, here is a section of a JSP page that results in 'Thanks for ordering Core  Web  Programming '  for  a  URL  of http://host/OrderConfirmation.jsp?title=Core+Web+Programming : J

Thanks for ordering &lt;I&gt;&lt;%= request.getParameter("title") %&gt;&lt;/I&gt;

Separating the static HTML from the dynamic content provides a number of  benefits  over  servlets  alone,  and  the  approach  used  in  JavaServer  Pages offers several advantages over competing technologies such as ASP, PHP, or ColdFusion. Section 1.4 (The Advantages of JSP) gives some details on these advantages, but they basically boil down to two facts: that JSP is widely supported and thus doesn't lock you into a particular operating system or Web server and that JSP gives you full access to servlet and Java technology for the dynamic part, rather than requiring you to use an unfamiliar and weaker special-purpose language.

The process of making JavaServer Pages accessible on the Web is much simpler than that for servlets. Assuming you have a Web server that supports JSP, you give your file a .jsp extension and simply install it in any place you

## Chapter 10 JSP Scripting Elements

could  put  a  normal  Web  page:  no  compiling,  no  packages,  and  no  user CLASSPATH settings.  However,  although your personal environment doesn't need any special settings, the server still has to be set up with access to the servlet and JSP class files and the Java compiler. For details, see your server's documentation or Section 1.5 (Installation and Setup).

Although what you write often looks more like a regular HTML file than a servlet, behind the scenes, the JSP page is automatically converted to a normal servlet, with the static HTML simply being printed to the output stream associated  with  the  servlet's service method.  This  translation  is  normally done the first time the page is requested. To ensure that the first real user doesn't get a momentary delay when the JSP page is translated into a servlet and compiled, developers can simply request the page themselves after first installing it. Many Web servers also let you define aliases so that a URL that appears to reference an HTML file really points to a servlet or JSP page.

Depending on how your server is set up, you can even look at the source code for servlets generated from your JSP pages. With Tomcat 3.0, you need to change the isWorkDirPersistent attribute from false to true in install\_dir /server.xml . After that, the code can be found in install\_dir /work/ port-number .  With  the  JSWDK  1.0.1,  you  need  to change the workDirIsPersistent attribute from false to true in install\_dir /webserver.xml . After that, the code can be found in install\_dir /work/%3A port-number %2F . With the Java Web Server, 2.0 the default setting is to save source code for automatically generated servlets. They can be found in install\_dir /tmpdir/default/pagecompile/jsp/\_JSP .

One warning about the automatic translation  process  is in  order.  If  you make an error in the dynamic portion of your JSP page, the system may not be able to properly translate it into a servlet. If your page has such a fatal translation-time error, the server will present an HTML error page describing the problem to the client. Internet Explorer 5, however, typically replaces server-generated error messages with a canned page that it considers friendlier. You will need to turn off this 'feature' when debugging JSP pages. To do so with Internet Explorer 5, go to the Tools menu, select Internet Options, choose the Advanced tab, and make sure 'Show friendly HTTP error messages' box is not checked.

<!-- image -->

## Core Warning

When debugging JSP pages, be sure to turn off Internet Explorer's 'friendly' HTTP error messages.