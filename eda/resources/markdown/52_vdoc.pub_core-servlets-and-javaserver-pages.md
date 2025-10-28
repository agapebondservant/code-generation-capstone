## 3.6 Filtering Strings for HTML-Specific Characters

## 3.6 Filtering Strings for HTML-Specific Characters

Normally, when a servlet wants to generate HTML that will contain characters like &lt; or &gt; , it simply uses &amp;lt; or &amp;gt; , the standard HTML character entities.  Similarly,  if  a  servlet  wants  a  double  quote  or  an  ampersand  to appear inside an HTML attribute value, it uses &amp;quot; or &amp;amp; . Failing to make these substitutions results in malformed HTML code, since &lt; or &gt; will often get interpreted as part of an HTML markup tag, a double quote in an attribute value may be interpreted as the end of the value, and ampersands are just plain illegal in attribute values. In most cases, it is easy to note the special  characters  and  use  the  standard  HTML  replacements.  However, there are two cases when it is not so easy to make this substitution manually.

The first case where manual conversion is difficult occurs when the string is  derived  from  a program excerpt or another source where it is already in some standard format. Going through manually and changing all the special characters can be tedious in such a case, but forgetting to convert even one special character can result in your Web page having missing or improperly formatted sections (see Figure 3-9 later in this section).

The  second  case  where  manual  conversion  fails  is  when  the  string  is derived  from  HTML  form  data.  Here,  the  conversion  absolutely  must  be performed at runtime, since of course the query data is not known at compile time. Failing to do this for an internal Web page can also result in missing or improperly formatted sections of the servlet's output if the user ever sends these special characters. Failing to do this filtering for externally-accessible Web pages also lets your page become a vehicle for the cross-site scripting attack . Here, a malicious programmer embeds GET parameters in a URL that refers  to  one  of  your  servlets.  These GET parameters  expand  to  HTML &lt;SCRIPT&gt; elements that exploit known browser bugs. However, by embedding the code in a URL that refers to your site and only distributing the URL, not  the  malicious  Web  page  itself,  the  attacker  can  remain  undiscovered more easily and can also exploit trusted relationships to make users think the scripts are coming from a trusted source (your servlet). For more details on this issue, see http://www.cert.org/advisories/ CA-2000-02.html and http://www.microsoft.com/technet/security/crssite.asp .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 3 Handling the Client Request: Form Data

## Code for Filtering

Replacing &lt; , &gt; , " , and &amp; in strings is a simple matter, and there are a number of different approaches that would accomplish the task. However, it is important to remember that Java strings are immutable (i.e., can't be modified), so string concatenation involves copying and then discarding many string segments. For example, consider the following two lines:

```
String s1 = "Hello"; String s2 = s1 + " World";
```

Since s1 cannot be modified, the second line makes a copy of s1 and appends "World" to the copy, then the copy is discarded. To avoid the expense of generating these temporary objects (garbage), you should use a mutable data structure, and StringBuffer is the natural choice. Listing 3.8 shows a static filter method that uses a StringBuffer to efficiently copy characters from an input string to a filtered version, replacing the four special characters along the way.

## Listing 3.8 ServletUtilities.java

```
package coreservlets; import javax.servlet.*; import javax.servlet.http.*;
```

```
public class ServletUtilities { // Other methods in ServletUtilities shown elsewhere... /** Given a string, this method replaces all occurrences of *  '<' with '&lt;', all occurrences of '>' with *  '&gt;', and (to handle cases that occur inside attribute *  values), all occurrences of double quotes with *  '&quot;' and all occurrences of '&' with '&amp;'. *  Without such filtering, an arbitrary string *  could not safely be inserted in a Web page. */ public static String filter(String input) { StringBuffer filtered = new StringBuffer(input.length()); char c; for(int i=0; i<input.length(); i++) { c = input.charAt(i); if (c == '<') { filtered.append("&lt;"); } else if (c == '>') { filtered.append("&gt;");
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 3.6 Filtering Strings for HTML-Specific Characters

```
} else if (c == '"') { filtered.append("&quot;"); } else if (c == '&') { filtered.append("&amp;"); } else { filtered.append(c); } } return(filtered.toString()); } } Listing 3.8 ServletUtilities.java (continued)
```

## Example

By means of illustration, consider a servlet that attempts to generate a Web page containing the following code listing:

```
if (a<b) { doThis(); } else { doThat(); }
```

If  the  code  was  inserted  into  the  Web  page  verbatim,  the &lt;b would  be interpreted as the beginning of an HTML tag, and all of the code up to the next &gt; would likely be interpreted as malformed pieces of that tag. For example, Listing 3.9 shows a servlet that outputs this code fragment, and Figure 3-9 shows the poor result. Listing 3.10 presents a servlet that changes nothing except for filtering the string containing the code fragment, and, as Figure 3-10 illustrates, the result is fine.

## Listing 3.9 BadCodeServlet.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; /** Servlet that displays a fragment of some Java code, *  but forgets to filter out the HTML-specific characters *  (the less-than sign in this case). */ public class BadCodeServlet extends HttpServlet { private String codeFragment =
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 3 Handling the Client Request: Form Data

```
"if (a<b) {\n" + "  doThis();\n" + "} else {\n" + "  doThat();\n" + "}\n"; public String getCodeFragment() { return(codeFragment); } public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "The Java 'if' Statement"; out.println(ServletUtilities.headWithTitle(title) + "<BODY>\n" + "<H1>" + title + "</H1>\n" + "<PRE>\n" + getCodeFragment() + "</PRE>\n" + "Note that you <I>must</I> use curly braces\n" + "when the 'if' or 'else' clauses contain\n" + "more than one expression.\n" + "</BODY></HTML>"); } } Listing 3.9 BadCodeServlet.java (continued)
```

## Listing 3.10 FilteredCodeServlet.java

package coreservlets;

/** Subclass of BadCodeServlet that keeps the same doGet method

- *  but filters the code fragment for HTML-specific characters.
- *  You should filter strings that are likely to contain
- *  special characters (like program excerpts) or strings
- *  that are derived from user input.

*/

```
public class FilteredCodeServlet extends BadCodeServlet { public String getCodeFragment() { return( ServletUtilities.filter(super.getCodeFragment()) ); } }
```

## 3.6 Filtering Strings for HTML-Specific Characters

<!-- image -->

Figure 3-9 Result of BadCodeServlet : much of the code fragment is lost, and the text following the code fragment is incorrectly displayed in a monospaced font.

<!-- image -->

Figure 3-10 Result of FilteredCodeServlet : use of the filter method solves problems with strings containing special characters.

<!-- image -->