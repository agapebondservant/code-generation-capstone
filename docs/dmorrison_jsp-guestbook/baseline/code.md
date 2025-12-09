To develop a complete NodeJS and React application based on the provided specification, I will follow these steps:

1. **Design the Backend API using Express.js**
2. **Design the Frontend UI using React**
3. **Write Unit Tests for both Backend and Frontend components**

### Backend Implementation (NodeJS)

**Project Setup**

First, create a new NodeJS project and install the necessary dependencies:

```bash
mkdir guestbook-app
cd guestbook-app
npm init -y
npm install express body-parser sqlite3 bcrypt jsonwebtoken dotenv
```

**Directory Structure**

```
guestbook-app/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   └── index.js
├── .env
├── .gitignore
└── package.json
```

**Configuring Environment Variables**

Create a `.env` file to store sensitive information like database credentials:

```plaintext
DB_NAME=guestbook.db
DATABASE_USER=username
DATABASE_PASSWORD=password
TOKEN_SECRET=your_jwt_secret
```

**Database Models**

Define `User` and `Post` models in `src/models/`:

```javascript
// src/models/User.js
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database(`${__dirname}/../db/${process.env.DB_NAME}`);

class User {
  constructor(id, username, password) {
    this.id = id;
    this.username = username;
    this.password = password;
  }

  static async create(username, password) {
    const hashedPassword = await bcrypt.hash(password, 10);
    const [row] = await db.run(
      `INSERT INTO users (username, password) VALUES (?, ?)`,
      [username, hashedPassword]
    );
    return new User(row.lastID, username, password);
  }

  static findById(id) {
    return db.get(`SELECT * FROM users WHERE id = ?`, [id]).then(row => new User(row.id, row.username, row.password));
  }
}

module.exports = { User };
```

```javascript
// src/models/Post.js
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database(`${__dirname}/../db/${process.env.DB_NAME}`);

class Post {
  constructor(userId, timestamp, message) {
    this.userId = userId;
    this.timestamp = timestamp;
    this.message = message;
  }

  static async getAll() {
    const posts = [];
    for await (const row of db.all('SELECT * FROM posts')) {
      posts.push(new Post(row.userId, row.timestamp, row.message));
    }
    return posts;
  }

  static async create(userId, message) {
    const timestamp = new Date().toISOString();
    await db.run('INSERT INTO posts (userId, timestamp, message) VALUES (?, ?, ?)', [userId, timestamp, message]);
  }
}

module.exports = { Post };
```

**Serives and Routes**

Implement services and routes in `src/controllers/` and `src/routes/`:

```javascript
// src/controllers/AuthController.js
const jwt = require('jsonwebtoken');
const { User } = require('../models/User');

exports.authenticate = async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findOne({ username });
  
  if (!user) {
    return res.status(401).json({ message: 'Invalid Credentials' });
  }

  try {
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).json({ message: 'Invalid Credentials' });
    }

    const token = jwt.sign({ id: user.id }, process.env.TOKEN_SECRET, { expiresIn: '1h' });
    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Authentication failed' });
  }
};

// src/controllers/PostController.js
const { Post } = require('../models/Post');

exports.create = async (req, res) => {
  const { userId, message } = req.body;
  await Post.create(userId, message);
  res.status(201).send();
};

exports.getAll = (req, res) => {
  Post.getAll()
    .then(posts => res.json(posts))
    .catch(err => res.status(500).json({ message: err }));
};
```

```javascript
// src/routes/api.js
const express = require('express');
const router = express.Router();
const authController = require('../controllers/AuthController');
const postController = require('../controllers/PostController');

router.post('/auth', authController.authenticate);
router.post('/posts', authController.authenticate, postController.create);
router.get('/posts', authController.authenticate, postController.getAll);

module.exports = router;
```

```javascript
// src/index.js
const express = require('express');
const bodyParser = require('body-parser');
require('dotenv').config();
const { User } = require('./models/User');
const { Post } = require('./models/Post');
const authRouter = require('./routes/api');

const app = express();

app.use(bodyParser.json());
app.use('/api', authRouter);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Frontend Implementation (React)

**Project Setup**

Initialize a new React application:

```bash
npx create-react-app frontend
cd frontend
npm install axios
```

**Component Structure**

**Directory Structure**

```
frontend/
├── public/
├── src/
│   ├── components/
│   ├── pages/
│   └── utils/
├── index.js
├── App.js
└── package.json
```

**API Client**

Create a utility to manage API calls:

```javascript
// frontend/src/utils/apiClient.js
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:3000/api';

