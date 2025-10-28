' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

<!-- image -->

his chapter gives a quick overview of servlets and JavaServer Pages (JSP),  outlining  the  major  advantages  of  each.  It  then  summarizes how to obtain and configure the software you need to write servlets and develop JSP documents. T

## 1.1 Servlets

Servlets are Java technology's answer to Common Gateway Interface (CGI) programming. They are programs that run on a Web server, acting as a middle layer between a request coming from a Web browser or other HTTP client and databases or applications on the HTTP server. Their job is to:

## 1. Read any data sent by the user.

This data is usually entered in a form on a Web page, but could also come from a Java applet or a custom HTTP client program.

- 2. Look up any other information about the request that is embedded in the HTTP request.
- This information includes details about browser capabilities, cookies, the host name of the requesting client, and so forth.

6

## Chapter 1 Overview of Servlets and JavaServer Pages

## 3. Generate the results.

This process may require talking to a database, executing an RMI or CORBA call, invoking a legacy application, or computing the response directly.

- 4. Format the results inside a document. In most cases, this involves embedding the information inside an HTML page.

## 5. Set the appropriate HTTP response parameters.

This means telling the browser what type of document is being returned (e.g., HTML), setting cookies and caching parameters,

- and other such tasks.

## 6. Send the document back to the client.

This document may be sent in text format (HTML), binary format (GIF images), or even in a compressed format like gzip that is layered on top of some other underlying format.

Many client requests  can be satisfied by returning pre-built  documents, and these requests would be handled by the server without invoking servlets. In many cases, however, a static result is not sufficient, and a page needs to be  generated  for  each  request.  There  are  a  number  of  reasons  why  Web pages need to be built on-the-fly like this:

## · The Web page is based on data submitted by the user.

For instance, the results page from search engines and order-confirmation pages at on-line stores are specific to particular user requests.

- · The Web page is derived from data that changes frequently.
- For example, a weather report or news headlines page might build the page dynamically, perhaps returning a previously built page if it is still up to date.
- · The Web page uses information from corporate databases or other server-side sources.

For example, an e-commerce site could use a servlet to build a Web page that lists the current price and availability of each item that is for sale.

In principle, servlets are not restricted to Web or application servers that handle HTTP requests, but can be used for other types of servers as well. For