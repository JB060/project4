# Inventory Management System

A Django-based web application to manage and track inventory items, organize them by categories, and receive alerts for low stock levels. This system allows users to register, authenticate, and access a personalized dashboard for efficient inventory management.

---

## User Experience (UX)

### Strategy

#### Project Goals
- Develop a user-friendly inventory management application for personal or small business use.
- Allow users to easily track inventory levels, organize items by category, and receive low-inventory alerts.

#### User Goals
- **Effortless item tracking**: Users should be able to add, edit, delete, and view items in their inventory.
- **Category organization**: Users can categorize items for easier navigation and organization.
- **Low inventory alerts**: Users receive warnings when items are running low to facilitate timely restocking.

#### Strategy Table

| Feature                | Importance | Viability |
|------------------------|------------|-----------|
| User authentication    | High       | High      |
| Item CRUD operations   | High       | High      |
| Low inventory alerts   | High       | High      |
| Category management    | Medium     | High      |
| Responsive design      | High       | High      |

---

### Scope

#### User Stories

1. As a user, I want to create an account so that I can securely log in to the app.
2. As a user, I want to add items to my inventory so that I can keep track of stock levels.
3. As a user, I want to categorize items to organize my inventory.
4. As a user, I want to receive alerts when items are running low to stay informed about restocking needs.
5. As a user, I want a dashboard that summarizes my inventory at a glance.

---

### Structure

- **Navigation**: Simple navigation with links to key features (dashboard, add item, sign in/out).
- **CRUD Operations**: Comprehensive item management options, including add, edit, delete, and view.
- **User Authentication**: Secure access to manage inventory.
![Start Page](media/project4-structure.png)



---

### Skeleton

- **Home Page**: Welcomes users and prompts them to log in or sign up.
- **Dashboard**: Main inventory management interface with a table of items.
- **Inventory Forms**: Forms for adding, editing, and deleting items.
- **Authentication Pages**: Separate pages for login, logout, and signup.

---

### Surface

- **Color Scheme**: Uses Bootstrap Minty theme for a clean, user-friendly interface.

![Color Swatch](media/Color-swatch.png)
- **Typography**: Readable and accessible fonts for a professional look.
- **Layout**: Responsive layout using Bootstrap grid, optimized for desktop and mobile.

---

## Features

### General
- **Responsive Design**: Accessible on all devices with a clean, minimalistic interface.
- **Error Messages**: Provides visual feedback for successful actions and alerts for low inventory.

### Home Page
- Introduces the app and allows users to log in or sign up.
![Home page](media/project4-startpage.png)


### Dashboard
- Displays an organized view of all inventory items.
- Allows for easy access to add, edit, or delete items.
![Dashboard Database](media/inventory-database.png)

### Authentication Pages
- **Login**: Authenticates existing users.
- **Signup**: Allows new users to register.
- **Logout**: Provides an option for users to log out securely.
![signin page](media/projet4-loginauthpage.png)
![Signup page](media/signup-page.png)
- New User added to the system.
![New User added](media/jasonbyrne060signup.png)
### Item Management Pages
- **Add Item**: Form to add a new item to the inventory.
![Dashboard Database](media/inventory-database.png)
![added item](media/item-added.png)
- **Edit Item**: Allows users to update item information.
![Dashboard Database](media/listed-itemsdropdown.png)
- **Delete Item**: Removes an item from the inventory.
![Dashboard Database](media/item-added.png)
- **Low Inventory Item**: Shows items with low inventory and gives a warning:
![New User added](media/jasonbyrne060signup.png)





---

## Technologies Used

### Languages Used
- **HTML5**: Structure and layout of pages.
- **CSS3**: Styling with Bootstrap framework.
- **Python**: Core application logic with Django framework.

### Libraries and Frameworks
- **Django**: Backend web framework for app functionality.
- **Bootstrap**: Frontend framework for styling and responsive design.
- **Crispy Forms**: For rendering Django forms with Bootstrap styling.

### Packages / Dependencies Installed
- **Django**: Main web framework.
- **Crispy Forms**: Enhances form styling with Bootstrap.
- **Django Authentication**: Manages user authentication flows.

### Database Management
- **SQLite**: Local database for development.
- **PostgreSQL** (optional): For production deployments.

### Tools and Programs
- **Visual Studio Code**: Development environment.
- **Git**: Version control.
- **Heroku**: For deployment.
- **Postman**: For testing API endpoints.
- **GitHub**: Version control and collaboration.

---

## Testing

The testing phase included a combination of manual and automated tests to ensure all functionality works as expected. 

### Manual Testing

Each feature was manually tested by simulating user interactions, including:
1. **User Authentication**: Verified sign-up, login, and logout functionalities.
2. **Inventory CRUD Operations**: Tested adding, editing, deleting, and viewing inventory items.
3. **Low Inventory Alerts**: Confirmed alerts display for items at or below the minimum threshold.
4. **Responsive Design**: Verified the application's compatibility across various screen sizes (desktop, tablet, and mobile).
5. **Error Handling**: Checked for error messages in case of incorrect inputs (e.g., empty fields).

### Automated Testing

Automated tests were written for critical components:
- **Models**: Validated data integrity and relationships, such as items linked to specific categories.
- **Views**: Ensured views return the correct data and templates based on user permissions.
- **Forms**: Tested form validation and field requirements.

---

## Deployment

### Steps to Deploy on Heroku

1. Create a Heroku account and install Heroku CLI.
2. Clone this repository and navigate to the project folder.
3. Run `heroku create` to create a new Heroku app.
4. Push the project to Heroku with `git push heroku main`.
5. Set environment variables and configure the database on Heroku.
6. Run `heroku run python manage.py migrate` to set up the database.

---

### Finished Product

Once deployed, access the live application to manage inventory items efficiently.








