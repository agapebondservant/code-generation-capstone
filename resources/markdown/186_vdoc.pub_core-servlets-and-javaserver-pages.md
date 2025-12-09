## A.3 Handling the Client Request: Form Data

## A.3 Handling the Client Request: Form Data

## Reading Parameters

- · request.getParameter : returns first value
- · request.getParameterValues : returns array of all values

## Example Servlet

ThreeParams.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; public class ThreeParams extends HttpServlet { public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Reading Three Request Parameters"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H1 ALIGN=CENTER>" + title + "</H1>\n" + "<UL>\n" + "  <LI><B>param1</B>: " + request.getParameter("param1") + "\n" + "  <LI><B>param2</B>: " + request.getParameter("param2") + "\n" + "  <LI><B>param3</B>: " + request.getParameter("param3") + "\n" + "</UL>\n" + "</BODY></HTML>"); } }
```