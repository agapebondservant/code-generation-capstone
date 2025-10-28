## 11.4 The session Attribute

tem guarantees that there will not be simultaneous access to the same servlet instance.  The  system  can  satisfy  this  guarantee  either  by  queuing  up  all requests and passing them to the same servlet instance or by creating a pool of instances, each of which handles a single request at a time.

You use &lt;%@ page isThreadSafe="false" %&gt; to indicate that your code is not thread safe and thus that the resulting servlet should implement SingleThreadModel .  (See  Section  2.6  (The  Servlet  Life  Cycle.)  The  default value  is true ,  which  means  that  the  system  assumes  you  made  your  code thread safe, and it can consequently use the higher-performance approach of multiple simultaneous threads accessing a single servlet instance. Be careful about  using isThreadSafe="false" when  your  servlet  has  instance  variables  (fields)  that  maintain  persistent  data.  In  particular,  note  that  servlet engines are permitted (but not required) to create multiple servlet instances in  such  a  case  and  thus  instance  variables  are  not  necessarily  unique.  You could still use static fields in such a case, however.

## 11.4 The session Attribute

The session attribute  controls  whether  or  not  the  page  participates  in HTTP sessions. Use of this attribute takes one of the following two forms:

```
<%@ page session="true" %> <%-- Default --%> <%@ page session="false" %>
```

A value of true (the default) indicates that the predefined variable session (of  type HttpSession ) should be bound to the existing session if one exists; otherwise, a new session should be created and bound to session . A value  of false means  that  no  sessions  will  be  used  automatically  and attempts to access the variable session will result in errors at the time the JSP page is translated into a servlet.

## 11.5 The buffer Attribute

The buffer attribute specifies the size of the buffer used by the out variable, which  is  of  type JspWriter (a  subclass  of PrintWriter ).  Use  of  this attribute takes one of two forms:

```
<%@ page buffer=" size kb" %> <%@ page buffer="none" %>
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.