## Listing 14.9 PrimeExample.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Some N-Digit Primes</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <H1>Some N-Digit Primes</H1>
```

## &lt;%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %&gt;

```
<UL> <LI>20-digit: <csajsp:prime length="20" /> <LI>40-digit: <csajsp:prime length="40" /> <LI>80-digit: <csajsp:prime length="80" /> <LI>Default (50-digit): <csajsp:prime />
```

&lt;/UL&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

Figure 14-3 Result of PrimeExample.jsp .

<!-- image -->

## 14.4 Including the Tag Body

Up to this point, all of the custom tags you have seen ignore the tag body and thus are used as stand-alone tags of the form

&lt;prefix:tagname /&gt;

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 14.4 Including the Tag Body

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

In this section, we see how to define tags that use their body content, and are thus used in the following manner:

&lt;prefix:tagname&gt;body&lt;/prefix:tagname&gt;

## The Tag Handler Class

In  the  previous  examples, the  tag  handlers defined  a doStartTag method that returned SKIP\_BODY . To instruct the system to make use of the body that occurs  between  the  new  element's  start  and  end  tags,  your doStartTag method should return EVAL\_BODY\_INCLUDE instead. The body content can contain JSP scripting elements, directives, and actions, just like the rest of the page. The JSP constructs are translated into servlet code at page translation time, and that code is invoked at request time.

If  you make use of a tag body, then you might want to take some action after the body as well as before it. Use the doEndTag method to specify this action. In almost all cases, you want to continue with the rest of the page after finishing with your tag, so the doEndTag method should return EVAL\_PAGE . If you  want  to  abort  the  processing  of  the  rest  of  the  page,  you  can  return SKIP\_PAGE instead.

Listing 14.10 defines a tag for a heading element that is more flexible than the standard HTML H1 through H6 elements. This new element allows a precise font size, a list of preferred font names (the first entry that is available on the client system will be used), a foreground color, a background color, a border, and an alignment ( LEFT , CENTER , RIGHT ). Only the alignment capability is  available  with the H1 through H6 elements. The heading is implemented through use of a one-cell table enclosing a SPAN element that has embedded style  sheet  attributes.  The doStartTag method  generates  the TABLE and SPAN start  tags, then returns EVAL\_BODY\_INCLUDE to instruct the system to include  the  tag  body.  The doEndTag method  generates  the &lt;/SPAN&gt; and &lt;/TABLE&gt; tags, then returns EVAL\_PAGE to continue with normal page processing. Various setAttributeName methods  are  used  to  handle  the attributes like bgColor and fontSize .

## Listing 14.10 HeadingTag.java

```
package coreservlets.tags; import javax.servlet.jsp.tagext.*;
```

```
import javax.servlet.jsp.*; import java.io.*;
```

/** Generates an HTML heading with the specified background

- *  color, foreground color, alignment, font, and font size.
- *  You can also turn on a border around it, which normally
- *  just barely encloses the heading, but which can also
- *  stretch wider. All attributes except the background
- *  color are optional.

*/

public class HeadingTag extends TagSupport {

```
private String bgColor; // The one required attribute private String color = null; private String align="CENTER"; private String fontSize="36"; private String fontList="Arial, Helvetica, sans-serif"; private String border="0"; private String width=null; public void setBgColor(String bgColor) { this.bgColor = bgColor; } public void setColor(String color) { this.color = color; } public void setAlign(String align) { this.align = align; } public void setFontSize(String fontSize) { this.fontSize = fontSize; } public void setFontList(String fontList) { this.fontList = fontList; } public void setBorder(String border) { this.border = border; } public void setWidth(String width) { this.width = width; }
```

## 14.4 Including the Tag Body

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

```
Listing 14.10 HeadingTag.java (continued)
```

```
public int doStartTag() { try { JspWriter out = pageContext.getOut(); out.print("<TABLE BORDER=" + border + " BGCOLOR=\"" + bgColor + "\"" + " ALIGN=\"" + align + "\""); if (width != null) { out.print(" WIDTH=\"" + width + "\""); } out.print("><TR><TH>"); out.print("<SPAN STYLE=\"" + "font-size: " + fontSize + "px; " + "font-family: " + fontList + "; "); if (color != null) { out.println("color: " + color + ";"); } out.print("\"> "); // End of <SPAN ...> } catch(IOException ioe) { System.out.println("Error in HeadingTag: " + ioe); } return(EVAL_BODY_INCLUDE); // Include tag body } public int doEndTag() { try { JspWriter out = pageContext.getOut(); out.print("</SPAN></TABLE>"); } catch(IOException ioe) { System.out.println("Error in HeadingTag: " + ioe); } return(EVAL_PAGE); // Continue with rest of JSP page } }
```

## The Tag Library Descriptor File

There is only one new feature in the use of the tag element for tags that use body  content:  the bodycontent element  should  contain  the  value JSP as below.

&lt;bodycontent&gt;JSP&lt;/bodycontent&gt;

The name , tagclass , info , and attribute elements are used in the same manner as described previously. Listing 14.11 gives the code.

## Listing 14.11 csajsp-taglib.tld

```
<?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" --> <tlibversion>1.0</tlibversion> <jspversion>1.1</jspversion> <shortname>csajsp</shortname> <urn></urn> <info> A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. </info> <!-- Other tags defined earlier... --> <tag> <name>heading</name> <tagclass>coreservlets.tags.HeadingTag</tagclass> <info>Outputs a 1-cell table used as a heading.</info> <bodycontent>JSP</bodycontent> <attribute> <name>bgColor</name> <required>true</required> <!-- bgColor is required --> </attribute> <attribute> <name>color</name> <required>false</required> </attribute> <attribute> <name>align</name> <required>false</required> </attribute> <attribute> <name>fontSize</name> <required>false</required> </attribute> <attribute> <name>fontList</name> <required>false</required> </attribute> <attribute> <name>border</name> <required>false</required> </attribute>
```

## 14.4 Including the Tag Body

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

## Listing 14.11 csajsp-taglib.tld (continued)

```
<attribute> <name>width</name> <required>false</required> </attribute> </tag> </taglib>
```

## The JSP File

Listing 14.12 shows a document that uses the heading tag just defined. Since the bgColor attribute was defined to be required, all uses of the tag include it. Figure 14-4 shows the result.

## Listing 14.12 HeadingExample.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Some Tag-Generated Headings</TITLE> </HEAD> <BODY> <%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %> <csajsp:heading bgColor="#C0C0C0"> Default Heading </csajsp:heading> <P> <csajsp:heading bgColor="BLACK" color="WHITE"> White on Black Heading </csajsp:heading> <P> <csajsp:heading bgColor="#EF8429" fontSize="60" border="5"> Large Bordered Heading </csajsp:heading> <P> <csajsp:heading bgColor="CYAN" width="100%"> Heading with Full-Width Background </csajsp:heading> <P> <csajsp:heading bgColor="CYAN" fontSize="60" fontList="Brush Script MT, Times, serif"> Heading with Non-Standard Font </csajsp:heading> <P> </BODY> </HTML>
```