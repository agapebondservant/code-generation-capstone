## Chapter 7 Generating the Server Response: HTTP Response Headers

## WWW-Authenticate

This header is always included with a 401 ( Unauthorized ) status code. It tells the browser what authorization type and realm the client should supply in its Authorization header. Frequently, servlets let password-protected Web pages be handled by the Web server's specialized mechanisms (e.g., .htaccess ) rather than handling them directly. For an example of servlets dealing directly with this header, see Section 4.5 (Restricting Access to Web Pages).

## 7.3 Persistent Servlet State and Auto-Reloading Pages

Here is an example that lets you ask for a list of some large, randomly chosen prime numbers. This computation may take some time for very large numbers (e.g.,  150  digits),  so  the  servlet  immediately  returns  initial  results  but then keeps calculating, using a low-priority thread so that it won't degrade Web server  performance.  If  the  calculations  are  not  complete,  the  servlet instructs the browser to ask for a new page in a few seconds by sending it a Refresh header.

In addition to illustrating the value of HTTP response headers, this example shows two other valuable servlet capabilities. First, it shows that the same servlet  can  handle  multiple  simultaneous  connections,  each  with  its  own thread. So, while one thread is finishing a calculation for one client, another client can connect and still see partial results.

Second, this example shows how easy it is for servlets to maintain state between requests,  something  that  is  cumbersome  to  implement  in  traditional CGI and many CGI alternatives. Only a single instance of the servlet is created, and each request simply results in a new thread calling the servlet's service method (which calls doGet or doPost ). So, shared data simply has to be placed in a regular instance variable (field) of the servlet. Thus, the  servlet  can  access  the  appropriate  ongoing  calculation  when  the browser  reloads  the  page  and  can  keep  a  list  of  the N most  recently requested  results,  returning them immediately  if  a  new  request  specifies the  same  parameters  as  a  recent  one.  Of  course,  the  normal  rules  that require  authors  to  synchronize  multithreaded  access  to  shared  data  still

## 7.3 Persistent Servlet State and Auto-Reloading Pages

apply  to  servlets.  Servlets  can  also  store  persistent  data  in  the ServletContext object that is available through the getServletContext method. ServletContext has setAttribute and getAttribute methods  that let you  store  arbitrary  data  associated  with  specified  keys.  The  difference between storing data in instance variables and storing it in the ServletContext is that the ServletContext is shared by all servlets in the servlet engine (or in the Web application, if your server supports such a capability).

Listing 7.1  shows the  main servlet  class.  First,  it  receives  a  request  that specifies two parameters: numPrimes and numDigits . These values are normally collected from the user and sent to the servlet by means of a simple HTML form. Listing 7.2 shows the source code and Figure 7-1 shows the result. Next, these parameters are converted to integers by means of a simple utility that uses Integer.parseInt (see Listing 7.5). These values are then matched by the findPrimeList method to a Vector of  recent or ongoing calculations to  see  if  there  is  a  previous  computation  corresponding  to  the same two values. If so, that previous value (of type PrimeList ) is used; otherwise, a new PrimeList is  created  and  stored  in  the ongoing-calculations Vector , potentially displacing the oldest previous list. Next, that PrimeList is checked to determine if it has finished finding all of its primes. If not, the client  is  sent  a Refresh header  to  tell  it  to  come  back  in  five  seconds  for updated results. Either way, a bulleted list of the current values is returned to the client.

Listings 7.3 ( PrimeList.java )  and 7.4 ( Primes.java )  present auxiliary code used by the servlet. PrimeList.java handles  the background thread for the creation of a list of primes for a specific set of values. Primes.java contains the low-level algorithms for choosing a random number of a specified length and then finding a prime at or above that value. It uses built-in methods in the BigInteger class; the algorithm for determining if the number is prime is a probabilistic one and thus has a chance of being mistaken. However, the probability of being wrong can be specified, and I use an error value of 100. Assuming that the algorithm used in most Java implementations is the Miller-Rabin test, the likelihood of falsely reporting a composite number as prime is provably less than 2 100 .  This is almost certainly smaller than the likelihood of a hardware error or random radiation causing an incorrect response in a deterministic algorithm, and thus the algorithm can be considered deterministic.

## Chapter 7 Generating the Server Response: HTTP Response Headers

