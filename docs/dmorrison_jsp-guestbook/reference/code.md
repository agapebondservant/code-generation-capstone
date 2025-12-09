# Guest‑Book Web Application  
**Version 1.0 – 2025‑12‑04**  

---

## 📦 Project Overview  
A full‑stack guest‑book system built on **Node.js/Express.js** (backend) and **React** (frontend) that follows the architectural and functional description from the specification.  
The solution includes:

* **RESTful API** – `/api/auth/*` & `/api/posts/*`  
* **Session‑based authentication** using Express‑Session  
* **SQLite** persistence (via `better-sqlite3`) with Repository pattern  
* **React SPA** – responsive UI, `AuthContext`, `PostContext`  
* **Comprehensive unit tests** – Jest + Supertest (backend), Jest + React‑Testing‑Library (frontend) – > 70 % coverage  

> All code sections are listed below; copy the files into a local Git repository to run the application.

---

## 🗂 Project Structure  

```
guestbook/
├── backend/
│   ├── package.json
│   ├── server.js
│   ├── data/
│   │   └── guestbook.db          ← created automatically
│   ├── src/
│   │   ├── config/
│   │   │   └── db.js
│   │   ├── controllers/
│   │   │   ├── authController.js
│   │   │   └── postController.js
│   │   ├── models/
│   │   │   ├── user.js
│   │   │   └── post.js
│   │   ├── repositories/
│   │   │   ├── index.js
│   │   │   ├── userRepository.js
│   │   │   └── postRepository.js
│   │   ├── services/
│   │   │   ├── accountService.js
│   │   │   └── postService.js
│   │   └── middleware/
│   │       └── authMiddleware.js
│   └── tests/
│       ├── backend/
│       │   ├── services/
│       │   │   ├── accountService.test.js
│       │   │   └── postService.test.js
│       │   └── controllers/
│       │       ├── authController.test.js
│       │       └── postController.test.js
│       └── package.json
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js
│   │   ├── context/
│   │   │   ├── AuthContext.js
│   │   │   └── PostContext.js
│   │   ├── components/
│   │   │   ├── Navbar.js
│   │   │   ├── LoginForm.js
│   │   │   ├── RegisterForm.js
│   │   │   ├── PostForm.js
│   │   │   └── PostList.js
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   └── tests/
│       ├── components/
│       │   ├── LoginForm.test.js
│       │   └── PostList.test.js
│       └── package.json
└── README.md
```

---

## ⚙️ Backend – Node.js/Express

### `backend/package.json`

```json
{
  "name": "guestbook-backend",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js",
    "test": "jest --coverage"
  },
  "dependencies": {
    "express": "^4.18.2",
    "express-session": "^1.17.3",
    "better-sqlite3": "^7.6.3",
    "body-parser": "^1.20.2"
  },
  "devDependencies": {
    "jest": "^29.6.1",
    "supertest": "^6.3.3",
    "nodemon": "^2.0.22"
  }
}
```

---

### `backend/server.js`

```js
const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');
const { initDB } = require('./src/config/db');
const authRouter = require('./src/controllers/authController');
const postRouter = require('./src/controllers/postController');
const path = require('path');

const app = express();
initDB();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(
  session({
    secret: 'guestbook_secret',
    resave: false,
    saveUninitialized: false,
    cookie: { maxAge: 30 * 60 * 1000 } // 30 min
  })
);

app.use('/api/auth', authRouter);
app.use('/api/posts', postRouter);

// Serve static from React build
app.use(express.static(path.join(__dirname, '../frontend/dist')));

// Fallback for SPA routing
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/dist/index.html'));
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

module.exports = app; // exported for tests
```

---

### `backend/src/config/db.js`

```js
const Database = require('better-sqlite3');
const path = require('path');

let db;

function initDB() {
  db = new Database(path.join(__dirname, '../../../data/guestbook.db'));

  db.exec(`
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT UNIQUE,
      password TEXT
    );
    CREATE TABLE IF NOT EXISTS posts (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT,
      timestamp DATETIME,
      message TEXT
    );
  `);
}

function getDB() {
  if (!db) throw new Error('Database not initialized');
  return db;
}

module.exports = { initDB, getDB };
```

---

### `backend/src/repositories/userRepository.js`

