## Chapter 4 Handling the Client Request: HTTP Request Headers

Figure 4-2 Request headers sent by Internet Explorer 5 on Windows 98.

<!-- image -->

## 4.3 HTTP 1.1 Request Headers

Access to the request headers permits servlets to perform a number of optimizations and to provide a number of features not otherwise possible. This section presents each of the possible HTTP 1.1 request headers along with a brief summary of how servlets can make use of them. The following sections give more detailed examples.

Note  that  HTTP  1.1  supports  a  superset  of  the  headers  permitted  in HTTP 1.0. For additional details on these headers, see the HTTP 1.1 specification, given in RFC 2616. There are a number of places the official RFCs are  archived  on-line;  your  best  bet  is  to  start  at http://www.rfc-editor.org/ to get a current list of the archive sites.

## Accept

This header specifies the MIME types that the browser or other client can handle. A servlet that can return a resource in more than one format

## 4.3 HTTP 1.1 Request Headers

can examine the Accept header to decide which format to use. For example, images in PNG format have some compression advantages over those in GIF, but only a few browsers support PNG. If you had images in both formats, a servlet could call request.getHeader("Accept") , check for image/png , and if it finds it, use xxx .png filenames in all the IMG elements it generates. Otherwise it would just use xxx .gif .

See Table 7.1 in Section 7.2 (HTTP 1.1 Response Headers and Their Meaning) for the names and meanings of the common MIME types.

## Accept-Charset

This header indicates the character sets (e.g., ISO-8859-1) the browser can use.

## Accept-Encoding

This header designates the types of encodings that the client knows how to handle. If it receives this header, the server is free to encode the page by using the format specified (usually to reduce transmission time), sending the Content-Encoding response header to indicate that it has done so. This encoding type is completely distinct from the MIME type of the actual document (as specified in the Content-Type response header), since this encoding is reversed before the browser decides what to do with the content. On the other hand, using an encoding the browser doesn't understand results in totally incomprehensible pages. Consequently, it is critical that you explicitly check the Accept-Encoding header before using any type of content encoding. Values of gzip or compress are the two standard possibilities.

Compressing pages before returning them is a very valuable service because the decoding time is likely to be small compared to the savings in transmission time. See Section 4.4 (Sending Compressed Web Pages) for an example where compression reduces download times by a factor of 10.

## Accept-Language

This header specifies the client's preferred languages, in case the servlet can produce results in more than one language. The value of the header should be one of the standard language codes such as en , en-us , da , etc. See RFC 1766 for details.

## Chapter 4 Handling the Client Request: HTTP Request Headers

## Authorization

This header is used by clients to identify themselves when accessing password-protected Web pages. See Section 4.5 (Restricting Access to Web Pages) for an example.

## Cache-Control

This header can be used by the client to specify a number of options for how pages should be cached by proxy servers. The request header is usually ignored by servlets, but the Cache-Control response header can be valuable to indicate that a page is constantly changing and shouldn't be cached. See Chapter 7 (Generating the Server Response: HTTP Response Headers) for details.

## Connection

This header tells whether or not the client can handle persistent HTTP connections. These let the client or other browser retrieve multiple files (e.g., an HTML file and several associated images) with a single socket connection, saving the overhead of negotiating several independent connections. With an HTTP 1.1 request, persistent connections are the default, and the client must specify a value of close for this header to use old-style connections. In HTTP 1.0, a value of keep-alive means that persistent connections should be used.

Each HTTP request results in a new invocation of a servlet, regardless of whether the request is a separate connection. That is, the server invokes the servlet only after the server has already read the HTTP request. This means that servlets need help from the server to handle persistent connections. Consequently, the servlet's job is just to make it possible for the server to use persistent connections, which is done by sending a Content-Length response header. Section 7.4 (Using Persistent HTTP Connections) has a detailed example.

## Content-Length

This header is only applicable to POST requests and gives the size of the POST data in bytes. Rather than calling request.getIntHeader("Content-Length") , you can simply use request.getContentLength() . However, since servlets take care of reading the form data for you (see Chapter 3, 'Handling the Client Request: Form Data'), you are unlikely to use this header explicitly.

## Content-Type

