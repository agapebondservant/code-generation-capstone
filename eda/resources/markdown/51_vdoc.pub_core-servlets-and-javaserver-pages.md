## Chapter 3 Handling the Client Request: Form Data

Figure 3-4 Output of ShowParameters servlet.

<!-- image -->

## 3.5 A Resumé Posting Service

On-line job services have become increasingly popular of late. A reputable site provides a useful service to job seekers by giving their skills wide exposure and provides a useful service to employers by giving them access to a large pool of prospective employees. This section presents a servlet that handles part of such a site: the submission of on-line resumés.

Listing 3.5 and Figure 3-5 show the HTML form that acts as the front end to the resumé-processing servlet. If you are not familiar with HTML forms, they are covered in detail in Chapter 16. The important thing to understand here is that the form uses POST to submit the data and that it gathers values for the following parameter names:

## 3.5 A Resumé Posting Service

DILBERT reprinted by permission of United Syndicate, Inc.

<!-- image -->

## · headingFont

Headings will be displayed in this font. A value of 'default' results in a sans-serif font such as Arial or Helvetica.

## · headingSize

The person's name will be displayed in this point size. Subheadings will be displayed in a slightly smaller size.

## · bodyFont

The main text (languages and skills) will be displayed in this font.

## · bodySize

The main text will be displayed in this point size.

- · fgColor

Text will be this color.

## · bgColor

The page background will be this color.

## · name

This parameter specifies the person's name. It will be centered at the top of the resumé in the font and point size previously specified.

## · title

This parameter specifies the person's job title. It will be centered under the name in a slightly smaller point size.

## · email

The job applicant's email address will be centered under the job title inside a mailto link.

## · languages

The programming languages listed will be placed in a bulleted list in the on-line resumé.

## · skills

Text from the skills text area will be displayed in the body font at the bottom of the resumé under a heading called 'Skills and Experience.'

## Chapter 3 Handling the Client Request: Form Data

Listing 3.6 shows the servlet that processes the data from the HTML form. When the 'Preview' button is pressed, the servlet first reads the font and color parameters. Before using any of the parameters, it checks to see if the value is null (i.e., there is an error in the HTML form and thus the parameter is missing) or is an empty string (i.e., the user erased the default value but did not enter anything in its place). The servlet uses a default value appropriate to each parameter in  such  a  case.  Parameters  that  represent  numeric  values  are  passed  to Integer.parseInt .  To guard against the possibility of improperly formatted numbers supplied by the user, this Integer.parseInt call is placed inside a try / catch block that supplies a default value when the parsing fails. Although it may seem a bit tedious to handle these cases, it generally is not too much work if you make use of some utility methods such as replaceIfMissing and replaceIfMissingOrDefault in Listing 3.6. Tedious or not, users will sometimes overlook certain fields or misunderstand the required field format, so it is critical that your servlet handle malformed parameters gracefully and that you test it with both properly formatted and improperly formatted data.

<!-- image -->

## Core Approach

Design your servlets to gracefully handle missing or improperly formatted parameters. Test them with malformed data as well as with data in the expected format.

Once  the  servlet  has  meaningful  values  for  each  of  the  font  and  color parameters, it builds a cascading style sheet out of them. If you are unfamiliar with style sheets, they are a standard way of specifying the font faces, font sizes, colors, indentation, and other formatting information in an HTML 4.0 Web page. Style sheets are usually placed in a separate file so that several Web  pages  at  a  site  can  share  the  same  style  sheet,  but  in  this  case  it  is more convenient  to  embed  the  style  information  directly  in  the  page  by using the STYLE element. For more  information on style sheets, see http://www.w3.org/TR/REC-CSS1 .

After creating the style sheet, the servlet places the job applicant's name, job title, and e-mail address centered under each other at the top of the page. The heading font is  used  for  these  lines,  and  the  e-mail  address  is  placed inside a mailto: hypertext  link  so  that prospective  employers  can  contact the applicant directly by clicking on the address. The programming languages specified in the languages parameter are parsed using StringTokenizer (assuming spaces and/or commas are used to separate the language names) and placed in a bulleted list beneath a 'Programming Languages' heading.

## 3.5 A Resumé Posting Service

Finally, the text from the skills parameter is placed at the bottom of the page beneath a 'Skills and Experience' heading.

