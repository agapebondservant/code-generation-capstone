## The JSP File

Listing 14.21 shows a JSP document that creates a numbered list of prime numbers. The number of primes in the list is taken from the request time repeats parameter. Figure 14-8 shows one possible result.

## Listing 14.21 RepeatExample.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Some 40-Digit Primes</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css">
```

&lt;/HEAD&gt;

&lt;BODY&gt;

&lt;H1&gt;Some 40-Digit Primes&lt;/H1&gt; Each entry in the following list is the first prime number higher than a randomly selected 40-digit number.

## &lt;%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %&gt;

&lt;OL&gt;

&lt;!-- Repeats N times. A null reps value means repeat once. --&gt;

&lt;csajsp:repeat reps='&lt;%= request.getParameter("repeats") %&gt;'&gt;

&lt;LI&gt;&lt;csajsp:prime length="40" /&gt;

&lt;/csajsp:repeat&gt;

&lt;/OL&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## 14.8 Using Nested Tags

Although Listing 14.21 places the csajsp:prime element within the csajsp:repeat element, the two elements are independent of each other. The first generates a prime number regardless of where it is used, and the second repeats the enclosed content regardless of whether that content uses a csajsp:prime element.

Some tags, however, depend on a particular nesting. For example, in standard HTML, the TD and TH elements can only appear within TR , which in turn

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 14.8 Using Nested Tags

## Chapter 14 Creating Custom JSP Tag Libraries

Figure 14-8 Result of RepeatExample.jsp when accessed with a repeats parameter of 20.

<!-- image -->

can only appear within TABLE . The color and alignment settings of TABLE are inherited by TR ,  and  the values of TR affect  how TD and TH behave.  So,  the nested elements cannot act in isolation even when nested properly. Similarly, the tag library descriptor file makes use of a number of elements like taglib , tag , attribute and required where a strict nesting hierarchy is imposed.

This section shows you how to define tags that depend on a particular nesting order and where the behavior of certain tags depends on values supplied by earlier ones.

## The Tag Handler Classes

Class definitions for nested tags can extend either TagSupport or BodyTagSupport , depending on whether they need to manipulate their body content (these extend BodyTagSupport ) or, more commonly, just ignore it or include it verbatim (these extend TagSupport ).

## 14.8 Using Nested Tags

There are two key new approaches for nested tags, however. First, nested tags  can  use findAncestorWithClass to  find  the  tag  in  which  they  are nested. This method takes a reference to the current class (e.g., this ) and the Class object of the enclosing class (e.g., EnclosingTag.class ) as arguments. If no enclosing class is found, the method in the nested class can throw a JspTagException that reports the problem. Second, if one tag wants to store data that a later tag will use, it can place that data in the instance of the enclosing tag. The definition of the enclosing tag should provide methods for storing and accessing this data. Listing 14.22 outlines this approach.

## Listing 14.22 Template for Nested Tags

```
public class OuterTag extends TagSupport { public void setSomeValue(SomeClass arg) { ... } public SomeClass getSomeValue() { ... } } public class FirstInnerTag extends BodyTagSupport { public int doStartTag() throws JspTagException { OuterTag parent = (OuterTag)findAncestorWithClass(this, OuterTag.class); if (parent == null) { throw new JspTagException("nesting error"); } else { parent.setSomeValue(...); } return(EVAL_BODY_TAG); } ... } public class SecondInnerTag extends BodyTagSupport { public int doStartTag() throws JspTagException { OuterTag parent = (OuterTag)findAncestorWithClass(this, OuterTag.class); if (parent == null) { throw new JspTagException("nesting error"); } else { SomeClass value = parent.getSomeValue(); doSomethingWith(value); } return(EVAL_BODY_TAG); } ... }
```

## Chapter 14 Creating Custom JSP Tag Libraries

Now, suppose that we want to define a set of tags that would be used like this:

```
<csajsp:if> <csajsp:condition><%= someExpression %></csajsp:condition> <csajsp:then>JSP to include if condition is true</csajsp:then> <csajsp:else>JSP to include if condition is false</csajsp:else> </csajsp:if>
```

To accomplish this task, the first step is to define an IfTag class to handle the csajsp:if tag. This handler should have methods to specify and check whether the condition is true or false ( setCondition and getCondition ) as well as methods to designate and check if the condition has ever been explicitly set ( setHasCondition and getHasCondition ), since we want to disallow csajsp:if tags that contain no csajsp:condition entry. Listing 14.23 shows the code for IfTag .

The second step is to define a tag handler for csajsp:condition . This class,  called IfConditionTag ,  defines  a doStartTag method that merely checks if the tag appears within IfTag . It returns EVAL\_BODY\_TAG if so and throws  an  exception  if  not.  The  handler's doAfterBody method  looks  up the body content ( getBodyContent ), converts it to a String ( getString ), and compares that to "true" . This approach means that an explicit value of true can  be  substituted  for  a JSP  expression  like &lt;%= expression %&gt; if, during initial page development, you want to temporarily designate that the then portion  should  always  be  used.  Using  a  comparison  to "true" also means that any other value will be considered 'false.' Once this comparison is performed, the result is stored in the enclosing tag by means of the setCondition method of IfTag .  The code for IfConditionTag is  shown in Listing 14.24.

The third  step  is  to  define  a  class  to  handle  the csajsp:then tag.  The doStartTag method  of  this  class  verifies  that  it  is  inside IfTag and  also checks that an explicit condition has been set (i.e., that the IfConditionTag has already appeared within the IfTag ).  The doAfterBody method checks for the condition in the IfTag class, and, if it is true, looks up the body content and prints it. Listing 14.25 shows the code.

The  final  step  in  defining  tag  handlers  is  to  define  a  class  for csajsp:else .  This class is very similar to the one to handle the then part of the tag, except that this handler only prints the tag body from doAfterBody if the condition from the surrounding IfTag is false. The code is shown in Listing 14.26.

```
Listing 14.23 IfTag.java
```

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import javax.servlet.*; /** A tag that acts like an if/then/else. */ public class IfTag extends TagSupport { private boolean condition; private boolean hasCondition = false; public void setCondition(boolean condition) { this.condition = condition; hasCondition = true; } public boolean getCondition() { return(condition); } public void setHasCondition(boolean flag) { this.hasCondition = flag; } /** Has the condition field been explicitly set? */ public boolean hasCondition() { return(hasCondition); } public int doStartTag() { return(EVAL_BODY_INCLUDE); } }
```

