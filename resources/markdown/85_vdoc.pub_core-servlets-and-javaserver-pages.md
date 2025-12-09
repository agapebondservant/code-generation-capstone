## 10.1 Scripting Elements

Aside  from  the  regular  HTML,  there  are  three  main  types  of  JSP  constructs that you embed in a page: scripting elements , directives , and actions . Scripting  elements  let  you  specify  Java  code  that  will  become  part  of  the resultant servlet, directives let you control the overall structure of the servlet, and actions let you specify existing components that should be used and otherwise control the behavior of the JSP engine. To simplify the scripting elements, you have access to a number of predefined variables, such as request in the code snippet just shown (see Section 10.5 for more details). Scripting elements are covered in this chapter, and directives and actions are explained in the following chapters. You can also refer to Appendix  (Servlet and JSP Quick Reference) for a thumbnail guide summarizing JSP syntax.

This book covers versions 1.0 and 1.1 of the JavaServer Pages specification. JSP  changed  dramatically  from  version  0.92  to  version  1.0,  and  although these changes are very much for the better, you should note that newer JSP pages are almost totally incompatible  with the  early 0.92  JSP  engines, and older JSP pages are equally incompatible with 1.0 JSP engines. The changes from version 1.0 to 1.1 are much less dramatic: the main additions in version 1.1 are the ability to portably define new tags and the use of the servlet 2.2 specification for the underlying servlets. JSP 1.1 pages that do not use custom tags  or  explicitly  call  2.2-specific  statements  are  compatible  with  JSP  1.0 engines,  and  JSP  1.0  pages  are  totally  upward  compatible  with  JSP  1.1 engines.

## 10.1 Scripting Elements

JSP scripting elements let you insert code into the servlet that will be generated from the JSP page. There are three forms:

- 1. Expressions of the form &lt;%= expression %&gt; , which are evaluated and inserted into the servlet's output
- 2. Scriptlets of the form &lt;% code %&gt; , which are inserted into the servlet's \_jspService method (called by service )
- 3. Declarations of the form &lt;%! code %&gt; , which are inserted into the body of the servlet class, outside of any existing methods

Each of these scripting elements is described in more detail in the following sections.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.