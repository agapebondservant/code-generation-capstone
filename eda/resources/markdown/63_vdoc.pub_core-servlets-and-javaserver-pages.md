## Chapter 6 Generating the Server Response: HTTP Status Codes

can  be  accomplished  with  them,  and  the  following  chapter  discusses  the response headers.

## 6.1 Specifying Status Codes

As just described, the HTTP response status line consists of an HTTP version, a status code, and an associated message. Since the message is directly associated with the status code and the HTTP version is determined by the server, all a servlet needs to do is to set the status code. The way to do this is by  the setStatus method  of HttpServletResponse .  If  your  response includes a special status code and a  document, be sure to call setStatus before actually  returning  any  of  the  content  via  the PrintWriter .  That's because an HTTP response consists of the status line, one or more headers, a  blank  line,  and  the  actual  document, in  that  order .  The  headers  can appear in any order, and servlets buffer the headers and send them all at once, so it is legal to set the status code (part of the first line returned) even after setting headers. But servlets do not necessarily buffer the document itself, since users might want to see partial results for long pages. In version 2.1 of the servlet specification, the PrintWriter output is not buffered at all, so the first time you use the PrintWriter , it is too late to go back and set headers. In version 2.2, servlet engines are permitted to partially buffer the output, but the size of the buffer is left unspecified. You can use the getBufferSize method of HttpServletResponse to  determine the size, or use setBufferSize to specify it. In version 2.2 with buffering enabled, you can set status codes until the buffer fills up and is actually sent to the client. If you aren't sure if the buffer has been sent, you can use the isCommitted method to check.

<!-- image -->

## Core Approach

Be sure to set status codes before sending any document content to the client.

## 6.1 Specifying Status Codes

The setStatus method takes an int (the status code) as an argument, but instead of using explicit numbers, it is clearer and more reliable to use the  constants  defined  in HttpServletResponse .  The  name  of  each  constant is derived from the standard HTTP 1.1 message for each constant, all uppercase  with  a  prefix  of SC (for Status  Code )  and  spaces  changed  to underscores. Thus, since the message for 404 is 'Not Found,' the equivalent constant in HttpServletResponse is SC\_NOT\_FOUND . In version 2.1 of the servlet specification, there are three exceptions. The constant for code 302 is derived from the HTTP 1.0 message (Moved Temporarily), not the HTTP 1.1 message (Found), and the constants for codes 307 (Temporary Redirect)  and  416  (Requested  Range  Not  Satisfiable)  are  missing  altogether. Version 2.2 added the constant for 416, but the inconsistencies for 307 and 302 remain.

Although  the  general  method  of  setting  status  codes  is  simply  to  call response.setStatus(int) , there are two common cases where a shortcut method in HttpServletResponse is  provided.  Just  be  aware  that  both  of these methods throw IOException , whereas setStatus doesn't.

## •

- public void sendError(int code, String message) The sendError method sends a status code (usually 404) along with a short message that is automatically formatted inside an HTML document and sent to the client.
- · public void sendRedirect(String url) The sendRedirect method generates a 302 response along with a Location header giving the URL of the new document. With servlets version 2.1, this must be an absolute URL. In version 2.2, either an absolute or a relative URL is permitted and the system automatically translates relative URLs into absolute ones before putting them in the Location header.

Setting  a  status  code  does  not  necessarily  mean  that  you  don't  need  to return a document. For example, although most servers automatically generate a small 'File Not Found' message for 404 responses, a servlet might want to customize this response. Remember that if you do send output, you have to call setStatus or sendError first .