## 18.5 An Interactive Query Viewer

## Listing 18.13 EmployeeCreation.java (continued)

```
"(5, 'Frank', 'Function', 'Common Lisp', 51500)", "(6, 'Justin', 'Timecompiler', 'Java', 98000)", "(7, 'Sir', 'Vlet', 'Java', 114750)", "(8, 'Jay', 'Espy', 'Java', 128500)" }; return( DatabaseUtilities.createTable(driver, url, username, password, "employees", format, employees, close) ); } public static void main(String[] args) { if (args.length < 5) { printUsage(); return; } String vendorName = args[4]; int vendor = DriverUtilities.getVendor(vendorName); if (vendor == DriverUtilities.UNKNOWN) { printUsage(); return; } String driver = DriverUtilities.getDriver(vendor); String host = args[0]; String dbName = args[1]; String url = DriverUtilities.makeURL(host, dbName, vendor); String username = args[2]; String password = args[3]; createEmployees(driver, url, username, password, true); } private static void printUsage() { System.out.println("Usage: EmployeeCreation host dbName " + "username password oracle|sybase."); } }
```

## 18.5 An Interactive Query Viewer

Up to this point, all the database results have been based upon queries that were known at the time the program was written. In many real applications, however, queries are derived from user input that is not known until runtime.

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

Sometimes  the  queries  follow  a  fixed  format  even  though  certain  values change. You should make use of prepared statements in such a case; see Section 18.6 for details. Other times, however, even the query format is variable. Fortunately, this situation presents no problem, since ResultSetMetaData can  be  used  to  determine  the  number,  names,  and  types  of  columns  in  a ResultSet , as was discussed in Section 18.1 (Basic Steps in Using JDBC). In fact,  the  database  utilities  of  Listing  18.6  store  that  metadata  in  the DBResults object that is returned from the showQueryData method. Access to this metadata makes it straightforward to implement an interactive graphical query viewer as shown in Figures 18-1 through 18-5. The code to accomplish this result is presented in the following subsection.

Figure 18-1 Initial appearance of the query viewer.

<!-- image -->

| ID   | FIRSTNAME   | LASTNAME     | LANGUAGE    | SALARY   |
|------|-------------|--------------|-------------|----------|
|      | Wye         | Tukay        | COBOL       |          |
| 2    | Britt       | Tell         | Ct+         | 62000    |
| 3    | Max         | Manager      | none        | 15500    |
|      | Polly       | Morphic      | Smalltalk   | 51500    |
| 5    | Frank       | Function     | Common Lisp | 51500    |
| 6    | Justin      | Timecompiler | Java        | 98000    |
|      | Sir         | Vlet         | Java        | 114750   |
|      | Jay         | Espy         | Java        | 128500   |

Figure 18-2 Query viewer after a request for the complete employees table from an Oracle database.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.5 An Interactive Query Viewer

Figure 18-3 Query viewer after a request for part of the employees table from an Oracle database.

<!-- image -->

Figure 18-4 Query viewer after a request for the complete fruits table from a Sybase database.

<!-- image -->

## Query Viewer Code

Building  the  display  shown  in  Figures  18-1  through  18-5  is  relatively straightforward.  In  fact,  given  the  database  utilities  shown  earlier,  it  takes substantially more code to build the user interface than it does to communicate with the database. The full code is shown in Listing 18.14, but I'll give a

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

Figure 18-5 Query viewer after a request for part of the fruits table from a Sybase database.

<!-- image -->

quick  summary of  the  process  that  takes  place  when  the  user  presses  the 'Show Results' button.

First, the system reads the host, port, database name, username, password, and driver type from the user interface elements shown. Next, it submits the query and stores the result, as below:

```
DBResults results = DatabaseUtilities.getQueryResults(driver, url, username, password, query, true);
```

Next, the system passes these results to a custom table model (see Listing 18.15). If you are not familiar with the Swing GUI library, a table model acts as the glue between a JTable and the actual data.

DBResultsTableModel model = new DBResultsTableModel(results); JTable table = new JTable(model);

Finally, the system places this JTable in the bottom region of the JFrame and calls pack to tell the JFrame to resize itself to fit the table.

## 18.5 An Interactive Query Viewer

## Listing 18.14 QueryViewer.java

