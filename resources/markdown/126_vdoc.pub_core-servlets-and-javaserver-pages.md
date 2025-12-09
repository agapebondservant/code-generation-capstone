## Chapter 15 Integrating Servlets and JSP

The same approach is required for addresses used in &lt;IMG SRC=...&gt; and &lt;A HREF=...&gt; .

## Alternative Means of Getting a RequestDispatcher

In servers that support version 2.2 of the servlet specification, there are two  additional  ways  of  obtaining  a RequestDispatcher besides  the getRequestDispatcher method of ServletContext .

First,  since  most  servers  let  you  give  explicit  names  to  servlets  or  JSP pages, it makes sense to access them by name rather than by path. Use the getNamedDispatcher method of ServletContext for this task.

Second, you might want to access a resource by a path relative to the current servlet's location, rather than relative to the server root. This approach is not common when servlets are accessed in the standard manner ( http://host/servlet/ServletName ),  because  JSP  files  would  not  be accessible  by  means  of http://host/servlet/... since  that  URL  is reserved especially  for  servlets.  However,  it  is  common  to  register  servlets under  another  path,  and  in  such  a  case  you  can  use  the getRequestDispatcher method  of HttpServletRequest rather  than  the  one  from ServletContext . For example, if the originating servlet is at http://host/travel/TopLevel ,

getServletContext().getRequestDispatcher("/travel/cruises.jsp")

could be replaced by request.getRequestDispatcher("cruises.jsp");

## 15.2 Example:  An On-Line Travel Agent

Consider the case of an on-line travel agent that has a quick-search page, as shown  in  Figure  15-1  and  Listing  15.2.  Users  need  to  enter  their  e-mail address and password to associate the request with their previously established customer  account.  Each  request  also  includes  a  trip  origin,  trip  destination, start date, and end date. However, the action that will result will vary substan-

## 15.2 Example: An On-Line Travel Agent

tially  based  upon  the  action  requested.  For  example,  pressing  the  'Book Flights'  button should show a list  of available flights on the dates specified, ordered by price (see Figure 15-1). The user's real name, frequent flyer information, and credit card number should be used to generate the page. On the other hand, selecting 'Edit Account' should show any previously entered customer information, letting the user modify values or add entries. Likewise, the actions resulting from choosing 'Rent Cars' or 'Find Hotels' will share much of the same customer data but will have a totally different presentation.

To accomplish the desired behavior, the front end (Listing 15.2) submits the request to the top-level travel servlet shown in Listing 15.3. This servlet looks up the customer information (see Listings 15.5 through 15.9), puts it in the HttpSession object associating the value (of type coreservlets.TravelCustomer )  with the name customer ,  and then forwards the request to a different JSP page corresponding to each of the possible actions. The destination page (see Listing 15.4 and the result in Figure 15-2) looks up the customer information by means of

```
<jsp:useBean id="customer" class="coreservlets.TravelCustomer" scope="session" />
```

then  uses jsp:getProperty to  insert  customer  information  into  various parts  of  the  page.  You  should  note  two  things  about  the TravelCustomer class (Listing 15.5).

First, the class spends a considerable amount of effort making the customer information accessible as plain strings or even HTML-formatted strings through simple  properties.  Almost  every  task  that  requires  any  substantial  amount  of programming at all is spun off into the bean, rather than being performed in the JSP page itself. This is typical of servlet/JSP integration-the use of JSP does not entirely obviate the need to format data as strings or HTML in Java code. Significant up-front effort to make the data conveniently available to JSP more than pays for itself when multiple JSP pages access the same type of data.

Second, remember that many servers that automatically reload servlets when their  class  files  change  do  not  allow  bean  classes  used  by  JSP  to  be  in the auto-reloading  directories.  Thus,  with  the  Java  Web  Server  for  example, TravelCustomer and its supporting classes  must  be in install\_dir / classes/coreservlets/ , not install\_dir /servlets/coreservlets/ . Tomcat  3.0  and  the  JSWDK  1.0.1  do  not  support  auto-reloading  servlets,  so TravelCustomer can be installed in the normal location.

