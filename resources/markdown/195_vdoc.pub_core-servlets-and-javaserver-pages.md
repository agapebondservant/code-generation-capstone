## A.6 Generating the Server Response: HTTP Status Codes

## A.6 Generating the Server Response: HTTP Status Codes

## Format of an HTTP Response

Status  line  (HTTP version,  status  code,  message),  response headers, blank line, document, in that order. For example:

HTTP/1.1 200 OK

Content-Type: text/plain

Hello World

## Methods That Set Status Codes

These are methods in HttpServletResponse .  Set  status codes  before  you send any document content to browser.

- · public void setStatus(int statusCode) Use a constant for the code, not an explicit int .
- · public void sendError(int code, String message) Wraps message inside small HTML document.
- public void sendRedirect(String url)
- · Relative URLs permitted in 2.2.

## Status Code Categories

- · 100-199 : informational; client should respond with some other action.
- · 200-299 : request was successful.
- · 300-399 : file has moved. Usually includes a Location header indicating new address.
- · 400-499 : error by client.
- · 500-599 : error by server.

## Common HTTP 1.1 Status Codes

- · 200 (OK) : Everything is fine; document follows. Default for servlets.
- · 204 (No Content) : Browser should keep displaying previous document.
- · 301 (Moved Permanently) : Requested document permanently moved elsewhere (indicated in Location header). Browsers go to new location automatically.
- · 302 (Found) : Requested document temporarily moved elsewhere (indicated in Location header). Browsers go to new location automatically. Servlets should use sendRedirect , not setStatus , when setting this header. See example in Section 6.3.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->