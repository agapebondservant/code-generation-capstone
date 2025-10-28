## 13.3 Setting Bean Properties

Figure 13-1 Result of StringBean.jsp .

<!-- image -->

## 13.3 Setting Bean Properties

You  normally  use jsp:setProperty to  set  bean  properties.  The  simplest form of this action takes three attributes: name (which should match the id given by jsp:useBean ), property (the name of the property to change), and value (the new value).

For example, the SaleEntry class  shown  in Listing 13.3  has  an itemID property (a String ), a numItems property (an int ), a discountCode property  (a double ),  and  two  read-only  properties itemCost and totalCost (each of type double ). Listing 13.4 shows a JSP file that builds an instance of the SaleEntry class by means of:

&lt;jsp:useBean id="entry" class="coreservlets.SaleEntry" /&gt;

The results are shown in Figure 13-2.

Once the bean is instantiated, using an input parameter to set the itemID is straightforward, as shown below:

```
<jsp:setProperty name="entry" property="itemID" value='<%= request.getParameter("itemID") %>' />
```

Notice that I used a JSP expression for the value parameter. Most JSP attribute values have to be fixed strings, but the value and name attributes of jsp:setProperty are  permitted  to  be  request-time  expressions.  If  the expression uses double quotes internally, recall that single quotes can be used instead of double quotes around attribute values and that \' and \" can be used to represent single or double quotes within an attribute value.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 13 Using JavaBeans with JSP

## Listing 13.3 SaleEntry.java

```
package coreservlets; /** Simple bean to illustrate the various forms *  of jsp:setProperty. */ public class SaleEntry { private String itemID = "unknown"; private double discountCode = 1.0; private int numItems = 0; public String getItemID() { return(itemID); } public void setItemID(String itemID) { if (itemID != null) { this.itemID = itemID; } else { this.itemID = "unknown"; } } public double getDiscountCode() { return(discountCode); } public void setDiscountCode(double discountCode) { this.discountCode = discountCode; } public int getNumItems() { return(numItems); } public void setNumItems(int numItems) { this.numItems = numItems; } // Replace this with real database lookup. public double getItemCost() { double cost; if (itemID.equals("a1234")) { cost = 12.99*getDiscountCode(); } else { cost = -9999;
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 13.3 Setting Bean Properties

## Listing 13.3 SaleEntry.java (continued)

```
} return(roundToPennies(cost)); } private double roundToPennies(double cost) { return(Math.floor(cost*100)/100.0); } public double getTotalCost() { return(getItemCost() * getNumItems()); } }
```

## Listing 13.4 SaleEntry1.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Using jsp:setProperty</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"> </HEAD> <BODY> <TABLE BORDER=5 ALIGN="CENTER"> <TR><TH CLASS="TITLE"> Using jsp:setProperty</TABLE> <jsp:useBean id="entry" class="coreservlets.SaleEntry" /> <jsp:setProperty name="entry" property="itemID" value='<%= request.getParameter("itemID") %>' /> <% int numItemsOrdered = 1; try { numItemsOrdered = Integer.parseInt(request.getParameter("numItems")); } catch(NumberFormatException nfe) {}
```

```
%>
```

<!-- image -->

## Chapter 13 Using JavaBeans with JSP

## &lt;jsp:setProperty name="entry" property="numItems" value="&lt;%= numItemsOrdered %&gt;" /&gt; &lt;% double discountCode = 1.0; try { String discountString = request.getParameter("discountCode"); // Double.parseDouble not available in JDK 1.1. discountCode = Double.valueOf(discountString).doubleValue(); } catch(NumberFormatException nfe) {} %&gt; &lt;jsp:setProperty name="entry" property="discountCode" value="&lt;%= discountCode %&gt;" /&gt; &lt;BR&gt; &lt;TABLE ALIGN="CENTER" BORDER=1&gt; &lt;TR CLASS="COLORED"&gt; &lt;TH&gt;Item ID&lt;TH&gt;Unit Price&lt;TH&gt;Number Ordered&lt;TH&gt;Total Price &lt;TR ALIGN="RIGHT"&gt; &lt;TD&gt;&lt;jsp:getProperty name="entry" property="itemID" /&gt; &lt;TD&gt;$&lt;jsp:getProperty name="entry" property="itemCost" /&gt; &lt;TD&gt;&lt;jsp:getProperty name="entry" property="numItems" /&gt; &lt;TD&gt;$&lt;jsp:getProperty name="entry" property="totalCost" /&gt; &lt;/TABLE&gt; &lt;/BODY&gt; &lt;/HTML&gt; Listing 13.4 SaleEntry1.jsp (continued)

## Associating Individual Properties with Input Parameters

Setting the itemID property was easy since its value is a String . Setting the numItems and discountCode properties  is  a  bit  more  problematic  since their values must be numbers and getParameter returns a String . Here is the somewhat cumbersome code required to set numItems :

```
<% int numItemsOrdered = 1; try { numItemsOrdered = Integer.parseInt(request.getParameter("numItems")); } catch(NumberFormatException nfe) {} %> <jsp:setProperty name="entry" property="numItems" value="<%= numItemsOrdered %>" />
```

