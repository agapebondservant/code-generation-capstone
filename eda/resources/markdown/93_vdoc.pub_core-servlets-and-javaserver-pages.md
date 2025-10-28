Chapter 11 The JSP page Directive: Structuring Generated Servlets

## 11.3 The isThreadSafe Attribute

The isThreadSafe attribute controls whether or not the servlet that results from the JSP page will implement the SingleThreadModel interface. Use of the isThreadSafe attribute takes one of the following two forms:

```
<%@ page isThreadSafe="true" %> <%!-- Default --%> <%@ page isThreadSafe="false" %>
```

With  normal  servlets,  simultaneous  user  requests  result  in  multiple threads  concurrently  accessing  the service method  of  the  same  servlet instance. This behavior assumes that the servlet is thread safe ; that is, that the servlet synchronizes access to data in its fields so that inconsistent values will not result from an unexpected ordering of thread execution. In some cases (such as page access counts), you may not care if two visitors occasionally get the same value, but in other cases  (such as user IDs), identical values  can spell disaster.  For  example, the following snippet is not thread safe since a thread could be preempted after reading idNum but before updating it, yielding two users with the same user ID.

```
<%! private int idNum = 0; %> <% String userID = "userID" + idNum; out.println("Your ID is " + userID + "."); idNum = idNum + 1; %>
```

The code should have used a synchronized block. This construct is written synchronized(someObject) { ... }

and means that once a thread enters the block of code, no other thread can enter the same block (or any other block marked with the same object reference) until the first thread exits. So, the previous snippet should have been written in the following manner.

```
<%! private int idNum = 0; %> <% synchronized(this) { String userID = "userID" + idNum; out.println("Your ID is " + userID + "."); idNum = idNum + 1; } %>
```

That's the normal servlet behavior: multiple simultaneous requests are dispatched to multiple threads concurrently accessing the same servlet instance. However, if a servlet implements the SingleThreadModel interface, the sys-