Chapter 15 Integrating Servlets and JSP

Figure 15-1 Front end to travel servlet (see Listing 15.2).

<!-- image -->

## 15.2 Example: An On-Line Travel Agent

Figure 15-2 Result of travel servlet (Listing 15.3) dispatching request to BookFlights.jsp (Listing 15.4).

<!-- image -->

## Listing 15.2 / travel/quick-search.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Online Travel Quick Search</TITLE> <LINK REL=STYLESHEET HREF="travel-styles.css" TYPE="text/css"> </HEAD>
```

## Chapter 15 Integrating Servlets and JSP

## Listing 15.2 / travel/quick-search.html (continued)

&lt;BODY&gt;

&lt;BR&gt;

&lt;H1&gt;Online Travel Quick Search&lt;/H1&gt;

&lt;FORM ACTION="/servlet/coreservlets.Travel" METHOD="POST"&gt; &lt;CENTER&gt;

Email address: &lt;INPUT TYPE="TEXT" NAME="emailAddress"&gt;&lt;BR&gt; Password: &lt;INPUT TYPE="PASSWORD" NAME="password" SIZE=10&gt;&lt;BR&gt; Origin: &lt;INPUT TYPE="TEXT" NAME="origin"&gt;&lt;BR&gt; Destination: &lt;INPUT TYPE="TEXT" NAME="destination"&gt;&lt;BR&gt;

Start date (MM/DD/YY):

&lt;INPUT TYPE="TEXT" NAME="startDate" SIZE=8&gt;&lt;BR&gt;

End date (MM/DD/YY):

&lt;INPUT TYPE="TEXT" NAME="endDate" SIZE=8&gt;&lt;BR&gt;

&lt;P&gt;

&lt;TABLE CELLSPACING=1&gt;

## &lt;TR&gt;

&lt;TH&gt;&amp;nbsp;&lt;IMG SRC="airplane.gif" WIDTH=100 HEIGHT=29

ALIGN="TOP" ALT="Book Flight"&gt;&amp;nbsp;

&lt;TH&gt;&amp;nbsp;&lt;IMG SRC="car.gif" WIDTH=100 HEIGHT=31

ALIGN="MIDDLE" ALT="Rent Car"&gt;&amp;nbsp;

&lt;TH&gt;&amp;nbsp;&lt;IMG SRC="bed.gif" WIDTH=100 HEIGHT=85

ALIGN="MIDDLE" ALT="Find Hotel"&gt;&amp;nbsp;

&lt;TH&gt;&amp;nbsp;&lt;IMG SRC="passport.gif" WIDTH=71 HEIGHT=100

ALIGN="MIDDLE" ALT="Edit Account"&gt;&amp;nbsp;

## &lt;TR&gt;

&lt;TH&gt;&lt;SMALL&gt;

&lt;INPUT TYPE="SUBMIT" NAME="flights" VALUE="Book Flight"&gt; &lt;/SMALL&gt;

&lt;TH&gt;&lt;SMALL&gt;

&lt;INPUT TYPE="SUBMIT" NAME="cars" VALUE="Rent Car"&gt;

&lt;/SMALL&gt;

&lt;TH&gt;&lt;SMALL&gt;

&lt;INPUT TYPE="SUBMIT" NAME="hotels" VALUE="Find Hotel"&gt;

&lt;/SMALL&gt;

&lt;TH&gt;&lt;SMALL&gt;

&lt;INPUT TYPE="SUBMIT" NAME="account" VALUE="Edit Account"&gt; &lt;/SMALL&gt;

&lt;/TABLE&gt;

&lt;/CENTER&gt;

&lt;/FORM&gt;

&lt;BR&gt;

&lt;P ALIGN="CENTER"&gt;

&lt;B&gt;Not yet a member? Get a free account

&lt;A HREF="accounts.jsp"&gt;here&lt;/A&gt;.&lt;/B&gt;&lt;/P&gt;

&lt;/BODY&gt;

&lt;/HTML&gt;

## Listing 15.3 Travel.java

package coreservlets;

```
import java.io.*; import javax.servlet.*; import javax.servlet.http.*;
```

/** Top-level travel-processing servlet. This servlet sets up

- *  the customer data as a bean, then forwards the request
- *  to the airline booking page, the rental car reservation
- *  page, the hotel page, the existing account modification
- *  page, or the new account page.

*/

```
public class Travel extends HttpServlet { private TravelCustomer[] travelData; public void init() { travelData = TravelData.getTravelData(); }
```

/** Since password is being sent, use POST only. However,

- *  the use of POST means that you cannot forward
- *  the request to a static HTML page, since the forwarded
- *  request uses the same request method as the original
- *  one, and static pages cannot handle POST. Solution:
- *  have the "static" page be a JSP file that contains
- *  HTML only. That's what accounts.jsp is. The other
- *  JSP files really need to be dynamically generated,
- *  since they make use of the customer data.

*/

```
public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { String emailAddress = request.getParameter("emailAddress"); String password = request.getParameter("password"); TravelCustomer customer = TravelCustomer.findCustomer(emailAddress, travelData); if ((customer == null) || (password == null) || (!password.equals(customer.getPassword()))) { gotoPage("/travel/accounts.jsp", request, response); } // The methods that use the following parameters will // check for missing or malformed values. customer.setStartDate(request.getParameter("startDate")); customer.setEndDate(request.getParameter("endDate")); customer.setOrigin(request.getParameter("origin"));
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 15.2 Example: An On-Line Travel Agent

## Chapter 15 Integrating Servlets and JSP

## Listing 15.3 Travel.java (continued)

```
customer.setDestination(request.getParameter ("destination")); HttpSession session = request.getSession(true); session.putValue("customer", customer); if (request.getParameter("flights") != null) { gotoPage("/travel/BookFlights.jsp", request, response); } else if (request.getParameter("cars") != null) { gotoPage("/travel/RentCars.jsp", request, response); } else if (request.getParameter("hotels") != null) { gotoPage("/travel/FindHotels.jsp", request, response); } else if (request.getParameter("cars") != null) { gotoPage("/travel/EditAccounts.jsp", request, response); } else { gotoPage("/travel/IllegalRequest.jsp", request, response);
```

}

}