Although this header is usually used in responses from the server, it can also be part of client requests when the client attaches a document as the POST data or when making PUT requests. You can access this header with the shorthand getContentType method of HttpServletRequest .

## Cookie

This header is used to return cookies to servers that previously sent them to the browser. For details, see Chapter 8 (Handling Cookies). Technically, Cookie is not part of HTTP 1.1. It was originally a Netscape extension but is now very widely supported, including in both Netscape and Internet Explorer.

## Expect

This rarely used header lets the client tell the server what kinds of behaviors it expects. The one standard value for this header, 100-continue , is sent by a browser that will be sending an attached document and wants to know if the server will accept it. The server should send a status code of either 100 ( Continue ) or 417 ( Expectation Failed ) in such a case. For more details on HTTP status codes, see Chapter 6 (Generating the Server Response: HTTP Status Codes).

## From

This header gives the e-mail address of the person responsible for the HTTP request. Browsers do not send this header, but Web spiders (robots) often set it as a courtesy to help identify the source of server overloading or repeated improper requests.

## Host

Browsers are required to specify this header, which indicates the host and port as given in the original URL. Due to request forwarding and machines that have multiple hostnames, it is quite possible that the server could not otherwise determine this information. This header is not new in HTTP 1.1, but in HTTP 1.0 it was optional, not required.

## 4.3 HTTP 1.1 Request Headers

## Chapter 4 Handling the Client Request: HTTP Request Headers

## If-Match

This rarely used header applies primarily to PUT requests. The client can supply a list of entity tags as returned by the ETag response header, and the operation is performed only if one of them matches.

## If-Modified-Since

This header indicates that the client wants the page only if it has been changed after the specified date. This option is very useful because it lets browsers cache documents and reload them over the network only when they've changed. However, servlets don't need to deal directly with this header. Instead, they should just implement the getLastModified method to have the system handle modification dates automatically. An illustration is given in Section 2.8 (An Example Using Servlet Initialization and Page Modification Dates).

## If-None-Match

This header is like If-Match , except that the operation should be performed only if no entity tags match.

## If-Range

This rarely used header lets a client that has a partial copy of a document ask for either the parts it is missing (if unchanged) or an entire new document (if it has changed since a specified date).

## If-Unmodified-Since

This header is like If-Modified-Since in reverse, indicating that the operation should succeed only if the document is older than the specified date. Typically, If-Modified-Since is used for GET requests ('give me the document only if it is newer than my cached version'), whereas If-Unmodified-Since is used for PUT requests ('update this document only if nobody else has changed it since I generated it').

## Pragma

A Pragma header with a value of no-cache indicates that a servlet that is acting as a proxy should forward the request even if it has a local copy. The only standard value for this header is no-cache .

## Proxy-Authorization

This header lets clients identify themselves to proxies that require it. Servlets typically ignore this header, using Authorization instead.

## Range

This rarely used header lets a client that has a partial copy of a document ask for only the parts it is missing.

## Referer

This header indicates the URL of the referring Web page. For example, if you are at Web page 1 and click on a link to Web page 2, the URL of Web page 1 is included in the Referer header when the browser requests Web page 2. All major browsers set this header, so it is a useful way of tracking where requests came from. This capability is helpful for tracking advertisers who refer people to your site, for changing content slightly depending on the referring site, or simply for keeping track of where your traffic comes from. In the last case, most people simply rely on Web server log files, since the Referer is typically recorded there. Although it's useful, don't rely too heavily on the Referer header since it can be easily spoofed by a custom client. Finally, note that this header is Referer , not the expected Referrer , due to a spelling mistake by one of the original HTTP authors.

## Upgrade

The Upgrade header lets the browser or other client specify a communication protocol it prefers over HTTP 1.1. If the server also supports that protocol, both the client and the server can switch protocols. This type of protocol negotiation is almost always performed before the servlet is invoked. Thus, servlets rarely care about this header.

## User-Agent

This header identifies the browser or other client making the request and can be used to return different content to different types of browsers. Be wary of this usage, however; relying on a hard-coded list of browser versions and associated features can make for unreliable and hard-to-modify servlet code. Whenever possible, use something specific in the HTTP headers instead. For example, instead of trying to remember which browsers support gzip on which platforms, simply

## 4.3 HTTP 1.1 Request Headers