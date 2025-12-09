## Chapter 4 Handling the Client Request: HTTP Request Headers

matically: the servlet needs to explicitly read the request headers to make use of this information.

```
GET /search?keywords=servlets+jsp HTTP/1.1 Accept: image/gif, image/jpg, */* Accept-Encoding: gzip Connection: Keep-Alive Cookie: userID=id456578 Host: www.somebookstore.com Referer: http://www.somebookstore.com/findbooks.html User-Agent: Mozilla/4.7 [en] (Win98; U)
```

## 4.1 Reading Request Headers from Servlets

Reading  headers  is  straightforward;  just  call  the getHeader method  of HttpServletRequest ,  which returns a String if  the  specified header was supplied on this request, null otherwise. Header names are not case sensitive. So, for example, request.getHeader("Connection") and request.getHeader("connection") are interchangeable.

Although getHeader is  the  general-purpose way to read incoming headers, there are a couple of headers that are so commonly used that they have special  access  methods  in HttpServletRequest .  I'll  list  them  here,  and remember that Appendix A (Servlet and JSP Quick Reference) gives a separate syntax summary.

## · getCookies

The getCookies method returns the contents of the Cookie header, parsed and stored in an array of Cookie objects. This method is discussed more in Chapter 8 (Handling Cookies).

## · getAuthType and getRemoteUser

The getAuthType and getRemoteUser methods break the Authorization header into its component pieces. Use of the Authorization header is illustrated in Section 4.5 (Restricting Access to Web Pages).

## · getContentLength

The getContentLength method returns the value of the Content-Length header (as an int ).

## · getContentType

The getContentType method returns the value of the Content-Type header (as a String ).

## · getDateHeader and getIntHeader

The getDateHeader and getIntHeader methods read the specified header and then convert them to Date and int values, respectively.

## · getHeaderNames

Rather than looking up one particular header, you can use the getHeaderNames method to get an Enumeration of all header names received on this particular request. This capability is illustrated in Section 4.2 (Printing All Headers).

## · getHeaders

In most cases, each header name appears only once in the request. Occasionally, however, a header can appear multiple times, with each occurrence listing a separate value. Accept-Language is one such example. If a header name is repeated in the request, version 2.1 servlets cannot access the later values without reading the raw input stream, since getHeader returns the value of the first occurrence of the header only. In version 2.2, however, getHeaders returns an Enumeration of the values of all occurrences of the header.

Finally, in addition to looking up the request headers, you can get information  on  the  main  request  line  itself,  also  by  means  of  methods  in HttpServletRequest .

## · getMethod

The getMethod method returns the main request method (normally GET or POST , but things like HEAD , PUT , and DELETE are possible).

## · getRequestURI

The getRequestURI method returns the part of the URL that comes after the host and port but before the form data. For example, for a URL of http://randomhost.com/servlet/search.BookSearch , getRequestURI would return

/servlet/search.BookSearch .

## · getProtocol

Lastly, the getProtocol method returns the third part of the request line, which is generally HTTP/1.0 or HTTP/1.1 . Servlets

## 4.1 Reading Request Headers from Servlets