private void gotoPage(String address, HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

RequestDispatcher dispatcher = getServletContext().getRequestDispatcher(address); dispatcher.forward(request, response);

}

}

## 15.2 Example: An On-Line Travel Agent

## Listing 15.4 BookFlights.jsp

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"&gt; &lt;HTML&gt; &lt;HEAD&gt; &lt;TITLE&gt;Best Available Flights&lt;/TITLE&gt; &lt;LINK REL=STYLESHEET HREF="/travel/travel-styles.css" TYPE="text/css"&gt; &lt;/HEAD&gt; &lt;BODY&gt; &lt;H1&gt;Best Available Flights&lt;/H1&gt; &lt;CENTER&gt; &lt;jsp:useBean id="customer" class="coreservlets.TravelCustomer" scope="session" /&gt; Finding flights for &lt;jsp:getProperty name="customer" property="fullName" /&gt; &lt;P&gt; &lt;jsp:getProperty name="customer" property="flights" /&gt; &lt;P&gt; &lt;BR&gt; &lt;HR&gt; &lt;BR&gt; &lt;FORM ACTION="/servlet/BookFlight"&gt; &lt;jsp:getProperty name="customer" property="frequentFlyerTable" /&gt; &lt;P&gt; &lt;B&gt;Credit Card:&lt;/B&gt; &lt;jsp:getProperty name="customer" property="creditCard" /&gt; &lt;P&gt; &lt;INPUT TYPE="SUBMIT" NAME="holdButton" VALUE="Hold for 24 Hours"&gt; &lt;P&gt; &lt;INPUT TYPE="SUBMIT" NAME="bookItButton" VALUE="Book It!"&gt; &lt;/FORM&gt; &lt;/CENTER&gt; &lt;/BODY&gt; &lt;/HTML&gt;

