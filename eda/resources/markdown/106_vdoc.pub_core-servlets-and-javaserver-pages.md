Chapter 12 Including Files and Applets in JSP Documents

## 12.3 Including Applets for the Java Plug-In

With JSP, you don't need any special syntax to include ordinary applets: just use the normal HTML APPLET tag. However, these applets must use JDK 1.1 or JDK 1.02 since neither Netscape 4.x nor Internet Explorer 5.x support the Java 2 platform (i.e., JDK 1.2). This lack of support imposes several restrictions on applets:

- · In order to use Swing, you must send the Swing files over the network. This process is time consuming and fails in Internet Explorer 3 and Netscape 3.x and 4.01-4.05 (which only support JDK 1.02), since Swing depends on JDK 1.1.
- · You cannot use Java 2D.
- · You cannot use the Java 2 collections package.
- · Your code runs more slowly, since most compilers for the Java 2 platform are significantly improved over their 1.1 predecessors.

Furthermore, early browser releases had a number of inconsistencies in the way they supported various AWT components, making testing and delivery of complex user interfaces more burdensome than it ought to have been. To address this problem, Sun developed a browser plug-in for Netscape and Internet Explorer that lets you use the Java 2 platform for applets in a variety of  browsers.  This  plug-in  is  available  at http://java.sun.com/products/plugin/ , and also comes bundled with JDK 1.2.2 and later. Since the plug-in is quite large (several megabytes), it is not reasonable to expect users on the WWW at large to download and install it just to run your applets. On the other hand, it is a reasonable alternative for fast corporate intranets, especially since applets can automatically prompt browsers that lack the plug-in to download it.

Unfortunately,  however,  the  normal APPLET tag  will  not  work  with  the plug-in, since browsers are specifically designed to use only their built-in virtual  machine  when  they  see APPLET .  Instead,  you  have  to  use  a  long  and messy OBJECT tag  for  Internet  Explorer and an  equally  long EMBED tag  for Netscape. Furthermore, since you typically don't know which browser type will  be  accessing  your  page,  you  have  to  either  include  both OBJECT and EMBED (placing the EMBED within the COMMENT section of OBJECT ) or identify the browser type at the time of the request and conditionally build the right tag. This process is straightforward but tedious and time consuming.

## 12.3 Including Applets for the Java Plug-In

The jsp:plugin element instructs the server to build a tag appropriate for applets that use the plug-in. Servers are permitted some leeway in exactly how they implement this support, but most simply include both OBJECT and EMBED .

## The jsp:plugin Element

The simplest way to use jsp:plugin is to supply four attributes: type , code , width , and height . You supply a value of applet for the type attribute and use the other three attributes in exactly the same way as with the APPLET element, with two exceptions: the attribute names are case sensitive, and single or  double  quotes  are  always  required  around  the  attribute  values.  So,  for example, you could replace

```
<APPLET CODE="MyApplet.class" </APPLET>
```

## with

```
WIDTH=475 HEIGHT=350> <jsp:plugin type="applet" code="MyApplet.class" width="475" height="350"> </jsp:plugin>
```

The jsp:plugin element has a number of other optional attributes. Most, but not all, parallel attributes of the APPLET element. Here is a full list.

## · type

For applets, this attribute should have a value of applet . However, the Java Plug-In also permits you to embed JavaBeans elements in Web pages. Use a value of bean in such a case.

## · code

This attribute is used identically to the CODE attribute of APPLET , specifying the top-level applet class file that extends Applet or JApplet . Just remember that the name code must be lower case with jsp:plugin (since it follows XML syntax), whereas with APPLET , case did not matter (since HTML attribute names are never case sensitive).

## · width

This attribute is used identically to the WIDTH attribute of APPLET , specifying the width in pixels to be reserved for the applet. Just remember that you must enclose the value in single or double quotes.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## Chapter 12 Including Files and Applets in JSP Documents

## · height

