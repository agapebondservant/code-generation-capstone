## 1.2 The Advantages of Servlets Over 'Traditional' CGI

example, servlets could be embedded in mail or FTP servers to extend their functionality. In practice, however, this use of servlets has not caught on, and I'll only be discussing HTTP servlets.

## 1.2 The Advantages of Servlets Over 'Traditional' CGI

Java servlets are more efficient, easier to use, more powerful, more portable, safer, and cheaper than traditional CGI and many alternative CGI-like technologies.

## Efficient

With traditional CGI, a new process is started for each HTTP request. If the CGI program itself is relatively short, the overhead of starting the process can dominate the execution time. With servlets, the Java Virtual Machine stays running  and  handles  each  request  using  a  lightweight  Java  thread,  not  a heavyweight operating system process. Similarly, in traditional CGI, if there are N simultaneous requests to the same CGI program, the code for the CGI program is loaded into memory N times. With servlets, however, there would be N threads but only a single copy of the servlet class. Finally, when a CGI program finishes handling a request, the program terminates. This makes it difficult  to  cache  computations,  keep  database connections open, and perform  other  optimizations  that  rely  on  persistent  data.  Servlets,  however, remain in memory even after they complete a response, so it is straightforward to store arbitrarily complex data between requests.

## Convenient

Servlets have an extensive infrastructure for automatically parsing and decoding HTML form data, reading and setting HTTP headers, handling cookies, tracking sessions, and many other such high-level utilities. Besides, you already know the Java programming language. Why learn Perl too? You're already convinced that Java technology makes for more reliable and reusable code than does C++. Why go back to C++ for server-side programming?

## Chapter 1 Overview of Servlets and JavaServer Pages

## Powerful

Servlets support several capabilities that are difficult or impossible to accomplish with regular CGI. Servlets can talk directly to the Web server, whereas regular  CGI  programs  cannot,  at  least  not  without  using  a  server-specific API. Communicating with the Web server makes it easier to translate relative URLs into concrete path names, for instance. Multiple servlets can also share data, making it easy to implement database connection pooling and similar resource-sharing optimizations. Servlets can also maintain information from request to request, simplifying techniques like session tracking and caching of previous computations.

## Portable

Servlets are written in the Java programming language and follow a standard API. Consequently, servlets written for, say, I-Planet Enterprise Server can run virtually unchanged on Apache, Microsoft Internet Information Server (IIS),  IBM WebSphere, or StarNine WebStar. For example, virtually all  of the  servlets  and  JSP  pages  in  this  book  were  executed  on  Sun's  Java  Web Server, Apache Tomcat  and Sun's JavaServer  Web  Development  Kit (JSWDK) with no changes  whatsoever  in  the  code.  Many  were  tested  on BEA WebLogic and IBM WebSphere as well. In fact, servlets are supported directly or by a plug-in on virtually every major Web server. They are now part of the Java 2 Platform, Enterprise Edition (J2EE; see http://java.sun.com/j2ee/ ), so industry support for servlets is becoming even more pervasive.

## Secure

One  of  the  main  sources  of  vulnerabilities  in  traditional  CGI  programs stems from the fact that they are often executed by general-purpose operating system shells. So the CGI programmer has to be very careful to filter out characters such as backquotes and semicolons that are treated specially by the shell. This is harder than one might think, and weaknesses stemming from  this  problem  are  constantly  being  uncovered  in  widely  used  CGI libraries. A second source of problems is the fact that some CGI programs are processed by languages that do not automatically check array or string bounds.  For  example,  in  C  and  C++  it  is  perfectly  legal  to  allocate  a