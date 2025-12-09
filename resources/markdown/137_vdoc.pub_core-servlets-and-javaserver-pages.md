## Chapter 16 Using HTML Forms

## 16.7 File Upload Controls

## HTML Element: &lt;INPUT TYPE="FILE" ...&gt; (No End Tag)

Attributes:

NAME (required), VALUE (ignored), SIZE , MAXLENGTH , ACCEPT , ONCHANGE , ONSELECT , ONFOCUS , ONBLUR (nonstandard)

This element results in a filename textfield next to a Browse button. Users can enter a path directly in the textfield or click on the button to bring up a file  selection  dialog  that  lets  them  interactively  choose  the  path  to  a  file. When the form is submitted, the contents of the file are transmitted as long as  an ENCTYPE of multipart/form-data was  specified  in  the  initial FORM declaration.  This element provides a convenient way to make  user-support pages, where the user sends a description of the problem along with any associated data or configuration files.

<!-- image -->

## Core Tip

Always specify ENCTYPE="multipart/form-data" in forms with file upload controls.

## NAME

The NAME attribute identifies the textfield when the form is submitted.

## VALUE

For security reasons, this attribute is ignored. Only the end user can specify a filename.

## SIZE and MAXLENGTH

The SIZE and MAXLENGTH attributes are used the same way as in textfields, specifying the number of visible and maximum allowable characters, respectively.

## ACCEPT

The ACCEPT attribute is intended to be a comma-separated list of MIME types used to restrict the available filenames. However, very few browsers support this attribute.

## 16.7 File Upload Controls

## ONCHANGE, ONSELECT, ONFOCUS, and ONBLUR

These attributes are used by browsers that support JavaScript to specify the action to take when the mouse leaves the textfield after a change has occurred, when the user selects text in the textfield, when the textfield gets the input focus, and when it loses the input focus, respectively.

For  example,  the  following  code  creates  a  file  upload  control.  Figure 16-19 shows the initial result, and Figure 16-20 shows a typical pop-up window that results when the Browse button is activated.

```
<FORM ACTION="http://localhost:8088/SomeProgram" ENCTYPE="multipart/form-data"> Enter data file below:<BR> <INPUT TYPE="FILE" NAME="fileName"> </FORM>
```

data file below: Enter

Figure 16-19 Initial look of a file upload control.

<!-- image -->

Figure 16-20 A file chooser resulting from the user clicking on Browse in a file upload control.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->