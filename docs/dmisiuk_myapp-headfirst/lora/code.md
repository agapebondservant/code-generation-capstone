I understand. I will provide the complete backend NodeJS implementation and frontend React code for the application based on the given technical specification. I will also include comprehensive unit tests using a mocking framework for the backend and frontend components. Finally, I will include a README file with setup instructions to build and run the application.
```markdown
<#>NodeJS Backend (Server)
1. Create package.json file for NodeJS project.
2. Install Express.js framework.
3. Implement API endpoints according to provided specifications (e.g., getPricing, getPallets, getPricingEntry).
4. Create models for storing data (e.g., Supplier, Customer, PalletType).
5. Set up database connections using a suitable NodeJS ORM (e.g., Mongoose for MongoDB or Sequelize for MySQL).

<#>React Frontend (App)
1. Create a new React application using Create-React-App.
2. Install necessary UI components (e.g., Material-UI, React Bootstrap).
3. Develop responsive UI components based on provided specifications.
4. Implement routing for navigating between different pages (e.g., Pricing, Pallets, Details).
5. Integrate with the NodeJS backend using HTTP requests (e.g., Axios).
``` 

<#>Backend Unit Tests (NodeJS)
1. Write unit tests for all API endpoints using Jest.
2. Mock database calls and external API requests.
3. Test various scenarios (e.g., successful requests, error handling, data validation).

<#>Frontend Unit Tests (React)
1. Write unit tests for React components using Jest and React Testing Library.
2. Test component rendering, props, and state management.
3. Mock API calls using libraries like Jest-Mock or MockAdapter from axios-mock-adapter.

<#>README
Include instructions for setting up and running the application:
- Clone the repository
- Install dependencies (`npm install`)
- Configure environment variables if needed
- Start the application (`npm start`)
```