## Chapter 15 Integrating Servlets and JSP

## Listing 15.5 TravelCustomer.java

```
package coreservlets; import java.util.*; import java.text.*; /** Describes a travel services customer. Implemented *  as a bean with some methods that return data in HTML *  format, suitable for access from JSP. */ public class TravelCustomer { private String emailAddress, password, firstName, lastName; private String creditCardName, creditCardNumber; private String phoneNumber, homeAddress; private String startDate, endDate; private String origin, destination; private FrequentFlyerInfo[] frequentFlyerData; private RentalCarInfo[] rentalCarData; private HotelInfo[] hotelData; public TravelCustomer(String emailAddress, String password, String firstName, String lastName, String creditCardName, String creditCardNumber, String phoneNumber, String homeAddress, FrequentFlyerInfo[] frequentFlyerData, RentalCarInfo[] rentalCarData, HotelInfo[] hotelData) { setEmailAddress(emailAddress); setPassword(password); setFirstName(firstName); setLastName(lastName); setCreditCardName(creditCardName); setCreditCardNumber(creditCardNumber); setPhoneNumber(phoneNumber); setHomeAddress(homeAddress); setStartDate(startDate); setEndDate(endDate); setFrequentFlyerData(frequentFlyerData); setRentalCarData(rentalCarData); setHotelData(hotelData); }
```

## 15.2 Example: An On-Line Travel Agent

## public String getEmailAddress() { return(emailAddress); } public void setEmailAddress(String emailAddress) { this.emailAddress = emailAddress; } public String getPassword() { return(password); } public void setPassword(String password) { this.password = password; } public String getFirstName() { return(firstName); } public void setFirstName(String firstName) { this.firstName = firstName; } public String getLastName() { return(lastName); } public void setLastName(String lastName) { this.lastName = lastName; } public String getFullName() { return(getFirstName() + " " + getLastName()); } public String getCreditCardName() { return(creditCardName); } public void setCreditCardName(String creditCardName) { this.creditCardName = creditCardName; } public String getCreditCardNumber() { return(creditCardNumber); } Listing 15.5 TravelCustomer.java (continued)

<!-- image -->

## 368

## Chapter 15 Integrating Servlets and JSP

## Listing 15.5 TravelCustomer.java (continued)

```
public void setCreditCardNumber(String creditCardNumber) { this.creditCardNumber = creditCardNumber; } public String getCreditCard() { String cardName = getCreditCardName(); String cardNum = getCreditCardNumber(); cardNum = cardNum.substring(cardNum.length() - 4); return(cardName + " (XXXX-XXXX-XXXX-" + cardNum + ")"); } public String getPhoneNumber() { return(phoneNumber); } public void setPhoneNumber(String phoneNumber) { this.phoneNumber = phoneNumber; } public String getHomeAddress() { return(homeAddress); } public void setHomeAddress(String homeAddress) { this.homeAddress = homeAddress; } public String getStartDate() { return(startDate); } public void setStartDate(String startDate) { this.startDate = startDate; } public String getEndDate() { return(endDate); } public void setEndDate(String endDate) { this.endDate = endDate; } public String getOrigin() { return(origin); }
```

## 15.2 Example: An On-Line Travel Agent

## Listing 15.5 TravelCustomer.java (continued)