Figures  3-6  through  3-8  show  a  couple  of  possible  results.  Listing  3.7 shows the underlying HTML of the first of these results.

## Listing 3.5 SubmitResume.html

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt;

&lt;HTML&gt;

&lt;HEAD&gt;

&lt;TITLE&gt;Free Resume Posting&lt;/TITLE&gt;

&lt;LINK REL=STYLESHEET

HREF="jobs-site-styles.css"

TYPE="text/css"&gt;

&lt;/HEAD&gt;

&lt;BODY&gt;

&lt;H1&gt;hotcomputerjobs.com&lt;/H1&gt;

&lt;P CLASS="LARGER"&gt;

To use our &lt;I&gt;free&lt;/I&gt; resume-posting service, simply fill out the brief summary of your skills below. Use "Preview" to check the results, then press "Submit" once it is ready. Your mini resume will appear on-line within 24 hours.&lt;/P&gt; &lt;HR&gt;

&lt;FORM ACTION="/servlet/coreservlets.SubmitResume"

METHOD="POST"&gt;

&lt;DL&gt;

&lt;DT&gt;&lt;B&gt;First, give some general information about the look of

your resume:&lt;/B&gt;

&lt;DD&gt;Heading font:

&lt;INPUT TYPE="TEXT"

NAME="headingFont" VALUE="default"&gt;

&lt;DD&gt;Heading text size:

&lt;INPUT TYPE="TEXT"

NAME="headingSize" VALUE=32&gt;

&lt;DD&gt;Body font:

&lt;INPUT TYPE="TEXT"

NAME="bodyFont" VALUE="default"&gt;

&lt;DD&gt;Body text size:

&lt;INPUT TYPE="TEXT"

NAME="bodySize" VALUE=18&gt;

&lt;DD&gt;Foreground color:

&lt;INPUT TYPE="TEXT"

NAME="fgColor" VALUE="BLACK"&gt;

&lt;DD&gt;Background color:

&lt;INPUT TYPE="TEXT"

NAME="bgColor" VALUE="WHITE"&gt;

&lt;DT&gt;&lt;B&gt;Next, give some general information about yourself:&lt;/B&gt; &lt;DD&gt;Name: &lt;INPUT TYPE="TEXT" NAME="name" &gt;

&lt;DD&gt;Current or most recent title:

&lt;INPUT TYPE="TEXT" NAME="title" &gt;

&lt;DD&gt;Email address: &lt;INPUT TYPE="TEXT"

NAME="email" &gt;

&lt;DD&gt;Programming Languages:

&lt;INPUT TYPE="TEXT" NAME="languages"

&gt;

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 3 Handling the Client Request: Form Data

## Listing 3.5 SubmitResume.html (continued)

```
<DT><B>Finally, enter a brief summary of your skills and experience:</B> (use &lt;P&gt; to separate paragraphs. Other HTML markup is also permitted.) <DD><TEXTAREA NAME="skills" ROWS=15 COLS=60 WRAP="SOFT"></TEXTAREA> </DL> <CENTER> <INPUT TYPE="SUBMIT" NAME="previewButton" Value="Preview"> <INPUT TYPE="SUBMIT" NAME="submitButton" Value="Submit"> </CENTER> </FORM> <HR> <P CLASS="TINY">See our privacy policy <A HREF="we-will-spam-you.html">here</A>.</P> </BODY> </HTML>
```

## Listing 3.6 SubmitResume.java

```
package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.util.*; /** Servlet that handles previewing and storing resumes *  submitted by job applicants. */ public class SubmitResume extends HttpServlet { public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { response.setContentType("text/html"); PrintWriter out = response.getWriter(); if (request.getParameter("previewButton") != null) { showPreview(request, out); } else { storeResume(request); showConfirmation(request, out); } }
```

## 3.5 A Resumé Posting Service

## Listing 3.6 SubmitResume.java (continued)

