## TARGET

The TARGET attribute is used by frame-capable browsers to determine which frame cell should be used to display the results of the servlet or other program handling the form submission. The default is to display the results in whatever frame contains the form being submitted.

## ONSUBMIT and ONRESET

These attributes are used by JavaScript to attach code that should be evaluated when the form is submitted or reset. For ONSUBMIT , if the expression evaluates to false , the form is not submitted. This case lets you invoke JavaScript code on the client that checks the format of the form field values before they are submitted, prompting the user for missing or illegal entries.

## ACCEPT and ACCEPT-CHARSET

These attributes are new in HTML 4.0 and specify the MIME types ( ACCEPT ) and character encodings ( ACCEPT-CHARSET ) that must be accepted by the servlet or other program processing the form data. The MIME types listed in ACCEPT could also be used by the client to limit which file types are displayed to the user for file upload elements.

## 16.3 Text Controls

HTML  supports  three  types  of  text-input  elements:  textfields,  password fields, and text areas. Each is given a name, and the value is taken from the content of the control. The name and value are sent to the server when the form is submitted, which is typically done by means of a submit button (see Section 16.4).

## Textfields

## HTML Element: &lt;INPUT TYPE="TEXT" NAME="..." ...&gt; (No End Tag)

Attributes:

NAME (required), VALUE , SIZE , MAXLENGTH , ONCHANGE , ONSELECT , ONFOCUS , ONBLUR , ONKEYDOWN , ONKEYPRESS , ONKEYUP

This element creates a single-line input field where the user can enter text, as illustrated  earlier  in  Listings  16.1,  16.2,  and  16.3.  For  multiline  fields,  see

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 16.3 Text Controls

## Chapter 16 Using HTML Forms

TEXTAREA in  the  following  subsection. TEXT is  the  default TYPE in INPUT forms,  although  it  is  recommended  that TEXT be  supplied  explicitly.  You should  remember  that  the  normal  browser  word  wrapping  applies  inside FORM elements, so be careful to make sure the browser will not separate the descriptive text from the associated textfield.

<!-- image -->

## Core Approach

Use explicit HTML constructs to group textfields with their descriptive text.

Some browsers submit the form when the user presses Enter when the cursor  is  in  a  textfield,  but  you  should  avoid  depending  on  this  behavior because it is not standard. For instance, Netscape submits the form when the user  types  a  carriage  return  only  if  the  current  form  has  a  single  textfield, regardless of the number of forms on the page. Internet Explorer submits the form on Enter only when there is a single form on the page, regardless of the number of  textfields  in  the  form.  Mosaic  submits  the  form  on  Enter  only when the cursor is in the last textfield on the entire page.

<!-- image -->

## Core Warning

Don't rely on the browser submitting the form when the user presses Enter when in a textfield. Always include a button or image map that submits the form explicitly.

The following subsections describe the attributes that apply specifically to textfields.  Attributes  that  apply  to  general  HTML  elements  (e.g., STYLE , CLASS , ID )  are not discussed. The TABINDEX attribute, which applies to all form elements, is discussed in Section 16.11 (Controlling Tab Order).

## NAME

The NAME attribute identifies the textfield when the form is submitted. In standard HTML the attribute is required. Because data is always sent to the server in the form of name/value pairs, no data is sent from form controls that have no NAME .

## VALUE

A VALUE attribute, if supplied, specifies the initial contents of the textfield. When the form is submitted, the current contents are sent; these can reflect user input. If the textfield is empty when the form is submit-

## 16.3 Text Controls

ted, the form data simply consists of the name and an equal sign (e.g., other-data&amp; textfieldname= &amp;other-data ).

## SIZE

This attribute specifies the width of the textfield, based on the average character width of the font being used. If text beyond this size is entered, the textfield scrolls to accommodate it. This could happen if the user enters more characters than the SIZE or enters SIZE number of wide characters (e.g., capital W) if a proportional-width font is being used. Netscape automatically uses a proportional font in textfields. Internet Explorer, unfortunately, does not, and you cannot change the font by embedding the INPUT element in a FONT or CODE element.

## MAXLENGTH

MAXLENGTH gives the maximum number of allowable characters. This number is in contrast to the number of visible characters, which is specified via SIZE .

## ONCHANGE, ONSELECT, ONFOCUS, ONBLUR, ONDBLDOWN, ONKEYPRESS, and ONKEYUP

