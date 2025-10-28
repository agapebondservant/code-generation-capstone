## Chapter 5 Accessing the Standard CGI Variables

## 5.1 Servlet Equivalent of CGI Variables

For each standard CGI variable, this section summarizes its purpose and the means of accessing it from a servlet. As usual, once you are familiar with this information,  you  may  want  to  use  Appendix  A  (Servlet  and  JSP  Quick Reference)  as  a  reminder.  Assume request is  the HttpServletRequest supplied to the doGet and doPost methods.

## AUTH\_TYPE

If an Authorization header was supplied, this variable gives the scheme specified ( basic or digest ). Access it with request.getAuthType() .

## CONTENT\_LENGTH

For POST requests only, this variable stores the number of bytes of data sent, as given by the Content-Length request header. Technically, since the CONTENT\_LENGTH CGI variable is a string, the servlet equivalent is String.valueOf(request.getContentLength()) or request.getHeader("Content-Length") . You'll probably want to just call request.getContentLength() , which returns an int .

## CONTENT\_TYPE

CONTENT\_TYPE designates the MIME type of attached data, if specified. See Table 7.1 in Section 7.2 (HTTP 1.1 Response Headers and Their Meaning) for the names and meanings of the common MIME types. Access CONTENT\_TYPE with request.getContentType() .

## DOCUMENT\_ROOT

The DOCUMENT\_ROOT variable specifies the real directory corresponding to the URL http://host/ . Access it with getServletContext().getRealPath("/") . In older servlet specifications you accessed this variable with request.getRealPath("/") ; the older access method is no longer supported. Also, you can use getServletContext().getRealPath to map an arbitrary URI (i.e., URL suffix that comes after the hostname and port) to an actual path on the local machine.

## HTTP\_XXX\_YYY

Variables of the form HTTP\_HEADER\_NAME were how CGI programs obtained access to arbitrary HTTP request headers. The Cookie header became HTTP\_COOKIE , User-Agent became HTTP\_USER\_AGENT , Referer became HTTP\_REFERER , and so forth. Servlets should just use request.getHeader or one of the shortcut methods described in Chapter 4 (Handling the Client Request: HTTP Request Headers).

## PATH\_INFO

This variable supplies any path information attached to the URL after the address of the servlet but before the query data. For example, with http://host/servlet/coreservlets.SomeServ- let/foo/bar?baz=quux , the path information is /foo/bar . Since servlets, unlike standard CGI programs, can talk directly to the server, they don't need to treat path information specially. Path information could be sent as part of the regular form data and then translated by getServletContext().getRealPath . Access the value of PATH\_INFO by using request.getPathInfo() .

## PATH\_TRANSLATED

PATH\_TRANSLATED gives the path information mapped to a real path on the server. Again, with servlets there is no need to have a special case for path information, since a servlet can call getServletContext().getRealPath to translate partial URLs into real paths. This translation is not possible with standard CGI because the CGI program runs entirely separately from the server. Access this variable by means of request.getPathTranslated() .

## QUERY\_STRING

For GET requests, this variable gives the attached data as a single string with values still URL-encoded. You rarely want the raw data in servlets; instead, use request.getParameter to access individual parameters, as described in Chapter 3 (Handling the Client Request: Form Data). However, if you do want the raw data, you can get it via request.getQueryString() .

## REMOTE\_ADDR

This variable designates the IP address of the client that made the request, as a String (e.g., "198.137.241.30" ). Access it by calling request.getRemoteAddr() .

## 5.1 Servlet Equivalent of CGI Variables

<!-- image -->

## Chapter 5 Accessing the Standard CGI Variables

## REMOTE\_HOST

REMOTE\_HOST indicates the fully qualified domain name (e.g., whitehouse.gov ) of the client that made the request. The IP address is returned if the domain name cannot be determined. You can access this variable with request.getRemoteHost() .

## REMOTE\_USER

If an Authorization header was supplied and decoded by the server itself, the REMOTE\_USER variable gives the user part, which is useful for session tracking in protected sites. Access it with request.getRemoteUser() . For decoding Authorization information directly in servlets, see Section 4.5 (Restricting Access to Web Pages).

## REQUEST\_METHOD

This variable stipulates the HTTP request type, which is usually GET or POST but is occasionally HEAD , PUT , DELETE , OPTIONS , or TRACE . Servlets rarely need to look up REQUEST\_METHOD explicitly, since each of the request types is typically handled by a different servlet method ( doGet , doPost , etc.). An exception is HEAD , which is handled automatically by the service method returning whatever headers and status codes the doGet method would use. Access this variable by means of request.getMethod() .

## SCRIPT\_NAME

This variable specifies the path to the servlet, relative to the server's root directory. It can be accessed through request.getServletPath() .

## SERVER\_NAME

SERVER\_NAME gives the host name of the server machine. It can be accessed by means of request.getServerName() .

## SERVER\_PORT

This variable stores the port the server is listening on. Technically, the servlet equivalent is String.valueOf(request.getServerPort()) , which returns a String . You'll usually just want request.getServerPort() , which returns an int .