```
// Shows a preview of the submitted resume. Takes // the font information and builds an HTML // style sheet out of it, then takes the real // resume information and presents it formatted with // that style sheet. private void showPreview(HttpServletRequest request, PrintWriter out) { String headingFont = request.getParameter("headingFont"); headingFont = replaceIfMissingOrDefault(headingFont, ""); int headingSize = getSize(request.getParameter("headingSize"), 32); String bodyFont = request.getParameter("bodyFont"); bodyFont = replaceIfMissingOrDefault(bodyFont, ""); int bodySize = getSize(request.getParameter("bodySize"), 18); String fgColor = request.getParameter("fgColor"); fgColor = replaceIfMissing(fgColor, "BLACK"); String bgColor = request.getParameter("bgColor"); bgColor = replaceIfMissing(bgColor, "WHITE"); String name = request.getParameter("name"); name = replaceIfMissing(name, "Lou Zer"); String title = request.getParameter("title"); title = replaceIfMissing(title, "Loser"); String email = request.getParameter("email"); email = replaceIfMissing(email, "contact@hotcomputerjobs.com"); String languages = request.getParameter("languages"); languages = replaceIfMissing(languages, "<I>None</I>"); String languageList = makeList(languages); String skills = request.getParameter("skills"); skills = replaceIfMissing(skills, "Not many, obviously."); out.println (ServletUtilities.DOCTYPE + "\n" + "<HTML>\n" + "<HEAD>\n" + "<TITLE>Resume for " + name + "</TITLE>\n" + makeStyleSheet(headingFont, headingSize, bodyFont, bodySize, fgColor, bgColor) + "\n" + "</HEAD>\n" + "<BODY>\n" + "<CENTER>\n"+ "<SPAN CLASS=\"HEADING1\">" + name + "</SPAN><BR>\n" + "<SPAN CLASS=\"HEADING2\">" + title + "<BR>\n" + "<A HREF=\"mailto:" + email + "\">" + email + "</A></SPAN>\n" +
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 3 Handling the Client Request: Form Data

## Listing 3.6 SubmitResume.java (continued)

```
"</CENTER><BR><BR>\n" + "<SPAN CLASS=\"HEADING3\">Programming Languages" + "</SPAN>\n" + makeList(languages) + "<BR><BR>\n" + "<SPAN CLASS=\"HEADING3\">Skills and Experience" + "</SPAN><BR><BR>\n" + skills + "\n" + "</BODY></HTML>"); }
```

// Builds a cascading style sheet with information // on three levels of headings and overall // foreground and background cover. Also tells // Internet Explorer to change color of mailto link // when mouse moves over it.

private String makeStyleSheet(String headingFont,

```
int heading1Size, String bodyFont, int bodySize, String fgColor, String bgColor) { int heading2Size = heading1Size*7/10; int heading3Size = heading1Size*6/10; String styleSheet = "<STYLE TYPE=\"text/css\">\n" + "<!--\n" + ".HEADING1 { font-size: " + heading1Size + "px;\n" + "            font-weight: bold;\n" + "            font-family: " + headingFont + "Arial, Helvetica, sans-serif;\n" + "}\n" + ".HEADING2 { font-size: " + heading2Size + "px;\n" + "            font-weight: bold;\n" + "            font-family: " + headingFont + "Arial, Helvetica, sans-serif;\n" + "}\n" + ".HEADING3 { font-size: " + heading3Size + "px;\n" + "            font-weight: bold;\n" + "            font-family: " + headingFont + "Arial, Helvetica, sans-serif;\n" + "}\n" + "BODY { color: " + fgColor + ";\n" + "       background-color: " + bgColor + ";\n" + "       font-size: " + bodySize + "px;\n" + "       font-family: " + bodyFont + "Times New Roman, Times, serif;\n" +
```

## 3.5 A Resumé Posting Service

## Listing 3.6 SubmitResume.java (continued)

```
"}\n" + "A:hover { color: red; }\n" + "-->\n" + "</STYLE>"; return(styleSheet); } // Replaces null strings (no such parameter name) or // empty strings (e.g., if textfield was blank) with // the replacement. Returns the original string otherwise. private String replaceIfMissing(String orig, String replacement) { if ((orig == null) || (orig.length() == 0)) { return(replacement); } else { return(orig); } } // Replaces null strings, empty strings, or the string // "default" with the replacement. // Returns the original string otherwise. private String replaceIfMissingOrDefault(String orig, String replacement) { if ((orig == null) || (orig.length() == 0) || (orig.equals("default"))) { return(replacement); } else { return(orig + ", "); } } // Takes a string representing an integer and returns it // as an int. Returns a default if the string is null // or in an illegal format. private int getSize(String sizeString, int defaultSize) { try { return(Integer.parseInt(sizeString)); } catch(NumberFormatException nfe) { return(defaultSize); } }
```

## Chapter 3 Handling the Client Request: Form Data

## Listing 3.6 SubmitResume.java (continued)

```
// Given "Java,C++,Lisp", "Java C++ Lisp" or // "Java, C++, Lisp", returns // "<UL> //   <LI>Java //   <LI>C++ //   <LI>Lisp //  </UL>" private String makeList(String listItems) { StringTokenizer tokenizer = new StringTokenizer(listItems, ", "); String list = "<UL>\n"; while(tokenizer.hasMoreTokens()) { list = list + "  <LI>" + tokenizer.nextToken() + "\n"; } list = list + "</UL>"; return(list); } // Show a confirmation page when they press the // "Submit" button. private void showConfirmation(HttpServletRequest request, PrintWriter out) { String title = "Submission Confirmed."; out.println(ServletUtilities.headWithTitle(title) + "<BODY>\n" + "<H1>" + title + "</H1>\n" + "Your resume should appear on-line within\n" + "24 hours. If it doesn't, try submitting\n" + "again with a different email address.\n" + "</BODY></HTML>"); } // Why it is bad to give your email address to untrusted sites private void storeResume(HttpServletRequest request) { String email = request.getParameter("email"); putInSpamList(email); } private void putInSpamList(String emailAddress) { // Code removed to protect the guilty. } }
```

## 3.5 A Resumé Posting Service

Figure 3-5 Front end to SubmitResume servlet.

<!-- image -->

## Chapter 3 Handling the Client Request: Form Data

Figure 3-6 SubmitResume servlet after 'Preview' button is pressed in Figure 3-5.

<!-- image -->

## Listing 3.7 HTML source of SubmitResume output shown in Figure 3-6.

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Resume for Al Gore Ithm</TITLE> <STYLE TYPE="text/css"> <!--.HEADING1 { font-size: 32px; font-weight: bold; font-family: Arial, Helvetica, sans-serif; }
```