This attribute is used identically to the HEIGHT attribute of APPLET , specifying the height in pixels to be reserved for the applet. Just remember that you must enclose the value in single or double quotes.

## · codebase

This attribute is used identically to the CODEBASE attribute of APPLET , specifying the base directory for the applets. The code attribute is interpreted relative to this directory. As with the APPLET element, if you omit this attribute, the directory of the current page is used as the default. In the case of JSP, this default location is the directory where the original JSP file resided, not the system-specific location of the servlet that results from the JSP file.

## · align

This attribute is used identically to the ALIGN attribute of APPLET and IMG , specifying the alignment of the applet within the Web page. Legal values are left , right , top , bottom , and middle . With jsp:plugin , don't forget to include these values in single or double quotes, even though quotes are optional for APPLET and IMG .

## · hspace

This attribute is used identically to the HSPACE attribute of APPLET , specifying empty space in pixels reserved on the left and right of the applet. Just remember that you must enclose the value in single or double quotes.

## · vspace

This attribute is used identically to the VSPACE attribute of APPLET , specifying empty space in pixels reserved on the top and bottom of the applet. Just remember that you must enclose the value in single or double quotes.

## · archive

This attribute is used identically to the ARCHIVE attribute of APPLET , specifying a JAR file from which classes and images should be loaded.

## · name

This attribute is used identically to the NAME attribute of APPLET , specifying a name to use for inter-applet communication or for identifying the applet to scripting languages like JavaScript.

## · title

This attribute is used identically to the very rarely used TITLE attribute of APPLET (and virtually all other HTML elements in HTML 4.0), specifying a title that could be used for a tool-tip or for indexing.

## · jreversion

This attribute identifies the version of the Java Runtime Environment (JRE) that is required. The default is 1.1.

## · iepluginurl

This attribute designates a URL from which the plug-in for Internet Explorer can be downloaded. Users who don't already have the plug-in installed will be prompted to download it from this location. The default value will direct the user to the Sun site, but for intranet use you might want to direct the user to a local copy.

## · nspluginurl

This attribute designates a URL from which the plug-in for Netscape can be downloaded. The default value will direct the user to the Sun site, but for intranet use you might want to direct the user to a local copy.

## The jsp:param and jsp:params Elements

The jsp:param element is used with jsp:plugin in a manner similar to the way that PARAM is  used  with APPLET ,  specifying  a  name  and  value  that  are accessed from within the applet by getParameter . There are two main differences,  however.  First,  since jsp:param follows  XML  syntax,  attribute names must be lower case, attribute values must be enclosed in single or double  quotes,  and  the  element  must  end  with /&gt; ,  not  just &gt; .  Second,  all jsp:param entries must be enclosed within a jsp:params element.

## So, for example, you would replace

```
<APPLET CODE="MyApplet.class" WIDTH=475 HEIGHT=350> </APPLET>
```

```
<PARAM NAME="PARAM1" VALUE="VALUE1"> <PARAM NAME="PARAM2" VALUE="VALUE2"> with
```

```
<jsp:plugin type="applet" code="MyApplet.class" width="475" height="350"> <jsp:params>
```

&lt;jsp:param name="PARAM1" value="VALUE1" /&gt;

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 12.3 Including Applets for the Java Plug-In

## Chapter 12 Including Files and Applets in JSP Documents

&lt;jsp:param name="PARAM2" value="VALUE2" /&gt; &lt;/jsp:params&gt; &lt;/jsp:plugin&gt;

## The jsp:fallback Element

The jsp:fallback element provides alternative text to browsers that do not support OBJECT or EMBED .  You use this element in almost the same way as you  would  use  alternative  text  placed  within  an APPLET element.  So,  for example, you would replace

&lt;APPLET CODE="MyApplet.class" WIDTH=475 HEIGHT=350&gt;

&lt;B&gt;Error: this example requires Java.&lt;/B&gt;

&lt;/APPLET&gt;

## with

