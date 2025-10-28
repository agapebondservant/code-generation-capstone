## Chapter 13 Using JavaBeans with JSP

change from English units to metric units internally, but still have getSpeedInMPH and getSpeedInKPH methods), and automatically perform side effects when values change (e.g., update the user interface when setPosition is called).

- 3. Persistent values should be accessed through methods called get Xxx and set Xxx . For example, if your Car class stores the current number of passengers, you might have methods named getNumPassengers (which takes no arguments and returns an int ) and setNumPassengers (which takes an int and has a void return type). In such a case, the Car class is said to have a property named numPassengers (notice the lowercase n in the property name, but the uppercase N in the method names). If the class has a get Xxx method but no corresponding set Xxx , the class is said to have a read-only property named xxx .

The one exception to this naming convention is with boolean properties: they use a method called is Xxx to look up their values. So, for example, your Car class might have methods called isLeased (which takes no arguments and returns a boolean ) and setLeased (which takes a boolean and has a void return type), and would be said to have a boolean property named leased (again, notice the lowercase leading letter in the property name).

Although you can use JSP scriptlets or expressions to access arbitrary methods of a class, standard JSP actions for accessing beans can only make use of methods that use the get Xxx / set Xxx or is Xxx / set Xxx design pattern.

## 13.1 Basic Bean Use

The jsp:useBean action  lets  you  load  a  bean  to  be  used  in  the  JSP page. Beans provide a very useful capability because they let you exploit the reusability of Java classes without sacrificing the convenience that JSP adds over servlets alone.

The simplest syntax for specifying that a bean should be used is:

&lt;jsp:useBean id="name" class="package.Class" /&gt;