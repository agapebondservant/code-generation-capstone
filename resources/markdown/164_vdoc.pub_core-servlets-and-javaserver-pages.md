Chapter 18 JDBC and Database Connection Pooling

## 18.8 Connection Pooling: A Case Study

OK, so we have a ConnectionPool class: what good does it do us? Let's find out. Listing 18.20 presents a simple servlet that allocates a ConnectionPool in  its init method,  then,  for  each  request,  performs  a  simple  database lookup and places the results in an HTML table. Listing 18.21 and Figure 18-6 show an HTML document that places a copy of this servlet in each of 25  frame  cells.  Since  the  servlet  stipulates  that  it  not  be  cached  by  the browser, this document results in 25 near simultaneous HTTP requests and thus 25 near simultaneous database lookups using connection pooling. This request pattern is similar to what would occur on high-traffic sites even when only a single servlet is used for each page.

Listing 18.22 shows a variation of the servlet that uses a 'pool' of only a single connection, and Listing 18.23 shows a third variation that doesn't use connection pooling at all. Each of these two servlets is also placed in a framed document nearly identical to that of Listing 18.21. Timing results are shown in Table 18.1.

One small reminder: since these servlets load a JDBC driver, the driver needs to be made accessible to the Web server. With most servers, you can make the driver accessible by placing the JAR file containing the driver into the server's lib directory or by unpacking the JAR file in the classes directory. See your server's documentation for definitive instructions.

| Table 18.1 Connection pool timing results                                                               |              |
|---------------------------------------------------------------------------------------------------------|--------------|
| Condition                                                                                               | Average Time |
| Slow modem connection to database, 10 initial connections, 50 max connections ( ConnectionPoolServlet ) | 11 seconds   |
| Slow modem connection to database, recycling a single connection ( ConnectionPoolServlet2 )             | 22 seconds   |
| Slow modem connection to database, no connection pooling ( ConnectionPoolServlet3 )                     | 82 seconds   |