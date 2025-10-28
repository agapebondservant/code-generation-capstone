## Chapter 2 First Servlets

Figure 2-4 Result of the HelloWWW3 servlet.

<!-- image -->

## 2.6 The Servlet Life Cycle

Earlier in this book, I vaguely referred to the fact that only a single instance of a servlet gets created, with each user request resulting in a new thread that is handed off to doGet or doPost as  appropriate. I'll now be more specific about how servlets are created and destroyed, and how and when the various methods are invoked. I'll give a quick summary here, then elaborate in the following subsections.

When the servlet  is first created, its init method is  invoked,  so  that  is where you put one-time setup code. After this, each user request results in a thread  that  calls  the service method  of  the  previously  created  instance. Multiple concurrent requests normally result in multiple threads calling service simultaneously, although your servlet can implement a special interface that stipulates that only a single thread is permitted to run at any one time. The service method then calls doGet , doPost , or another do Xxx method, depending on the type of HTTP request it received. Finally, when the server decides to unload a servlet, it first calls the servlet's destroy method.

## The init Method

The init method is called when the servlet is first created and is not called again for each user request. So, it is used for one-time initializations, just as with the init method of applets. The servlet can be created when a user first invokes a URL corresponding to the servlet or when the server is first started,

## 2.6 The Servlet Life Cycle

depending on how you have registered the servlet with the Web server. It will be  created  for  the  first  user  request  if  it  is  not  explicitly  registered  but  is instead just placed in one of the standard server directories. See the discussion of Section 2.2 (A Simple Servlet Generating Plain Text) for details on these directories.

There are two versions of init : one that takes no arguments and one that takes a ServletConfig object as an argument. The first version is used when the servlet does not need to read any settings that vary from server to server. The method definition looks like this:

```
public void init() throws ServletException { // Initialization code... }
```

For  examples of this  type  of  initialization,  see  Section  2.8  (An  Example Using Servlet Initialization and Page Modification Dates) later in this chapter. Section 18.8 (Connection Pooling: A Case Study) in the chapter on JDBC gives a more advanced application where init is used to preallocate multiple database connections.

The  second  version  of init is  used  when  the  servlet  needs  to  read server-specific settings before it can complete the initialization. For example, the  servlet  might  need  to  know  about  database  settings,  password  files, server-specific performance parameters, hit count files, or serialized cookie data from previous requests. The second version of init looks like this:

```
public void init(ServletConfig config) throws ServletException { super.init(config); // Initialization code...
```

}

Notice two things about this code. First, the init method takes a ServletConfig as  an  argument. ServletConfig has a getInitParameter method with which you can look up initialization parameters associated with the servlet. Just as with the getParameter method used in the init method of applets, both the input (the parameter name) and the output (the parameter value) are strings. For a simple example of the use of initialization parameters, see Section 2.7 (An Example Using Initialization Parameters); for a more complex example, see Section 4.5 (Restricting Access to Web Pages) where the location of a password  file  is  given  through  the  use  of getInitParameter .  Note  that although  you look  up parameters  in  a  portable  manner,  you set them  in  a server-specific way. For example, with Tomcat, you embed servlet properties in a file called web.xml , with the JSWDK you use servlets.properties , with the  WebLogic  application  server  you  use weblogic.properties ,  and  with the Java Web Server you set the properties interactively via the administration

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 2 First Servlets

console. For examples of these settings, see Section 2.7 (An Example Using Initialization Parameters).

The second thing to note about the second version of init is that the first line  of  the  method  body  is  a  call  to super.init .  This  call  is  critical!  The ServletConfig object is used elsewhere in the servlet, and the init method of the superclass registers it where the servlet can find it later. So, you can cause yourself huge headaches later if you omit the super.init call.

<!-- image -->

## Core Approach

If you write an init method that takes a ServletConfig as an argument, always call super.init on the first line.

## The service Method

