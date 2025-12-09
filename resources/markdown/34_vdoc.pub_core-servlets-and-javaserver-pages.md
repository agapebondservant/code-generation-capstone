## Chapter 1 Overview of Servlets and JavaServer Pages

## Versus Static HTML

Regular  HTML,  of  course,  cannot  contain  dynamic  information,  so  static HTML pages cannot be based upon user input or server-side data sources. JSP is so easy and convenient that it is quite reasonable to augment HTML pages that only benefit slightly by the insertion of dynamic data. Previously, the difficulty of using dynamic data precluded its use in all but the most valuable instances.

## 1.5 Installation and Setup

Before you can get started, you have to download the software you need and configure your system to take advantage of it. Here's an outline of the steps involved. Please note, however, that although your servlet code will follow a standard API, there is no standard for downloading and configuring Web or application  servers.  Thus,  unlike  most  sections  of  this  book,  the  methods described here vary significantly from server to server, and the examples in this  section  should  be  taken  only  as  representative  samples.  Check  your server's documentation for authoritative instructions.

## Obtain Servlet and JSP Software

Your first step is to download software that implements the Java Servlet 2.1 or 2.2  and  JavaServer  Pages  1.0  or  1.1  specifications.  If  you  are  using  an up-to-date Web or application server, there is a good chance that it already has everything you need. Check your server documentation or see the latest list of servers that support servlets at http://java.sun.com/products/servlet/industry.html .  Although you'll eventually want to deploy in a commercial-quality server, when first learning it is useful to have a free system that you  can install  on  your desktop  machine for development and testing purposes. Here are some of the most popular options:

## · Apache Tomcat.

Tomcat is the official reference implementation of the servlet 2.2 and JSP 1.1 specifications. It can be used as a small stand-alone server for testing servlets and JSP pages, or can be integrated into the Apache Web server. However, many other servers have announced upcoming support, so these specifications will be

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 1.5 Installation and Setup

covered in detail throughout this book. Tomcat, like Apache itself, is free. However, also like Apache (which is very fast, highly reliable, but a bit hard to configure and install), Tomcat requires significantly more effort to set up than do the commercial servlet engines. For details, see http://jakarta.apache.org/ .

## · JavaServer Web Development Kit (JSWDK).

- The JSWDK is the official reference implementation of the servlet 2.1 and JSP 1.0 specifications. It is used as a small stand-alone server for testing servlets and JSP pages before they are deployed to a full Web server that supports these technologies. It is free and reliable, but takes quite a bit of effort to install and configure. For details, see http://java.sun.com/products/servlet/download.html .

## · Allaire JRun.

JRun is a servlet and JSP engine that can be plugged into Netscape Enterprise or FastTrack servers, IIS, Microsoft Personal Web Server, older versions of Apache, O'Reilly's WebSite, or StarNine WebSTAR. A limited version that supports up to five simultaneous connections is available for free; the commercial version removes this restriction and adds capabilities like a remote administration console. For details, see http://www.allaire.com/products/jrun/ .

- · New Atlanta's ServletExec. ServletExec is a servlet and JSP engine that can be plugged into most popular Web servers for Solaris, Windows, MacOS, HP-UX and Linux. You can download and use it for free, but many of the advanced features and administration utilities are disabled until you purchase a license. For details, see http://newatlanta.com/ .

## · LiteWebServer (LWS) from Gefion Software.

- LWS is a small free Web server derived from Tomcat that supports servlets version 2.2 and JSP 1.1. Gefion also has a free plug-in called WAICoolRunner that adds servlet 2.2 and JSP 1.1 support to Netscape FastTrack and Enterprise servers. For details, see http://www.gefionsoftware.com/.

## · Sun's Java Web Server.

This server is written entirely in Java and was one of the first Web servers to fully support the servlet 2.1 and JSP 1.0 specifications. Although it is no longer under active development because Sun is concentrating on the Netscape/I-Planet server, it is still a popular choice for learning

13

## Chapter 1 Overview of Servlets and JavaServer Pages

servlets and JSP. For a free trial version, see . For a http://www.sun.com/software/jwebserver/try/ free non-expiring version for teaching purposes at academic institutions, see http://freeware.thesphere.com/ .

## Bookmark or Install the Servlet and JSP API Documentation

Just as no serious programmer should develop general-purpose Java applications without access to the JDK 1.1 or 1.2 API documentation, no serious programmer should develop servlets or JSP pages without access to the API for classes in the javax.servlet packages. Here is a summary of where to find the API:

