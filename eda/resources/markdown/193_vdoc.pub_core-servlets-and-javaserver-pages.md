## Appendix A Servlet and JSP Quick Reference

- · Cookie : cookies sent to client by server sometime earlier. Use getCookies , not getHeader . See Chapter 8.
- · Host : host given in original URL. This is a required header in HTTP 1.1.
- · If-Modified-Since : indicates client wants page only if it has been changed after specified date. Don't handle this situation directly; implement getLastModified instead. See example in Section 2.8.
- · Referer : URL of referring Web page.
- · User-Agent : string identifying the browser making the request.

## A.5 Accessing the Standard CGI Variables

You should usually think in terms of request info, response info, and server info, not CGI variables.

## Capabilities Not Discussed Elsewhere

- · getServletContext().getRealPath("uri") : maps URI to real path
- · request.getRemoteHost() : name of host making request
- · request.getRemoteAddress() : IP address of host making request

## Servlet Equivalent of CGI Variables

- · AUTH\_TYPE: request.getAuthType()
- · CONTENT\_LENGTH: request.getContentLength()
- · CONTENT\_TYPE: request.getContentType()
- · DOCUMENT\_ROOT: getServletContext().getRealPath("/")
- · HTTP\_XXX\_YYY: request.getHeader("Xxx-Yyy")
- · PATH\_INFO: request.getPathInfo()
- · PATH\_TRANSLATED: request.getPathTranslated()
- · QUERY\_STRING: request.getQueryString()
- · REMOTE\_ADDR: request.getRemoteAddr()
- · REMOTE\_HOST: request.getRemoteHost()
- · REMOTE\_USER: request.getRemoteUser()
- · REQUEST\_METHOD: request.getMethod()
- · SCRIPT\_NAME: request.getServletPath()
- · SERVER\_NAME: request.getServerName()
- · SERVER\_PORT: request.getServerPort()
- · SERVER\_PROTOCOL: request.getProtocol()
- · SERVER\_SOFTWARE: getServletContext().getServerInfo()