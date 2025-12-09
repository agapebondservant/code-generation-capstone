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
Using this specification, write the code for a complete NodeJS and React  application based on the provided  document. The code should include both  backend and frontend components with comprehensive unit testing using mock objects. Backend Requirements (NodeJS):

1. Write the code for a RESTful API using Express.js or your preferred NodeJS framework.
2. Follow the services, data models, and business logic defined in the spec.

Frontend Requirements (React):

1. Write the code for responsive UI components in React.
2. Develop the components according to the design specifications in the spec.
3. Use Jest and React Testing Library for unit testing.
4. Aim for high code coverage (70%+ minimum).

Code:
```markdown
## Backend Code (NodeJS with Express.js)

### Components
- **AccountManager**: Handles user registration and authentication.
  - `registerUser`: Validates and saves user if username is unique.
  - `authenticateUser`: Checks credentials against `User` database.

- **PostManager**: Manages guestbook postings.
  - `savePost`: Adds post after user authentication.
  - `getPosts`: Retrieves posts viewable by logged-in users.

- **User**: Represents a user with fields `id`, `username`, `password`.

- **Repository**: Interacts with the underlying database (e.g., MongoDB).

### Database Models (`User.js`)
```javascript
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true },
});

module.exports = mongoose.model('User', userSchema);
```

### Authentication Routes (routes.js)
```javascript
const express = require('express');
const router = express.Router();
const { authenticateUser } = require('../services/accountManager');
const { savePost } = require('../services/postManager');

router.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const authenticated = await authenticateUser(username, password);
  if (authenticated) {
    res.json({ message: 'Login successful', username: username });
  } else {
    res.status(401).json({ message: 'Invalid credentials' });
  }
});

router.post('/register', async (req, res) => {
  const { username, password, confirmPassword } = req.body;
  if (password !== confirmPassword) {
    return res.status(400).json({ message: 'Passwords do not match' });
  }
  try {
    const getUser = await mongoose.model('User').findOne({ username });
    if (getUser) {
      return res.status(400).json({ message: 'Username already exists' });
    }
    const savedUser = await mongoose.model('User').create({ username, password });
    res.status(201).json({ message: 'User registered', data: savedUser });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
});

router.post('/post', (req, res) => {
  const { content } = req.body;
  savePost(req.session.user.username, content);
  res.json({ message: 'Post saved' });
});

module.exports = router;
```

### Test Suites (Jest)
```javascript
// user.test.js
const mongoose = require('mongoose');
const User = require('../models/user');

beforeEach(async () => {
  await mongoose.connect('mongodb://test');
});

afterEach(async () => {
  await mongoose.connection.db.dropDatabase();
});

test('username must be unique', async () => {
  await mongoose.model('User').create({ username: 'testUser', password: 'password' });
  const duplicateUser = await mongoose.model('User').create({ username: 'testUser', password: 'anotherPassword' });
  expect(Book.find().count()).toBe(1);
});
```

## Frontend Code (React)

### Components
- **LoginForm**: Handles login credentials submission.
- **RegistrationForm**: Forms for user registration.
- **GuestbookView**: Displays guestbook entries if logged in.

### Login Component (`Login.js`)
```jsx
import React, { useState } from 'react';
import axios from 'axios';

const LoginForm = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/login', { username, password });
      onLogin(response.data.username);
    } catch (error) {
      // Handle error display
    }
  };

  // Render login form...
};

export default LoginForm;
```

### Registration Component (`Register.js`)
```jsx
import React, { useState } from 'react';
import axios from 'axios';

const RegistrationForm = ({ onRegister }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      // Handle validation error
    }
    try {
      const response = await axios.post('/api/register', { username, password, confirmPassword });
      onRegister(response.data.username);
    } catch (error) {
      // Handle error display
    }
  };

  // Render registration form...
};

export default RegistrationForm;
```

### Test Suites (Jest & React Testing Library)
```javascript
// LoginForm.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import LoginForm from './LoginForm';

test('renders LoginForm', () => {
  render(<LoginForm />);
  // Assert elements exist (input fields...)
});

// RegistrationForm.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import RegistrationForm from './RegistrationForm';

test('renders RegistrationForm', () => {
  render(<RegistrationForm />);
});
```

### Middleware for Session (middleware/session.js)
```javascript
const sessionMiddleware = (req, res, next) => {
  req.session.user = req.session.user; // Placeholder
  next();
};

module.exports = sessionMiddleware;
```

## Setup Instructions  
- Install dependencies: `npm install express mongoose axios`.
- Start server: `node server.js`.
- Build frontend: `npm run build`.
```
Instructions: This is the expected criteria for your final answer: The code for a complete backend NodeJS implementation and frontend React  application, with test suites and a README for setup instructions. All code should align with the requirements and technical specifications provided in the spec.
You MUST return the actual complete content as the final answer, not a summary. 
Your final answer MUST be formatted in Markdown syntax.
Follow these guidelines:
- Use # for headers
- Use ** for bold text  
- Use * for italic text
- Use - or * for bullet points
- Use `code` for inline code
- Use ```language for code blocks  
Begin! This is VERY important to you, use the tools available and give your best Final Answer, your job depends on it!
```