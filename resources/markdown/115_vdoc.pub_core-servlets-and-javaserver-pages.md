' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter Creating Custom JSP Tag Libraries

<!-- image -->

## Topics in This Chapter

- · Tag handler classes
- · Tag library descriptor files
- · The JSP taglib directive
- · Simple tags
- · Tags that use attributes
- · Tags that use the body content between their start and end tags
- · Tags that modify their body content
- · Looping tags
- · Nested tags

Home page for this book: http://www.coreservlets.com.

Home page for sequel: http://www.moreservlets.com.

Servlet and JSP training courses: http://courses.coreservlets.com.

<!-- image -->

SP 1.1 introduced an extremely valuable new capability: the ability to define your own JSP tags. You define how the tag, its attributes, and its body are interpreted, then group your tags into collections called tag libraries that  can  be  used  in  any  number  of  JSP  files.  The  ability  to define tag libraries in this way permits Java developers to boil down complex server-side  behaviors  into  simple  and  easy-to-use  elements  that  content developers can easily incorporate into their JSP pages. J

Custom tags accomplish some of the same goals as beans that are accessed with jsp:useBean (see Chapter 13, 'Using JavaBeans with JSP')-encapsulating complex behaviors into simple and accessible forms. There are several differences,  however.  First,  beans  cannot  manipulate  JSP  content;  custom tags can. Second, complex operations can be reduced to a significantly simpler form with custom tags than with beans. Third, custom tags require quite a bit more work to set up than do beans. Fourth, beans are often defined in one servlet and then used in a different servlet or JSP page (see Chapter 15, 'Integrating  Servlets  and  JSP'),  whereas  custom  tags  usually  define  more self-contained behavior. Finally, custom tags are available only in JSP 1.1, but beans can be used in both JSP 1.0 and 1.1.

At the time this book went to press, no official release of Tomcat 3.0 properly supported custom tags, so the examples in this chapter use the beta version  of  Tomcat  3.1.  Other  than  the  support  for  custom  tags  and  a  few efficiency improvements and minor bug fixes, there is little difference in the