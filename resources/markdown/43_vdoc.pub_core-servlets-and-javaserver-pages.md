## Chapter 2 First Servlets

Figure 2-7 Specifying initialization parameters for a named servlet with the Java Web Server.

<!-- image -->

## 2.8 An Example Using Servlet Initialization and Page Modification Dates

Listing 2.11 shows a servlet that uses init to do two things. First, it builds an array of 10 integers. Since these numbers are based upon complex calculations,  I  don't  want  to  repeat  the  computation  for  each  request.  So  I  have doGet look  up  the  values  that init computed instead  of  generating them each time. The results of this technique are shown in Figure 2-8.

However, since all users get the same result, init also stores a page modification date that is used by the getLastModified method. This method should return a modification time expressed in milliseconds since 1970, as is standard

## 2.8 An Example Using Servlet Initialization and Page Modification Dates

Figure 2-8 Output of LotteryNumbers servlet.

<!-- image -->

with Java dates. The time is automatically converted to a date in GMT appropriate for the Last-Modified header. More importantly, if the server receives a  conditional GET request  (one  specifying  that  the  client  only  wants  pages marked If-Modified-Since a  particular  date),  the  system  compares  the specified date to that returned by getLastModified , only returning the page if it has been changed after the specified date. Browsers frequently make these conditional requests for pages stored in their caches, so supporting conditional requests helps your users as well as reducing server load. Since the Last-Modified and If-Modified-Since headers  use  only  whole  seconds,  the getLastModified method should round times down to the nearest second.

Figures 2-9 and 2-10 show the result of requests for the same servlet with two slightly different If-Modified-Since dates. To set the request headers and see the response headers, I used WebClient , a Java application shown in Section 2.10 (WebClient: Talking to Web Servers Interactively) that lets you interactively set up HTTP requests, submit them, and see the results.

## 46

## Chapter 2 First Servlets

## Listing 2.11 LotteryNumbers.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; /** Example using servlet initialization and the *  getLastModified method. */ public class LotteryNumbers extends HttpServlet { private long modTime; private int[] numbers = new int[10]; *  is first loaded, before the first request *  is processed.
```

```
/** The init method is called only when the servlet */ public void init() throws ServletException { // Round to nearest second (ie 1000 milliseconds) modTime = System.currentTimeMillis()/1000*1000; for(int i=0; i<numbers.length; i++) { numbers[i] = randomNum(); } } public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Your Lottery Numbers"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>\n" +
```

## 2.8 An Example Using Servlet Initialization and Page Modification Dates

## Listing 2.11 LotteryNumbers.java (continued)

```
"<B>Based upon extensive research of " + "astro-illogical trends, psychic farces, " + "and detailed statistical claptrap, " + "we have chosen the " + numbers.length + " best lottery numbers for you.</B>" + "<OL>"); for(int i=0; i<numbers.length; i++) { out.println("  <LI>" + numbers[i]); } out.println("</OL>" + "</BODY></HTML>"); }
```

/** The standard service method compares this date

- *  against any date specified in the If-Modified-Since
- *  request header. If the getLastModified date is
- *  later, or if there is no If-Modified-Since header,
- *  the doGet method is called normally. But if the
- *  getLastModified date is the same or earlier,
- *  the service method sends back a 304 (Not Modified)
- *  response, and does &lt;B&gt;not&lt;/B&gt; call doGet.
- *  The browser should use its cached version of
- *  the page in such a case.

*/

## public long getLastModified(HttpServletRequest request) { return(modTime);

```
} // A random int from 0 to 99. private int randomNum() { return((int)(Math.random() * 100)); } }
```

<!-- image -->

## Chapter 2 First Servlets

Figure 2-9 Accessing the LotteryNumbers servlet with an unconditional GET request or with a conditional request specifying a date before servlet initialization results in the normal Web page.

<!-- image -->

## 2.8 An Example Using Servlet Initialization and Page Modification Dates

<!-- image -->

Figure 2-10 Accessing the LotteryNumbers servlet with a conditional GET request specifying a date at or after servlet initialization results in a 304 ( Not Modified ) response.

<!-- image -->