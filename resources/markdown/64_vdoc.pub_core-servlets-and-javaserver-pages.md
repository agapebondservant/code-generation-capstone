## Chapter 6 Generating the Server Response: HTTP Status Codes

## 6.2 HTTP 1.1 Status Codes and Their Purpose

The following sections describe each of the status codes available for use in servlets talking to HTTP 1.1 clients, along with the standard message associated with each code. A good understanding of these codes can dramatically increase  the  capabilities  of  your  servlets,  so  you  should  at  least  skim  the descriptions to see what options are at your disposal. You can come back to get details when you are ready to make use of some of the capabilities. Note that Appendix A (Servlet and JSP Quick Reference) presents a brief summary of these codes in tabular format.

The complete HTTP 1.1 specification is given in RFC 2616, which you can access on-line by going to http://www.rfc-editor.org/ and following the links  to  the  latest  RFC  archive  sites.  Codes  that  are  new  in  HTTP 1.1  are noted, since many browsers support only HTTP 1.0. You should only send the  new  codes  to  clients  that  support  HTTP  1.1,  as  verified  by  checking request.getRequestProtocol .

The  rest  of  this  section  describes  the  specific  status  codes  available  in HTTP 1.1. These codes fall into five general categories:

- · 100-199 Codes in the 100s are informational, indicating that the client
- should respond with some other action.
- · 200-299

Values in the 200s signify that the request was successful.

- · 300-399
- Values in the 300s are used for files that have moved and usually include a Location header indicating the new address.
- · 400-499
- Values in the 400s indicate an error by the client.
- · 500-599

Codes in the 500s signify an error by the server.

The constants in HttpServletResponse that represent the various codes are derived from the standard messages associated with the codes. In servlets, you usually refer to status codes only by means of these constants. For example, you would use response.setStatus(response.SC\_NO\_CONTENT) rather  than response.setStatus(204) , since  the  latter  is  unclear  to  readers  and  is  prone  to  typographical  errors.

## 6.2 HTTP 1.1 Status Codes and Their Purpose

However,  you  should  note  that  servers  are  allowed  to  vary  the  messages slightly, and clients pay attention only to the numeric value. So, for example, you might see a server return a status line of HTTP/1.1 200 Document Follows instead of HTTP/1.1 200 OK .

## 100 (Continue)

If the server receives an Expect request header with a value of 100-continue , it means that the client is asking if it can send an attached document in a follow-up request. In such a case, the server should either respond with status 100 ( SC\_CONTINUE ) to tell the client to go ahead or use 417 ( Expectation Failed ) to tell the browser it won't accept the document. This status code is new in HTTP 1.1.

## 101 (Switching Protocols)

A 101 ( SC\_SWITCHING\_PROTOCOLS ) status indicates that the server will comply with the Upgrade header and change to a different protocol. This status code is new in HTTP 1.1.

## 200 (OK)

A value of 200 ( SC\_OK ) means that everything is fine. The document follows for GET and POST requests. This status is the default for servlets; if you don't use setStatus , you'll get 200.

## 201 (Created)

A status code of 201 ( SC\_CREATED ) signifies that the server created a new document in response to the request; the Location header should give its URL.

## 202 (Accepted)

A value of 202 ( SC\_ACCEPTED ) tells the client that the request is being acted upon, but processing is not yet complete.

## 203 (Non-Authoritative Information)

A 203 ( SC\_NON\_AUTHORITATIVE\_INFORMATION ) status signifies that the document is being returned normally, but some of the response headers might be incorrect since a document copy is being used. This status code is new in HTTP 1.1.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 6 Generating the Server Response: HTTP Status Codes

## 204 (No Content)

A status code of 204 ( SC\_NO\_CONTENT ) stipulates that the browser should continue to display the previous document because no new document is available. This behavior is useful if the user periodically reloads a page by pressing the 'Reload' button, and you can determine that the previous page is already up-to-date. For example, a servlet might do something like this:

```
int pageVersion = Integer.parseInt(request.getParameter("pageVersion")); if (pageVersion >= currentVersion) { response.setStatus(response.SC_NO_CONTENT); } else { // Create regular page }
```

However, this approach does not work for pages that are automatically reloaded via the Refresh response header or the equivalent &lt;META HTTP-EQUIV="Refresh" ...&gt; HTML entry, since returning a 204 status code stops future reloading. JavaScript-based automatic reloading could still work in such a case, though. See the discussion of Refresh in Section 7.2 (HTTP 1.1 Response Headers and Their Meaning) for details.

## 205 (Reset Content)

A value of 205 ( SC\_RESET\_CONTENT ) means that there is no new document, but the browser should reset the document view. This status code is used to force browsers to clear form fields. It is new in HTTP 1.1.

## 206 (Partial Content)

A status code of 206 ( SC\_PARTIAL\_CONTENT ) is sent when the server fulfills a partial request that includes a Range header. This value is new in HTTP 1.1.

## 300 (Multiple Choices)

A value of 300 ( SC\_MULTIPLE\_CHOICES ) signifies that the requested document can be found several places, which will be listed in the returned document. If the server has a preferred choice, it should be listed in the Location response header.

