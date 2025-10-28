Chapter

<!-- image -->

he previous chapter showed you how to install the software you need and how to set up your development environment. Now you want to really write a few servlets. Good. This chapter shows you how, outlining the structure that almost all servlets follow, walking you through the steps required to compile and execute a servlet, and giving details on how servlets are initialized and when the various methods are called. It also introduces a few general tools that you will find helpful in your servlet development. T

## 2.1 Basic Servlet Structure

Listing 2.1 outlines a basic servlet that handles GET requests. GET requests, for those unfamiliar with HTTP, are the usual type of browser requests for Web pages. A browser generates this request when the user types a URL on the address line, follows a link from a Web page, or submits an HTML form that does not specify a METHOD . Servlets can also very easily handle POST requests, which  are  generated  when  someone  submits  an  HTML  form  that  specifies METHOD="POST" . For details on using HTML forms, see Chapter 16.

To be a servlet, a class should extend HttpServlet and override doGet or doPost , depending on whether the data is being sent by GET or by POST .  If you want the same servlet to handle both GET and POST and to take the same action for each, you can simply have doGet call doPost , or vice versa.

## Chapter 2 First Servlets

```
Listing 2.1 ServletTemplate.java import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class ServletTemplate extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { // Use "request" to read incoming HTTP headers // (e.g. cookies) and HTML form data (e.g. data the user // entered and submitted). // Use "response" to specify the HTTP response status // code and headers (e.g. the content type, cookies). PrintWriter out = response.getWriter(); // Use "out" to send content to browser } }
```

Both of these methods take two arguments: an HttpServletRequest and an HttpServletResponse .  The HttpServletRequest has  methods  by which you can find out about incoming information such as form data, HTTP request headers, and the client's hostname. The HttpServletResponse lets you specify outgoing information such as HTTP status codes (200, 404, etc.), response headers ( Content-Type , Set-Cookie ,  etc.), and, most importantly, lets you obtain a PrintWriter used to send the document content back to the client. For simple servlets, most of the effort is spent in println statements that  generate  the  desired  page.  Form  data,  HTTP  request  headers,  HTTP responses, and cookies will all be discussed in detail in the following chapters.

Since doGet and doPost throw  two  exceptions,  you  are  required  to include  them  in  the  declaration.  Finally,  you  have  to  import  classes  in java.io (for PrintWriter , etc.), javax.servlet (for HttpServlet , etc.), and javax.servlet.http (for HttpServletRequest and HttpServletResponse ).

Strictly speaking, HttpServlet is not the only starting point for servlets, since servlets could, in principle, extend mail, FTP , or other types of servers. Servlets for  these  environments  would  extend  a  custom  class  derived  from GenericServlet ,  the  parent class of HttpServlet .  In  practice,  however, servlets are used almost exclusively for servers that communicate via HTTP (i.e., Web and application servers), and the discussion in this book will be limited to this usage.