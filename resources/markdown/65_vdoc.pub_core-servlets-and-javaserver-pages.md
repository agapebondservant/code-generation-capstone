## 6.3 A Front End to Various Search Engines

## 501 (Not Implemented)

The 501 ( SC\_NOT\_IMPLEMENTED ) status notifies the client that the server doesn't support the functionality to fulfill the request. It is used, for example, when the client issues a command like PUT that the server doesn't support.

## 502 (Bad Gateway)

A value of 502 ( SC\_BAD\_GATEWAY ) is used by servers that act as proxies or gateways; it indicates that the initial server got a bad response from the remote server.

## 503 (Service Unavailable)

A status code of 503 ( SC\_SERVICE\_UNAVAILABLE ) signifies that the server cannot respond because of maintenance or overloading. For example, a servlet might return this header if some thread or database connection pool is currently full. The server can supply a Retry-After header to tell the client when to try again.

## 504 (Gateway Timeout)

A value of 504 ( SC\_GATEWAY\_TIMEOUT ) is used by servers that act as proxies or gateways; it indicates that the initial server didn't get a timely response from the remote server. This status code is new in HTTP 1.1.

## 505 (HTTP Version Not Supported)

The 505 ( SC\_HTTP\_VERSION\_NOT\_SUPPORTED ) code means that the server doesn't support the version of HTTP named in the request line. This status code is new in HTTP 1.1.

## 6.3 A Front End to Various Search Engines

Listing 6.1 presents an example that makes use of the two most common status codes other than 200 (OK): 302 (Found) and 404 (Not Found). The 302 code  is  set  by  the  shorthand sendRedirect method  of HttpServletResponse , and 404 is specified by sendError .

In this application, an HTML form (see Figure 6-1 and the source code in Listing 6.3) first displays a page that lets the user choose a search string, the number of results to show per page, and the search engine to use. When the

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 6 Generating the Server Response: HTTP Status Codes

form is submitted, the servlet extracts those three parameters, constructs a URL with  the  parameters  embedded  in  a  way  appropriate  to  the  search engine selected (see the SearchSpec class of Listing 6.2), and redirects the user to that URL (see Figure 6-2). If the user fails to choose a search engine or specify search terms, an error page informs the client of this fact (see Figures 6-3 and 6-4).

## 6.3 A Front End to Various Search Engines

## Listing 6.1 SearchEngines.java

package coreservlets;

```
import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.net.*;
```

/** Servlet that takes a search string, number of results per

- *  page, and a search engine name, sending the query to
- *  that search engine. Illustrates manipulating
- *  the response status line. It sends a 302 response
- *  (via sendRedirect) if it gets a known search engine,
- *  and sends a 404 response (via sendError) otherwise.

*/

```
public class SearchEngines extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { if ((searchString == null) || (searchString.length() == 0)) { reportProblem(response, "Missing search string."); return;
```

```
String searchString = request.getParameter("searchString"); } // The URLEncoder changes spaces to "+" signs and other // non-alphanumeric characters to "%XY", where XY is the // hex value of the ASCII (or ISO Latin-1) character. // Browsers always URL-encode form values, so the // getParameter method decodes automatically. But since // we're just passing this on to another server, we need to // re-encode it. searchString = URLEncoder.encode(searchString); String numResults = request.getParameter("numResults");
```

<!-- image -->

## Chapter 6 Generating the Server Response: HTTP Status Codes

## Listing 6.1 SearchEngines.java (continued)

```
if ((numResults == null) || (numResults.equals("0")) || (numResults.length() == 0)) { numResults = "10"; } String searchEngine = request.getParameter("searchEngine"); if (searchEngine == null) { reportProblem(response, "Missing search engine name."); return; } SearchSpec[] commonSpecs = SearchSpec.getCommonSpecs(); for(int i=0; i<commonSpecs.length; i++) { SearchSpec searchSpec = commonSpecs[i]; if (searchSpec.getName().equals(searchEngine)) { String url = searchSpec.makeURL(searchString, numResults); response.sendRedirect(url); return; } } reportProblem(response, "Unrecognized search engine."); } private void reportProblem(HttpServletResponse response, String message) throws IOException { response.sendError(response.SC_NOT_FOUND, "<H2>" + message + "</H2>"); } public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } }
```

## 6.3 A Front End to Various Search Engines

```
Listing 6.2 SearchSpec.java package coreservlets;
```

```
/** Small class that encapsulates how to construct a *  search string for a particular search engine. */ class SearchSpec { private String name, baseURL, numResultsSuffix; private static SearchSpec[] commonSpecs = { new SearchSpec("google", "http://www.google.com/search?q=", "&num="), new SearchSpec("infoseek", "http://infoseek.go.com/Titles?qt=", "&nh="), new SearchSpec("lycos", "http://lycospro.lycos.com/cgi-bin/" + "pursuit?query=", "&maxhits="), new SearchSpec("hotbot", "http://www.hotbot.com/?MT=", "&DC=") }; public SearchSpec(String name, String baseURL, String numResultsSuffix) { this.name = name; this.baseURL = baseURL; this.numResultsSuffix = numResultsSuffix; } public String makeURL(String searchString, String numResults) { return(baseURL + searchString + numResultsSuffix + numResults); } public String getName() { return(name); } public static SearchSpec[] getCommonSpecs() { return(commonSpecs); } }
```

<!-- image -->

## Chapter 6 Generating the Server Response: HTTP Status Codes

Figure 6-1 Front end to the SearchEngines servlet. See Listing 6.3 for the HTML source code.

<!-- image -->

Figure 6-2 Result of the SearchEngines servlet when the form of Figure 6-1 is submitted.

<!-- image -->

## 6.3 A Front End to Various Search Engines

Figure 6-3 Result of SearchEngines servlet when no search string was specified. Internet Explorer 5 displays its own error page, even though the servlet generates one.

<!-- image -->

Figure 6-4 Result of SearchEngines servlet when no search string was specified.

<!-- image -->

Netscape correctly displays the servlet-generated error page.

<!-- image -->

## 142

## Chapter 6 Generating the Server Response: HTTP Status Codes

## Listing 6.3 SearchEngines.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;Searching the Web&lt;/TITLE&gt;

&lt;/HEAD&gt;

&lt;BODY BGCOLOR="#FDF5E6"&gt;

&lt;H1 ALIGN="CENTER"&gt;Searching the Web&lt;/H1&gt;

## &lt;FORM ACTION="/servlet/coreservlets.SearchEngines" &gt;

&lt;CENTER&gt;

Search String:

&lt;INPUT TYPE="TEXT" NAME="searchString"&gt;&lt;BR&gt;

Results to Show Per Page:

&lt;INPUT TYPE="TEXT" NAME="numResults"

VALUE=10 SIZE=3&gt;&lt;BR&gt;

&lt;INPUT TYPE="RADIO" NAME="searchEngine"

VALUE="google"&gt;

Google |

&lt;INPUT TYPE="RADIO" NAME="searchEngine"

VALUE="infoseek"&gt;

Infoseek |

&lt;INPUT TYPE="RADIO" NAME="searchEngine" VALUE="lycos"&gt;

Lycos |

&lt;INPUT TYPE="RADIO" NAME="searchEngine"

VALUE="hotbot"&gt;

HotBot

&lt;BR&gt;

&lt;INPUT TYPE="SUBMIT" VALUE="Search"&gt;

&lt;/CENTER&gt;

&lt;/FORM&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## 6.3 A Front End to Various Search Engines

143