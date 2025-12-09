Your final answer must be the great and the most complete as possible, it must be outcome described.
Here is the structure with headers for my Software Design Document (SDD):

# System Architecture
The **COMP 6006 Guestbook** registers JSP files use a **frontend/backend separation** architecture:
## Overall Design  
- An **JSP-based front-end** handles HTML form presentation and captures user inputs.
- A **backend component** processes form submissions, likely implemented in **Java** (though specifics aren't provided).
- Session tracking manages user interactions and login state.
## Key Components
- `setupdb.jsp` - Configures the backend database.
- **Login/Registration**:
  - `Log In` form sends credentials to **AccountManager**.
  - Successful login stores `username` in session on `AccountManager`.
- **Registration**:
  - `/register.jsp` submits username and password to `AccountManager`.
  - Registration logic invokes `User` object creation and DB persistence via `Repository`.
- **User Management** (`User.java`) stores username/password, etc.
- **Post/Repository handlers** (`Post.java`, `PostManager.java`, `Repository.java`) process guestbook entries if logged in.
- **Errors/Status** communication via `error` and `status` session variables.

# Functional Requirements
- Allow **anonymous browsing** of guestbook entries.
- Provide **registration page** when not logged in, with:
  ```html
  <form action="accountmanager" method="post">
    <table>...fields</table>
    <input type="submit" name="register" id="register" value="Register" />
  </form>
  ```
- Validate **username/password** via `AccountManager`.
- On success, **store username** in session and redirect back to guestbook.
- On failure, display **error messages** using session attributes.
- **Log Out** form submits to `AccountManager`, clears username/session.
# Business Requirements
- **New User Registration**:
  - Require **unique username** (validated by `User`/`Repository` constraints).
  - Password **must match confirmation** field.
- **Login Authentication**:
  - Verify username/password pair against `User` records.
  - Session management grants access to guestbook content post-login.
- **Guestbook Access**:
  - After login, display recent guestbook entries.
  - Prevent access without valid session state.

This SDD outlines the high-level **components**, **inputs/outputs**, and **core business rules**. Technical details like triggers, exact DB schemas, or CSS layouts are abstracted as per the request to focus on the overall system architecture and domain model.