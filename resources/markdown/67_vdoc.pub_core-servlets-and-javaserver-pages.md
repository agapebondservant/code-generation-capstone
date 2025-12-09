Chapter

<!-- image -->

response from a Web server normally consists of a status line, one or more response headers, a blank line, and the document. To get the most out of your servlets, you need to know how to use the status line and response headers effectively, not just how to generate the document. A

Setting the HTTP response headers often goes hand in hand with setting the status codes in the status line, as discussed in the previous chapter. For example, all the 'document moved' status codes (300 through 307) have an accompanying Location header,  and  a  401  ( Unauthorized )  code  always includes an accompanying WWW-Authenticate header. However, specifying headers can also play a useful role even when no unusual status code is set. Response headers can be used to specify cookies, to supply the page modification  date  (for  client-side  caching),  to  instruct  the  browser  to  reload  the page after a designated interval, to give the file size so that persistent HTTP connections can be used, to designate the type of document being generated, and to perform many other tasks.

## 7.1 Setting Response Headers from Servlets

The most general way to specify headers is to use the setHeader method of HttpServletResponse . This method takes two strings: the header name and

## Chapter 7 Generating the Server Response: HTTP Response Headers

the  header  value.  As  with  setting  status  codes,  you  must  specify  headers before returning the actual document. With servlets version 2.1, this means that you must set the headers before the first use of the PrintWriter or raw OutputStream that  transmits  the  document  content. With servlets version 2.2 (the version in J2EE), the PrintWriter may use a buffer, so you can set headers until the first time the buffer is flushed. See Section 6.1 (Specifying Status Codes) for details.

<!-- image -->

## Core Approach

Be sure to set response headers before sending any document content to the client.

In  addition  to  the  general-purpose setHeader method, HttpServletResponse also has two specialized methods to set headers that contain dates and integers:

- · setDateHeader(String header, long milliseconds)
- This method saves you the trouble of translating a Java date in milliseconds since 1970 (as returned by
- System.currentTimeMillis , Date.getTime , or
- Calendar.getTimeInMillis ) into a GMT time string.
- · setIntHeader(String header, int headerValue) This method spares you the minor inconvenience of converting an int to a String before inserting it into a header.

HTTP allows  multiple  occurrences  of  the  same  header  name,  and  you sometimes want to add a new header rather than replace any existing header with  the  same  name.  For  example,  it  is  quite  common  to  have  multiple Accept and Set-Cookie headers  that  specify  different  supported  MIME types  and  different  cookies,  respectively.  With  servlets  version  2.1, setHeader , setDateHeader and setIntHeader always add new  headers,  so there is no way to 'unset' headers that were set earlier (e.g., by an inherited method). With servlets version 2.2, setHeader , setDateHeader ,  and setIntHeader replace any  existing  headers  of  the  same  name,  whereas addHeader , addDateHeader , and addIntHeader add a header regardless of whether a header of that name already exists. If it matters to you whether a specific header has already been set, use containsHeader to check.

Finally, HttpServletResponse also  supplies  a  number  of  convenience methods for specifying common headers. These methods are summarized as follows.