## Appendix A Servlet and JSP Quick Reference

## HttpSession Methods

- · public Object getValue(String name) [2.1] public Object getAttribute(String name) [2.2] Extracts a previously stored value from a session object. Returns null
- if no value is associated with given name.
- · public void putValue(String name, Object value) [2.1] public void setAttribute(String name, Object value) [2.2] Associates a value with a name. If value implements HttpSessionBindingListener , its valueBound method is called. If previous value implements HttpSessionBindingListener , its valueUnbound method is called.
- · public void removeValue(String name) [2.1] public void removeAttribute(String name) [2.2] Removes any values associated with designated name. If value being removed implements HttpSessionBindingListener , its valueUnbound method is called.
- · public String[] getValueNames() [2.1] public Enumeration getAttributeNames() [2.2]

Returns the names of all attributes in the session.

- · public String getId()

Returns the unique identifier generated for each session.

- · public boolean isNew() Returns true if the client (browser) has never seen the session; false otherwise.
- · public long getCreationTime() Returns time at which session was first created (in milliseconds since 1970). To get a value useful for printing, pass value to Date constructor or the setTimeInMillis method of GregorianCalendar .
- · public long getLastAccessedTime()

Returns time at which the session was last sent from the client.

- · public int getMaxInactiveInterval()
- public void setMaxInactiveInterval(int seconds) without access before being automatically invalidated. A negative value

Gets or sets the amount of time, in seconds, that a session should go indicates that session should never time out. Not the same as cookie expiration date.

- · public void invalidate()

Invalidates the session and unbinds all objects associated with it.