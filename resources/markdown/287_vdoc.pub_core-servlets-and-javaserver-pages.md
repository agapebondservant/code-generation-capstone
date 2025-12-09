## Appendix A Servlet and JSP Quick Reference

## Connection pool timing results

| Condition                                                                                             | Average Time   |
|-------------------------------------------------------------------------------------------------------|----------------|
| Slow modem connection to database, no con- nection pooling ( ConnectionPoolServlet3 )                 | 82 seconds     |
| Fast LAN connection to database, 10 initial connections, 50 max connections ( ConnectionPoolServlet ) | 1.8 seconds    |
| Fast LAN connection to database, recycling a single connection ( ConnectionPoolServlet2 )             | 2.0 seconds    |
| Fast LAN connection to database, no connec- tion pooling ( ConnectionPoolServlet3 )                   | 2.8 seconds    |