Fortunately, JSP has a nice solution to this problem that lets you associate a  property  with  a  request  parameter  and  that  automatically  performs  type conversion from strings to numbers, characters, and boolean values. Instead of using the value attribute, you use param to name an input parameter. The value of this parameter is automatically used as the value of the property, and simple type conversions are performed automatically. If the specified input parameter is missing from the request, no action is taken (the system does not  pass null to  the  associated  property).  So,  for  example,  setting  the numItems property can be simplified to:

Figure 13-2 Result of SaleEntry1.jsp .

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

300

' Prentice Hall and Sun Microsystems. Personal use only; do not redistribute.

## Chapter 13 Using JavaBeans with JSP

name="entry" property="numItems" param="numItems" /&gt;

Listing 13.5 shows the entire JSP page reworked in this manner.

## Listing 13.5 SaleEntry2.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;Using jsp:setProperty&lt;/TITLE&gt; &lt;LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;TABLE BORDER=5 ALIGN="CENTER"&gt; &lt;TR&gt;&lt;TH CLASS="TITLE"&gt; Using jsp:setProperty&lt;/TABLE&gt; &lt;jsp:useBean id="entry" class="coreservlets.SaleEntry" /&gt; &lt;jsp:setProperty name="entry" property="itemID" param="itemID" /&gt; &lt;jsp:setProperty name="entry" property="numItems" param="numItems" /&gt; &lt;%-- WARNING! Both the JSWDK 1.0.1 and the Java Web Server have a bug that makes them fail on double type conversions of the following sort. --%&gt; &lt;jsp:setProperty name="entry" property="discountCode" param="discountCode" /&gt; &lt;BR&gt; &lt;TABLE ALIGN="CENTER" BORDER=1&gt; &lt;TR CLASS="COLORED"&gt; &lt;TH&gt;Item ID&lt;TH&gt;Unit Price&lt;TH&gt;Number Ordered&lt;TH&gt;Total Price &lt;TR ALIGN="RIGHT"&gt; &lt;TD&gt;&lt;jsp:getProperty name="entry" property="itemID" /&gt; &lt;TD&gt;$&lt;jsp:getProperty name="entry" property="itemCost" /&gt; &lt;TD&gt;&lt;jsp:getProperty name="entry" property="numItems" /&gt; &lt;TD&gt;$&lt;jsp:getProperty name="entry" property="totalCost" /&gt; &lt;/TABLE&gt; &lt;/BODY&gt; &lt;/HTML&gt;

## 13.3 Setting Bean Properties

## Chapter 13 Using JavaBeans with JSP

## Automatic Type Conversions

Table  13.1  summarizes  the  automatic  type  conversions  performed  when  a bean property is automatically associated with an input parameter. One warning is in order, however: both JSWDK 1.0.1 and the Java Web Server 2.0 have a bug that causes them to crash at page translation time for pages that try to perform automatic type conversions for properties that expect double values. Tomcat and most commercial servers work as expected.

<!-- image -->

## Core Warning

With the JSWDK and the Java Web Server, you cannot associate properties that expect double-precision values with input parameters.

## Table 13.1 Type Conversions When Properties Are Associated with Input Parameters

## Property Type Conversion Routine

boolean

Boolean.valueOf(paramString).booleanValue()

Boolean

Boolean.valueOf(paramString)

byte

Byte.valueOf(paramString).byteValue()

Byte

Byte.valueOf(paramString)

char

Character.valueOf(paramString).charValue()

Character

Character.valueOf(paramString)

double

Double.valueOf(paramString).doubleValue()

Double

Double.valueOf(paramString)

int

Integer.valueOf(paramString).intValue()

Integer

Integer.valueOf(paramString)

float

Float.valueOf(paramString).floatValue()

Float

Float.valueOf(paramString)

long

Long.valueOf(paramString).longValue()

Long

Long.valueOf(paramString)

## 13.3 Setting Bean Properties

## Associating All Properties with Input Parameters

Associating a property with an input parameter saves you the bother of performing conversions for many of the simple built-in types. JSP lets you take the  process  one  step  further  by  associating all properties  with  identically named input parameters. All you have to do is to supply "*" for the property parameter. So, for example, all three of the jsp:setProperty statements of Listing 13.5 can be replaced by the following simple line. Listing 13.6 shows the complete page.

&lt;jsp:setProperty name="entry" property="*" /&gt;

Although this approach is simple, four small warnings are in order. First, as with  individually  associated  properties,  no  action  is  taken  when  an  input parameter is missing. In particular, the system does not supply null as  the property value. Second, the JSWDK and the Java Web Server both fail for conversions to properties that expect double values. Third,  automatic type conversion does not guard against illegal values as effectively as does manual type conversion. So you might consider error pages (see Sections 11.9 and 11.10) when using  automatic  type  conversion.  Fourth,  since both property names and input parameters are case sensitive, the property name and input parameter must match exactly.

## Core Warning

In order for all properties to be associated with input parameters, the property names must match the parameter names exactly , including case.

## Listing 13.6 SaleEntry3.jsp

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Using jsp:setProperty</TITLE> <LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css">
```

&lt;/HEAD&gt;

&lt;BODY&gt;

<!-- image -->