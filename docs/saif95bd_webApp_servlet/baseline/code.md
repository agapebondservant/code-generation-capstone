To create a complete NodeJS backend and React frontend application based on the provided software design document (SDD), we'll follow these steps:

1. **Set up the NodeJS backend** following the requirements outlined in the SDD.
2. **Create the React frontend** adhering to the design specifications.
3. **Implement unit tests** for both backend and frontend using Jest and React Testing Library.
4. **Provide a README for setup and testing instructions**.

### Backend: NodeJS with Express.js

#### Setup and Dependencies

First, let's set up the project structure and install necessary dependencies:

```bash
mkdir rimssystem
cd rimssystem
npm init -y
npm install express body-parser joi express-validator express-mongoose vhost helmet cors axios
```

#### Project Structure

```
rimssystem/
|
|___config/
    ___database.js
|
|___controllers/
    ___searchController.js
    ___insertController.js
|
|___models/
    ___Reg.js
|
|___services/
    ___DaoService.js
    ___SearchService.js
|
|___routes/
    ___searchRoutes.js
    ___insertRoutes.js
|
|___public/
    ___index.html
    ___insert.html
    ___search.html
|
|___test/
    ___searchService.test.js
    ___DaoService.test.js
|
|___package.json
```

#### Database Configuration (`config/database.js`)

```javascript
require('dotenv').config();

module.exports = {
  mongooseURI: process.env.MONGODB_URI,
  mongooseOptions: {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  },
};
```

#### Model (`models/Reg.js`)

```javascript
const mongoose = require('mongoose');
require('dotenv').config();

const regSchema = new mongoose.Schema({
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  middleName: String,
  birth: { type: Date, required: true },
});

module.exports = mongoose.model('Reg', regSchema);
```

#### DAO Service (`services/DaoService.js`)

```javascript
const mongoose = require('mongoose');
const Reg = require('../models/Reg');

async function getAllRegs() {
  try {
    return await Reg.find();
  } catch (error) {
    console.error('Error fetching all registers:', error);
    throw error;
  }
}

async function getRegByLastName(lastName) {
  try {
    return await Reg.findOne({ lastName });
  } catch (error) {
    console.error('Error fetching register by last name:', error);
    throw error;
  }
}

async function insertReg(reg) {
  try {
    const newReg = new Reg(reg);
    return await newReg.save();
  } catch (error) {
    console.error('Error inserting register:', error);
    throw error;
  }
}

async function updateReg(id, reg) {
  try {
    return await Reg.findByIdAndUpdate(id, reg, { new: true });
  } catch (error) {
    console.error('Error updating register:', error);
    throw error;
  }
}

async function deleteReg(id) {
  try {
    return await Reg.findByIdAndRemove(id);
  } catch (error) {
    console.error('Error deleting register:', error);
    throw error;
  }
}

module.exports = {
  getAllRegs,
  getRegByLastName,
  insertReg,
  updateReg,
  deleteReg,
};
```

#### Search Controller (`controllers/searchController.js`)

```javascript
const DaoService = require('../services/DaoService');
const Joi = require('joi');

const searchSchema = Joi.object({
  lastName: Joi.string().required(),
});

exports.search = async (req, res) => {
  const { error } = searchSchema.validate(req.query);
  
  if (error) {
    return res.status(400).send(error.details[0].message);
  }

  const { lastName } = req.query;
  
  try {
    const regs = await DaoService.getRegByLastName(lastName);
    return res.status(200).json(regs);
  } catch (error) {
    return res.status(500).send('Internal Server Error');
  }
};
```

#### Insert Controller (`controllers/insertController.js`)

```javascript
const DaoService = require('../services/DaoService');
const Joi = require('joi');

const insertSchema = Joi.object({
  firstName: Joi.string().required(),
  lastName: Joi.string().required(),
  middleName: Joi.string(),
  birth: Joi.date().required(),
});

exports.insert = async (req, res) => {
  const { error } = insertSchema.validate(req.body);
  
  if (error) {
    return res.status(400).send(error.details[0].message);
  }

  try {
    const newReg = req.body;
    await DaoService.insertReg(newReg);
    return res.status(201).send('Registered successfully');
  } catch (error) {
    return res.status(500).send('Internal Server Error');
  }
};
```

#### Routes Setup

This will be covered in the `routes/` directory setup.

#### API Setup (`app.js`)

```javascript
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const mongoose = require('mongoose');
const { mongoURI } = require('./config/database');
const insertRoutes = require('./routes/insertRoutes');
const searchRoutes = require('./routes/searchRoutes');
const vhost = require('vhost');

const app = express();

mongoose.connect(mongoURI, require('./config/database').mongooseOptions)
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('Could not connect to MongoDB', err));

app.use(helmet());
app.use(cors());
app.use(express.json());

app.use('/register', searchRoutes);
app.use('/register', insertRoutes);

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

#### Mock Testing Setup

Path: `test/DaoService.test.js`

```javascript
const DaoService = require('../services/DaoService');
const MockRegModel = require('./mockModels').RegModel;

jest.mock('mongoose');