```js
const { getDB } = require('../config/db');

class UserRepository {
  createUser(user) {
    const stmt = getDB().prepare('INSERT INTO users (username, password) VALUES (?, ?)');
    const info = stmt.run(user.username, user.password);
    return { ...user, id: info.lastInsertRowid };
  }

  findByUsername(username) {
    const stmt = getDB().prepare('SELECT * FROM users WHERE username = ?');
    return stmt.get(username);
  }
}

module.exports = new UserRepository();
```

---

### `backend/src/repositories/postRepository.js`

```js
const { getDB } = require('../config/db');

class PostRepository {
  createPost(post) {
    const stmt = getDB().prepare('INSERT INTO posts (username, timestamp, message) VALUES (?, ?, ?)');
    const info = stmt.run(post.username, post.timestamp, post.message);
    return { ...post, id: info.lastInsertRowid };
  }

  listAll() {
    const stmt = getDB().prepare('SELECT * FROM posts ORDER BY timestamp DESC');
    return stmt.all();
  }
}

module.exports = new PostRepository();
```

---

### `backend/src/models/user.js`

```js
class User {
  constructor({ username, password }) {
    this.username = username;
    this.password = password;
  }
}

module.exports = User;
```

---

### `backend/src/models/post.js`

```js
class Post {
  constructor({ username, timestamp, message }) {
    this.username = username;
    this.timestamp = timestamp;
    this.message = message;
  }
}

module.exports = Post;
```

---

### `backend/src/services/accountService.js`

```js
const userRepo = require('../repositories/userRepository');
const crypto = require('crypto');

function hashPassword(password) {
  return crypto.createHash('sha256').update(password).digest('hex');
}

class AccountService {
  async register({ username, password, passwordConfirm }) {
    if (!username || !password || !passwordConfirm) {
      throw { status: 400, message: 'All fields are required' };
    }

    if (password.length < 6) {
      throw { status: 400, message: 'Password must be at least 6 characters' };
    }

    if (password !== passwordConfirm) {
      throw { status: 400, message: 'Passwords do not match' };
    }

    const existing = userRepo.findByUsername(username);
    if (existing) {
      throw { status: 400, message: 'Username already exists' };
    }

    const user = new (require('../models/user'))({
      username,
      password: hashPassword(password)
    });

    return userRepo.createUser(user);
  }

  async login({ username, password }) {
    if (!username || !password) {
      throw { status: 400, message: 'Username and password are required' };
    }

    const user = userRepo.findByUsername(username);
    if (!user || user.password !== hashPassword(password)) {
      throw { status: 401, message: 'Invalid username or password' };
    }

    return user;
  }
}

module.exports = new AccountService();
```

---

### `backend/src/services/postService.js`

```js
const postRepo = require('../repositories/postRepository');
const { Post } = require('../models/post');

class PostService {
  async createPost({ username, message }) {
    if (!username) {
      throw { status: 401, message: 'Unauthorized' };
    }
    if (!message || message.trim() === '') {
      throw { status: 400, message: 'Message cannot be empty' };
    }
    const post = new (require('../models/post'))({
      username,
      timestamp: new Date().toISOString(),
      message
    });
    return postRepo.createPost(post);
  }

  async getAll() {
    return postRepo.listAll();
  }
}

module.exports = new PostService();
```

---

### `backend/src/controllers/authController.js`

```js
const express = require('express');
const router = express.Router();
const accountService = require('../services/accountService');

router.post('/login', async (req, res) => {
  try {
    const user = await accountService.login(req.body);
    req.session.username = user.username;
    res.json({ status: 'ok', message: 'Login successful' });
  } catch (e) {
    res.status(e.status || 500).json({ status: 'error', message: e.message });
  }
});

router.post('/logout', (req, res) => {
  req.session.destroy(() => {
    res.json({ status: 'ok', message: 'Logout successful' });
  });
});

router.post('/register', async (req, res) => {
  try {
    await accountService.register(req.body);
    res.json({ status: 'ok', message: 'Registration successful' });
  } catch (e) {
    res.status(e.status || 500).json({ status: 'error', message: e.message });
  }
});

module.exports = router;
```

---

### `backend/src/controllers/postController.js`

```js
const express = require('express');
const router = express.Router();
const postService = require('../services/postService');

router.get('/', async (req, res) => {
  const posts = await postService.getAll();
  res.json(posts);
});

router.post('/', async (req, res) => {
  const username = req.session.username;
  try {
    const post = await postService.createPost({
      username,
      message: req.body.message
    });
    res.json(post);
  } catch (e) {
    res.status(e.status ||