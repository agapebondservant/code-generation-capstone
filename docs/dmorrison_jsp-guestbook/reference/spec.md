# System Design Document: COMP 6006 Guestbook

## 1. Architectural Overview

The COMP 6006 Guestbook application implements a **multi-tier architecture** with clear separation between presentation and business logic layers:

- **Presentation Layer**: JSP-based user interface manages form rendering and user input collection.

- **Business Logic Layer**: Java backend components handle authentication, validation, and data processing operations.

- **Session Management**: Server-side session tracking maintains user state and authentication status throughout the application lifecycle.

## 2. Component Specification

### 2.1 Database Configuration
- `setupdb.jsp`: Initializes and configures the application database schema.

### 2.2 Authentication Module

**Login Processing**:
- User credentials submitted to `AccountManager` servlet
- Successful authentication results in `username` stored in session scope
- Invalid credentials trigger error messaging via session attributes

**Registration Processing**:
- `/register.jsp` captures new user credentials
- `AccountManager` validates input and delegates to `User` object instantiation
- `Repository` layer persists new user records to database

### 2.3 Data Management
- **User.java**: Entity class encapsulating user credentials and profile data
- **Post.java**: Represents individual guestbook entries
- **PostManager.java**: Business logic for guestbook post operations
- **Repository.java**: Data access layer providing database persistence operations

### 2.4 Session Communication

Application state managed through session-scoped variables:
- `error`: Communicates validation failures and system errors
- `status`: Provides user feedback on operation outcomes

## 3. Functional Specifications

### 3.1 Anonymous Access
Users may browse existing guestbook entries without authentication.

### 3.2 User Registration Interface

Non-authenticated users will be presented with a registration form to register prior to login.

### 3.3 Authentication Flow
1. `AccountManager` validates submitted credentials
2. Successful authentication: session established, user redirected to guestbook
3. Failed authentication: error message displayed via session attributes

### 3.4 Session Termination
Logout form submission to `AccountManager` invalidates session and clears user state.

## 4. Business Rules

### 4.1 Registration Constraints
- **Username Uniqueness**: `UserRepository` enforces unique username constraint at database level
- **Password Confirmation**: Registration requires matching password and confirmation field values

### 4.2 Authentication Requirements
- Credentials validated against persisted `User` records
- Valid session required for guestbook content access
- Session establishment grants authorization for guestbook operations

### 4.3 Access Control
- **Authenticated View**: Logged-in users access full guestbook entry display
- **Access Restriction**: Guestbook functionality unavailable without valid session authentication