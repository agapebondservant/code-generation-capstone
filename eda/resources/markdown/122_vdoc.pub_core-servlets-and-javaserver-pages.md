## Chapter 14 Creating Custom JSP Tag Libraries

Figure 14-7 The csajsp:filter element lets you insert text without worrying about it containing special HTML characters.

<!-- image -->

## 14.7 Including or Manipulating the Tag Body Multiple Times

Rather than just including or processing the body of the tag a single time, you sometimes  want  to  do  so  more  than  once.  The  ability  to  support  multiple body inclusion lets you define a variety of iteration tags that repeat JSP fragments  a  variable  number  of  times,  repeat  them  until  a  certain  condition occurs, and so forth. This section shows you how to build such tags.

## The Tag Handler Class

Tags that process the body content multiple times should start by extending BodyTagSupport and  implementing doStartTag , doEndTag ,  and,  most importantly, doAfterBody as before. The difference lies in the return value of doAfterBody .  If  this  method  returns EVAL\_BODY\_TAG ,  the  tag  body  is evaluated again, resulting in a new call to doAfterBody . This process continues until doAfterBody returns SKIP\_BODY .

## 14.7 Including or Manipulating the Tag Body Multiple Times

Listing 14.19 defines a tag that repeats the body content the number of times specified by the reps attribute. Since the body content can contain JSP (which gets made into servlet code at page translation time but invoked at request time), each repetition does not necessarily result in the same output to the client.

## Listing 14.19

```
RepeatTag.java
```

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; /** A tag that repeats the body the specified *  number of times. */ public class RepeatTag extends BodyTagSupport { private int reps; public void setReps(String repeats) { try { reps = Integer.parseInt(repeats); } catch(NumberFormatException nfe) { reps = 1; } } public int doAfterBody() { if (reps-- >= 1) { BodyContent body = getBodyContent(); try { JspWriter out = body.getEnclosingWriter(); out.println(body.getString()); body.clearBody(); // Clear for next evaluation } catch(IOException ioe) { System.out.println("Error in RepeatTag: " + ioe); } return(EVAL_BODY_TAG); } else { return(SKIP_BODY); } } }
```

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

## The Tag Library Descriptor File

Listing 14.20 shows a TLD file that gives the name csajsp:repeat to  the tag just defined. To accommodate request time values in the reps attribute, the file uses an rtexprvalue element (enclosing a value of true ) within the attribute element.

## Listing 14.20 csajsp-taglib.tld

```
<?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" --> <tlibversion>1.0</tlibversion> <jspversion>1.1</jspversion> <shortname>csajsp</shortname> <urn></urn> <info> A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. </info> <!-- Other tags defined earlier... --> <tag> <name>repeat</name> <tagclass>coreservlets.tags.RepeatTag</tagclass> <info>Repeats body the specified number of times.</info> <bodycontent>JSP</bodycontent> <attribute> <name>reps</name> <required>true</required> <!-- rtexprvalue indicates whether attribute can be a JSP expression. --> <rtexprvalue>true</rtexprvalue> </attribute> </tag> </taglib>
```