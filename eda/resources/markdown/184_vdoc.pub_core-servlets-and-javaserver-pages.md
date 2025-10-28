## Appendix A Servlet and JSP Quick Reference

## Servlet Life Cycle

- · public void init() throws ServletException, public void init(ServletConfig config) throws ServletException Executed once when the servlet is first loaded. Not called for each request. Use getInitParameter to read initialization parameters.
- · public void service(HttpServletRequest request, public void service(HttpServletResponse response)

## throws ServletException, IOException

Called in a new thread by server for each request. Dispatches to doGet , doPost , etc. Do not override this method!

- · public void doGet(HttpServletRequest request,

## public void doGet(HttpServletResponse response)

## throws ServletException, IOException

Handles GET requests. Override to provide your behavior.

- · public void doPost(HttpServletRequest request, public void doPost(HttpServletResponse response)

## throws ServletException, IOException

Handles POST requests. Override to provide your behavior. If you want GET and POST to act identically, call doGet here.

- · doPut , doTrace , doDelete , etc. PUT TRACE

Handles the uncommon HTTP requests of , , etc.

- · public void destroy() Called when server deletes servlet instance. Not request.

called after each

- · public long getLastModified(HttpServletRequest request) Called by server when client sends conditional GET due to cached copy. See Section 2.8.
- · SingleThreadModel

If this interface implemented, causes server to avoid concurrent invocations.