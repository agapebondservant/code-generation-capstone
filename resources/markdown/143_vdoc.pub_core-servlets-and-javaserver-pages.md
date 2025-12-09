' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter Using Applets As Servlet Front Ends

<!-- image -->

## Topics in This Chapter

- · Sending GET data and having the browser display the results
- · Sending GET data and processing the results within the applet (HTTP tunneling)
- · Using object serialization to exchange high-level data structures between applets and servlets
- · Sending POST data and processing the results within the applet
- · Bypassing the HTTP server altogether

Home page for this book: http://www.coreservlets.com.

Home page for sequel: http://www.moreservlets.com. Servlet and JSP training courses: http://courses.coreservlets.com.

<!-- image -->

TML forms, discussed in Chapter 16, provide a simple but limited way of collecting user input and transmitting it to a servlet or CGI program. Occasionally, however, a more sophisticated user interface is required. Applets give you more control over the size, color, and font of the GUI controls; provide more built-in capability (sliders, line drawing, pop-up windows, and the like); let you track mouse and keyboard events; support the development of custom input forms (dials, thermometers, draggable icons, and  so  forth);  and  let  you  send  a  single  user  submission  to  multiple server-side  programs.  This  extra  capability  comes  at  a  cost,  however,  as  it tends to require much more effort to design an interface in the Java programming language than it does using HTML forms, particularly if the interface contains a lot of formatted text. So, the choice between HTML forms and applets will depend upon the application. H

With HTML forms, GET and POST requests  are  handled almost exactly the  same  way.  All  the  input  elements  are  identical;  only  the METHOD attribute  of  the FORM element  needs  to  change.  With  applets,  however, there are three distinct approaches. In the first approach, covered in Section 17.1, the applet imitates a GET -based HTML form, with GET data being transmitted and the resultant page being displayed by the browser. Section 17.2 (A Multisystem Search Engine Front End) gives an example. In the second approach, covered in Section 17.3, the applet sends GET data  to a servlet and then processes the results itself. Section 17.4 (A Query Viewer