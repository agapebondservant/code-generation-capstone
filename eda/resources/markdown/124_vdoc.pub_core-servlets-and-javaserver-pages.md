' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter Integrating Servlets and JSP

<!-- image -->

## Topics in This Chapter

- · Obtaining a RequestDispatcher
- · Forwarding requests from servlets to dynamic resources
- · Forwarding requests from servlets to static resources
- · Using servlets to set up beans for use by JSP pages
- · An on-line travel agency combining servlets and JSP
- · Including JSP output in servlets
- · A servlet that shows the raw HTML output of JSP pages
- · Using jsp:forward to forward requests from JSP pages

Home page for this book: http://www.coreservlets.com.

Servlet and JSP training courses: http://courses.coreservlets.com.

<!-- image -->

ervlets are great when your application requires a lot of real programming  to  accomplish  its  task.  As  you've  seen  elsewhere  in  the  book, servlets can manipulate HTTP status codes and headers, use cookies, track  sessions,  save  information  between  requests,  compress  pages,  access databases,  generate  GIF  images  on-the-fly,  and  perform  many  other  tasks flexibly and efficiently. But, generating HTML with servlets can be tedious and can yield a result that is hard to modify. That's where JSP comes in; it lets you separate much of the presentation from the dynamic content. That way, you can write the HTML in the normal manner, even using HTML-specific tools and putting your Web content developers to work on your JSP documents. JSP expressions, scriptlets, and declarations let you insert simple Java code into the servlet that results from the JSP page, and directives let you control the overall layout of the page. For more complex requirements, you can wrap up Java code inside beans or define your own JSP tags. S

Great.  We  have  everything  we  need,  right?  Well,  no,  not  quite.  The assumption behind a JSP document is that it provides a single overall presentation. What if you want to give totally different results depending on the data that you receive? Beans and custom tags, although extremely powerful and flexible, don't overcome the limitation that the JSP page defines a relatively fixed top-level page appearance. The solution is to use both servlets and JavaServer Pages. If you have a complicated application that may require several substantially different presentations, a servlet can handle the initial request,