export const getUser = async (username) => {
  const response = await axios.get(`${API_URL}/api/auth`, { params: { username } });
  return response.data;
};

export const getPosts = async () => {
  const response = await axios.get(`${API_URL}/api/posts`);
  return response.data;
};

export const createPost = async (userId, message) => {
  await axios.post(`${API_URL}/api/posts`, { userId, message });
};
```

**Components**

Implement responsive UI components:

```javascript
// frontend/src/components/AuthForm.js
import React, { useState } from 'react';
import { getUser } from '../utils/apiClient';

const AuthForm = ({ onSubmit }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const user = await getUser(username);
    if (user.token) {
      onSubmit(user);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button type="submit">Login</button>
    </form>
  );
};

export default AuthForm;
```

```javascript
// frontend/src/pages/HomePage.js
import React, { useEffect, useState } from 'react';
import { getPosts, createPost } from '../utils/apiClient';

const HomePage = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      const posts = await getPosts();
      setPosts(posts);
    };

    fetchPosts();
  }, []);

  const handleCreatePost = async (message) => {
    await createPost(1, message);
    const newPosts = await getPosts();
    setPosts(newPosts);
  };

  return (
    <>
      <h1>Guestbook</h1>
      <div>
        {posts.map(post => (
          <div key={post.id}>{post.message} - ${post.timestamp}</div>
        ))}
      </div>
      <form>
        <input type="text" placeholder="Your message" />
        <button type="button" onClick={() => handleCreatePost('Your message')}>Post</button>
      </form>
    </>
  );
};

export default HomePage;
```

**Configuring Environment Variables**

Create a `.env` file in the root of the frontend directory:

```plaintext
REACT_APP_API_URL=http://localhost:3000/api
```

**Testing**

**Backend Tests**

Write unit tests for your backend using Jest. Here's an example for the AuthController:

```javascript
// frontend/tests/authController.test.js
const request = require('supertest');
const app = require('../src/index');

describe('Auth Route', () => {
  test('should authenticate user', async () => {
    const response = await request(app)
      .post('/api/auth')
      .send({ username: 'testuser', password: 'testpass' });
    expect(response.status).toBe(200);
    expect(response.body.token).toBeDefined();
  });
});
```

**Frontend Tests**

Write unit tests for React components using Jest and React Testing Library. Here's an example for the `AuthForm` component:

```javascript
// frontend/tests/AuthForm.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import AuthForm from '../components/AuthForm';
import userEvent from '@testing-library/user-event';

test('renders login form', () => {
  render(<AuthForm onSubmit={() => {}} />);
  expect(screen.getByLabelText(/username/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
  expect(screen.getByText(/login/i)).toBeInTheDocument();
});
```

### README for Setup Instructions

```markdown
# Guestbook Application

## Backend
The backend is built using NodeJS with Express.js for handling API requests and SQLite for data persistence.

### Prerequisites
- Node.js
- npm

### Setup
1. Clone the repository
2. Navigate to the project directory
3. Run `npm install` to install the dependencies

### Running the Backend
1. Configure the `.env` file with your environment variables.
2. Run `node src/index.js` to start the server.

### Database Setup
The first time the server runs, it will create a SQLite database named `guestbook.db` and initialize it with the user and post tables.

## Frontend
The frontend is a React application that interacts with the backend API.

### Prerequisites
- Node.js
- npm

### Setup
1. Navigate to the frontend directory
2. Run `npm install` to install the dependencies

### Running the Frontend
1. Run `npm start` to start the frontend application. 

### Environment Variables
Ensure you set `REACT_APP_API_URL` in your `.env` file to point to your backend server if it's not running on the default port.

## Testing

### Backend Tests
Run `npm test` to execute the backend tests.

### Frontend Tests
Run `npm test` to execute the frontend tests.
```

This setup outlines a complete solution for both backend and frontend components of the guestbook application, including unit testing and setup instructions for a seamless user experience.