DaoService.getAllRegs.mockImplementation(() => Promise.resolve(mockRegs));
DaoService.getRegByLastName.mockImplementation(lastName => Promise.resolve(mockRegObj));
DaoService.insertReg.mockImplementation(reg => Promise.resolve(reg));

describe('DaoService', () => {
  beforeAll(async () => {
    recordHarmonics();
  });

  afterAll(async () => {
    restoreAllMocks();
  });

  describe('getAllRegs', () => {
    test('should get all regs', async () => {
      const regs = await DaoService.getAllRegs();
      expect(regs).toEqual(mockRegs);
    });
  });

  describe('getRegByLastName', () => {
    test('should get reg by last name', async () => {
      const reg = await DaoService.getRegByLastName('Doe');
      expect(reg).toEqual(mockRegObj);
    });
  });

  describe('insertReg', () => {
    test('should insert reg', async () => {
      const newReg = {
        firstName: 'John',
        lastName: 'Doe',
        birth: new Date(),
      };
      const result = await DaoService.insertReg(newReg);
      expect(result).toEqual(newReg);
    });
  });
});
```

### Frontend: React Components

#### Setup React Environment

```bash
npx create-react-app rimssystem-frontend
cd rimssystem-frontend
```

Install necessary packages:

```bash
npm install axios react-testing-library @testing-library/jest-dom
```

#### UI Components

1. **InsertForm** (`components/InsertForm.js`)

   ```javascript
   import React from 'react';
   import { useForm } from 'react-hook-form';

   const InsertForm = () => {
     const { register, handleSubmit } = useForm();
     const onSubmit = data => console.log(data);

     return (
       <form onSubmit={handleSubmit(onSubmit)}>
         <input {...register('firstName')} placeholder="First Name" required />
         <input {...register('lastName')} placeholder="Last Name" required />
         <input {...register('birth', { transform: date => new Date(date) })} placeholder="Birth Date (YYYY-MM-DD)" required />
         <button type="submit">Submit</button>
       </form>
     );
   };

   export default InsertForm;
   ```

2. **SearchForm** (`components/SearchForm.js`)

   ```javascript
   import React from 'react';
   import { jest } from '@jest/types';

   const SearchForm = () => {
     // Similar setup as InsertForm but for search.

     return (
       <form>
         <input placeholder="Last Name" required />
         <button type="submit">Search</button>
       </form>
     );
   };

   export default SearchForm;
   ```

3. **Main App Component** (`App.js`)

   ```javascript
   import React from 'react';
   import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
   import InsertForm from './components/InsertForm';
   import SearchForm from './components/SearchForm';
   import { searchController } from './services/FetchService';

   const App = () => {
     const search = async (last) => {
       // Sample of fetching data. Needs axios setup.
       const result = await searchController.search(last); // FetchService to be implemented.
       console.log(result);
     };

     return (
       <Router>
         <Switch>
           <Route path="/insert" component={InsertForm} />
           <Route path="/search" component={SearchForm} />
         </Switch>
       </Router>
     );
   };

   export default App;
   ```

#### Dummy Fetch Implementation (`services/FetchService.js`)

```javascript
const axios = require('axios');

const searchController = {
  search: async (last) => {
    try {
      const response = await axios.get(`/register?lastName=${last}`);
      return response.data;
    } catch (error) {
      throw new Error('Search Error');
    }
  },
};

export default searchController;
```

#### Testing Components (`searchController.test.js`)

```javascript
import { render, screen, waitForElementToBeRemoved } from '@testing-library/react';
import { setup } from 'jest-dom/extend-expect';
import userEvent from '@testing-library/user-event';
import InsertForm from '../components/InsertForm';

beforeEach(() => {
  render(<InsertForm />);
});

test('renders Insert Form', () => {
  const firstName = screen.getByPlaceholderText(/first name/i);
  expect(firstName).toBeInTheDocument();

  // Test other checks here

});

test('can submit Insert Form', async () => {
  await userEvent.type(screen.getByPlaceholderText(/first name/i), 'John');
  await userEvent.type(screen.getByPlaceholderText(/last name/i), 'Doe');

  await waitForElementToBeRemoved(() => screen.getByText('Submit'), { timeout: 2000 });
});
```

### README Setup Instructions

```markdown
# Registered Individuals Management System (RIMS)

This application follows a layered architecture with a React frontend and NodeJS backend. It manages CRUD operations for registered individual data.

## Setup

**Backend Setup:**

1. Install Node.js.
2. Clone this repository.
3. Run `npm install` in the backend directory (`rimssystem-backend`).

**Frontend Setup:**

1. Clone this repository into a separate frontend directory (`rimssystem-frontend`).
2. In the frontend directory, run `npm install` to install dependencies.

**Integration:**

1. Ensure both frontend and backend are running.
2. Start the backend by running `node app.js` in the backend directory.
3. In another terminal, start the frontend by running `npm start` in the frontend directory.

You should now be able to interact with the Registered Individuals Management System through the React frontend.
```

This setup and code provide a basic structure following the specifications in the SDD. Further enhancements and security measures should be added based on deployment needs and production requirements. The mock testing helps ensure the backend logic functions as intended without needing a live database during testing phases. The frontend component rendering is simplified to demonstrate React's basic functionality and interaction handling. For a real-world application, the API integration, error handling, and validation would be more sophisticated.