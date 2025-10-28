## Chapter 2 First Servlets

## 2.9 Debugging Servlets

Naturally, when you write servlets, you never make mistakes. However, some of  your  colleagues  might  make  an  occasional  error,  and  you  can  pass  this advice  on  to  them.  Seriously,  though,  debugging  servlets  can  be  tricky because you don't execute them directly. Instead, you trigger their execution by means of an HTTP request, and they are executed by the Web server. This remote execution makes it difficult to insert break points or to read debugging messages and stack traces. So, approaches to servlet debugging  differ somewhat from those used in general development. Here are seven general strategies that can make your life easier.

## 1. Look at the HTML source.

If the result you see in the browser looks funny, choose 'View Source' from the browser's menu. Sometimes a small HTML error like &lt;TABLE&gt; instead of &lt;/TABLE&gt; can prevent much of the page from being viewed. Even better, use a formal HTML validator on the servlet's output. See Section 2.5 (Simple HTML-Building Utilities) for a discussion of this approach.

## 2. Return error pages to the client.

Sometimes certain classes of errors can be anticipated by the servlet. In these cases, the servlet should build descriptive information about the problem and return it to the client in a regular page or by means of the sendError method of HttpServletResponse . See Chapter 6 (Generating the Server Response: HTTP Status Codes) for details on sendError . For example, you should plan for cases when the client forgets some of the required form data and send an error page detailing what was missing. Error pages are not always possible, however. Sometimes something unexpected goes wrong with your servlet, and it simply crashes. The remaining approaches help you in those situations.

## 3. Start the server from the command line.

Most Web servers execute from a background process, and this process is often automatically started when the system is booted. If you are having trouble with your servlet, you should consider shutting down the server and restarting it from the command line. After this, System.out.println or System.err.println calls can be easily read from the window in which the server was started. When something goes wrong with

## 2.9 Debugging Servlets

your servlet, your first task is to discover exactly how far the servlet got before it failed and to gather some information about the key data structures during the time period just before it failed. Simple println statements are surprisingly effective for this purpose. If you are running your servlets on a server that you cannot easily halt and restart, then do your debugging with the JSWDK, Tomcat, or the Java Web Server on your personal machine, and save deployment to the real server for later.

## 4. Use the log file.

The HttpServlet class has a method called log that lets you write information into a logging file on the server. Reading debugging messages from the log file is a bit less convenient than watching them directly from a window as with the previous approach, but using the log file does not require stopping and restarting the server. There are two variations of this method: one that takes a String , and the other that takes a String and a Throwable (an ancestor class of Exception ). The exact location of the log file is server-specific, but it is generally clearly documented or can be found in subdirectories of the server installation directory.

## 5. Look at the request data separately.

Servlets read data from the HTTP request, construct a response, and send it back to the client. If something in the process goes wrong, you want to discover if it is because the client is sending the wrong data or because the servlet is processing it incorrectly. The EchoServer class, shown in Section 16.12 (A Debugging Web Server), lets you submit HTML forms and get a result that shows you exactly how the data arrived at the server.

## 6. Look at the response data separately.

Once you look at the request data separately, you'll want to do the same for the response data. The WebClient class, presented next in Section 2.10 (WebClient: Talking to Web Servers Interactively), permits you to connect to the server interactively, send custom HTTP request data, and see everything that comes back, HTTP response headers and all.

## 7. Stop and restart the server.

Most full-blown Web servers that support servlets have a designated location for servlets that are under development. Servlets in this location (e.g., the servlets directory for the Java Web Server) are supposed to be automatically reloaded when their associated class file changes. At times, however, some servers can