## Listing 7.1 PrimeNumbers.java package coreservlets; import java.io.*; import javax.servlet.*; import javax.servlet.http.*; import java.util.*; /** Servlet that processes a request to generate n *  prime numbers, each with at least m digits. *  It performs the calculations in a low-priority background *  thread, returning only the results it has found so far. *  If these results are not complete, it sends a Refresh *  header instructing the browser to ask for new results a *  little while later. It also maintains a list of a *  small number of previously calculated prime lists *  to return immediately to anyone who supplies the *  same n and m as a recent completed computation. */ public class PrimeNumbers extends HttpServlet { private Vector primeListVector = new Vector(); private int maxPrimeLists = 30; public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { int numPrimes = ServletUtilities.getIntParameter(request, "numPrimes", 50); int numDigits = ServletUtilities.getIntParameter(request, "numDigits", 120); PrimeList primeList = findPrimeList(primeListVector, numPrimes, numDigits); if (primeList == null) { primeList = new PrimeList(numPrimes, numDigits, true); // Multiple servlet request threads share the instance // variables (fields) of PrimeNumbers. So // synchronize all access to servlet fields. synchronized(primeListVector) { if (primeListVector.size() &gt;= maxPrimeLists) primeListVector.removeElementAt(0); primeListVector.addElement(primeList); } } Vector currentPrimes = primeList.getPrimes(); int numCurrentPrimes = currentPrimes.size(); int numPrimesRemaining = (numPrimes - numCurrentPrimes); boolean isLastResult = (numPrimesRemaining == 0); if (!isLastResult) { response.setHeader("Refresh", "5"); }

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

## 7.3 Persistent Servlet State and Auto-Reloading Pages

```
PrimeNumbers.java (continued)
```

## Listing 7.1

```
response.setContentType("text/html"); PrintWriter out = response.getWriter(); String title = "Some " + numDigits + "-Digit Prime Numbers"; out.println(ServletUtilities.headWithTitle(title) + "<BODY BGCOLOR=\"#FDF5E6\">\n" + "<H2 ALIGN=CENTER>" + title + "</H2>\n" + "<H3>Primes found with " + numDigits + " or more digits: " + numCurrentPrimes + ".</H3>"); if (isLastResult) out.println("<B>Done searching.</B>"); else out.println("<B>Still looking for " + numPrimesRemaining + " more<BLINK>...</BLINK></B>"); out.println("<OL>"); for(int i=0; i<numCurrentPrimes; i++) { out.println("  <LI>" + currentPrimes.elementAt(i)); } out.println("</OL>"); out.println("</BODY></HTML>"); } public void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException { doGet(request, response); } // See if there is an existing ongoing or completed // calculation with the same number of primes and number // of digits per prime. If so, return those results instead // of starting a new background thread. Keep this list // small so that the Web server doesn't use too much memory. // Synchronize access to the list since there may be // multiple simultaneous requests. private PrimeList findPrimeList(Vector primeListVector, int numPrimes, int numDigits) { synchronized(primeListVector) { for(int i=0; i<primeListVector.size(); i++) { PrimeList primes = (PrimeList)primeListVector.elementAt(i); if ((numPrimes == primes.numPrimes()) && (numDigits == primes.numDigits())) return(primes); } return(null); } } }
```

<!-- image -->

## Chapter 7 Generating the Server Response: HTTP Response Headers

