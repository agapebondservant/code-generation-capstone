# Software Design Document (SDD)

## 1. System Architecture

### 1.1 Overall Design
The web application follows a Model-View-Controller (MVC) architectural pattern, which separates the application into three interconnected components. This separation allows for modular development, where the application logic (Model), user interface (View), and data access (Controller) can be managed independently. The application interacts with a SQLite database for data persistence, ensuring data integrity and state management.

### 1.2 Key Components
The application is composed of several key components that work together to deliver its functionality:

#### Core Components
- **Servlets**:
  - `AccountManager`: Manages user accounts, including registration, authentication, and login/logout functionalities.
  - `PostManager`: Handles the creation, retrieval, and management of guest book posts.

- **Data Access Layer**:
  - `Repository`: Responsible for executing database operations, including user and post management. It abstracts the database interactions, allowing the application to focus on business logic without concerning itself with the specifics of the database.

#### Model Classes
- **User**: Represents user account information, including `id`, `username`, and `password`. This model encapsulates user data and is used for authentication and authorization purposes.
- **Post**: Represents a guest book post, containing `userId`, `timestamp`, and `message`. This model is utilized by the `PostManager` for managing the guest book functionality.

#### Experience and Description Pages
- **setupdb.jsp**: This JSP file sets up the SQLite database schema and populates it with initial data, preparing the environment for the application to function.

### Interactions
The components interact as follows:
- Users interact with the application through the UI, which triggers actions in the `AccountManager` and `PostManager` based on the user's inputs.
- Input requests from users are handled by the Servlets, which in turn use the `Repository` to perform necessary database operations to either retrieve data or update it, based on user actions.
- The `Repository` communicates directly with the SQLite database to execute SQL queries, adhering to the principles of the Data Access Layer pattern.

This architecture ensures a clean separation of concerns, making the system easier to maintain, scale, and update. The next section delves into the specific functional and business requirements that drive the design and development of these components.

## 2. Functional Requirements

### 2.1 Input Handling
- **Registration/Landing Page**: Users fill out a form with their credentials to register.
- **Login Page**: Users input their credentials to log in.
- **Post Creation Page**: Users submit their posts by filling out a form.
- All inputs are validated both on the client and server sides to ensure data integrity and compliance with business rules.

### 2.2 Data Processing
- **User Authentication**: Validates user credentials against the database and logs the user in upon successful authentication.
- **User Registration**: Inserts new user data into the database after validating inputs.
- **Post Creation**: Inserts new posts into the database, associating them with the correct user.
- **Post Retrieval**: Retrieves all posts from the database, including author information, for display on the guest book page.

### 2.3 Output Generation
- **Registration/Login Success/Failure**: Suitable messages are displayed to the user based on the outcome of their authentication or registration process.
- **Post Management**: Guests can view posts but can only create new posts if authenticated.
- **Database Results**: Display users and their posts in a structured format on the web application.

## 3. Business Requirements

### 3.1 Business Rules
- **User Authentication**: Users must provide correct credentials to log in; otherwise, access to certain functionalities is restricted.
- **Post Management**: Only authenticated users can create posts; all posts are associated with a user.
- **Data Integrity**: No duplicate user registrations; user credentials must be securely hashed.

### 3.2 Success Criteria
- Ability to register, login, and logout successfully.
- Ability to create, view, and delete guest book posts.
- Secure storage and handling of user credentials through hashing techniques.
- Consistent performance and responsiveness of the application, ensuring a good user experience across devices.

This SDD encapsulates the design and structure of the web application based on the provided summary. It delineates the architectural approach, functional capabilities, and business logic that govern the application, providing a comprehensive overview from which both technical and non-technical stakeholders can reference and understand the application's design and purpose.