## 16.6 Combo Boxes and List Boxes

## 16.6 Combo Boxes and List Boxes

A SELECT element presents a set of options to the user. If only a single entry can be selected and no visible size has been specified, the options are presented in a combo box (drop-down menu); list boxes are used when multiple selections  are  permitted  or  a  specific  visible  size  has  been  specified.  The choices themselves are specified by OPTION entries embedded in the SELECT element. The typical format is as follows:

```
<SELECT NAME=" Name " ...> <OPTION VALUE=" Value1 "> Choice 1 Text <OPTION VALUE=" Value2 "> Choice 2 Text ... <OPTION VALUE=" ValueN "> Choice N Text </SELECT>
```

The HTML 4.0 specification suggests the use of OPTGROUP (with a single attribute of LABEL ) to enclose OPTION elements in order to create cascading menus, but neither Netscape nor Internet Explorer supports this element.

## HTML Element: &lt;SELECT NAME="..." ...&gt; ... &lt;/SELECT&gt;

Attributes: NAME (required), SIZE , MULTIPLE , ONCLICK , ONFOCUS , ONBLUR , ONCHANGE

SELECT creates  a  combo  box  or  list  box  for  selecting  among  choices.  You specify  each  choice  with  an OPTION element  enclosed  between &lt;SELECT ...&gt; and &lt;/SELECT&gt; .

## NAME

NAME identifies the form to the servlet or CGI program.

## SIZE

SIZE gives the number of visible rows. If SIZE is used, the SELECT menu is usually represented as a list box instead of a combo box. A combo box is the normal representation when neither SIZE nor MULTIPLE is supplied.

## MULTIPLE

The MULTIPLE attribute specifies that multiple entries can be selected simultaneously. If MULTIPLE is omitted, only a single selection is permitted.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 16 Using HTML Forms

## ONCLICK, ONFOCUS, ONBLUR, and ONCHANGE

These nonstandard attributes are supported by browsers that understand JavaScript. They indicate code to be executed when the entry is clicked on, gains the input focus, loses the input focus, and loses the focus after having been changed, respectively.

## HTML Element: &lt;OPTION ...&gt; (End Tag Optional)

Attributes:

SELECTED , VALUE

Only valid inside a SELECT element, this element specifies the menu choices.

## VALUE

VALUE gives the value to be transmitted with the NAME of the SELECT menu if the current option is selected. This is not the text that is displayed to the user; that is specified by separate text listed after the OPTION tag.

## SELECTED

If present, SELECTED specifies that the particular menu item shown is selected when the page is first loaded.

The following example creates a menu of programming language choices. Because only a single selection is allowed and no visible SIZE is specified, it is displayed as a combo box. Figures 16-16 and 16-17 show the initial appearance and the appearance after the user activates the menu by clicking on it. If the entry Java is active when the form is submitted, then language=java is sent to the server-side program. Notice that it is the VALUE attribute, not the descriptive text, that is transmitted.

```
Favorite language: <SELECT NAME="language"> <OPTION VALUE="c">C <OPTION VALUE="c++">C++ <OPTION VALUE="java" SELECTED>Java <OPTION VALUE="lisp">Lisp <OPTION VALUE="perl">Perl <OPTION VALUE="smalltalk">Smalltalk </SELECT>
```

Figure 16-16 A SELECT element displayed as a combo box (drop-down menu).

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 16.6 Combo Boxes and List Boxes

Figure 16-17 Choosing options from a SELECT menu.

<!-- image -->

The second example shows a SELECT element  rendered as  a  list  box.  If more than one entry is active when the form is submitted, then more than one value is sent, listed as separate entries (repeating the NAME ). For instance, in  the  example  shown  in  Figure  16-18, language=java&amp;language=perl gets added to the data being sent to the server. Multiple entries that share the same name is the reason servlet authors need be familiar with the getParameterValues method of HttpServletRequest in addition to the more common getParameter method. See Chapter 3 (Handling the Client Request: Form Data) for details.

```
Languages you know:<BR> <SELECT NAME="language" MULTIPLE > <OPTION VALUE="c">C <OPTION VALUE="c++">C++ <OPTION VALUE="java" SELECTED>Java <OPTION VALUE="lisp">Lisp <OPTION VALUE="perl" SELECTED>Perl <OPTION VALUE="smalltalk">Smalltalk
```

&lt;/SELECT&gt;

## Languages you know:

Figure 16-18 A SELECT element that specifies MULTIPLE or SIZE results in a list box.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->