## Listing 7.2 PrimeNumbers.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML> <HEAD> <TITLE>Finding Large Prime Numbers</TITLE> </HEAD> <BODY BGCOLOR="#FDF5E6"> <H2 ALIGN="CENTER">Finding Large Prime Numbers</H2> <BR><BR> <CENTER> <FORM ACTION="/servlet/coreservlets.PrimeNumbers" > <B>Number of primes to calculate:</B> <INPUT TYPE="TEXT" NAME="numPrimes" VALUE=25 SIZE=4><BR> <B>Number of digits:</B> <INPUT TYPE="TEXT" NAME="numDigits" VALUE=150 SIZE=3><BR> <INPUT TYPE="SUBMIT" VALUE="Start Calculating"> </FORM> </CENTER> </BODY> </HTML>
```

Figure 7-1 Result of PrimeNumbers.html , used as a front end to the PrimeNumbers servlet.

<!-- image -->

## 7.3 Persistent Servlet State and Auto-Reloading Pages

Figure 7-2 Intermediate result of a request to the PrimeNumbers servlet. This result can be obtained when the browser reloads automatically or when a different client independently enters the same parameters as those from an ongoing or recent request. Either way, the browser will automatically reload the page to get updated results.

<!-- image -->

Figure 7-3 Final result of a request to the PrimeNumbers servlet. This result can be obtained when the browser reloads automatically or when a different client independently enters the same parameters as those from an ongoing or recent request. The browser will stop updating the page at this point.

<!-- image -->

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## 160

## Chapter 7 Generating the Server Response: HTTP Response Headers

## Listing 7.3 PrimeList.java

```
package coreservlets; import java.util.*; import java.math.BigInteger; /** Creates a Vector of large prime numbers, usually in *  a low-priority background thread. Provides a few small *  thread-safe access methods. */ public class PrimeList implements Runnable { private Vector primesFound; private int numPrimes, numDigits; /** Finds numPrimes prime numbers, each of which are *  numDigits long or longer. You can set it to only *  return when done, or have it return immediately, *  and you can later poll it to see how far it *  has gotten. */ public PrimeList(int numPrimes, int numDigits, boolean runInBackground) { // Using Vector instead of ArrayList // to support JDK 1.1 servlet engines primesFound = new Vector(numPrimes); this.numPrimes = numPrimes; this.numDigits = numDigits; if (runInBackground) { Thread t = new Thread(this); // Use low priority so you don't slow down server. t.setPriority(Thread.MIN_PRIORITY); t.start(); } else { run(); } } public void run() { BigInteger start = Primes.random(numDigits); for(int i=0; i<numPrimes; i++) { start = Primes.nextPrime(start); synchronized(this) { primesFound.addElement(start); } } } public synchronized boolean isDone() { return(primesFound.size() == numPrimes); }
```

## 7.3 Persistent Servlet State and Auto-Reloading Pages

## public synchronized Vector getPrimes() { if (isDone()) return(primesFound); else return((Vector)primesFound.clone()); } public int numDigits() { return(numDigits); } public int numPrimes() { return(numPrimes); } public synchronized int numCalculatedPrimes() { return(primesFound.size()); } } Listing 7.3 PrimeList.java (continued)

## Listing 7.4 Primes.java

package coreservlets;

```
import java.math.BigInteger; /** A few utilities to generate a large random BigInteger, *  and find the next prime number above a given BigInteger. */ public class Primes { // Note that BigInteger.ZERO was new in JDK 1.2, and 1.1 // code is being used to support the most servlet engines. private static final BigInteger ZERO = new BigInteger("0"); private static final BigInteger ONE = new BigInteger("1"); private static final BigInteger TWO = new BigInteger("2"); // Likelihood of false prime is less than 1/2^ERR_VAL // Assumedly BigInteger uses the Miller-Rabin test or // equivalent, and thus is NOT fooled by Carmichael numbers. // See section 33.8 of Cormen et al's Introduction to // Algorithms for details. private static final int ERR_VAL = 100; public static BigInteger nextPrime(BigInteger start) { if (isEven(start)) start = start.add(ONE); else
```

Home page for this book: www.coreservlets.com; Home page for sequel: www.moreservlets.com. Servlet and JSP training courses by book's author: courses.coreservlets.com.

<!-- image -->

## 162 Chapter 7 Generating the Server Response: HTTP Response Headers

```
start = start.add(TWO); if (start.isProbablePrime(ERR_VAL)) return(start); else return(nextPrime(start)); } private static boolean isEven(BigInteger n) { return(n.mod(TWO).equals(ZERO)); } private static StringBuffer[] digits = { new StringBuffer("0"), new StringBuffer("1"), new StringBuffer("2"), new StringBuffer("3"), new StringBuffer("4"), new StringBuffer("5"), new StringBuffer("6"), new StringBuffer("7"), new StringBuffer("8"), new StringBuffer("9") }; private static StringBuffer randomDigit() { int index = (int)Math.floor(Math.random() * 10); return(digits[index]); } public static BigInteger random(int numDigits) { StringBuffer s = new StringBuffer(""); for(int i=0; i<numDigits; i++) { s.append(randomDigit()); } return(new BigInteger(s.toString())); } /** Simple command-line program to test. Enter number *  of digits, and it picks a random number of that *  length and then prints the first 50 prime numbers *  above that. */ public static void main(String[] args) { int numDigits; if (args.length > 0) numDigits = Integer.parseInt(args[0]); else numDigits = 150; BigInteger start = random(numDigits); for(int i=0; i<50; i++) { start = nextPrime(start); System.out.println("Prime " + i + " = " + start); } } } Listing 7.4 Primes.java (continued)
```