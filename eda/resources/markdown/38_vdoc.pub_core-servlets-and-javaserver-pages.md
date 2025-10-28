## Chapter 2 First Servlets

## 2.3 A Servlet That Generates HTML

Most servlets generate HTML, not plain text as in the previous example. To build HTML, you need two additional steps:

- 1. Tell the browser that you're sending back HTML, and
- 2. Modify the println statements to build a legal Web page.

You  accomplish  the  first  step  by  setting  the  HTTP Content-Type response header. In general, headers are set by the setHeader method  of HttpServletResponse , but setting the content type is such a common task that  there  is  also  a  special setContentType method  just  for  this  purpose. The way to designate HTML is with a type of text/html , so the code would look like this:

response.setContentType("text/html");

Although HTML is the most common type of document servlets create, it is not unusual to create other document types. For example, Section 7.5 (Using Servlets to Generate GIF Images) shows how servlets can build and return custom images,  specifying  a  content type  of image/gif .  As  a  second  example, Section 11.2 (The contentType Attribute) shows how to generate and return Excel spreadsheets, using a content type of application/vnd.ms-excel .

Don't be concerned if you are not yet familiar with HTTP response headers;  they  are  discussed  in  detail  in  Chapter  7.  Note  that  you  need  to  set response headers before actually returning any of the content via the PrintWriter . That's because an HTTP response consists of the status line, one or more headers, a blank line, and the actual document, in that order . The headers can appear in any order, and servlets buffer the headers and send them all at once, so it is legal to set the status code (part of the first line returned) even after  setting  headers.  But  servlets  do  not  necessarily  buffer  the  document itself, since users might want to see partial results for long pages. In version 2.1 of the servlet specification, the PrintWriter output is not buffered at all, so the first time you use the PrintWriter ,  it  is  too late  to  go back and set headers. In version 2.2, servlet engines are permitted to partially buffer the output, but the size of the buffer is left unspecified. You can use the getBufferSize method of HttpServletResponse to determine the size, or use setBufferSize to specify it. In version 2.2 with buffering enabled, you can set headers until the buffer fills up and is actually sent to the client. If you aren't sure if the buffer has been sent, you can use the isCommitted method to check.