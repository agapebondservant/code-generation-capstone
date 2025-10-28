' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter Including Files and Applets in JSP Documents

<!-- image -->

## Topics in This Chapter

- · Including JSP files at the time the main page is translated into a servlet
- · Including HTML or plain text files at the time the client requests the page
- · Including applets that use the Java Plug-In

Home page for this book: http://www.coreservlets.com.

<!-- image -->

SP has three main capabilities for including external pieces into a JSP document. The include directive lets you reuse navigation bars, tables, and other elements  in  multiple  pages.  The  included  elements  can  contain  JSP code and thus are inserted into the page before the page is translated into a servlet. This capability is discussed in Section 12.1. J

Although including external pieces that use JSP is a powerful capability, other times you would rather sacrifice  some power for the convenience of being able to change the included documents without updating the main JSP page. For example, my family's church has a Web page on which it posts snow cancellation announcements. This page is updated by 6:30 AM on Sundays when there is a cancellation. It is hardly reasonable to expect the Web developer to post this update; he probably sleeps in and barely makes the late-late service.  Instead,  a  simple  plain  text  file  could  be  uploaded  with  the announcement, and the main page could use the jsp:include element to insert the announcement into the home page. This capability is discussed in Section 12.2.

Although this book is primarily about server-side Java, client-side Java in the form of Web-embedded applets continues to play a role, especially within fast corporate intranets. The jsp:plugin element is  used to insert applets that use the Java Plug-In into JSP pages. This capability is discussed in Section 12.3.