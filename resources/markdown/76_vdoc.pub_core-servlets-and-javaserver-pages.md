## Chapter 8 Handling Cookies

## Placing Cookies in the Response Headers

The cookie is inserted into a Set-Cookie HTTP response header by means of the addCookie method of HttpServletResponse .  The method is called addCookie ,  not setCookie ,  because  any  previously  specified Set-Cookie headers are left alone and a new header is set. Here's an example:

Cookie userCookie = new Cookie("user", "uid1234"); userCookie.setMaxAge(60*60*24*365); // 1 year response.addCookie(userCookie);

## Reading Cookies from the Client

To send cookies to the  client,  you  create  a Cookie ,  then  use addCookie to send a Set-Cookie HTTP response header. To  read the cookies that come back from the client, you call getCookies on the HttpServletRequest . This call returns an array of Cookie objects corresponding to the values that came in on the Cookie HTTP request header. If there are no cookies in the request, getCookies returns null . Once you have this array, you typically loop down it, calling getName on each Cookie until  you find one matching the name you have in mind. You then call getValue on the matching Cookie and finish with some processing specific to the resultant value. This is such a common process that Section 8.5 presents two utilities that simplify retrieving a cookie or cookie value that matches a designated cookie name.

## 8.4 Examples of Setting and Reading Cookies

Listing 8.1 and Figure 8-1 show the SetCookies servlet, a servlet that sets six cookies. Three have the default expiration date, meaning that they should apply only until the user next restarts the browser. The other three use setMaxAge to  stipulate  that  they  should  apply  for  the  next  hour,  regardless  of whether the user restarts the browser or reboots the computer to initiate a new browsing session.

Listing 8.2 shows a servlet that creates a table of all  the cookies sent to it in  the  request.  Figure  8-2  shows  this  servlet  immediately  after  the SetCookies servlet is visited. Figure 8-3 shows it after SetCookies is visited then the browser is closed and restarted.

## 8.4 Examples of Setting and Reading Cookies

## Listing 8.1 SetCookies.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; /** Sets six cookies: three that apply only to the current *  session (regardless of how long that session lasts) *  and three that persist for an hour (regardless of *  whether the browser is restarted). */ public class SetCookies extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { for(int i=0; i<3; i++) { // Default maxAge is -1, indicating cookie // applies only to current browsing session. Cookie cookie = new Cookie("Session-Cookie " + i, "Cookie-Value-S" + i); response.addCookie(cookie); cookie = new Cookie("Persistent-Cookie " + i, "Cookie-Value-P" + i); // Cookie is valid for an hour, regardless of whether // user quits browser, reboots computer, or whatever. cookie.setMaxAge(3600); response.addCookie(cookie); } response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Setting Cookies"; out.println (ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=\"CENTER\">" + title + "</H1>\n" + "There are six cookies associated with this page.\n" + "To see them, visit the\n" + "<A HREF=\"/servlet/coreservlets.ShowCookies\">\n" + "<CODE>ShowCookies</CODE> servlet</A>.\n" + "<P>\n" + "Three of the cookies are associated only with the\n" + "current session, while three are persistent.\n" + "Quit the browser, restart, and return to the\n" + "<CODE>ShowCookies</CODE> servlet to verify that\n" + "the three long-lived ones persist across sessions.\n" + "</BODY></HTML>"); } }
```

<!-- image -->

## Chapter 8 Handling Cookies

Figure 8-1 Result of SetCookies servlet.

<!-- image -->

## Listing 8.2 ShowCookies.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; /** Creates a table of the cookies associated with *  the current page. */ public class ShowCookies extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Active Cookies"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=\"CENTER\">" + title + "</H1>\n" +
```

## 8.4 Examples of Setting and Reading Cookies

## "&lt;TABLE BORDER=1 ALIGN=\"CENTER\"&gt;\n" + "&lt;TR BGCOLOR=\"#FFAD00\"&gt;\n" + "  &lt;TH&gt;Cookie Name\n" + "  &lt;TH&gt;Cookie Value"); Cookie[] cookies = request.getCookies(); Cookie cookie; for(int i=0; i&lt;cookies.length; i++) { cookie = cookies[i]; out.println("&lt;TR&gt;\n" + "  &lt;TD&gt;" + cookie.getName() + "\n" + "  &lt;TD&gt;" + cookie.getValue()); } out.println("&lt;/TABLE&gt;&lt;/BODY&gt;&lt;/HTML&gt;"); } } Listing 8.2 ShowCookies.java (continued)

Figure 8-2 Result of visiting the ShowCookies

<!-- image -->

SetCookies in the same browser session.

servlet within an hour of visiting

<!-- image -->