## 6.2 HTTP 1.1 Status Codes and Their Purpose

## 301 (Moved Permanently)

The 301 ( SC\_MOVED\_PERMANENTLY ) status indicates that the requested document is elsewhere; the new URL for the document is given in the Location response header. Browsers should automatically follow the link to the new URL.

## 302 (Found)

This value is similar to 301, except that the URL given by the Location header should be interpreted as a temporary replacement, not a permanent one. Note: in HTTP 1.0, the message was Moved Temporarily instead of Found , and the constant in HttpServletResponse is SC\_MOVED\_TEMPORARILY , not the expected SC\_FOUND .

## Core Note

The constant representing 302 is SC\_MOVED\_TEMPORARILY , not SC\_FOUND .

<!-- image -->

Status code 302 is very useful because browsers automatically follow the reference to the new URL given in the Location response header. It is so useful, in fact, that there is a special method for it, sendRedirect . Using response.sendRedirect(url) has a couple of advantages over using response.setStatus(response.SC\_MOVED\_TEMPORARILY) and response.setHeader("Location", url) . First, it is shorter and easier. Second, with sendRedirect , the servlet automatically builds a page containing the link to show to older browsers that don't automatically follow redirects. Finally, with version 2.2 of servlets (the version in J2EE), sendRedirect can handle relative URLs, automatically translating them into absolute ones. You must use an absolute URL in version 2.1, however.

If you redirect the user to another page within your own site, you should pass the URL through the encodeURL method of HttpServletResponse . Doing so is a simple precaution in case you ever use session tracking based on URL-rewriting. URL-rewriting is a way to track users who have cookies disabled while they are at your site. It is implemented by adding extra path information to the end of each URL, but the servlet session-tracking API takes care of the details automatically. Session

## Chapter 6 Generating the Server Response: HTTP Status Codes

tracking is discussed in Chapter 9, and it is a good idea to use encodeURL routinely so that you can add session tracking at a later time with minimal changes to the code.

<!-- image -->

## Core Approach

If you redirect users to a page within your site, plan ahead for session tracking by using response.sendRedirect(response.encodeURL(url)) ,

rather than just response.sendRedirect(url) .

This status code is sometimes used interchangeably with 301. For example, if you erroneously ask for http://host/~user (missing the trailing slash), some servers will reply with a 301 code while others will use 302.

Technically, browsers are only supposed to automatically follow the redirection if the original request was GET . For details, see the discussion of the 307 status code.

## 303 (See Other)

The 303 ( SC\_SEE\_OTHER ) status is similar to 301 and 302, except that if the original request was POST , the new document (given in the Location header) should be retrieved with GET . This code is new in HTTP 1.1.

## 304 (Not Modified)

When a client has a cached document, it can perform a conditional request by supplying an If-Modified-Since header to indicate that it only wants the document if it has been changed since the specified date. A value of 304 ( SC\_NOT\_MODIFIED ) means that the cached version is up-to-date and the client should use it. Otherwise, the server should return the requested document with the normal (200) status code. Servlets normally should not set this status code directly. Instead, they should implement the getLastModified method and let the default service method handle conditional requests based upon this modification date. An example of this approach is given in Section 2.8 (An Example Using Servlet Initialization and Page Modification Dates).

## 305 (Use Proxy)

A value of 305 ( SC\_USE\_PROXY ) signifies that the requested document should be retrieved via the proxy listed in the Location header. This status code is new in HTTP 1.1.

## 307 (Temporary Redirect)

The rules for how a browser should handle a 307 status are identical to those for 302. The 307 value was added to HTTP 1.1 since many browsers erroneously follow the redirection on a 302 response even if the original message is a POST . Browsers are supposed to follow the redirection of a POST request only when they receive a 303 response status. This new status is intended to be unambiguously clear: follow redirected GET and POST requests in the case of 303 responses; follow redirected GET but not POST requests in the case of 307 responses. Note: For some reason there is no constant in HttpServletResponse corresponding to this status code. This status code is new in HTTP 1.1.

## Core Note

There is no SC\_TEMPORARY\_REDIRECT constant in HttpServletResponse , so you have to use 307 explicitly.

## 400 (Bad Request)

A 400 ( SC\_BAD\_REQUEST ) status indicates bad syntax in the client request.

## 401 (Unauthorized)

A value of 401 ( SC\_UNAUTHORIZED ) signifies that the client tried to access a password-protected page without proper identifying information in the Authorization header. The response must include a WWW-Authenticate header. For an example, see Section 4.5, 'Restricting Access to Web Pages.'

## 403 (Forbidden)

A status code of 403 ( SC\_FORBIDDEN ) means that the server refuses to supply the resource, regardless of authorization. This status is often the result of bad file or directory permissions on the server.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## 6.2 HTTP 1.1 Status Codes and Their Purpose

## Chapter 6 Generating the Server Response: HTTP Status Codes

## 404 (Not Found)

