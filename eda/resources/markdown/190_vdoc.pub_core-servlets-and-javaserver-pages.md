## A.4 Handling the Client Request: HTTP Request Headers

## · public int getIntHeader(String headerName)

Reads header that represents an integer and converts it to an int . Returns -1 if header not in request. Throws NumberFormatException for non-ints.

Returns array of Cookie objects. Array is zero-length if no cookies. See

- · public Cookie[] getCookies() Chapter 8.
- · public int getContentLength()

Returns value of Content-Length header as int . Returns -1 if unknown.

header if it exists in request (i.e., for

- · public String getContentType() Returns value of Content-Type attached files) or null if not.
- · public String getAuthType() Returns "BASIC" , "DIGEST" , "SSL" , or null .
- · public String getRemoteUser()

Returns username if authentication used; null otherwise.

## Other Request Information

- · public String getMethod() Returns HTTP request method ( "GET" , "POST" , "HEAD" , etc.)
- · public String getRequestURI()

Returns part of the URL that came after host and port.

- · public String getProtocol() "HTTP/1.0" "HTTP/1.1"

Returns HTTP version ( or , usually).

## Common HTTP 1.1 Request Headers

See RFC 2616. Get RFCs on-line starting at http://www.rfc-editor.org/.

- · Accept : MIME types browser can handle.
- · Accept-Encoding : encodings (e.g., gzip or compress) browser can handle. See compression example in Section 4.4.
- · Authorization : user identification for password-protected pages. See example in Section 4.5. Normal approach is to not use HTTP authorization but instead use HTML forms to send username/password and then for servlet to store info in session object.
- · Connection : In HTTP 1.0, keep-alive means browser can handle persistent connection. In HTTP 1.1, persistent connection is default. Servlets should set Content-Length with setContentLength (using ByteArrayOutputStream to determine length of output) to support persistent connections. See example in Section 7.4.

<!-- image -->