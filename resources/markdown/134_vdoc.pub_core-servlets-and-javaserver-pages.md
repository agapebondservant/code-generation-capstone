## Chapter 16 Using HTML Forms

The following example creates a text area with 5 visible rows that can hold about 30 characters per row. The result is shown in Figure 16-10.

```
<CENTER> <P> Enter some HTML:<BR> <TEXTAREA NAME="HTML" ROWS=5 COLS=30> Delete this text and replace with some HTML to validate. </TEXTAREA> <CENTER>
```

## Enter some HTML:

Figure 16-10 A text area.

<!-- image -->

## 16.4 Push Buttons

Push buttons  are  used  for  two  main  purposes  in  HTML  forms:  to  submit forms and to reset the controls to the values specified in the original HTML. Browsers that use JavaScript can also use buttons for a third purpose: to trigger arbitrary JavaScript code.

Traditionally, buttons have been created by the INPUT element used with a TYPE attribute of SUBMIT , RESET , or BUTTON . In HTML 4.0, the BUTTON element was introduced but is currently supported only by Internet Explorer. This new element lets you create buttons with multiline labels, images, font changes, and the like, so is  preferred if you are sure your users will all be using browsers that support it (e.g., in a corporate intranet). Since the element is not supported by Netscape, at least as of Netscape version 4.7, for now  you  should  reserve BUTTON for  intranets  that  use  Internet  Explorer exclusively.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Core Warning

Netscape does not support the BUTTON element.

## Submit Buttons

## HTML Element: &lt;INPUT TYPE="SUBMIT" ...&gt; (No End Tag)

Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR

When a  submit  button  is  clicked,  the  form  is  sent  to  the  servlet  or  other server-side  program  designated  by  the ACTION parameter  of  the FORM . Although the action can be triggered other ways, such as the user clicking on an image map, most forms have at least one submit button. Submit buttons, like other form controls, adopt the look and feel of the client operating system, so will look slightly different on different platforms. Figure 16-11 shows a submit button on Windows 98, created by

&lt;INPUT TYPE="SUBMIT"&gt;

Figure 16-11 A submit button with the default label.

## NAME and VALUE

Most input elements have a name and an associated value. When the form is submitted, the names and values of active elements are concatenated to form the data string. If a submit button is used simply to initiate the submission of the form, its name can be omitted and then it does not contribute to the data string that is sent. If a name is supplied, then only the name and value of the button that was actually clicked are sent. The label is used as the value that is transmitted. Supplying an explicit VALUE will change the default label. For instance, the following code snippet creates a textfield and two submit buttons, shown in Figure 16-12. If, for example, the first button is selected, the data string sent to the server would be

Item=256MB+SIMM&amp;Add=Add+Item+to+Cart .

&lt;CENTER&gt;

Item:

&lt;INPUT TYPE="TEXT" NAME="Item" VALUE="256MB SIMM"&gt;&lt;BR&gt;

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 16.4 Push Buttons

401

<!-- image -->

## Chapter 16 Using HTML Forms

&lt;INPUT TYPE="SUBMIT" NAME="Add" VALUE="Add Item to Cart"&gt; &lt;INPUT TYPE="SUBMIT" NAME="Delete" VALUE="Delete Item from Cart"&gt;

&lt;/CENTER&gt;

Figure 16-12 Submit buttons with user-defined labels.

<!-- image -->

## ONCLICK, ONDBLCLICK, ONFOCUS, and ONBLUR

These nonstandard attributes are used by JavaScript-capable browsers to associate JavaScript code with the button. The ONCLICK and ONDBLCLICK code is executed when the button is pressed, the ONFOCUS code when the button gets the input focus, and the ONBLUR code when the button loses the focus. If the code attached to a button returns false , the submission of the form is suppressed. HTML attributes are not case sensitive, and these attributes are traditionally called onClick , onDblClick , onFocus , and onBlur by JavaScript programmers.

## HTML Element: &lt;BUTTON TYPE="SUBMIT" ...&gt; HTML Markup

&lt;/BUTTON&gt;

Attributes: NAME , VALUE , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR

This alternative way of creating submit buttons, supported only by Internet Explorer, lets you use arbitrary HTML markup for the content of the button. This element lets you to have multiline button labels, button labels with font changes, image buttons, and so forth. Listing 16.4 gives a few examples, with results shown in Figure 16-13.

## NAME, VALUE, ONCLICK, ONDBLCLICK, ONFOCUS, and ONBLUR

These attributes are used in the same way as with &lt;INPUT TYPE="SUBMIT" ...&gt; .

## Listing 16.4 ButtonElement.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>The BUTTON Element</TITLE> </HEAD> <BODY BGCOLOR="WHITE"> <H2 ALIGN="CENTER">The BUTTON Element</H2> <FORM ACTION="http://localhost:8088/SomeProgram"> <CENTER> <BUTTON TYPE="SUBMIT">Single-line Label</BUTTON> &nbsp;&nbsp; <BUTTON TYPE="SUBMIT">Multi-line<BR>label</BUTTON> <P> <BUTTON TYPE="SUBMIT"> <B>Label</B> with <I>font</I> changes. </BUTTON> <P> <BUTTON TYPE="SUBMIT"> <IMG SRC="images/Java-Logo.gif" WIDTH=110 HEIGHT=101 ALIGN="LEFT" ALT="Java Cup Logo"> Label<BR>with image </BUTTON> </CENTER> </FORM> </BODY> </HTML>
```

Figure 16-13 Submit buttons created with the BUTTON element.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 16.4 Push Buttons

## Chapter 16 Using HTML Forms

## Reset Buttons

## HTML Element: &lt;INPUT TYPE="RESET" ...&gt; (No End Tag)

Attributes: VALUE , NAME , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR

Reset buttons serve to reset the values of all items in the FORM to those specified in the original VALUE parameters. Their value is never transmitted as part of the form's contents.

## VALUE

The VALUE attribute specifies the button label; 'Reset' is the default.

## NAME

Because reset buttons do not contribute to the data string transmitted when the form is submitted, they are not named in standard HTML. However, JavaScript permits a NAME attribute to be used to simplify reference to the element.

## ONCLICK, ONDBLCLICK, ONFOCUS, and ONBLUR

These nonstandard attributes are used by JavaScript-capable browsers to associate JavaScript code with the button. The ONCLICK and ONDBLCLICK code is executed when the button is pressed, the ONFOCUS code when the button gets the input focus, and the ONBLUR code when it loses the focus. HTML attributes are not case sensitive, and these attributes are traditionally called onClick , onDblClick , onFocus , and onBlur by JavaScript programmers.

HTML Element:

&lt;BUTTON TYPE="RESET" ...&gt; HTML Markup &lt;/BUTTON&gt;

Attributes: VALUE , NAME , ONCLICK , ONDBLCLICK , ONFOCUS , ONBLUR

This  alternative  way  of  creating  reset  buttons,  supported  only  by  Internet Explorer, lets you use arbitrary HTML markup for the content of the button. All attributes are used identically to those in &lt;INPUT TYPE="RESET" ...&gt; .