- · http://java.sun.com/products/jsp/download.html This site lets you download either the 2.1/1.0 API or the 2.2/1.1 API to your local system. You may have to download the entire reference implementation and then extract the documentation.
- · http://java.sun.com/products/servlet/2.2/javadoc/ This site lets you browse the servlet 2.2 API on-line.
- · http://www.java.sun.com/j2ee/j2sdkee/techdocs/api/ This address lets you browse the complete API for the Java 2 Platform, Enterprise Edition (J2EE), which includes the servlet 2.2 and JSP 1.1 packages.

If Sun or Apache place any new additions on-line (e.g., a place to browse the  2.1/1.0  API),  they  will  be  listed  under  Chapter  1  in  the  book  source archive at http://www.coreservlets.com/ .

## Identify the Classes to the Java Compiler

Once you've obtained the necessary software, you need to tell the Java compiler ( javac ) where to find the servlet and JSP class files when it compiles your servlets. Check the documentation of your particular package for definitive details, but the necessary class files are usually in the lib subdirectory of the server's installation directory, with the servlet classes in servlet.jar and the  JSP  classes  in jsp.jar , jspengine.jar ,  or jasper.jar .  There  are  a couple of different ways to tell javac about these classes, the easiest of which is  to  put  the  JAR  files  in  your CLASSPATH .  If  you've  never  dealt  with  the CLASSPATH before,  it  is  the  variable  that  specifies  where javac looks  for

## 1.5 Installation and Setup

classes when compiling. If the variable is unspecified, javac looks in the current directory and the standard system libraries. If you set CLASSPATH yourself, be sure to include ' . ', signifying the current directory.

Following is a brief summary of how to set the environment variable on a couple of different platforms. Assume dir is the directory in which the servlet and JSP classes are found.

## Unix (C Shell)

setenv CLASSPATH .: dir /servlet.jar: dir /jspengine.jar

Add :$CLASSPATH to  the  end  of  the setenv line  if  your CLASSPATH is already set and you want to add more to it, not replace it. Note that on Unix systems you use forward slashes to separate directories within an entry and colons to separate entries, whereas you use backward slashes and semicolons on Windows. To make this setting permanent, you would typically put this statement in your .cshrc file.

## Windows

set CLASSPATH=.; dir \servlet.jar; dir \jspengine.jar

Add ;%CLASSPATH% to  the  end  of  the  above  line  if  your CLASSPATH is already set and you want to add more to it, not replace it. Note that on Windows you use backward slashes to separate directories within an entry and semicolons to separate entries, while you use forward slashes and colons on Unix. To make this setting permanent on Windows 95/98, you'd typically put this  statement  in  your autoexec.bat file.  On  Windows  NT  or  2000,  you would go to the Start menu, select Settings, select Control Panel, select System, select Environment, then enter the variable and value.

## Package the Classes

As you'll see in the next chapter, you probably want to put your servlets into packages  to  avoid  name  conflicts  with  servlets  other  people  write  for  the same Web or application server. In that case, you may find it convenient to add the top-level directory of your package hierarchy to the CLASSPATH as well. See Section 2.4 (Packaging Servlets) for details.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 1 Overview of Servlets and JavaServer Pages

## Configure the Server

Before you start the server, you may want to designate parameters like the port on which it listens, the directories in which it looks for HTML files, and so  forth.  This  process  is  totally  server-specific,  and  for  commercial-quality Web servers should be clearly documented in the installation notes. However, with the small stand-alone servers that Apache and Sun provide as reference implementations of the servlet 2.2/JSP 1.1 specs (Apache Tomcat) or 2.1/1.0 specs (Sun JSWDK), there are a number of important but poorly documented settings that I'll describe here.

## Port Number

Tomcat and the JSWDK both use a nonstandard port by default in order to avoid conflicts with existing Web servers. If you use one of these products for initial development and testing, and don't have another Web server running, you will probably find it convenient to switch to 80, the standard HTTP port number.  With  Tomcat  3.0,  do  so  by  editing install\_dir /server.xml , changing 8080 to 80 in the line

&lt;ContextManager port="8080" hostName="" inet=""&gt;

With the JSWDK 1.0.1, edit the install\_dir /webserver.xml file and replace 8080 with 80 in the line port NMTOKEN "8080"

The Java Web Server 2.0 also uses a non-standard port. To change it, use the  remote  administration  interface,  available  by  visiting http:// somehostname :9090/ , where somehostname is replaced by either the real name of the host running the server or by localhost if the server is running on the local machine.