```
public void setOrigin(String origin) { this.origin = origin; } public String getDestination() { return(destination); } public void setDestination(String destination) { this.destination = destination; } public FrequentFlyerInfo[] getFrequentFlyerData() { return(frequentFlyerData); } public void setFrequentFlyerData(FrequentFlyerInfo[] frequentFlyerData) { this.frequentFlyerData = frequentFlyerData; } public String getFrequentFlyerTable() { FrequentFlyerInfo[] frequentFlyerData = getFrequentFlyerData(); if (frequentFlyerData.length == 0) { return("<I>No frequent flyer data recorded.</I>"); } else { String table = "<TABLE>\n" + "  <TR><TH>Airline<TH>Frequent Flyer Number\n"; for(int i=0; i<frequentFlyerData.length; i++) { FrequentFlyerInfo info = frequentFlyerData[i]; table = table + "<TR ALIGN=\"CENTER\">" + "<TD>" + info.getAirlineName() + "<TD>" + info.getFrequentFlyerNumber() + "\n"; } table = table + "</TABLE>\n"; return(table); } } public RentalCarInfo[] getRentalCarData() { return(rentalCarData); }
```

## Chapter 15 Integrating Servlets and JSP

## Listing 15.5 TravelCustomer.java (continued)

```
public void setRentalCarData(RentalCarInfo[] rentalCarData) { this.rentalCarData = rentalCarData; } public HotelInfo[] getHotelData() { return(hotelData); } public void setHotelData(HotelInfo[] hotelData) { this.hotelData = hotelData; } // This would be replaced by a database lookup // in a real application. public String getFlights() { String flightOrigin = replaceIfMissing(getOrigin(), "Nowhere"); String flightDestination = replaceIfMissing(getDestination(), "Nowhere"); Date today = new Date(); DateFormat formatter = DateFormat.getDateInstance(DateFormat.MEDIUM); String dateString = formatter.format(today); String flightStartDate = replaceIfMissing(getStartDate(), dateString); String flightEndDate = replaceIfMissing(getEndDate(), dateString); String [][] flights = { { "Java Airways", "1522", "455.95", "Java, Indonesia", "Sun Microsystems", "9:00", "3:15" }, { "Servlet Express", "2622", "505.95", "New Atlanta", "New Atlanta", "9:30", "4:15" }, { "Geek Airlines", "3.14159", "675.00", "JHU", "MIT", "10:02:37", "2:22:19" } }; String flightString = ""; for(int i=0; i<flights.length; i++) { String[] flightInfo = flights[i];
```

## 15.2 Example: An On-Line Travel Agent

## Listing 15.5 TravelCustomer.java (continued)

```
flightString = flightString + getFlightDescription(flightInfo[0], flightInfo[1], flightInfo[2], flightInfo[3], flightInfo[4], flightInfo[5], flightInfo[6], flightOrigin, flightDestination, flightStartDate, flightEndDate); } return(flightString); } private String getFlightDescription(String airline, String flightNum, String price, String stop1, String stop2, String time1, String time2, String flightOrigin, String flightDestination, String flightStartDate, String flightEndDate) { String flight = "<P><BR>\n" + "<TABLE WIDTH=\"100%\"><TR><TH CLASS=\"COLORED\">\n" + "<B>" + airline + " Flight " + flightNum + " ($" + price + ")</B></TABLE><BR>\n" + "<B>Outgoing:</B> Leaves " + flightOrigin + " at " + time1 + " AM on " + flightStartDate + ", arriving in " + flightDestination + " at " + time2 + " PM (1 stop -- " + stop1 + ").\n" + "<BR>\n" + "<B>Return:</B> Leaves " + flightDestination + " at " + time1 + " AM on " + flightEndDate + ", arriving in " + flightOrigin + " at " + time2 + " PM (1 stop -- " + stop2 + ").\n"; return(flight); }
```

## 372 Chapter 15 Integrating Servlets and JSP

## Listing 15.5 TravelCustomer.java (continued)

