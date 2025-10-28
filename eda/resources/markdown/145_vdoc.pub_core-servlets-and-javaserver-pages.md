## 17.2 A Multisystem Search Engine Front End

encode the value of each entry, but not the equal sign (=) between each entry name and its value or the ampersand (&amp;) between each name/value pair. So, you  cannot  necessarily  simply  call URLEncoder.encode(someData) but instead need to selectively encode the value parts of each name/value pair. This could be accomplished as follows:

```
String someData = name1 + "=" + URLEncoder.encode(val1) + "&" + name2 + "=" + URLEncoder.encode(val2) + "&" + ... nameN + "=" + URLEncoder.encode(valN); try { URL programURL = new URL(baseURL + "?" + someData); getAppletContext().showDocument(programURL); } catch(MalformedURLException mue) { ... }
```

The following section gives a full-fledged example.

## 17.2 A Multisystem Search Engine Front End

In Section 6.3 (A Front End to Various Search Engines), the SearchSpec class  (Listing  6.2)  was  used  by  a  servlet  to  generate  the  specific  URLs needed  to  redirect  requests  to  various  different  search  engines.  The SearchSpec class  can  be  used  by  applets  as  well.  Listing  17.1  shows  an applet that creates a textfield to gather user input. When the user submits the data, the applet URL-encodes the textfield value and generates three distinct URLs with embedded GET data: one each for the Google, Infoseek, and Lycos search engines. The applet then uses showDocument to instruct the browser to display the results of those URLs in three different frame cells. The results are shown in Figures 17-1 and 17-2. HTML forms cannot be used for this application since a form can submit its data to only a single URL.

Listing 17.2 shows the top-level HTML document used and Listing 17.3 shows the HTML used for the frame cell actually containing the applet. Please refer to this book's Web site ( http://www.coreservlets.com/ ) for the three tiny HTML files used for the initial contents of the bottom three frame cells shown in Figure 17-1.

## Chapter 17 Using Applets As Servlet Front Ends

## Listing 17.1 SearchApplet.java

```
import java.applet.Applet; import java.awt.*; import java.awt.event.*; import java.net.*;
```

import coreservlets.SearchSpec;

/** An applet that reads a value from a TextField,

- *  then uses it to build three distinct URLs with embedded
- *  GET data: one each for Google, Infoseek, and Lycos.
- *  The browser is directed to retrieve each of these
- *  URLs, displaying them in side-by-side frame cells.
- *  Note that standard HTML forms cannot automatically
- *  perform multiple submissions in this manner.

*/

```
public class SearchApplet extends Applet implements ActionListener { private TextField queryField; private Button submitButton; public void init() { setFont(new Font("Serif", Font.BOLD, 18)); add(new Label("Search String:")); queryField = new TextField(40); queryField.addActionListener(this); add(queryField); submitButton = new Button("Send to Search Engines"); submitButton.addActionListener(this); add(submitButton); } /** Submit data when button is pressed <B>or</B> *  user presses Return in the TextField. */ public void actionPerformed(ActionEvent event) { String query = URLEncoder.encode(queryField.getText()); SearchSpec[] commonSpecs = SearchSpec.getCommonSpecs(); // Omitting HotBot (last entry), as they use JavaScript to // pop result to top-level frame. Thus the length-1 below. for(int i=0; i<commonSpecs.length-1; i++) { try { SearchSpec spec = commonSpecs[i]; // The SearchSpec class builds URLs of the // form needed by some common search engines. URL searchURL = new URL(spec.makeURL(query, "10")); String frameName = "results" + i; getAppletContext().showDocument(searchURL, frameName); } catch(MalformedURLException mue) {} } } }
```

## 17.2 A Multisystem Search Engine Front End

Figure 17-1 SearchApplet allows the user to enter a search string.

<!-- image -->

Figure 17-2 Submitting the query yields side-by-side results from three different search engines.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.