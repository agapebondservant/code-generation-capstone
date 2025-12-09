## 8.6 A Customized Search Engine Interface

```
Listing 8.3 ServletUtilities.java String defaultValue) {
```

```
package coreservlets; import javax.servlet.*; import javax.servlet.http.*; public class ServletUtilities { // Other methods in this class shown in earlier chapters. public static String getCookieValue(Cookie[] cookies, String cookieName, for(int i=0; i<cookies.length; i++) { Cookie cookie = cookies[i]; if (cookieName.equals(cookie.getName())) return(cookie.getValue()); } return(defaultValue); } public static Cookie getCookie(Cookie[] cookies, String cookieName) { for(int i=0; i<cookies.length; i++) { Cookie cookie = cookies[i]; if (cookieName.equals(cookie.getName())) return(cookie); } return(null); } }
```

## Creating Long-Lived Cookies

Listing 8.4 shows a small class that you can use instead of Cookie if you want your cookie to automatically persist when the client quits the browser. See Listing 8.5 for a servlet that uses this class.

## 8.6 A Customized Search Engine Interface

Listing 8.5 shows the CustomizedSearchEngines servlet, a variation of the SearchEngines example previously shown in Section 6.3. Like the SearchEngines servlet  (see  Figure  8-5),  the CustomizedSearchEngines servlet

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 8 Handling Cookies

## Listing 8.4 LongLivedCookie.java

```
package coreservlets; import javax.servlet.http.*; /** Cookie that persists 1 year. Default Cookie doesn't *  persist past current session. */ public class LongLivedCookie extends Cookie { public static final int SECONDS_PER_YEAR = 60*60*24*365; public LongLivedCookie(String name, String value) { super(name, value); setMaxAge(SECONDS_PER_YEAR); } }
```

reads the user choices from the HTML front end and forwards them to the appropriate  search  engine.  In  addition,  the CustomizedSearchEngines servlet returns to the client cookies that store the search values. Then, when the user comes back to the front-end servlet at a later time (even after quitting the browser and restarting), the front-end page is initialized with the values from the previous search.

To accomplish this customization, the front end is dynamically generated instead  of  coming from a  static  HTML file  (see  Listing 8.6 for  the source code and Figure 8-4 for the result). The front-end servlet reads the cookie values and uses them for the initial values of the HTML form fields. Note that it would not have been possible for the front end to return the cookies directly to the client. That's because the search selections aren't known until the user interactively fills in the form and submits it, which cannot occur until after the servlet that generated the front end has finished executing.

This example uses the LongLivedCookie class, shown in the previous section, for creating a Cookie that automatically has a long-term expiration date, instructing the browser to use it beyond the current session.

## 8.6 A Customized Search Engine Interface

## Listing 8.5 CustomizedSearchEngines.java

package coreservlets;

```
import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.net.*;
```

/** A variation of the SearchEngine servlet that uses

- *  cookies to remember users choices. These values
- *  are then used by the SearchEngineFrontEnd servlet
- *  to initialize the form-based front end.

*/

public class CustomizedSearchEngines extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

```
String searchString = request.getParameter("searchString"); if ((searchString == null) || (searchString.length() == 0)) { reportProblem(response, "Missing search string."); return; } Cookie searchStringCookie = new LongLivedCookie("searchString", searchString); response.addCookie(searchStringCookie); // The URLEncoder changes spaces to "+" signs and other // non-alphanumeric characters to "%XY", where XY is the // hex value of the ASCII (or ISO Latin-1) character. // Browsers always URL-encode form values, so the // getParameter method decodes automatically. But since // we're just passing this on to another server, we need to // re-encode it. searchString = URLEncoder.encode(searchString); String numResults = request.getParameter("numResults"); if ((numResults == null) || (numResults.equals("0")) || (numResults.length() == 0)) { numResults = "10"; } Cookie numResultsCookie = new LongLivedCookie("numResults", numResults); response.addCookie(numResultsCookie); String searchEngine = request.getParameter("searchEngine"); if (searchEngine == null) { reportProblem(response, "Missing search engine name."); return; }
```

## Chapter 8 Handling Cookies