These attributes are used only by browsers that support JavaScript. They specify the action to take when the mouse leaves the textfield after a change has occurred, when the user selects text in the textfield, when the textfield gets the input focus, when it loses the input focus, and when individual keys are pressed.

## Password Fields

## HTML Element: &lt;INPUT TYPE="PASSWORD" NAME="..." ...&gt; (No End Tag )

Attributes:

NAME (required), VALUE , SIZE , MAXLENGTH , ONCHANGE , ONSELECT , ONFOCUS , ONBLUR , ONKEYDOWN , ONKEYPRESS , ONKEYUP

Password fields are created and used just like textfields, except that when the user enters text, the input is not echoed but instead some obscuring character, usually an asterisk, is displayed (see Figure 16-9). Obscured input is useful for collecting data such as credit card numbers or passwords that the user would not want shown to people who may be near his computer. The regular, unobscured text is transmitted as the value of the field when the form is submitted. Since GET data is appended to the URL after a question mark, you

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 16 Using HTML Forms

will  want  to  use  the POST method  when  using  a  password  field  so  that  a bystander cannot read the unobscured password from the URL display at the top of the browser.

<!-- image -->

## Core Approach

To protect the user's privacy, always use POST when creating forms with password fields.

## NAME, VALUE, SIZE, MAXLENGTH, ONCHANGE, ONSELECT, ONFOCUS, ONBLUR, ONKEYDOWN, ONKEYPRESS, and ONKEYUP

Attributes for password fields are used in exactly the same manner as with textfields.

Figure 16-9 A password field created by means of

&lt;INPUT TYPE="PASSWORD" ...&gt; .

Enter Password:

## Text Areas

HTML Element:

&lt;TEXTAREA NAME="..."

ROWS=xxx COLS=yyy&gt; ...

## &lt;/TEXTAREA&gt;

Attributes:

NAME (required), ROWS (required), COLS (required), WRAP (nonstandard), ONCHANGE , ONSELECT , ONFOCUS , ONBLUR , ONKEYDOWN , ONKEYPRESS , ONKEYUP

The TEXTAREA element creates a multiline text area; see Figure 16-10. There is no VALUE attribute; instead, text between the start and end tags is used as the initial contents of the text area. The initial text between &lt;TEXTAREA ...&gt; and &lt;/TEXTAREA&gt; is treated similarly to text inside the now-obsolete XMP element.  That  is,  white  space  in  this  initial  text  is  maintained  and  HTML markup between the start and end tags is taken literally, except for character entities such as &amp;lt; , &amp;copy; , and so forth, which are interpreted normally. Unless a custom ENCTYPE is used in the form (see Section 16.2, 'The FORM

## 16.3 Text Controls

Element'), characters, including those generated from character entities, are URL-encoded before being transmitted. That is, spaces become plus signs and other nonalphanumeric characters become % XX , where XX is the numeric value of the character in hex.

## NAME

This attribute specifies the name that will be sent to the server.

## ROWS

ROWS specifies the number of visible lines of text. If more lines of text are entered, a vertical scrollbar will be added to the text area.

## COLS

COLS specifies the visible width of the text area, based on the average width of characters in the font being used. If the text on a single line contains more characters than the specified width allows, the result is browser dependent. In Netscape, horizontal scrollbars are added (but see the WRAP attribute, described next, to change this behavior). In Internet Explorer, the word wraps around to the next line.

## WRAP

The Netscape-specific WRAP attribute specifies what to do with lines that are longer than the size specified by COLS . A value of OFF disables word wrap and is the default. The user can still enter explicit line breaks in such a case. A value of HARD causes words to wrap in the text area and the associated line breaks to be transmitted when the form is submitted. Finally, a value of SOFT causes the words to wrap in the text area but no extra line breaks to be transmitted when the form is submitted.

## ONCHANGE, ONSELECT, ONFOCUS, ONBLUR, ONKEYDOWN, ONKEYPRESS, and ONKEYUP

These attributes apply only to browsers that support JavaScript; they specify code to be executed when certain conditions arise. ONCHANGE handles the situation when the input focus leaves the text area after it has changed, ONSELECT describes what to do when text in the text area is selected by the user, ONFOCUS and ONBLUR specify what to do when the text area acquires or loses the input focus, and the remaining attributes determine what to do when individual keys are typed.