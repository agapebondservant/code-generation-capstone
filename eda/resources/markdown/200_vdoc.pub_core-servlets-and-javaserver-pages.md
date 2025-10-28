## Appendix A Servlet and JSP Quick Reference

- · 401 (Unauthorized) : Browser tried to access password-protected page without proper Authorization header. See example in Section 4.5.
- · 404 (Not Found) : No such page. Servlets should use sendError to set this header. See example in Section 6.3.

## A.7 Generating the Server Response: HTTP Response Headers

## Setting Arbitrary Headers

These are methods in HttpServletResponse .  Set response headers before you send any document content to browser.

- · public void setHeader(String headerName, String headerValue) Sets an arbitrary header.
- · public void setDateHeader(String headerName, long milliseconds)

Converts milliseconds since 1970 to a date string in GMT format.

- · public void setIntHeader(String headerName, int headerValue) Prevents need to convert int to String before calling setHeader .
- · addHeader , addDateHeader , addIntHeader Adds new occurrence of header instead of replacing. 2.2 only.

## Setting Common Headers

- · setContentType : Sets the Content-Type header. Servlets almost always use this. See Table 7.1 for the most common MIME types.
- · setContentLength : Sets the Content-Length header. Used for persistent HTTP connections. Use ByteArrayOutputStream to buffer document before sending it, to determine size. See Section 7.4 for an example.
- · addCookie : Adds a value to the Set-Cookie header. See Chapter 8.
- · sendRedirect : Sets the Location header (plus changes status code). See example in Section 6.3.

## Common HTTP 1.1 Response Headers

- · Allow : the request methods server supports. Automatically set by the default service method when servlet receives OPTIONS requests.
- · Cache-Control : A no-cache value prevents browsers from caching results. Send Pragma header with same value in case browser only understands HTTP 1.0.
- · Content-Encoding : the way document is encoded. Browser reverses this encoding before handling document. Servlets must confirm that