Each time the server receives a request for a servlet, the server spawns a new thread and calls service .  The service method checks the HTTP request type ( GET , POST , PUT , DELETE ,  etc.) and calls doGet , doPost , doPut , doDelete ,  etc.,  as  appropriate.  Now,  if  you  have  a  servlet  that  needs  to  handle both POST and GET requests identically, you may be tempted to override service directly as below, rather than implementing both doGet and doPost .

```
public void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { // Servlet Code }
```

This  is  not  a  good  idea.  Instead,  just  have doPost call doGet (or  vice versa), as below.

```
public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { // Servlet Code } public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); }
```

Although this approach takes  a  couple  of extra lines of  code,  it  has five advantages over directly overriding service :

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 2.6 The Servlet Life Cycle

- 1. You can add support for other services later by adding doPut , doTrace , etc., perhaps in a subclass. Overriding service directly precludes this possibility.
- 2. You can add support for modification dates by adding a getLastModified method. If you use doGet , the standard service method uses the getLastModified method to set Last-Modified headers and to respond properly to conditional GET requests (those containing an If-Modified-Since header). See Section 2.8 (An Example Using Servlet Initialization and Page Modification Dates) for an example.
- 3. You get automatic support for HEAD requests. The system just returns whatever headers and status codes doGet sets, but omits the page body. HEAD is a useful request method for custom HTTP clients. For example, link validators that check a page for dead hypertext links often use HEAD instead of GET in order to reduce server load.
- 4. You get automatic support for OPTIONS requests. If a doGet method exists, the standard service method answers OPTIONS requests by returning an Allow header indicating that GET , HEAD , OPTIONS , and TRACE are supported.
- 5. You get automatic support for TRACE requests. TRACE is a request method used for client debugging: it just returns the HTTP request headers back to the client.

## Core Tip

If your servlet needs to handle both GET and POST identically, have your doPost method call doGet , or vice versa. Don't override service directly.

<!-- image -->

## The doGet, doPost, and doXxx Methods

These methods contain the real meat of your servlet. Ninety-nine percent of the  time,  you  only  care  about GET and/or POST requests,  so  you  override doGet and/or doPost . However, if you want to, you can also override doDelete for DELETE requests, doPut for PUT , doOptions for OPTIONS , and doTrace for TRACE .  Recall,  however,  that  you  have  automatic  support  for OPTIONS and TRACE ,  as  described  in  the  previous  section  on  the service method. Note that there is  no doHead method.  That's  because  the  system

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 2 First Servlets

automatically  uses  the  status  line  and  header  settings  of doGet to  answer HEAD requests.

## The SingleThreadModel Interface

Normally, the system makes a single instance of your servlet and then creates a new thread for each user request, with multiple simultaneous threads running if a new request comes in while a previous request is still executing. This means that your doGet and doPost methods must be careful to synchronize access to fields and other shared data, since multiple threads may be trying to access the data simultaneously. See Section 7.3 (Persistent Servlet State and Auto-Reloading Pages) for more discussion of this. If you want to prevent this multithreaded access, you can have your servlet implement the SingleThreadModel interface, as below.

public class YourServlet extends HttpServlet implements SingleThreadModel {

}

If you implement this interface, the system guarantees that there is never more than one request thread accessing a single instance of your servlet. It does so either by queuing up all the requests and passing them one at a time to a single servlet instance, or by creating a pool of multiple instances, each of which handles one request at a time. This means that you don't have to worry about simultaneous access to regular fields (instance variables) of the servlet. You do ,  however, still have to synchronize access to class variables ( static fields) or shared data stored outside the servlet.

Synchronous  access  to  your  servlets  can  significantly  hurt  performance (latency)  if  your  servlet  is  accessed  extremely  frequently.  So  think  twice before using the SingleThreadModel approach.

## The destroy Method

The server may decide to remove a previously loaded servlet instance, perhaps because it is explicitly asked to do so by the server administrator, or perhaps because the servlet is idle for a long time. Before it does, however, it calls the servlet's destroy method. This method gives your servlet a chance to close database connections, halt background threads, write cookie lists or hit counts to disk, and perform other such cleanup activities. Be aware, however, that it is possible for the Web server to crash. After all, not all Web servers are written in reliable programming languages like Java; some are written

...