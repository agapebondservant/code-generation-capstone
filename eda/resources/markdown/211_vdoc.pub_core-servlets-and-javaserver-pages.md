## Encoding URLs

In  case  servlet  is  using  URL  rewriting  to  implement  session  tracking,  you should give the system a chance to encode the URLs.

## · Regular URLs

String originalURL = someRelativeOrAbsoluteURL; String encodedURL = response.encodeURL(originalURL); out.println("&lt;A HREF=\"" + encodedURL + "\"&gt;...&lt;/A&gt;");

## · Redirect URLs

String originalURL = someURL; // Relative URL OK in 2.2 String encodedURL = response.encodeRedirectURL(originalURL); response.sendRedirect(encodedURL);

## A.10 JSP Scripting Elements

## Types of Scripting Elements

- · Expressions: &lt;%= expression %&gt;

Evaluated and inserted into servlet's output. You can also use

&lt;jsp:expression&gt; expression

&lt;/jsp:expression&gt;

- · Scriptlets: &lt;% code %&gt;

Inserted into servlet's \_jspService method (called by service ). You can also use

&lt;jsp:scriptlet&gt;

code

&lt;/jsp:scriptlet&gt;

## · Declarations: &lt;%! code %&gt;

Inserted into body of servlet class, outside of any existing methods. You can also use

&lt;jsp:declaration&gt;

code

&lt;/jsp:declaration&gt;

## Template Text

- · Use &lt;\% to get &lt;% in output.
- · &lt;%-- JSP Comment --%&gt;
- · &lt;!-- HTML Comment --&gt;
- · All other non-JSP-specific text passed through to output page.

## Predefined Variables

Implicit objects automatically available in expressions and scriptlets (not declarations).

- · request : the HttpServletRequest associated with request.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## A.10 JSP Scripting Elements