## JAVA\_HOME Setting

If  you  use  JDK  1.2  or  1.3  with  Tomcat  or  the  JSWDK,  you  must  set  the JAVA\_HOME environment variable to refer to the JDK installation directory. This setting is unnecessary with JDK 1.1. The easiest way to specify this variable is  to insert  a  line  that  sets  it  into  the  top  of  the startup (Tomcat) or startserver (JSWDK) script. For example, here's the top of the modified version of startup.bat and startserver.bat that I use:

rem Marty Hall: added JAVA\_HOME setting below set JAVA\_HOME=C:\jdk1.2.2

## DOS Memory Setting

If you start Tomcat or the JSWDK server from Windows 95 or 98, you probably have to modify the amount of memory DOS allocates for environment variables. To do this, start a fresh DOS window, click on the MS-DOS icon in the  top-left  corner  of  the  window,  and  select Properties .  From  there, choose the Memory tab, go to the Initial Environment setting, and change the value from Auto to 2816. This configuration only needs to be done once.

## Tomcat 3.0 CR/LF Settings

The first releases of Tomcat suffered from a serious problem: the text files were saved in Unix format (where the end of line is marked with a linefeed), not Windows format (where the end of the line is marked with a carriage return/linefeed pair). As a result, the startup and shutdown scripts failed on Windows. You can determine if your version suffers from  this  problem  by opening install\_dir/startup.bat in  Notepad;  if  it  appears  normal  you have a patched version. If the file appears to be one long jumbled line, then quit Notepad and open and immediately save the following files using Wordpad ( not Notepad):

- · install\_dir / startup.bat
- · install\_dir / tomcat.bat
- · install\_dir / shutdown.bat
- · install\_dir / tomcatEnv.bat
- · install\_dir / webpages/WEB-INF/web.xml
- · install\_dir / examples/WEB-INF/web.xml

## Start the Server

To  start  one  of  the  'real'  Web  servers,  check  its  documentation.  In  many cases, starting it involves executing a command called httpd either from the command line or by instructing the operating system to do so automatically when the system is first booted.

With Tomcat 3.0, you start the server by executing a script called startup in the main installation directory. With the JSWDK 1.0.1, you execute a similar script called startserver .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 1.5 Installation and Setup

## Chapter 1 Overview of Servlets and JavaServer Pages

## Compile and Install Your Servlets

Once you've properly set your CLASSPATH ,  as  described earlier  in  this section, just use ' javac ServletName.java ' to compile a servlet. The resultant class file needs to go in a location that the server knows to check during execution. As you might expect, this location varies from server to server. Following is a quick summary of the locations used by the latest releases of Tomcat,  the  JSWDK,  and  the  Java  Web  Server.  In  all  three  cases,  assume install\_dir is the server's main installation directory.

## Tomcat

- install\_dir/webpages/WEB-INF/classes
- · Standard location for servlet classes.
- · install\_dir/classes
- Alternate location for servlet classes.
- · install\_dir/lib
- Location for JAR files containing classes.

## Tomcat 3.1

Just  before  this  book  went  to  press,  Apache  released  a  beta  version  of Tomcat 3.1. If there is a final version of this version available when you go to download Tomcat, you should use it. Here is the new directory organization that Tomcat 3.1 uses:

- install\_dir/webapps/ROOT/WEB-INF/classes
- · Standard location for servlet classes.
- · install\_dir/classes

Alternate location for servlet classes.

- · install\_dir/lib

Location for JAR files containing classes.

## The JSWDK

- · install\_dir/webpages/WEB-INF/servlets Standard location for servlet classes.
- · install\_dir/classes

Alternate location for servlet classes.

- •
- install\_dir/lib

Location for JAR files containing classes.

## Java Web Server 2.0

## · install\_dir/servlets

Location for frequently changing servlet classes. The server automatically detects when servlets in this directory change, and reloads them if necessary. This is in contrast to Tomcat and the JSWDK, where you have to restart the server when a servlet that is already in server memory changes. Most commercial servers have an option similar to this auto-reloading feature.

- · install\_dir/classes

Location for infrequently changing servlet classes.

- · install\_dir/lib

Location for JAR files containing classes.

I  realize  that  this  sounds  a  bit  overwhelming.  Don't  worry,  I'll  walk  you through the process with a couple of different servers when I introduce some real servlet code in the next chapter.

## 1.5 Installation and Setup

19