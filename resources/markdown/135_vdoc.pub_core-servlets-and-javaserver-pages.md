## JavaScript Buttons

HTML Element: &lt;INPUT TYPE="BUTTON" ...&gt; (No End Tag) Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR

The BUTTON element is recognized only by browsers that support JavaScript. It  creates  a  button  with  the  same visual  appearance  as  a SUBMIT or RESET button  and  allows  the  author  to  attach  JavaScript  code  to  the ONCLICK , ONDBLCLICK , ONFOCUS , or ONBLUR attributes. The name/value pair associated with a JavaScript button is not transmitted as part of the data when the form is submitted. Arbitrary code can be associated with the button, but one of the most common uses is to verify that all input elements are in the proper format before the form is submitted to the server. For instance, the following would create a button where the user-defined validateForm function would be called whenever the button is activated.

&lt;INPUT TYPE="BUTTON" VALUE="Check Values" onClick="validateForm()"&gt;

## HTML Element: &lt;BUTTON TYPE="BUTTON" ...&gt; HTML Markup &lt;/BUTTON&gt;

Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR

This  alternative  way  of  creating  JavaScript  buttons,  supported  only  by Internet Explorer, lets you use arbitrary HTML markup for the content of the button. All attributes are used identically to those in &lt;INPUT TYPE="BUTTON" ...&gt; .

## 16.5 Check Boxes and Radio Buttons

Check boxes and radio buttons are useful controls for allowing the user to select  among a set of predefined choices. While each individual check box can be selected or deselected individually, radio buttons can be grouped so that only a single member of the group can be selected at a time.

## 16.5 Check Boxes and Radio Buttons

## Chapter 16 Using HTML Forms

## Check boxes

## HTML Element: &lt;INPUT TYPE="CHECKBOX" NAME="..." ...&gt; (No End Tag)

Attributes: NAME (required), VALUE , CHECKED , ONCLICK , ONFOCUS , ONBLUR

This input element creates a check box whose name/value pair is transmitted only if  the check box is checked when the form is submitted. For instance, the following code results in the check box shown in Figure 16-14.

```
<P> <INPUT TYPE="CHECKBOX" NAME="noEmail" CHECKED> Check here if you do <I>not</I> want to get our email newsletter
```

Check here do not want to our emall newsletter ifyou get

Figure 16-14 An HTML check box.

Note  that  the  descriptive  text  associated  with  the  check  box  is  normal HTML, and care should be taken to guarantee that it appears next  to  the check box. Thus, the &lt;P&gt; in  the  preceding  example ensures that the check box isn't part of the previous paragraph.

<!-- image -->

## Core Approach

Paragraphs inside a FORM are filled and wrapped just like regular paragraphs. So, be sure to insert explicit HTML markup to keep input elements with the text that describes them.

## NAME

This attribute supplies the name that is sent to the server. It is required for standard HTML check boxes but optional when used with JavaScript.

## VALUE

The VALUE attribute is optional and defaults to on . Recall that the name and value are only sent to the server if the check box is checked when the form is submitted. For instance, in the preceding example, noEmail=on would be added to the data string since the box is checked, but nothing would be added if the box was unchecked. As a result, servlets or CGI programs often check only for the existence of the check box name, ignoring its value.

## CHECKED

If the CHECKED attribute is supplied, then the check box is initially checked when the associated Web page is loaded. Otherwise, it is initially unchecked.

## ONCLICK, ONFOCUS, and ONBLUR

These attributes supply JavaScript code to be executed when the button is clicked, receives the input focus, and loses the focus, respectively.

## Radio Buttons

HTML Element: &lt;INPUT TYPE="RADIO" NAME="..." VALUE="..." ...&gt; (No End Tag) ,

Attributes: NAME (required), VALUE (required), CHECKED , ONCLICK ONFOCUS , ONBLUR

Radio buttons differ from check boxes in that only a single radio button in a given group can be selected at any one time. You indicate a group of radio buttons by providing all of them with the same NAME .  Only one button in a group can be depressed at a time; selecting a new button when one is already selected results in the previous choice becoming deselected. The value of the one  selected  is  sent  when  the  form  is  submitted.  Although  radio  buttons technically need not appear near to each other, this proximity is almost always recommended.

An  example  of  a  radio  button  group  follows.  Because  input  elements  are wrapped as part of normal paragraphs, a DL list is used to make sure that the buttons appear under each other in the resultant page and are indented from the heading  above  them.  Figure  16-15  shows  the  result.  In  this  case, creditCard=java would get sent as part of the form data when the form is submitted.

```
<DL> <DT>Credit Card: <DD><INPUT TYPE="RADIO" NAME="creditCard" VALUE="visa"> Visa <DD><INPUT TYPE="RADIO" NAME="creditCard" VALUE="mastercard"> Master Card <DD><INPUT TYPE="RADIO" NAME="creditCard" VALUE="java" CHECKED> Java Smart Card <DD><INPUT TYPE="RADIO" NAME="creditCard" VALUE="amex"> American Express <DD><INPUT TYPE="RADIO" NAME="creditCard" VALUE="discover"> Discover </DL>
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 16.5 Check Boxes and Radio Buttons

## Chapter 16 Using HTML Forms

Figure 16-15 Radio buttons in HTML.

## Credit Card:

- { Visa

- Master Card

- Java Smatt Card

- American Express

- Discover

## NAME

Unlike the NAME attribute of most input elements, this NAME is shared by multiple elements. All radio buttons associated with the same name are grouped logically so that no more than one can be selected at any given time. Note that attribute values are case sensitive, so the following would result in two radio buttons that are not logically connected.

&lt;INPUT TYPE="RADIO" NAME="Foo" VALUE="Value1"&gt; &lt;INPUT TYPE="RADIO" NAME="FOO" VALUE="Value2"&gt;

## Core Warning

Be sure the NAME of each radio button in a logical group matches exactly.

## VALUE

The VALUE attribute supplies the value that gets transmitted with the NAME when the form is submitted. It doesn't affect the appearance of the radio button. Instead, normal text and HTML markup are placed around the radio button, just as with check boxes.

## CHECKED

If the CHECKED attribute is supplied, then the radio button is initially checked when the associated Web page is loaded. Otherwise, it is initially unchecked.

## ONCLICK, ONFOCUS, and ONBLUR

These attributes  supply JavaScript code to be executed when the button is clicked, receives the input focus, and loses the focus, respectively.

<!-- image -->