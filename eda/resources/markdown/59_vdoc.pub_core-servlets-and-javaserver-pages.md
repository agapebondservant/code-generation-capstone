' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter Accessing the Standard CGI Variables

<!-- image -->

## Topics in This Chapter

- · The idea of 'CGI variables'
- · The servlet equivalent of each standard CGI variable
- · A servlet that shows the values of all CGI variables

<!-- image -->

f you come to servlets with a background in traditional Common Gateway Interface (CGI) programming, you are probably used to the idea of 'CGI variables.' These are a somewhat eclectic collection of information about the current request. Some are based on the HTTP request line and headers (e.g., form data), others are derived from the socket itself (e.g., the name and IP address of the requesting host), and still others are taken from  server  installation  parameters  (e.g.,  the  mapping  of  URLs  to  actual paths). I

Although it  probably  makes  more  sense  to  think  of  different  sources  of data (request data, server information, etc.) as distinct, experienced CGI programmers may find it useful to see the servlet equivalent of each of the CGI variables. If you don't have a background in traditional CGI, first, count your blessings;  servlets  are  easier  to  use,  more  flexible  and  more  efficient  than standard CGI. Second, just skim this chapter, noting the parts not directly related to the incoming HTTP request. In particular, observe that you can use getServletContext().getRealPath to  map  a  URI  (the  part  of  the URL that comes after the host and port) to an actual path and that you can use request.getRemoteHost and request.getRemoteAddress to get the name and IP address of the client.