## Chapter 14 Creating Custom JSP Tag Libraries

behavior of the two versions. However, Tomcat 3.1 uses a slightly different directory structure, as summarized Table 14.1.

Table 14.1  Standard T omcat Directories

|                                                                  | Tomcat 3.0                             | Tomcat 3.1                                 |
|------------------------------------------------------------------|----------------------------------------|--------------------------------------------|
| Location of startup and shutdown Scripts                         | install_dir                            | install_dir /bin                           |
| Standard Top-Level Directory for Servlets and Supporting Classes | install_dir /webpages/ WEB-INF/classes | install_dir /webapps/ ROOT/WEB-INF/classes |
| Standard Top-Level Directory for HTML and JSP Files              | install_dir /webpages                  | install_dir /webapps/ ROOT                 |

## 14.1 The Components That Make Up a Tag Library

In order to use custom JSP tags, you need to define three separate components:  the  tag  handler  class  that  defines  the  tag's  behavior,  the  tag  library descriptor  file  that  maps  the  XML  element names to  the tag implementations, and the JSP file that uses the tag library. The rest of this section gives an  overview  of  each  of  these  components  and  the  following  sections  give details on how to build these components for various different styles of tags.

## The Tag Handler Class

When defining a new tag, your first task is to define a Java class that tells the system  what  to  do  when  it  sees  the  tag.  This  class  must  implement  the javax.servlet.jsp.tagext.Tag interface. This is usually accomplished by extending  the TagSupport or BodyTagSupport class.  Listing  14.1  is  an example of a simple tag that just inserts ' Custom tag example (coreservlets.tags.ExampleTag) '  into  the  JSP  page  wherever  the  corresponding tag is used. Don't worry about understanding the exact behavior of this class; that will be made clear in the next section. For now, just note that it is in the

## 14.1 The Components That Make Up a Tag Library

coreservlets.tags class and is called ExampleTag . Thus, with Tomcat 3.1, the class file would be in install\_dir /webapps/ROOT/WEB-INF/classes/coreservlets/tags/ExampleTag.class .

## Listing 14.1 ExampleTag.java

```
package coreservlets.tags; import javax.servlet.jsp.*; import javax.servlet.jsp.tagext.*; import java.io.*; /** Very simple JSP tag that just inserts a string *  ("Custom tag example...") into the output. *  The actual name of the tag is not defined here; *  that is given by the Tag Library Descriptor (TLD) *  file that is referenced by the taglib directive *  in the JSP file. */ System.out.println("Error in ExampleTag: " + ioe);
```

```
public class ExampleTag extends TagSupport { public int doStartTag() { try { JspWriter out = pageContext.getOut(); out.print("Custom tag example " + "(coreservlets.tags.ExampleTag)"); } catch(IOException ioe) { } return(SKIP_BODY); } }
```

## The Tag Library Descriptor File

Once you have defined a tag handler, your next task is to identify the class to the server and to associate it with a particular XML tag name. This task is accomplished by means of a tag library descriptor file (in XML format) like the one shown in Listing 14.2. This file contains some fixed information, an arbitrary short name for your library, a short description, and a series of tag descriptions. The nonbold part of the listing is the same in virtually all tag library descriptors and can be copied verbatim from the source code archive at http://www.coreservlets.com/ or from the Tomcat 3.1 standard examples ( install\_dir /webapps/examples/WEB-INF/jsp ).

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 14 Creating Custom JSP Tag Libraries

The format of tag descriptions will be described in later sections. For now, just note that the tag element defines the main name of the tag (really tag suffix,  as  will  be  seen  shortly)  and  identifies the  class that  handles  the  tag. Since the tag handler class is in the coreservlets.tags package, the fully qualified  class  name  of coreservlets.tags.ExampleTag is  used.  Note that this  is  a  class  name,  not  a  URL  or  relative  path  name.  The  class  can be installed  anywhere  on  the server that  beans  or  other supporting classes can be put. With Tomcat 3.1, the standard base location is install\_dir /webapps/ROOT/WEB-INF/classes ,  so ExampleTag would  be  in install\_dir /webapps/ROOT/WEB-INF/classes/coreservlets/tags .  Although it  is  always a good idea to put your servlet classes in packages, a surprising feature of Tomcat 3.1 is that tag handlers are required to be in packages.

## Listing 14.2 csajsp-taglib.tld

```
<?xml version="1.0" encoding="ISO-8859-1" ?> <!DOCTYPE taglib PUBLIC "-//Sun Microsystems, Inc.//DTD JSP Tag Library 1.1//EN" "http://java.sun.com/j2ee/dtds/web-jsptaglibrary_1_1.dtd"> <!-- a tag library descriptor --> <taglib> <!-- after this the default space is "http://java.sun.com/j2ee/dtds/jsptaglibrary_1_2.dtd" --> <tlibversion>1.0</tlibversion> <jspversion>1.1</jspversion> <shortname>csajsp</shortname> <urn></urn> <info> A tag library from Core Servlets and JavaServer Pages, http://www.coreservlets.com/. </info> <tag> <name>example</name> <tagclass>coreservlets.tags.ExampleTag</tagclass> <info>Simplest example: inserts one line of output</info> <bodycontent>EMPTY</bodycontent> </tag> <!-- Other tags defined later... --> </taglib>
```

## The JSP File

Once you have a tag handler implementation and a tag library description, you are ready to write a JSP file that makes use of the tag. Listing 14.3 gives an example. Somewhere before the first use of your tag, you need to use the taglib directive. This directive has the following form:

&lt;%@ taglib uri="..." prefix="..." %&gt;

The required uri attribute  can  be  either  an  absolute  or  relative  URL referring to a tag library descriptor file like the one shown in Listing 14.2. To complicate matters a little, however, Tomcat 3.1 uses a web.xml file that maps an absolute URL for a tag library descriptor to a file on the local system.  I  don't  recommend  that  you  use  this  approach,  but  you  should  be aware  of  it  in  case  you  look  at  the  Apache  examples  and  wonder  why  it works when they specify a nonexistent  URL for the uri attribute  of  the taglib directive.

The prefix attribute, also required, specifies a prefix that will be used in front of whatever tag name the tag library descriptor defined. For example, if the TLD file defines a tag named tag1 and the prefix attribute has a value of test , the actual tag name would be test:tag1 . This tag could be used in either of the following two ways, depending on whether it is defined to be a container that makes use of the tag body:

&lt;test:tag1&gt; Arbitrary JSP &lt;/test:tag1&gt;

or just

&lt;test:tag1 /&gt;

To illustrate, the descriptor file of Listing 14.2 is called csajsp-taglib.tld , and resides in the same directory as the JSP file shown in Listing 14.3. Thus, the taglib directive in the JSP file uses a simple relative URL giving just the filename, as shown below.

&lt;%@ taglib uri="csajsp-taglib.tld" prefix="csajsp" %&gt;

Furthermore, since the prefix attribute is csajsp (for Core Servlets and JavaServer Pages ), the rest of the JSP page uses csajsp:example to refer to the example tag  defined  in  the  descriptor  file.  Figure  14-1  shows  the result.

## 14.1 The Components That Make Up a Tag Library