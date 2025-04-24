# Django Shopping Cart Application

This is a Django-based shopping cart application that allows users to browse products, add them to a cart, update quantities, and view the cart details. The application supports user authentication and session-based cart management for unauthenticated users.

---

## **Features**

- **Product Listing**: Displays a list of available products with their prices.
- **Add to Cart**: Users can add products to their cart and specify quantities.
- **Cart Management**:
  - View cart details, including product names, prices, and quantities.
  - Update product quantities in the cart.
  - Remove products from the cart.
- **User Authentication**:
  - Authenticated users have their cart data stored in the database.
  - Unauthenticated users have their cart data stored in the session.
- **Dynamic Pricing**: Supports product-specific discount rules based on quantity.

---

## **Technologies Used**

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (with Fetch API)
- **Database**: SQLite (default Django database)
- **Session Management**: Django sessions for unauthenticated users

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

3. Install Dependencies
Install the required Python packages using pip:

pip install -r requirements.txt
4. Apply Migrations
Run the following commands to set up the database:

python manage.py makemigrations
python manage.py migrate
5. Create a Superuser
Create an admin user to access the Django admin panel:

python manage.py createsuperuser
6. Run the Development Server
Start the Django development server:

python manage.py runserver
Visit the application at http://127.0.0.1:8000/.