## Chapter 14 Creating Custom JSP Tag Libraries

## 14.6 Manipulating the Tag Body

The csajsp:prime element  (Section  14.3)  ignored  any  body  content,  the csajsp:heading element (Section 14.4) used body content, and the csajsp:debug element (Section 14.5) ignored or used it depending on a request time parameter. The common thread among these elements is that the tag body was never modified; it was either ignored or included verbatim (after JSP translation). This section shows you how to process the tag body.

## The Tag Handler Class

Up to this point, all of the tag handlers have extended the TagSupport class. This  is  a  good  standard  starting  point,  as  it  implements  the  required Tag interface and performs a number of useful setup operations like storing the PageContext reference in the pageContext field. However, TagSupport is not powerful enough for tag implementations that need to manipulate their body content, and BodyTagSupport should be used instead.

BodyTagSupport extends TagSupport , so the doStartTag and doEndTag methods are used in the same way as before. The two important new methods defined by BodyTagSupport are:

- 1. doAfterBody , a method that you should override to handle the manipulation of the tag body. This method should normally return SKIP\_BODY when it is done, indicating that no further body processing should be performed.
- 2. getBodyContent , a method that returns an object of type BodyContent that encapsulates information about the tag body.

The BodyContent class has three important methods:

- 1. getEnclosingWriter , a method that returns the JspWriter being used by doStartTag and doEndTag .
- 2. getReader , a method that returns a Reader that can read the tag's body.
- 3. getString , a method that returns a String containing the entire tag body.

In Section 3.4 (Example: Reading All Parameters), we saw a static filter method that would take a string and replace &lt; , &gt; , " , and &amp; with &amp;lt; , &amp;gt; ,

## 14.6 Manipulating the Tag Body

&amp;quot; , and &amp;amp; , respectively. This method is useful when servlets output strings  that  might  contain  characters  that  would  interfere  with  the  HTML structure of the page in which the strings are embedded. Listing 14.16 shows a  tag  implementation that gives this filtering functionality to a custom JSP tag.

## Listing 14.16 FilterTag.java

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import coreservlets.*;
```

/** A tag that replaces &lt;, &gt;, ", and &amp; with their HTML

- *  character entities (&amp;lt;, &amp;gt;, &amp;quot;, and &amp;amp;).
- *  After filtering, arbitrary strings can be placed
- *  in either the page body or in HTML attributes.

*/

```
public class FilterTag extends BodyTagSupport { public int doAfterBody() { BodyContent body = getBodyContent(); String filteredBody = ServletUtilities.filter( body.getString() ); try { JspWriter out = body.getEnclosingWriter() ; out.print(filteredBody); } catch(IOException ioe) { System.out.println("Error in FilterTag: " + ioe); } // SKIP_BODY means I'm done. If I wanted to evaluate // and handle the body again, I'd return EVAL_BODY_TAG. return(SKIP_BODY); } }
```

## The Tag Library Descriptor File

Tags  that  manipulate their body content should use the bodycontent element the same way as tags that simply include it verbatim; they should supply a value of JSP . Other than that, nothing new is required in the descriptor file, as you can see by examining Listing 14.17.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

```
Listing 14.17 csajsp-taglib.tld <?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" --> <tlibversion>1.0</tlibversion> <jspversion>1.1</jspversion> <shortname>csajsp</shortname> <urn></urn> <info> A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. </info> <!-- Other tags defined earlier... --> <tag> <name>filter</name> <tagclass>coreservlets.tags.FilterTag</tagclass> <info>Replaces HTML-specific characters in body.</info> <bodycontent>JSP</bodycontent> </tag> </taglib>
```

## The JSP File

Listing 14.18 shows a page that uses a table to show some sample HTML and its  result. Creating this table would be tedious in regular HTML since the table cell that shows the original HTML would have to change all the &lt; and &gt; characters to &amp;lt; and &amp;gt; . Doing so is particularly onerous during development when the sample HTML is frequently changing. Use of the &lt;csajsp:filter&gt; tag  greatly simplifies the process, as Listing 14.18 illustrates. Figure 14-7 shows the result.

## Listing 14.18 FilterExample.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;HTML Logical Character Styles&lt;/TITLE&gt;

&lt;LINK REL=STYLESHEET

HREF="JSP-Styles.css"

TYPE="text/css"&gt;

&lt;/HEAD&gt;

&lt;BODY&gt;

&lt;H1&gt;HTML Logical Character Styles&lt;/H1&gt; Physical character styles (B, I, etc.) are rendered consistently in different browsers. Logical character styles, however, may be rendered differently by different browsers. Here's how your browser (&lt;%= request.getHeader("User-Agent") %&gt;) renders the HTML 4.0 logical character styles: &lt;P&gt;

## &lt;%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %&gt;

&lt;TABLE BORDER=1 ALIGN="CENTER"&gt; &lt;TR CLASS="COLORED"&gt;&lt;TH&gt;Example&lt;TH&gt;Result &lt;TR&gt;

&lt;TD&gt;&lt;PRE&gt; &lt;csajsp:filter&gt;

&lt;EM&gt;Some emphasized text.&lt;/EM&gt;&lt;BR&gt; &lt;STRONG&gt;Some strongly emphasized text.&lt;/STRONG&gt;&lt;BR&gt; &lt;CODE&gt;Some code.&lt;/CODE&gt;&lt;BR&gt; &lt;SAMP&gt;Some sample text.&lt;/SAMP&gt;&lt;BR&gt; &lt;KBD&gt;Some keyboard text.&lt;/KBD&gt;&lt;BR&gt; &lt;DFN&gt;A term being defined.&lt;/DFN&gt;&lt;BR&gt; &lt;VAR&gt;A variable.&lt;/VAR&gt;&lt;BR&gt; &lt;CITE&gt;A citation or reference.&lt;/CITE&gt;

&lt;/csajsp:filter&gt; &lt;/PRE&gt;

&lt;TD&gt;

&lt;EM&gt;Some emphasized text.&lt;/EM&gt;&lt;BR&gt; &lt;STRONG&gt;Some strongly emphasized text.&lt;/STRONG&gt;&lt;BR&gt; &lt;CODE&gt;Some code.&lt;/CODE&gt;&lt;BR&gt; &lt;SAMP&gt;Some sample text.&lt;/SAMP&gt;&lt;BR&gt; &lt;KBD&gt;Some keyboard text.&lt;/KBD&gt;&lt;BR&gt; &lt;DFN&gt;A term being defined.&lt;/DFN&gt;&lt;BR&gt; &lt;VAR&gt;A variable.&lt;/VAR&gt;&lt;BR&gt; &lt;CITE&gt;A citation or reference.&lt;/CITE&gt;

&lt;/TABLE&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## 14.6 Manipulating the Tag Body

<!-- image -->