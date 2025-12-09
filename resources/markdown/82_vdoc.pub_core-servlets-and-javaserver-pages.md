## Core Approach

Plan ahead: pass URLs that refer to your own site through response.encodeURL or response.encodeRedirectURL , regardless of whether your servlet is using session tracking.

## 9.3 A Servlet Showing Per-Client Access Counts

<!-- image -->

<!-- image -->

## 9.3 A Servlet Showing Per-Client Access Counts

Listing 9.1 presents a simple servlet that shows basic information about the client's session. When the client connects, the servlet uses request.getSession(true) to either retrieve the existing session or, if there was no session, to create a new one. The servlet then looks for an attribute of type Integer called accessCount . If it cannot find such an attribute, it uses 0 as the number of previous accesses. This value is then incremented and associated with the  session  by putValue .  Finally,  the  servlet  prints  a  small  HTML  table showing information about the session. Figures 9-1 and 9-2 show the servlet on the initial visit and after the page was reloaded several times.

## Listing 9.1 ShowSession.java

import java.io.*;

import javax.servlet.*;

import javax.servlet.http.*;

import java.net.*;

import java.util.*;

/** Simple example of session tracking. See the shopping

- *  cart example for a more detailed one.

*/

public class ShowSession extends HttpServlet {

public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Session Tracking Example"; HttpSession session = request.getSession(true); String heading; // Use getAttribute instead of getValue in version 2.2. Integer accessCount =

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 9 Session Tracking

```
(Integer)session.getValue("accessCount"); if (accessCount == null) { accessCount = new Integer(0); heading = "Welcome, Newcomer"; } else { heading = "Welcome Back"; accessCount = new Integer(accessCount.intValue() + 1); } // Use setAttribute instead of putValue in version 2.2. session.putValue("accessCount", accessCount); out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=\"CENTER\">" + heading + "</H1>\n" + "<H2>Information on Your Session:</H2>\n" + "<TABLE BORDER=1 ALIGN=\"CENTER\">\n" + "<TR BGCOLOR=\"#FFAD00\">\n" + "  <TH>Info Type<TH>Value\n" + "<TR>\n" + "  <TD>ID\n" + "  <TD>" + session.getId() + "\n" + "<TR>\n" + "  <TD>Creation Time\n" + "  <TD>" + new Date( session.getCreationTime() ) + "\n" + "<TR>\n" + "  <TD>Time of Last Access\n" + "  <TD>" + new Date( session.getLastAccessedTime() ) + "\n" + "<TR>\n" + "  <TD>Number of Previous Accesses\n" + "  <TD>" + accessCount + "\n" + "</TABLE>\n" + "</BODY></HTML>"); } /** Handle GET and POST requests identically. */ public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } } Listing 9.1 ShowSession.java (continued)
```