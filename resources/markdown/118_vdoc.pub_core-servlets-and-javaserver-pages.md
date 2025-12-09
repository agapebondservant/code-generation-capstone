## 14.3 Assigning Attributes to Tags

Figure 14-2 Result of SimplePrimeExample.jsp .

<!-- image -->

## 14.3 Assigning Attributes to Tags

## Allowing tags like

&lt;prefix:name attribute1="value1" attribute2="value2" ... /&gt;

adds significant flexibility to your tag library. This section explains how to add attribute support to your tags.

## The Tag Handler Class

Providing support for attributes is straightforward. Use of an attribute called attribute1 simply  results  in  a  call  to  a method  called setAttribute1 in your class that extends TagSupport (or otherwise implements the Tag interface).  The  attribute  value  is  supplied  to  the  method  as  a String .  Consequently,  adding  support  for  an  attribute  named attribute1 is  merely  a matter of implementing the following method:

```
public void setAttribute1(String value1) { doSomethingWith(value1); }
```

Note that an attribute of attributeName (lowercase a ) corresponds to a method called setAttributeName (uppercase A ).

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 14 Creating Custom JSP Tag Libraries

One of the most common things to do in the attribute handler is to simply store the attribute in a field that will later be used by doStartTag or a similar method. For example, following is a section of a tag implementation that adds support for the message attribute.

```
private String message = "Default Message"; public void setMessage(String message) { this.message = message; }
```

If the tag handler will be accessed from other classes, it is a good idea to provide a getAttributeName method in addition to the setAttributeName method. Only setAttributeName is required, however.

Listing  14.7  shows a subclass  of SimplePrimeTag that  adds  support  for the length attribute. When such an attribute is supplied, it results in a call to setLength , which converts the input String to an int and stores it in the len field already used by the doStartTag method in the parent class.

## Listing 14.7 PrimeTag.java

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import java.math.*; import coreservlets.*;
```

/** Generates an N-digit random prime (default N = 50).

- *  Extends SimplePrimeTag, adding a length attribute
- *  to set the size of the prime. The doStartTag
- *  method of the parent class uses the len field
- *  to determine the approximate length of the prime.

*/

```
public class PrimeTag extends SimplePrimeTag {
```

```
public void setLength(String length) { try { len = Integer.parseInt(length); } catch(NumberFormatException nfe) { len = 50; } } }
```

## 14.3 Assigning Attributes to Tags

## The Tag Library Descriptor File

Tag  attributes  must  be  declared  inside  the tag element  by  means  of  an attribute element. The attribute element has three nested elements that can appear between &lt;attribute&gt; and &lt;/attribute&gt; .

- 1. name , a required element that defines the case-sensitive attribute name. In this case, I use &lt;name&gt;length&lt;/name&gt;
- 2. required , a required element that stipulates whether the attribute must always be supplied ( true ) or is optional ( false ). In this case, to indicate that length is optional, I use &lt;required&gt;false&lt;/required&gt; If you omit the attribute, no call is made to the setAttributeName method. So, be sure to give default values to the fields that the method sets.
- 3. rtexprvalue , an optional attribute that indicates whether the attribute value can be a JSP expression like &lt;%= expression %&gt; ( true ) or whether it must be a fixed string ( false ). The default value is false , so this element is usually omitted except when you want to allow attributes to have values determined at request time.

Listing  14.8  shows  the  complete tag element  within  the  tag  library descriptor file. In addition to supplying an attribute element to describe the length attribute,  the tag element  also  contains  the  standard name ( prime ), tagclass ( coreservlets.tags.PrimeTag ), info (short description), and bodycontent ( EMPTY ) elements.

## Listing 14.8 csajsp-taglib.tld

```
<?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" -->
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 14 Creating Custom JSP Tag Libraries

## &lt;tlibversion&gt;1.0&lt;/tlibversion&gt; &lt;jspversion&gt;1.1&lt;/jspversion&gt; &lt;shortname&gt;csajsp&lt;/shortname&gt; &lt;urn&gt;&lt;/urn&gt; &lt;info&gt; A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. &lt;/info&gt; &lt;!-- Other tag defined earlier... --&gt; &lt;tag&gt; &lt;name&gt;prime&lt;/name&gt; &lt;tagclass&gt;coreservlets.tags.PrimeTag&lt;/tagclass&gt; &lt;info&gt;Outputs a random N-digit prime.&lt;/info&gt; &lt;bodycontent&gt;EMPTY&lt;/bodycontent&gt; &lt;attribute&gt; &lt;name&gt;length&lt;/name&gt; &lt;required&gt;false&lt;/required&gt; &lt;/attribute&gt; &lt;/tag&gt; &lt;/taglib&gt; Listing 14.8 csajsp-taglib.tld (continued)

## The JSP File

Listing 14.9 shows a JSP document that uses the taglib directive to load the tag library descriptor file and to specify a prefix of csajsp . Since the prime tag is defined to permit a length attribute, Listing 14.9 uses

&lt;csajsp:prime length="xxx" /&gt;

Remember that custom tags follow XML syntax, which requires attribute values  to  be  enclosed  in  either  single  or  double  quotes.  Also,  since  the length attribute is not required, it is permissible to use

&lt;csajsp:prime /&gt;

The tag handler is responsible for using a reasonable default value in such a case.

Figure 14-3 shows the result of Listing 14.9.