## 14.8 Using Nested Tags

<!-- image -->

## 346

## Chapter 14 Creating Custom JSP Tag Libraries

```
Listing 14.24 IfConditionTag.java throw new JspTagException("condition not inside if");
```

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import javax.servlet.*; /** The condition part of an if tag. */ public class IfConditionTag extends BodyTagSupport { public int doStartTag() throws JspTagException { IfTag parent = (IfTag)findAncestorWithClass(this, IfTag.class); if (parent == null) { } return(EVAL_BODY_TAG); } public int doAfterBody() { IfTag parent = (IfTag)findAncestorWithClass(this, IfTag.class); String bodyString = getBodyContent().getString(); if (bodyString.trim().equals("true")) { parent.setCondition(true); } else { parent.setCondition(false); } return(SKIP_BODY); } }
```

```
Listing 14.25 IfThenTag.java
```

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import javax.servlet.*; /** The then part of an if tag. */ public class IfThenTag extends BodyTagSupport { public int doStartTag() throws JspTagException { IfTag parent = (IfTag)findAncestorWithClass(this, IfTag.class); if (parent == null) { throw new JspTagException("then not inside if"); } else if (!parent.hasCondition()) { String warning = "condition tag must come before then tag"; throw new JspTagException(warning); } return(EVAL_BODY_TAG); } public int doAfterBody() { IfTag parent = (IfTag)findAncestorWithClass(this, IfTag.class); if (parent.getCondition()) { try { BodyContent body = getBodyContent(); JspWriter out = body.getEnclosingWriter(); out.print(body.getString()); } catch(IOException ioe) { System.out.println("Error in IfThenTag: " + ioe); } } return(SKIP_BODY); } }
```

## 14.8 Using Nested Tags

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

```
Listing 14.26 IfElseTag.java package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; import javax.servlet.*; /** The else part of an if tag. */ public class IfElseTag extends BodyTagSupport { public int doStartTag() throws JspTagException { IfTag parent = (IfTag)findAncestorWithClass(this, IfTag.class); if (parent == null) { throw new JspTagException("else not inside if"); } else if (!parent.hasCondition()) { String warning = "condition tag must come before else tag"; throw new JspTagException(warning); } return(EVAL_BODY_TAG); } public int doAfterBody() { IfTag parent = (IfTag)findAncestorWithClass(this, IfTag.class); if (!parent.getCondition()) { try { BodyContent body = getBodyContent(); JspWriter out = body.getEnclosingWriter(); out.print(body.getString()); } catch(IOException ioe) { System.out.println("Error in IfElseTag: " + ioe); } } return(SKIP_BODY); } }
```

