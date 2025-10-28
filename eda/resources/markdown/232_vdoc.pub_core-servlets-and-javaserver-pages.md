## Appendix A Servlet and JSP Quick Reference

- · code : used identically to the CODE attribute of APPLET .
- · width : used identically to the WIDTH attribute of APPLET .
- · height : used identically to the HEIGHT attribute of APPLET .
- · codebase : used identically to the CODEBASE attribute of APPLET .
- · align : used identically to the ALIGN attribute of APPLET and IMG .
- · hspace : used identically to the HSPACE attribute of APPLET .
- · vspace : used identically to the VSPACE attribute of APPLET .
- · archive : used identically to the ARCHIVE attribute of APPLET .
- · name : used identically to the NAME attribute of APPLET .
- · title : used identically to the rare TITLE attribute of APPLET (and virtually all other HTML elements in HTML 4.0), specifying a title that could be used for a tool-tip or for indexing.
- · jreversion : identifies the version of the Java Runtime Environment (JRE) that is required. The default is 1.1.
- · iepluginurl : designates a URL from which the plug-in for Internet Explorer can be downloaded.
- · nspluginurl : designates a URL from which the plug-in for Netscape can be downloaded.

## Parameters in HTML: jsp:param

## · Regular form:

&lt;APPLET CODE="MyApplet.class" WIDTH=475 HEIGHT=350&gt;

&lt;PARAM NAME="PARAM1" VALUE="VALUE1"&gt; &lt;PARAM NAME="PARAM2" VALUE="VALUE2"&gt;

&lt;/APPLET&gt;

## · JSP form for Java Plug-In:

&lt;jsp:plugin type="applet" code="MyApplet.class" width="475" height="350"&gt;

&lt;jsp:params&gt;

&lt;jsp:param name="PARAM1" value="VALUE1" /&gt;

&lt;jsp:param name="PARAM2" value="VALUE2" /&gt;

&lt;/jsp:params&gt;

&lt;/jsp:plugin&gt;

## Alternative Text

## · Regular form:

&lt;APPLET CODE="MyApplet.class" WIDTH=475 HEIGHT=350&gt;

&lt;B&gt;Error: this example requires Java.&lt;/B&gt;

&lt;/APPLET&gt;

## · JSP form for Java Plug-In:

&lt;jsp:plugin type="applet"

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.