The infamous 404 ( SC\_NOT\_FOUND ) status tells the client that no resource could be found at that address. This value is the standard 'no such page' response. It is such a common and useful response that there is a special method for it in the HttpServletResponse class: sendError("message") . The advantage of sendError over setStatus is that, with sendError , the server automatically generates an error page showing the error message. Unfortunately, however, the default behavior of Internet Explorer 5 is to ignore the error page you send back and displays its own, even though doing so contradicts the HTTP specification. To turn off this setting, go to the Tools menu, select Internet Options, choose the Advanced tab, and make sure 'Show friendly HTTP error messages' box is not checked. Unfortunately, however, few users are aware of this setting, so this 'feature' prevents most users of Internet Explorer version 5 from seeing any informative messages you return. Other major browsers and version 4 of Internet Explorer properly display server-generated error pages. See Figures 6-3 and 6-4 for an example.

## Core Warning

By default, Internet Explorer version 5 ignores server-generated error pages.

## 405 (Method Not Allowed)

A 405 ( SC\_METHOD\_NOT\_ALLOWED ) value indicates that the request method ( GET , POST , HEAD , PUT , DELETE , etc.) was not allowed for this particular resource. This status code is new in HTTP 1.1.

## 406 (Not Acceptable)

A value of 406 ( SC\_NOT\_ACCEPTABLE ) signifies that the requested resource has a MIME type incompatible with the types specified by the client in its Accept header. See Table 7.1 in Section 7.2 (HTTP 1.1 Response Headers and Their Meaning) for the names and meanings of the common MIME types. The 406 value is new in HTTP 1.1.

<!-- image -->

## 6.2 HTTP 1.1 Status Codes and Their Purpose

## 407 (Proxy Authentication Required)

The 407 ( SC\_PROXY\_AUTHENTICATION\_REQUIRED ) value is similar to 401, but it is used by proxy servers. It indicates that the client must authenticate itself with the proxy server. The proxy server returns a Proxy-Authenticate response header to the client, which results in the browser reconnecting with a Proxy-Authorization request header. This status code is new in HTTP 1.1.

## 408 (Request Timeout)

The 408 ( SC\_REQUEST\_TIMEOUT ) code means that the client took too long to finish sending the request. It is new in HTTP 1.1.

## 409 (Conflict)

Usually associated with PUT requests, the 409 ( SC\_CONFLICT ) status is used for situations such as an attempt to upload an incorrect version of a file. This status code is new in HTTP 1.1.

## 410 (Gone)

A value of 410 ( SC\_GONE ) tells the client that the requested document is gone and no forwarding address is known. Status 410 differs from 404 in that the document is known to be permanently gone, not just unavailable for unknown reasons, as with 404. This status code is new in HTTP 1.1.

## 411 (Length Required)

A status of 411 ( SC\_LENGTH\_REQUIRED ) signifies that the server cannot process the request (assumedly a POST request with an attached document) unless the client sends a Content-Length header indicating the amount of data being sent to the server. This value is new in HTTP 1.1.

## 412 (Precondition Failed)

The 412 ( SC\_PRECONDITION\_FAILED ) status indicates that some precondition specified in the request headers was false. It is new in HTTP 1.1.

## 413 (Request Entity Too Large)

A status code of 413 ( SC\_REQUEST\_ENTITY\_TOO\_LARGE ) tells the client that the requested document is bigger than the server wants to handle

## Chapter 6 Generating the Server Response: HTTP Status Codes

now. If the server thinks it can handle it later, it should include a Retry-After response header. This value is new in HTTP 1.1.

## 414 (Request URI Too Long)

The 414 ( SC\_REQUEST\_URI\_TOO\_LONG ) status is used when the URI is too long. In this context, 'URI' means the part of the URL that came after the host and port in the URL. For example, in http://www.y2k-disaster.com:8080/we/look/silly/now/ , the URI is /we/look/silly/now/ . This status code is new in HTTP 1.1.

## 415 (Unsupported Media Type)

A value of 415 ( SC\_UNSUPPORTED\_MEDIA\_TYPE ) means that the request had an attached document of a type the server doesn't know how to handle. This status code is new in HTTP 1.1.

## 416 (Requested Range Not Satisfiable)

A status code of 416 signifies that the client included an unsatisfiable Range header in the request. This value is new in HTTP 1.1. Surprisingly, the constant that corresponds to this value was omitted from HttpServletResponse in version 2.1 of the servlet API.

## Core Note

In version 2.1 of the servlet specification, there is no SC\_REQUESTED\_RANGE\_NOT\_SATISFIABLE constant in HttpServletResponse , so you have to use 416 explicitly. The constant is available in version 2.2 and later.

## 417 (Expectation Failed)

If the server receives an Expect request header with a value of 100-continue , it means that the client is asking if it can send an attached document in a follow-up request. In such a case, the server should either respond with this status (417) to tell the browser it won't accept the document or use 100 ( SC\_CONTINUE ) to tell the client to go ahead. This status code is new in HTTP 1.1.

## 500 (Internal Server Error)

500 ( SC\_INTERNAL\_SERVER\_ERROR ) is the generic 'server is confused' status code. It often results from CGI programs or (heaven forbid!) servlets that crash or return improperly formatted headers.

<!-- image -->