```
<jsp:plugin type="applet" code="MyApplet.class" width="475" height="350"> <jsp:fallback> <B>Error: this example requires Java.</B> </jsp:fallback> </jsp:plugin>
```

However, you should note that the  Java  Web  Server  2.0  has  a  bug  that causes it to fail when translating pages that include jsp:fallback elements. Tomcat,  the  JSWDK,  and  most  commercial  servers  handle jsp:fallback properly.

<!-- image -->

## Core Warning

The Java Web Server does not properly handle jsp:fallback .

## 12.3 Including Applets for the Java Plug-In

## Example: Building Shadowed Text

In  Section  7.5  (Using  Servlets  to  Generate  GIF  Images),  Listings  7.9  and 7.11 show a JFrame that uses Java 2D to create shadowed text in the size and font of the user's choosing. Listings 12.10 and 12.11 present an applet that uses Swing components to control this frame.

Since  the applet  uses  Swing  and  Java  2D, it  can  run  only  with  the  Java Plug-In. Listing 12.8 shows a page that uses jsp:plugin to load the applet. Listing 12.9 shows the HTML that results from this page (I added some line breaks for readability) and Figures 12-3 through 12-6 show some typical output.

## Listing 12.8 ShadowedTextApplet.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;Using jsp:plugin&lt;/TITLE&gt; &lt;LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;TABLE BORDER=5 ALIGN="CENTER"&gt; &lt;TR&gt;&lt;TH CLASS="TITLE"&gt; Using jsp:plugin&lt;/TABLE&gt; &lt;P&gt; &lt;CENTER&gt; &lt;jsp:plugin type="applet" code="coreservlets.ShadowedTextApplet.class" width="475" height="350"&gt; &lt;jsp:params&gt; &lt;jsp:param name="MESSAGE" value="Your Message Here" /&gt; &lt;/jsp:params&gt; &lt;/jsp:plugin&gt; &lt;/CENTER&gt; &lt;/BODY&gt; &lt;/HTML&gt;

## Chapter 12 Including Files and Applets in JSP Documents

## Listing 12.9 HTML resulting from ShadowedTextApplet.jsp . &lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;Using jsp:plugin&lt;/TITLE&gt; &lt;LINK REL=STYLESHEET HREF="JSP-Styles.css" TYPE="text/css"&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;TABLE BORDER=5 ALIGN="CENTER"&gt; &lt;TR&gt;&lt;TH CLASS="TITLE"&gt; Using jsp:plugin&lt;/TABLE&gt; &lt;P&gt; &lt;CENTER&gt; &lt;OBJECT classid="clsid:8AD9C840-044E-11D1-B3E9-00805F499D93" width="475"  height="350" codebase="http://java.sun.com/products/plugin/1.2.2/jin- stall-1\_2\_2-win.cab#Version=1,2,2,0"&gt; &lt;PARAM name="java\_code" value="coreservlets.ShadowedTextApplet.class"&gt; &lt;PARAM name="type" value="application/x-java-applet;"&gt; &lt;PARAM name="MESSAGE" value="Your Message Here"&gt; &lt;COMMENT&gt; &lt;EMBED type="application/x-java-applet;" width="475"  height="350" pluginspage="http://java.sun.com/products/plugin/" java\_code="coreservlets.ShadowedTextApplet.class" MESSAGE="Your Message Here" &gt; &lt;NOEMBED&gt; &lt;/COMMENT&gt; &lt;/NOEMBED&gt;&lt;/EMBED&gt; &lt;/OBJECT&gt; &lt;/CENTER&gt; &lt;/BODY&gt; &lt;/HTML&gt;

## 12.3 Including Applets for the Java Plug-In

## Listing 12.10 ShadowedTextApplet.java