## The Tag Library Descriptor File

Even though there is an explicit required nesting structure for the tags just defined, the tags must be declared separately in the TLD file. This means that nesting validation is performed only at request time, not at page transla-

## 14.8 Using Nested Tags

tion time. In principle, you could instruct the system to do some validation at page translation time by using a TagExtraInfo class. This class has a getVariableInfo method  that you  can  use  to  check  that  attributes  exist  and where they are used. Once you have defined a subclass of TagExtraInfo , you associate it with your tag in the tag library descriptor file by means of the teiclass element, which is used just like tagclass .  In  practice, however, TagExtraInfo is poorly documented and cumbersome to use.

## Listing 14.27 csajsp-taglib.tld

```
<?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" --> <tlibversion>1.0</tlibversion> <jspversion>1.1</jspversion> <shortname>csajsp</shortname> <urn></urn> <info> A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. </info> <!-- Other tags defined earlier... --> <tag> <name>if</name> <tagclass>coreservlets.tags.IfTag</tagclass> <info>if/condition/then/else tag.</info> <bodycontent>JSP</bodycontent> </tag> <tag> <name>condition</name> <tagclass>coreservlets.tags.IfConditionTag</tagclass> <info>condition part of if/condition/then/else tag.</info> <bodycontent>JSP</bodycontent> </tag>
```

## Chapter 14 Creating Custom JSP Tag Libraries

## &lt;tag&gt; &lt;name&gt;then&lt;/name&gt; &lt;tagclass&gt;coreservlets.tags.IfThenTag&lt;/tagclass&gt; &lt;info&gt;then part of if/condition/then/else tag.&lt;/info&gt; &lt;bodycontent&gt;JSP&lt;/bodycontent&gt; &lt;/tag&gt; &lt;tag&gt; &lt;name&gt;else&lt;/name&gt; &lt;tagclass&gt;coreservlets.tags.IfElseTag&lt;/tagclass&gt; &lt;info&gt;else part of if/condition/then/else tag.&lt;/info&gt; &lt;bodycontent&gt;JSP&lt;/bodycontent&gt; &lt;/tag&gt; &lt;/taglib&gt; Listing 14.27 csajsp-taglib.tld (continued)

## The JSP File

Listing 14.28 shows a page that uses the csajsp:if tag three different ways. In the first instance, a value of true is  hardcoded for the condition. In the second instance, a parameter from the HTTP request is used for the condition, and in the third case, a random number is generated and compared to a fixed cutoff. Figure 14-9 shows a typical result.

## Listing 14.28 IfExample.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>If Tag Example</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <H1>If Tag Example</H1>
```

&lt;%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %&gt;

## &lt;csajsp:if&gt;

&lt;csajsp:condition&gt;true&lt;/csajsp:condition&gt;

&lt;csajsp:then&gt;Condition was true&lt;/csajsp:then&gt;

&lt;csajsp:else&gt;Condition was false&lt;/csajsp:else&gt;

&lt;/csajsp:if&gt;

## Listing 14.28 IfExample.jsp (continued)

## &lt;P&gt;

&lt;csajsp:if&gt;

&lt;csajsp:condition&gt;&lt;%= request.isSecure() %&gt;&lt;/csajsp:condition&gt; &lt;csajsp:then&gt;Request is using SSL (https)&lt;/csajsp:then&gt; &lt;csajsp:else&gt;Request is not using SSL&lt;/csajsp:else&gt;

&lt;/csajsp:if&gt;

&lt;P&gt;

Some coin tosses:&lt;BR&gt;

&lt;csajsp:repeat reps="20"&gt;

&lt;csajsp:if&gt;

&lt;csajsp:condition&gt;

&lt;%= Math.random() &gt; 0.5 %&gt;

&lt;/csajsp:condition&gt;

&lt;csajsp:then&gt;&lt;B&gt;Heads&lt;/B&gt;&lt;BR&gt;&lt;/csajsp:then&gt;

&lt;csajsp:else&gt;&lt;B&gt;Tails&lt;/B&gt;&lt;BR&gt;&lt;/csajsp:else&gt;

&lt;/csajsp:if&gt;

&lt;/csajsp:repeat&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

<!-- image -->

Figure 14-9 Result of

IfExample.jsp .

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 14.8 Using Nested Tags