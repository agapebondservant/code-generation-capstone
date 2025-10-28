## A.7 Generating the Server Response: HTTP Response Headers

browser supports a given encoding (by checking the Accept-Encoding request header) before using it. See compression example in Section 4.4.

- · Content-Length : the number of bytes in the response. See setContentLength above.
- · Content-Type : the MIME type of the document being returned. See setContentType above.
- · Expires : the time at which document should be considered out-of-date and thus should no longer be cached. Use setDateHeader to set this header.
- · Last-Modified : the time document was last changed. Don't set this header explicitly; provide a getLastModified method instead. See example in Section 2.8.
- · Location : the URL to which browser should reconnect. Use sendRedirect instead of setting this header directly. For an example, see Section 6.3.
- · Pragma : a value of no-cache instructs HTTP 1.0 clients not to cache document. See the Cache-Control response header (Section 7.2).
- · Refresh : the number of seconds until browser should reload page. Can also include URL to connect to. For an example, see Section 7.3.
- · Set-Cookie : the cookies that browser should remember. Don't set this header directly; use addCookie instead. See Chapter 8 for details.
- · WWW-Authenticate : the authorization type and realm client should supply in its Authorization header in the next request. For an example, see Section 4.5.

## Generating GIF Images from Servlets

- · Create an Image.

Use the createImage method of Component .

- · Draw into the Image.

Call getGraphics on the Image , then do normal drawing operations.

- · Set the Content-Type response header.

Use response.setContentType("image/gif") .

- · Get an output stream.

Use response.getOutputStream()

.

- · Send the Image down output stream in GIF format.

Use Jef Poskanzer's GifEncoder . See http://www.acme.com/java/.

<!-- image -->