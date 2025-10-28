## Appendix

## Servlet and JSP Quick Reference 518

A.1 Overview of Servlets and JavaServer Pages 519

Advantages of Servlets 519

Advantages of JSP 519

Free Servlet and JSP Software 519

Documentation 520

Servlet Compilation: CLASSPATH Entries 520

Tomcat 3.0 Standard Directories 520

Tomcat 3.1 Standard Directories 520

JSWDK 1.0.1 Standard Directories 520

Java Web Server 2.0 Standard Directories

521

## A.2 First Servlets 521

Simple Servlet 521

Installing Servlets 521

Invoking Servlets 521

Servlet Life Cycle 522

A.3 Handling the Client Request: Form Data 523

Reading Parameters 523

Example Servlet 523

Example Form 524

Filtering HTML-Specific Characters 524

A.4

Handling the Client Request: HTTP Request Headers

524

Methods That Read Request Headers 524

Other Request Information 525

Common HTTP 1.1 Request Headers 525

A.5 Accessing the Standard CGI Variables 526

Capabilities Not Discussed Elsewhere 526

Servlet Equivalent of CGI Variables 526

A.6

Generating the Server Response: HTTP Status Codes

527

Format of an HTTP Response 527

Methods That Set Status Codes

527

Status Code Categories

527

Common HTTP 1.1 Status Codes 527

A.7

Generating the Server Response: HTTP Response Headers

528

Setting Arbitrary Headers 528

## Contents

## Contents

|           | Setting Common Headers 528                                                                                                                                                                                                                                                                                                  |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A.8 A.9   | Handling Cookies 530 Typical Uses of Cookies 530 Problems with Cookies 530 General Usage 530 Cookie Methods 530 Session Tracking 531 Looking Up Session Information: getValue 531 Associating Information with a Session: putValue 531 HttpSession Methods 532                                                              |
| A.10 A.11 | JSP Scripting Elements 533 Types of Scripting Elements 533 Template Text 533 Predefined Variables 533 The JSP page Directive: Structuring Generated Servlets 534 The import Attribute 534 The contentType Attribute 534 Example of Using contentType 534 Example of Using setContentType 535 The isThreadSafe Attribute 535 |
|           | The session Attribute 536 The buffer Attribute 536 The autoflush Attribute 536 The extends Attribute 536 The info Attribute 536                                                                                                                                                                                             |
| A.12      | The errorPage Attribute 536 The isErrorPage Attribute 536 The language Attribute 536 XML Syntax 537 Including Files and Applets in JSP Documents 537 Including Files at Page Translation Time 537                                                                                                                           |
|           | Including Files at Request Time 537 Applets for the Java Plug-In: Simple Case 537 Attributes of jsp:plugin 537                                                                                                                                                                                                              |

Contents

| Parameters in HTML: jsp:param 538 Alternative Text 538                                                                                                                                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A.13 Using JavaBeans with JSP 539 Basic Requirements for Class to be a Bean 539                                                                                                                                                                                                                                                                           |
| A.15 Integrating Servlets and JSP 542 Big Picture 542 Request Forwarding Syntax 543 Forwarding to Regular HTML Pages 543 Setting Up Globally Shared Beans 543 Setting Up Session Beans 543 Interpreting Relative URLs in the Destination Page 543 Getting a RequestDispatcher by Alternative Means (2.2 Only) 543 Including Static or Dynamic Content 544 |
| Forwarding Requests from JSP Pages 544                                                                                                                                                                                                                                                                                                                    |
| A.16 Using HTML Forms 544 The FORM Element 544 Textfields 544 Password Fields 544 Text Areas 545 Submit Buttons 545 Alternative Push Buttons 545 Reset Buttons 545                                                                                                                                                                                        |

xvii

' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## xviii Contents

JavaScript Buttons

546

Alternative JavaScript Buttons 546

Check Boxes 546

Radio Buttons 546

Combo Boxes 546

File Upload Controls

547

Server-Side Image Maps 547

Hidden Fields 547

Internet Explorer Features 547

A.17 Using Applets As Servlet Front Ends 547

Sending Data with GET and Displaying the Resultant Page

547

Sending Data with GET and Processing the Results Directly

(HTTP Tunneling) 548

Sending Serialized Data: The Applet Code 549

Sending Serialized Data: The Servlet Code 549

Sending Data by POST and Processing the Results Directly (HTTP Tunneling) 550

Bypassing the HTTP Server

551

A.18 JDBC and Database Connection Pooling 552

Basic Steps in Using JDBC 552

Database Utilities 553

Prepared Statements (Precompiled Queries) 553

Steps in Implementing Connection Pooling 554

Index

557

Chapter

Many people have helped me out with this book. Without their assistance, I would still be on the third chapter. John Guthrie, Amy Karlson, Rich Slywczak, and Kim Topley provided valuable technical feedback on virtually every chapter. Others pointing out errors and providing useful suggestions include Don Aldridge, Camille Bell, Ben Benokraitis, Larry Brown, Carl Burnham, Andrew Burton, Rick Cannon, Kevin Cropper, Chip Downs, Frank Erickson, Payam Fard, Daniel Goldman, Rob Gordon, Andy Gravatt, Jeff Hall, Russell Holley,  David  Hopkins,  Lis  Immer,  Herman  Ip,  Truong  Le,  Frank  Lewis, Tanner Lovelace, Margaret Lyell, Paul McNamee, Mike Oliver, Barb Ridenour, Himanso Sahni, Bob Samson, Ron Tosh, Tsung-Wen Tsai, Peggy Sue Vickers, and Maureen Knox Yencha. Hopefully I learned from their advice. Mary Lou 'Eagle Eye' Nohr spotted my errant commas, awkward sentences, typographical  errors,  and  grammatical  inconsistencies.  She  improved  the result  immensely.  Joanne  Anzalone  produced  the  final  version;  she  did  a great job despite my many last-minute changes. Ralph Semmel provided a supportive work environment and a flexible schedule, not to mention interesting projects on which to put servlets and JSP to work. Greg Doench of Prentice Hall believed in the concept from the beginning and encouraged me to write the book. Rachel Borden got Sun Microsystems Press to believe in it also. Thanks to all.

Most of all, thanks to B.J., Lindsay, and Nathan for their patience with my funny schedule and my hogging the computer when they wanted to work or play on it. God has blessed me with a great family.