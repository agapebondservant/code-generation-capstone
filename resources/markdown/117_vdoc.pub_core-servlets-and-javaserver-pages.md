## Chapter 14 Creating Custom JSP Tag Libraries

```
Listing 14.3 SimpleExample.jsp <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %> <TITLE> <csajsp:example /> </TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <H1> <csajsp:example /> </H1> <csajsp:example /> </BODY> </HTML>
```

Figure 14-1 Result of SimpleExample.jsp .

<!-- image -->

## 14.2 Defining a Basic Tag

This  section  gives  details  on  defining  simple  tags  without  attributes  or  tag bodies; the tags are thus of the form &lt;prefix:tagname /&gt; .

## The Tag Handler Class

Tags  that  either  have  no  body  or  that  merely  include  the  body  verbatim should extend the TagSupport class. This is a built-in class in the javax.servlet.jsp.tagext package  that  implements  the Tag interface and contains much of the standard functionality basic tags need. Because of other  classes  you  will  use,  your  tag  should  normally  import  classes  in  the javax.servlet.jsp and java.io packages as well. So, most tag implementations contain the following import statements after the package declaration:

```
import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*;
```

I recommend that you download an example from http://www.coreservlets.com/ and use it as the starting point for your own implementations.

For  a  tag  without  attributes  or  body,  all  you  need  to  do  is  override  the doStartTag method,  which  defines  code  that  gets  called at  request  time where  the  element's  start  tag  is  found.  To  generate  output,  the  method should obtain the JspWriter (the specialized PrintWriter available in JSP pages through  use  of  the  predefined out variable)  from  the pageContext field by means of getOut . In addition to the getOut method, the pageContext field (of type PageContext ) has methods for obtaining other data structures associated with the request. The most important ones are getRequest , getResponse , getServletContext , and getSession .

Since the print method of JspWriter throws IOException , the print statements  should  be  inside  a try / catch block.  To  report  other  types  of errors to the client, you can declare that your doStartTag method throws a JspException and then throw one when the error occurs.

If  your  tag  does  not  have  a  body,  your doStartTag should  return  the SKIP\_BODY constant. This instructs the system to ignore any content between the tag's start and end tags. As we will see in Section 14.5 (Optionally Including the Tag Body), SKIP\_BODY is sometimes useful even when there is a tag body, but the simple tag we're developing here will be used as a stand-alone tag ( &lt;prefix:tagname /&gt; ) and thus does not have body content.

Listing 14.4 shows a tag implementation that uses this approach to generate a  random 50-digit prime through use of the Primes class  developed in Chapter 7 (Generating the Server Response: HTTP Response Headers) see Listing 7.4.

## 14.2 Defining a Basic Tag

## 316

## Chapter 14 Creating Custom JSP Tag Libraries

## Listing 14.4 SimplePrimeTag.java

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import java.math.*; import coreservlets.*; /** Generates a prime of approximately 50 digits. *  (50 is actually the length of the random number *  generated -- the first prime above that number will *  be returned.) */ public class SimplePrimeTag extends TagSupport { protected int len = 50; public int doStartTag () { try { JspWriter out = pageContext.getOut(); BigInteger prime = Primes.nextPrime(Primes.random(len)); out.print (prime); } catch(IOException ioe) { System.out.println("Error generating prime: " + ioe); } return(SKIP_BODY); } }
```

## The Tag Library Descriptor File

The general format of a descriptor file is almost always the same: it should contain  an  XML  version  identifier  followed  by  a DOCTYPE declaration followed by  a taglib container element. To get started,  just  download a sample  from http://www.coreservlets.com/ .  The  important  part  to understand is what goes in the taglib element: the tag element. For tags without attributes, the tag element should contain four elements between &lt;tag&gt; and &lt;/tag&gt; :

- 1. name , whose body defines the base tag name to which the prefix of the taglib directive will be attached. In this case, I use &lt;name&gt;simplePrime&lt;/name&gt; to assign a base tag name of simplePrime .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 14.2 Defining a Basic Tag

- 2. tagclass , which gives the fully qualified class name of the tag handler. In this case, I use &lt;tagclass&gt;coreservlets.tags.SimplePrimeTag &lt;/tagclass&gt;
- 3. info , which gives a short description. Here, I use &lt;info&gt;Outputs a random 50-digit prime.&lt;/info&gt;
- 4. bodycontent , which should have the value EMPTY for tags without bodies. Tags with normal bodies that might be interpreted as normal JSP use a value of JSP , and the rare tags whose handlers completely process the body themselves use a value of TAGDEPENDENT . For the SimplePrimeTag discussed here, I use EMPTY as below:
- &lt;bodycontent&gt;EMPTY&lt;/bodycontent&gt;

Listing 14.5 shows the full TLD file.

## Listing 14.5 csajsp-taglib.tld

```
<?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" --> <tlibversion>1.0</tlibversion> <jspversion>1.1</jspversion> <shortname>csajsp</shortname> <urn></urn> <info> A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. </info> <!-- Other tags defined earlier... -->
```

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

## Listing 14.5 csajsp-taglib.tld (continued)

&lt;tag&gt;

&lt;name&gt;simplePrime&lt;/name&gt;

&lt;tagclass&gt;coreservlets.tags.SimplePrimeTag&lt;/tagclass&gt;

&lt;info&gt;Outputs a random 50-digit prime.&lt;/info&gt;

&lt;bodycontent&gt;EMPTY&lt;/bodycontent&gt;

&lt;/tag&gt;

&lt;/taglib&gt;

## The JSP File

JSP documents that make use of custom tags need to use the taglib directive, supplying a uri attribute that gives the location of the tag library descriptor file and a prefix attribute that specifies a short string that will be attached (along with a colon) to the main tag name. Listing 14.6 shows a JSP document that uses

&lt;%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %&gt;

to use the TLD file just shown in Listing 14.5 with a prefix of csajsp . Since the base tag name is simplePrime , the full tag used is

&lt;csajsp:simplePrime /&gt;

Figure 14-2 shows the result.

## Listing 14.6 SimplePrimeExample.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;Some 50-Digit Primes&lt;/TITLE&gt; &lt;LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;H1&gt;Some 50-Digit Primes&lt;/H1&gt;

## &lt;%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %&gt;

```
<UL> <LI> <csajsp:simplePrime /> <LI> <csajsp:simplePrime /> <LI> <csajsp:simplePrime /> <LI> <csajsp:simplePrime /> </UL> </BODY> </HTML>
```