## 3.5 A Resumé Posting Service

## Listing 3.7 HTML source of SubmitResume output shown in Figure 3-6. (continued)

.HEADING2 { font-size: 22px; font-weight: bold; font-family: Arial, Helvetica, sans-serif; } .HEADING3 { font-size: 19px; font-weight: bold; font-family: Arial, Helvetica, sans-serif; } BODY { color: BLACK; background-color: WHITE; font-size: 18px; font-family: Times New Roman, Times, serif; } A:hover { color: red; } --&gt; &lt;/STYLE&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;CENTER&gt; &lt;SPAN CLASS="HEADING1"&gt;Al Gore Ithm&lt;/SPAN&gt;&lt;BR&gt; &lt;SPAN CLASS="HEADING2"&gt;Chief Technology Officer&lt;BR&gt; &lt;A HREF="mailto:ithm@aol.com"&gt;ithm@aol.com&lt;/A&gt;&lt;/SPAN&gt; &lt;/CENTER&gt;&lt;BR&gt;&lt;BR&gt; &lt;SPAN CLASS="HEADING3"&gt;Programming Languages&lt;/SPAN&gt;

&lt;UL&gt;

&lt;LI&gt;Java

&lt;LI&gt;C++

&lt;LI&gt;Smalltalk

&lt;LI&gt;Ada

&lt;/UL&gt;&lt;BR&gt;&lt;BR&gt;

&lt;SPAN CLASS="HEADING3"&gt;Skills and Experience&lt;/SPAN&gt;&lt;BR&gt;&lt;BR&gt; Expert in data structures and computational methods.

&lt;P&gt;

Well known for finding efficient solutions to &lt;I&gt;apparently&lt;/I&gt; intractable problems, then rigorously proving time and memory requirements for best, worst, and average-case performance.

&lt;P&gt;

Can prove that P is not equal to NP. Doesn't want to work for companies that don't know what this means.

&lt;P&gt;

Not related to the American politician.

&lt;/BODY&gt;&lt;/HTML&gt;

## Chapter 3 Handling the Client Request: Form Data

Figure 3-7 Another possible result of SubmitResume servlet.

<!-- image -->

Figure 3-8 SubmitResume servlet when 'Submit' button is pressed.

<!-- image -->