```
private String replaceIfMissing(String value, String defaultValue) { if ((value != null) && (value.length() > 0)) { return(value); } else { return(defaultValue); } } public static TravelCustomer findCustomer (String emailAddress, TravelCustomer[] customers) { if (emailAddress == null) { return(null); } for(int i=0; i<customers.length; i++) { String custEmail = customers[i].getEmailAddress(); if (emailAddress.equalsIgnoreCase(custEmail)) { return(customers[i]); } } return(null); } }
```

## Listing 15.6 TravelData.java

package coreservlets;

/** This class simply sets up some static data to

- *  describe some supposed preexisting customers.
- *  Use a database call in a real application. See
- *  CSAJSP Chapter 18 for many examples of the use
- *  of JDBC from servlets.

*/

```
public class TravelData { private static FrequentFlyerInfo[] janeFrequentFlyerData = { new FrequentFlyerInfo("Java Airways", "123-4567-J"), new FrequentFlyerInfo("Delta", "234-6578-D") }; private static RentalCarInfo[] janeRentalCarData = { new RentalCarInfo("Alamo", "345-AA"), new RentalCarInfo("Hertz", "456-QQ-H"), new RentalCarInfo("Avis", "V84-N8699") };
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 15.2 Example: An On-Line Travel Agent

## Listing 15.6 TravelData.java (continued)

```
private static HotelInfo[] janeHotelData = { new HotelInfo("Marriot", "MAR-666B"), new HotelInfo("Holiday Inn", "HI-228-555") }; private static FrequentFlyerInfo[] joeFrequentFlyerData = { new FrequentFlyerInfo("Java Airways", "321-9299-J"), new FrequentFlyerInfo("United", "442-2212-U"), new FrequentFlyerInfo("Southwest", "1A345") }; private static RentalCarInfo[] joeRentalCarData = { new RentalCarInfo("National", "NAT00067822") }; private static HotelInfo[] joeHotelData = { new HotelInfo("Red Roof Inn", "RRI-PREF-236B"), new HotelInfo("Ritz Carlton", "AA0012") }; private static TravelCustomer[] travelData = { new TravelCustomer("jane@somehost.com", "tarzan52", "Jane", "Programmer", "Visa", "1111-2222-3333-6755", "(123) 555-1212", "6 Cherry Tree Lane\n" + "Sometown, CA 22118", janeFrequentFlyerData, janeRentalCarData, janeHotelData), new TravelCustomer("joe@somehost.com", "qWeRtY", "Joe", "Hacker", "JavaSmartCard", "000-1111-2222-3120", "(999) 555-1212", "55 25th St., Apt 2J\n" + "New York, NY 12345", joeFrequentFlyerData, joeRentalCarData, joeHotelData) }; public static TravelCustomer[] getTravelData() { return(travelData); } }
```

## 374

## Chapter 15 Integrating Servlets and JSP

## Listing 15.7 FrequentFlyerInfo.java

package coreservlets;

/** Simple class describing an airline and associated

- *  frequent flyer number, used from the TravelData class
- *  (where an array of FrequentFlyerInfo is associated with
- *  each customer).

*/

```
public class FrequentFlyerInfo { private String airlineName, frequentFlyerNumber; public FrequentFlyerInfo(String airlineName, String frequentFlyerNumber) { this.airlineName = airlineName; this.frequentFlyerNumber = frequentFlyerNumber; } public String getAirlineName() { return(airlineName); } public String getFrequentFlyerNumber() { return(frequentFlyerNumber); } }
```

## Listing 15.8 RentalCarInfo.java

package coreservlets;

/** Simple class describing a car company and associated

- *  frequent renter number, used from the TravelData class
- *  (where an array of RentalCarInfo is associated with
- *  each customer).

*/

```
public class RentalCarInfo { private String rentalCarCompany, rentalCarNumber; public RentalCarInfo(String rentalCarCompany, String rentalCarNumber) { this.rentalCarCompany = rentalCarCompany; this.rentalCarNumber = rentalCarNumber; } public String getRentalCarCompany() { return(rentalCarCompany); } public String getRentalCarNumber() { return(rentalCarNumber); } }
```