## Listing 8.5 CustomizedSearchEngines.java (continued)

```
Cookie searchEngineCookie = new LongLivedCookie("searchEngine", searchEngine); response.addCookie(searchEngineCookie); SearchSpec[] commonSpecs = SearchSpec.getCommonSpecs(); for(int i=0; i<commonSpecs.length; i++) { SearchSpec searchSpec = commonSpecs[i]; if (searchSpec.getName().equals(searchEngine)) { String url = searchSpec.makeURL(searchString, numResults); response.sendRedirect(url); return; } } reportProblem(response, "Unrecognized search engine."); } private void reportProblem(HttpServletResponse response, String message) throws IOException { response.sendError(response.SC_NOT_FOUND, "<H2>" + message + "</H2>"); } public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } }
```

## Listing 8.6 SearchEnginesFrontEnd.java

package coreservlets;

```
import java.io.*; import javax.servlet.*; import java.net.*;
```

```
import javax.servlet.http.*; /** Dynamically generated variation of the *  SearchEngines.html front end that uses cookies *  to remember a user's preferences. */
```

## 8.6 A Customized Search Engine Interface

## Listing 8.6 SearchEnginesFrontEnd.java (continued)

public class SearchEnginesFrontEnd extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { Cookie[] cookies = request.getCookies(); String searchString = ServletUtilities.getCookieValue(cookies, "searchString", "Java Programming"); String numResults = ServletUtilities.getCookieValue(cookies, "numResults", "10"); String searchEngine = ServletUtilities.getCookieValue(cookies, "searchEngine", "google"); response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Searching the Web"; out.println (ServletUtilities.headWithTitle(title) + "&lt;BODY BGCOLOR=\"#FDF5E6\"&gt;\n" + "&lt;H1 ALIGN=\"CENTER\"&gt;Searching the Web&lt;/H1&gt;\n" + "\n" + "&lt;FORM ACTION=\"/servlet/" + "coreservlets.CustomizedSearchEngines\"&gt;\n" + "&lt;CENTER&gt;\n" + "Search String:\n" + "&lt;INPUT TYPE=\"TEXT\" NAME=\"searchString\"\n" + "       VALUE=\"" + searchString + "\"&gt;&lt;BR&gt;\n" + "Results to Show Per Page:\n" + "&lt;INPUT TYPE=\"TEXT\" NAME=\"numResults\"\n" + "       VALUE=" + numResults + " SIZE=3&gt;&lt;BR&gt;\n" + "&lt;INPUT TYPE=\"RADIO\" NAME=\"searchEngine\"\n" + "       VALUE=\"google\"" + checked("google", searchEngine) + "&gt;\n" + "Google |\n" + "&lt;INPUT TYPE=\"RADIO\" NAME=\"searchEngine\"\n" + "       VALUE=\"infoseek\"" + checked("infoseek", searchEngine) + "&gt;\n" + "Infoseek |\n" + "&lt;INPUT TYPE=\"RADIO\" NAME=\"searchEngine\"\n" + "       VALUE=\"lycos\"" + checked("lycos", searchEngine) + "&gt;\n" + "Lycos |\n" + "&lt;INPUT TYPE=\"RADIO\" NAME=\"searchEngine\"\n" + "       VALUE=\"hotbot\"" +

## Chapter 8 Handling Cookies

## private String checked(String name1, String name2) { Listing 8.6 SearchEnginesFrontEnd.java (continued)

```
checked("hotbot", searchEngine) + ">\n" + "HotBot\n" + "<BR>\n" + "<INPUT TYPE=\"SUBMIT\" VALUE=\"Search\">\n" + "</CENTER>\n" + "</FORM>\n" + "\n" + "</BODY>\n" + "</HTML>\n"); } if (name1.equals(name2)) return(" CHECKED"); else return(""); } }
```

Figure 8-4 Result of SearchEnginesFrontEnd servlet. Whatever options you specify will be the initial choices next time you visit the same servlet.

<!-- image -->

## 8.6 A Customized Search Engine Interface

<!-- image -->

Figure 8-5 Result of CustomizedSearchEngines servlet.

<!-- image -->