A word of caution, however. Nobody becomes a great developer just by reading. You have to write some real code, too. The more, the better. In each chapter, I suggest that you start by making a simple program or a small variation of one of the examples given, then strike off on your own with a more significant project. Skim the sections you don't plan on using right away, then come back when you are ready to try them out.

If  you  do  this,  you  should  quickly  develop  the  confidence  to  handle  the real-world problems that brought you here in  the first place. You should be able to decide where servlets apply well, where JSP is better, and where a combination is best. You should not only know how to generate HTML content, but you  should  also  understand  building  other  media  types  like  GIF  images  or Excel spreadsheets. You should understand HTTP 1.1 well enough to use its capabilities  to  enhance  the  effectiveness  of  your  pages.  You  should  have  no qualms about  developing  Web  interfaces  to  your  corporate  databases,  using either HTML forms or applets as front ends. You should be able to spin off complex  behaviors  into  JavaBeans  components  or  custom  JSP  tag  libraries, then decide when to use these components directly and when to start requests with servlets that set things up for separate presentation pages. You should have fun along the way. You should get a raise.

## How This Book Is Organized

This book is  divided  into  three parts: Servlets, JavaServer Pages, and Supporting Technologies.

## Part I: Servlets

Part I covers servlet development with the 2.1 and 2.2 specifications. Although version 2.2 (along with JSP 1.1) is mandated by the Java 2 Platform, Enterprise Edition (J2EE), many commercial products are still at the earlier releases, so it is important to understand the differences. Also, although servlet code is portable across a huge variety of servers and operating systems, server setup and configuration details are not standardized. So, I include specific details for Apache Tomcat, Sun's JavaServer Web Development Kit (JSWDK), and the Java Web Server. Servlet topics include:

- · When and why you would use servlets
- · Obtaining and configuring the servlet and JSP software

<!-- image -->

## Introduction

- · The basic structure of servlets
- · The process of compiling, installing, and invoking servlets
- · Generating HTML from servlets
- · The servlet life cycle
- · Page modification dates and browser caches
- · Servlet debugging strategies
- · Reading form data from servlets
- · Handling both GET and POST requests with a single servlet
- · An on-line resume posting service
- · Reading HTTP request headers from servlets
- · The purpose of each of the HTTP 1.1 request headers
- · Reducing download times by compressing pages
- · Restricting access with password-protected servlets
- · The servlet equivalent of each standard CGI variable
- · Using HTTP status codes
- · The meaning of each of the HTTP 1.1 status code values
- · A search engine front end
- · Setting response headers from servlets
- · The purpose of each of the HTTP 1.1 response headers
- · Common MIME types
- · A servlet that uses the Refresh header to repeatedly access ongoing computations
- · Servlets that exploit persistent (keep-alive) HTTP connections
- · Generating GIF images from servlets
- · Cookie purposes and problems
- · The Cookie API
- · Some utilities that simplify cookie handling
- · A customized search engine front end
- · The purposes of session tracking
- · The servlet session tracking API
- · Using sessions to show per-client access counts
- · An on-line store that uses session tracking, shopping carts, and pages automatically built from catalog entries