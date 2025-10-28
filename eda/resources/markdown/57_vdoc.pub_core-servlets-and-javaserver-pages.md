## Chapter 4 Handling the Client Request: HTTP Request Headers

check the Accept-Encoding header. Admittedly, this is not always possible, but when it is not, you should ask yourself if the browser-specific feature you are using really adds enough value to be worth the maintenance cost.

Most Internet Explorer versions list a 'Mozilla' (Netscape) version first in their User-Agent line, with the real browser version listed parenthetically. This is done for compatibility with JavaScript, where the User-Agent header is sometimes used to determine which JavaScript features are supported. Also note that this header can be easily spoofed, a fact that calls into question the reliability of sites that use this header to 'show' market penetration of various browser versions. Hmm, millions of dollars in marketing money riding on statistics that could be skewed by a custom client written in less than an hour, and I should take those numbers as accurate ones?

## Via

This header is set by gateways and proxies to show the intermediate sites the request passed through.

## Warning

This rarely used catchall header lets clients warn about caching or content transformation errors.

## 4.4 Sending Compressed Web Pages

Several recent browsers know how to handle gzipped content, automatically uncompressing  documents  that  are  marked  with  the Content-Encoding header and then treating the result as though it were the original document. Sending  such  compressed  content  can  be  a  real  timesaver,  since  the  time required to compress the document on the server and then uncompress it on the  client  is  typically  dwarfed  by  the  savings  in  download  time,  especially when dialup connections are used.

Browsers that support content encoding include most versions of Netscape for Unix, most versions of Internet Explorer for Windows, and Netscape 4.7 and later for Windows. Earlier Netscape versions on Windows and Internet

## 4.4 Sending Compressed Web Pages

DILBERT reprinted by permission of United Syndicate, Inc.

<!-- image -->

Explorer on non-Windows platforms generally do not support content encoding. Fortunately, browsers that support this feature indicate that they do so by setting the Accept-Encoding request header. Listing 4.2 shows a servlet that checks this header, sending a compressed Web page to clients that support gzip encoding and sending a regular Web page to those that don't. The result showed a tenfold speedup for the compressed page when a dialup connection was used. In repeated tests with Netscape 4.7 and Internet Explorer 5.0 on a 28.8K modem connection, the compressed page averaged less than 5 seconds  to  completely  download,  whereas  the  uncompressed  page  consistently took more than 50 seconds.

## Core Tip

Gzip compression can dramatically reduce the download time of long text pages.

<!-- image -->

Implementing compression is straightforward since gzip format is built in to the Java programming languages via classes in java.util.zip . The servlet first checks the Accept-Encoding header to see if it contains an entry for gzip.  If  so,  it  uses  a GZIPOutputStream to  generate  the  page,  specifying gzip as the value of the Content-Encoding header. You must explicitly call close when using a GZIPOutputStream . If gzip is not supported, the servlet uses the normal PrintWriter to  send  the  page.  To  make it easy  to  create benchmarks with a single browser, I also added a feature whereby compression  could  be  suppressed  by including ?encoding=none at  the  end  of  the URL.

## Chapter 4 Handling the Client Request: HTTP Request Headers

## Listing 4.2 EncodedPage.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.util.zip.*; /** Example showing benefits of gzipping pages to browsers *  that can handle gzip. */ public class EncodedPage extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); String encodings = request.getHeader("Accept-Encoding"); String encodeFlag = request.getParameter("encoding"); PrintWriter out; String title; if ((encodings != null) && (encodings.indexOf("gzip") != -1) && !"none".equals(encodeFlag)) { title = "Page Encoded with GZip"; OutputStream out1 = response.getOutputStream(); out = new PrintWriter(new GZIPOutputStream(out1), false); response.setHeader("Content-Encoding", "gzip"); } else { title = "Unencoded Page"; out = response.getWriter(); } out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>\n"); String line = "Blah, blah, blah, blah, blah. " + "Yadda, yadda, yadda, yadda."; for(int i=0; i<10000; i++) { out.println(line); } out.println("</BODY></HTML>"); out.close(); } }
```