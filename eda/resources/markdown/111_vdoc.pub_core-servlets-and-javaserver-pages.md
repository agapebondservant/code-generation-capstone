## Chapter 13 Using JavaBeans with JSP

change from English units to metric units internally, but still have getSpeedInMPH and getSpeedInKPH methods), and automatically perform side effects when values change (e.g., update the user interface when setPosition is called).

- 3. Persistent values should be accessed through methods called get Xxx and set Xxx . For example, if your Car class stores the current number of passengers, you might have methods named getNumPassengers (which takes no arguments and returns an int ) and setNumPassengers (which takes an int and has a void return type). In such a case, the Car class is said to have a property named numPassengers (notice the lowercase n in the property name, but the uppercase N in the method names). If the class has a get Xxx method but no corresponding set Xxx , the class is said to have a read-only property named xxx .

The one exception to this naming convention is with boolean properties: they use a method called is Xxx to look up their values. So, for example, your Car class might have methods called isLeased (which takes no arguments and returns a boolean ) and setLeased (which takes a boolean and has a void return type), and would be said to have a boolean property named leased (again, notice the lowercase leading letter in the property name).

Although you can use JSP scriptlets or expressions to access arbitrary methods of a class, standard JSP actions for accessing beans can only make use of methods that use the get Xxx / set Xxx or is Xxx / set Xxx design pattern.

## 13.1 Basic Bean Use

The jsp:useBean action  lets  you  load  a  bean  to  be  used  in  the  JSP page. Beans provide a very useful capability because they let you exploit the reusability of Java classes without sacrificing the convenience that JSP adds over servlets alone.

The simplest syntax for specifying that a bean should be used is:

&lt;jsp:useBean id="name" class="package.Class" /&gt;

## 13.1 Basic Bean Use

This usually means 'instantiate an object of the class specified by Class , and bind it to a variable with the name specified by id .' So, for example, the JSP action

&lt;jsp:useBean id="book1" class="coreservlets.Book" /&gt;

can normally be thought of as equivalent to the scriptlet

&lt;% coreservlets.Book book1 = new coreservlets.Book(); %&gt;

Although it is convenient to think of jsp:useBean as being equivalent to building an object, jsp:useBean has  additional  options  that  make  it  more powerful.  As  we'll  see  in  Section  13.4  (Sharing  Beans),  you  can  specify  a scope attribute that makes the bean associated with more than just the current page. If beans can be shared, it is useful to obtain references to existing beans, so the jsp:useBean action specifies that a new object is instantiated only if there is no existing one with the same id and scope .

Rather than using the class attribute, you are permitted to use beanName instead. The difference is that beanName can refer either to a class or to a file containing a serialized bean object. The value of the beanName attribute is passed to the instantiate method of java.beans.Bean .

In most cases, you want the  local variable  to have  the same  type as the object being created. In a few cases, however, you might want the variable to be declared to have a type that is a superclass of the actual bean type or is an interface that the bean implements. Use the type attribute to control this, as in the following example:

&lt;jsp:useBean id="thread1" class="MyClass" type="Runnable" /&gt;

This  use  results  in  code  similar  to  the  following  being  inserted  into  the \_jspService method:

Runnable thread1 = new MyClass();

Note that since jsp:useBean uses XML syntax, the format differs in three ways from HTML syntax: the attribute names are case sensitive, either single or double quotes can be used (but one or the other must be used), and the end of the tag is marked with /&gt; ,  not  just &gt; .  The  first  two  syntactic differences apply to all JSP elements that look like jsp: xxx . The third difference applies unless the element is a container with a separate start and end tag.

## Core Warning

Syntax for jsp: xxx elements differs in three ways from HTML syntax: attribute names are case sensitive, you must enclose the value in single or

<!-- image -->

## Chapter 13 Using JavaBeans with JSP

double quotes, and noncontainer elements should end the tag with /&gt; , not just &gt; .

There are also a few character sequences that require special handling in order to appear inside attribute values:

- · To get ' within an attribute value, use \' .
- · To get " within an attribute value, use \" .
- · To get \ within an attribute value, use \\ .
- · To get %&gt; within an attribute value, use %\&gt; .
- · To get &lt;% within an attribute value, use &lt;\% .

## Accessing Bean Properties

Once you have a bean, you can access its properties with jsp:getProperty , which takes a name attribute that should match the id given in jsp:useBean and a property attribute that names the property of interest. Alternatively, you could use a JSP expression and explicitly call a method on the object that has the variable name specified with the id attribute. For example, assuming that the Book class has a String property called title and that you've created an instance called book1 by using the jsp:useBean example just given, you could insert the value of the title property into the JSP page in either of the following two ways:

&lt;jsp:getProperty name="book1" property="title" /&gt; &lt;%= book1.getTitle() %&gt;

The first approach is preferable in this case, since the syntax is more accessible to Web page designers who are not familiar with the Java programming language. However, direct access to the variable is useful when you are using loops, conditional statements, and methods not represented as properties.

If you are not familiar with the concept of bean properties, the standard interpretation of the statement 'this bean has a property of type T called foo ' is 'this class has a method called getFoo that returns something of type T and has another method called setFoo that takes a T as an argument and stores it for later access by getFoo .'

## Setting Bean Properties: Simple Case

To modify bean properties, you normally use jsp:setProperty . This action has several different forms, but with the simplest form you just supply three

## 13.1 Basic Bean Use

attributes: name (which should match the id given by jsp:useBean ), property (the name of the property to change), and value (the new value). Section  13.3  (Setting  Bean  Properties)  discusses  some  alternate  forms  of jsp:setProperty that  let  you  automatically  associate  a  property  with  a request parameter. That section also explains how to supply values that are computed at request time (rather than fixed strings) and discusses the type conversion conventions that let you supply string values for parameters that expect numbers, characters, or boolean values.

An alternative to using the jsp:setProperty action is to use a scriptlet that  explicitly  calls  methods  on  the  bean  object.  For  example,  given  the book1 object shown earlier in this section, you could use either of the following two forms to modify the title property:

&lt;jsp:setProperty name="book1"

property="title"

value="Core Servlets and JavaServer Pages" /&gt;

&lt;% book1.setTitle("Core Servlets and JavaServer Pages"); %&gt;

Using jsp:setProperty has  the  advantage that  it  is  more  accessible  to the nonprogrammer, but direct access to the object lets you perform more complex operations such as setting the value conditionally or calling methods other than get Xxx or set Xxx on the object.

## Installing Bean Classes

The class specified for the bean must be in the server's regular class path, not the  part  reserved  for  classes  that  get  automatically  reloaded  when  they change. For example, in the Java Web Server, the main bean class and all the auxiliary classes it uses should go in the install\_dir /classes directory or be in a JAR file in install\_dir /lib , not in install\_dir /servlets . Since Tomcat and the JSWDK don't support auto-reloading servlets, bean classes can  be  installed  in  any  of  the  normal  servlet  directories.  For  Tomcat  3.0, assuming you haven't defined your own Web application, the primary directory for servlet class files is install\_dir /webpages/WEB-INF/classes ; for the JSWDK, the default location is install\_dir /webpages/WEB-INF/servlets . With all three servers, remember that a package name corresponds to a subdirectory. So, for example, a bean called Fordhook that declares ' package lima; ' would typically be installed in the following locations:

## · Tomcat 3.0:

install\_dir /webpages/WEB-INF/classes/lima/Fordhook.cla ss

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.