```
package coreservlets; import java.awt.*; import java.awt.event.*; import javax.swing.*; import javax.swing.table.*; /** An interactive database query viewer. Connects to *  the specified Oracle or Sybase database, executes a query, *  and presents the results in a JTable. */ public class QueryViewer extends JFrame implements ActionListener{ public static void main(String[] args) { new QueryViewer(); } private JTextField hostField, dbNameField, queryField, usernameField; private JRadioButton oracleButton, sybaseButton; private JPasswordField passwordField; private JButton showResultsButton; private Container contentPane; private JPanel tablePanel; public QueryViewer () { super("Database Query Viewer"); WindowUtilities.setNativeLookAndFeel(); addWindowListener(new ExitListener()); contentPane = getContentPane(); contentPane.add(makeControlPanel(), BorderLayout.NORTH); pack(); setVisible(true); } /** When the "Show Results" button is pressed or *  RETURN is hit while the query textfield has the *  keyboard focus, a database lookup is performed, *  the results are placed in a JTable, and the window *  is resized to accommodate the table. */ public void actionPerformed(ActionEvent event) { String host = hostField.getText(); String dbName = dbNameField.getText(); String username = usernameField.getText();
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## String password = String.valueOf(passwordField.getPassword()); String query = queryField.getText(); int vendor; if (oracleButton.isSelected()) { vendor = DriverUtilities.ORACLE; } else { vendor = DriverUtilities.SYBASE; } if (tablePanel != null) { contentPane.remove(tablePanel); } tablePanel = makeTablePanel(host, dbName, vendor, username, password, query); contentPane.add(tablePanel, BorderLayout.CENTER); pack(); } // Executes a query and places the result in a // JTable that is, in turn, inside a JPanel. private JPanel makeTablePanel(String host, String dbName, int vendor, String username, String password, String query) { String driver = DriverUtilities.getDriver(vendor); String url = DriverUtilities.makeURL(host, dbName, vendor); DBResults results = DatabaseUtilities.getQueryResults(driver, url, username, password, query, true); JPanel panel = new JPanel(new BorderLayout()); if (results == null) { panel.add(makeErrorLabel()); return(panel); } DBResultsTableModel model = new DBResultsTableModel(results); JTable table = new JTable(model); table.setFont(new Font("Serif", Font.PLAIN, 17)); table.setRowHeight(28); JTableHeader header = table.getTableHeader(); header.setFont(new Font("SansSerif", Font.BOLD, 13)); panel.add(table, BorderLayout.CENTER); panel.add(header, BorderLayout.NORTH); Listing 18.14 QueryViewer.java (continued)

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 18.5 An Interactive Query Viewer

## panel.setBorder (BorderFactory.createTitledBorder("Query Results")); return(panel); } // The panel that contains the textfields, check boxes, // and button. private JPanel makeControlPanel() { JPanel panel = new JPanel(new GridLayout(0, 1)); panel.add(makeHostPanel()); panel.add(makeUsernamePanel()); panel.add(makeQueryPanel()); panel.add(makeButtonPanel()); panel.setBorder (BorderFactory.createTitledBorder("Query Data")); return(panel); } // The panel that has the host and db name textfield and // the driver radio buttons. Placed in control panel. private JPanel makeHostPanel() { JPanel panel = new JPanel(); panel.add(new JLabel("Host:")); hostField = new JTextField(15); panel.add(hostField); panel.add(new JLabel("    DB Name:")); dbNameField = new JTextField(15); panel.add(dbNameField); panel.add(new JLabel("    Driver:")); ButtonGroup vendorGroup = new ButtonGroup(); oracleButton = new JRadioButton("Oracle", true); vendorGroup.add(oracleButton); panel.add(oracleButton); sybaseButton = new JRadioButton("Sybase"); vendorGroup.add(sybaseButton); panel.add(sybaseButton); return(panel); } // The panel that has the username and password textfields. // Placed in control panel. private JPanel makeUsernamePanel() { JPanel panel = new JPanel(); usernameField = new JTextField(10); Listing 18.14 QueryViewer.java (continued)

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.14 QueryViewer.java (continued)

```
passwordField = new JPasswordField(10); panel.add(new JLabel("Username: ")); panel.add(usernameField); panel.add(new JLabel("    Password:")); panel.add(passwordField); return(panel); } // The panel that has textfield for entering queries. // Placed in control panel. private JPanel makeQueryPanel() { JPanel panel = new JPanel(); queryField = new JTextField(40); queryField.addActionListener(this); panel.add(new JLabel("Query:")); panel.add(queryField); return(panel); } // The panel that has the "Show Results" button. // Placed in control panel. private JPanel makeButtonPanel() { JPanel panel = new JPanel(); showResultsButton = new JButton("Show Results"); showResultsButton.addActionListener(this); panel.add(showResultsButton); return(panel); } // Shows warning when bad query sent. private JLabel makeErrorLabel() { JLabel label = new JLabel("No Results", JLabel.CENTER); label.setFont(new Font("Serif", Font.BOLD, 36)); return(label); } }
```

## 18.5 An Interactive Query Viewer

```
Listing 18.15 DBResultsTableModel.java package coreservlets;
```

```
import javax.swing.table.*; /** Simple class that tells a JTable how to extract *  relevant data from a DBResults object (which is *  used to store the results from a database query). */
```

```
public class DBResultsTableModel extends AbstractTableModel { private DBResults results; public DBResultsTableModel(DBResults results) { this.results = results; } public int getRowCount() { return(results.getRowCount()); } public int getColumnCount() { return(results.getColumnCount()); } public String getColumnName(int column) { return(results.getColumnNames()[column]); } public Object getValueAt(int row, int column) { return(results.getRow(row)[column]); } }
```

## Chapter 18 JDBC and Database Connection Pooling

## Listing 18.16 WindowUtilities.java

```
package coreservlets; import javax.swing.*; import java.awt.*; /** A few utilities that simplify using windows in Swing. */ public class WindowUtilities { /** Tell system to use native look and feel, as in previous *  releases. Metal (Java) LAF is the default otherwise. */ public static void setNativeLookAndFeel() { try { UIManager.setLookAndFeel (UIManager.getSystemLookAndFeelClassName()); } catch(Exception e) { System.out.println("Error setting native LAF: " + e); } } public static void setJavaLookAndFeel() { try { UIManager.setLookAndFeel (UIManager.getCrossPlatformLookAndFeelClassName()); } catch(Exception e) { System.out.println("Error setting Java LAF: " + e); } } public static void setMotifLookAndFeel() { try { UIManager.setLookAndFeel ("com.sun.java.swing.plaf.motif.MotifLookAndFeel"); } catch(Exception e) { System.out.println("Error setting Motif LAF: " + e); } } }
```