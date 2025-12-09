## Chapter 1 Overview of Servlets and JavaServer Pages

## Listing 1.1 A sample JSP page

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD><TITLE>Welcome to Our Store</TITLE></HEAD> <BODY> <H1>Welcome to Our Store</H1> <SMALL>Welcome, <!-- User name is "New User" for first-time visitors --> <%= Utils.getUserNameFromCookie(request) %> To access your account settings, click <A HREF="Account-Settings.html">here.</A></SMALL> <P> Regular HTML for all the rest of the on-line store's Web page. </BODY> </HTML>
```

## 1.4 The Advantages of JSP

JSP has a number of advantages over many of its alternatives. Here are a few of them.

## Versus Active Server Pages (ASP)

ASP is a competing technology from Microsoft. The advantages of JSP are twofold. First, the dynamic part is written in Java, not VBScript or another ASP-specific language, so it is more powerful and better suited to complex applications  that  require  reusable  components.  Second,  JSP  is  portable  to other operating  systems and  Web  servers;  you  aren't  locked  into  Windows NT/2000 and IIS. You could make the same argument when comparing JSP to  ColdFusion;  with JSP  you  can  use  Java  and  are  not  tied  to  a  particular server product.

## Versus PHP

PHP is a free, open-source HTML-embedded scripting language that is somewhat similar to both ASP and JSP . The advantage of JSP is that the dynamic part is written in Java, which you probably already know, which already has an

## 1.4 The Advantages of JSP

extensive API for networking, database access, distributed objects, and the like, whereas PHP requires learning an entirely new language.

## Versus Pure Servlets

JSP  doesn't  provide  any  capabilities  that  couldn't  in  principle  be  accomplished  with  a  servlet.  In  fact,  JSP  documents  are  automatically  translated into servlets  behind the scenes. But it is more convenient to write (and to modify!) regular HTML than to have a zillion println statements that generate the HTML. Plus, by separating the presentation from the content, you can put different people on different tasks: your Web page design experts can build the HTML using familiar tools and leave places for your servlet programmers to insert the dynamic content.

## Versus Server-Side Includes (SSI)

SSI is a widely supported technology for inserting externally defined pieces into a static Web page. JSP is better because you have a richer set of tools for building that external piece and have more options regarding the stage of the HTTP response  at  which  the  piece  actually  gets  inserted.  Besides,  SSI  is really  intended only for simple inclusions, not for 'real' programs that use form data, make database connections, and the like.

## Versus JavaScript

JavaScript, which is completely distinct from the Java programming language, is normally used to generate HTML dynamically on the client , building parts of the Web page as the browser loads the document. This is a useful capability but only handles situations where the dynamic information is based on the client's environment. With the exception of cookies, the HTTP request data is not available to client-side JavaScript routines. And, since JavaScript lacks routines  for  network  programming,  JavaScript  code  on  the  client  cannot access server-side resources like databases, catalogs, pricing information, and the like. JavaScript can also be used on the server, most notably on Netscape servers and as a scripting language for IIS. Java is far more powerful, flexible, reliable, and portable.