```
package coreservlets; import java.awt.*; import javax.swing.*; import java.awt.event.*; /** Applet interface to the ShadowedTextFrame *  class. Requires Swing and Java 2D. */ public class ShadowedTextApplet extends JApplet implements ActionListener { private JTextField messageField; private JComboBox fontBox; private JSlider fontSizeSlider; private JButton showFrameButton; public void init() { WindowUtilities.setNativeLookAndFeel(); Color bgColor = new Color(0xFD, 0xF5, 0xE6); Font font = new Font("Serif", Font.PLAIN, 16); Container contentPane = getContentPane(); contentPane.setLayout(new GridLayout(4, 1)); contentPane.setBackground(bgColor); // Use a JTextField to gather the text for the message. // If the MESSAGE parameter is in the HTML, // use it as the initial value of this text field. messageField = new JTextField(20); String message = getParameter("MESSAGE"); if (message != null) { messageField.setText(message); } JPanel messagePanel = new LabelPanel("Message:", "Message to Display", bgColor, font, messageField); contentPane.add(messagePanel); // Use a JComboBox to let users choose any // font available on their system. GraphicsEnvironment env = GraphicsEnvironment.getLocalGraphicsEnvironment(); String[] fontNames = env.getAvailableFontFamilyNames();
```

## Chapter 12 Including Files and Applets in JSP Documents

## fontBox = new JComboBox(fontNames); fontBox.setEditable(false); JPanel fontPanel = new LabelPanel("Font:", "Font to Use", bgColor, font, fontBox); contentPane.add(fontPanel); // Use a JSlider to select the font size. fontSizeSlider = new JSlider(0, 150); fontSizeSlider.setBackground(bgColor); fontSizeSlider.setMajorTickSpacing(50); fontSizeSlider.setMinorTickSpacing(25); fontSizeSlider.setPaintTicks(true); fontSizeSlider.setPaintLabels(true); JPanel fontSizePanel = new LabelPanel("Font Size:", "Font Size to Use", bgColor, font, fontSizeSlider); contentPane.add(fontSizePanel); // Pressing the button will open the frame // that shows the shadowed text. showFrameButton = new JButton("Open Frame"); showFrameButton.addActionListener(this); JPanel buttonPanel = new LabelPanel("Show Shadowed Text:", "Open JFrame to Show Shadowed Text", bgColor, font, showFrameButton); contentPane.add(buttonPanel); } public void actionPerformed(ActionEvent event) { String message = messageField.getText(); if (message.length() == 0) { message = "No Message"; } String fontName = (String)fontBox.getSelectedItem(); int fontSize = fontSizeSlider.getValue(); JFrame frame = new JFrame("Shadowed Text"); JPanel panel = new ShadowedTextFrame(message, fontName, fontSize); frame.setContentPane(panel); frame.pack(); frame.setVisible(true); } } Listing 12.10 ShadowedTextApplet.java (continued)

## 12.3 Including Applets for the Java Plug-In

```
Listing 12.11 LabelPanel.java package coreservlets;
```

```
import java.awt.*; import javax.swing.*; /** A small JPanel that includes a JLabel to the left *  of a designated component. Also puts a titled border *  around the panel. */ public class LabelPanel extends JPanel { public LabelPanel(String labelMessage, String title, Color bgColor, Font font, JComponent component) { setBackground(bgColor); setFont(font); setBorder(BorderFactory.createTitledBorder(title)); JLabel label = new JLabel(labelMessage); label.setFont(font); add(label); component.setFont(font); add(component); } }
```

<!-- image -->

Chapter 12 Including Files and Applets in JSP Documents

<!-- image -->

Figure 12-3 Initial result of ShadowedTextApplet.jsp in a browser that has the JDK 1.2 plug-in installed.

<!-- image -->

Figure 12-4 ShadowedTextApplet.jsp after changing the message, font, and size entries.

## 12.3 Including Applets for the Java Plug-In

<!-- image -->

Figure 12-5 Result of pressing the 'Open Frame' button in Figure 12-4.

<!-- image -->

Figure 12-6 Another possible frame built by ShadowedTextApplet.jsp .

<!-- image -->