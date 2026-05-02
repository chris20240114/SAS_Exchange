# SAS Exchange

A full-featured peer-to-peer marketplace platform built with Django. SAS Exchange allows users to list items for sale, browse available products, and communicate with other buyers and sellers through an integrated messaging system.

SAS: Shanghai American School puxi. This project was built in 2023 meant for the use of Shanghai American School puxi students.

## 🎯 Project Overview

SAS Exchange is a production-grade marketplace application designed to facilitate item trading and selling between authenticated users. The platform includes seller verification, item categorization, search functionality, and real-time user communication—demonstrating full-stack web development capabilities.

**Purpose:** Peer-to-peer marketplace platform  
**User Base:** Community sellers and buyers  
**Key Features:** Item listings, messaging, seller approval system

## 🏗️ Architecture & Features

### Core Functionality
- **Item Marketplace** - Browse, list, search, and filter items by category
- **User Authentication** - Secure user registration and login system
- **Seller Verification** - Approval-based seller account system
- **Messaging System** - Direct communication between buyers and sellers
- **Search & Discovery** - Full-text search with category filtering
- **Item Management** - Create, edit, and manage listings with images
- **Category Organization** - Organized product catalog structure

### Technical Architecture
```
Backend Layer:
  - Django MVT architecture
  - Django ORM for database operations
  - User authentication and permissions
  - Admin dashboard for management

Frontend Layer:
  - Django templates for server-side rendering
  - Bootstrap/CSS styling
  - Responsive forms for item creation/editing

Database:
  - SQLite (development) / PostgreSQL (production-ready)
  - Relational models for items, categories, users, messages
```

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Framework** | Django 3.x/4.x |
| **Language** | Python |
| **Frontend** | HTML5, CSS3, Django Templates |
| **Database** | SQLite / PostgreSQL |
| **Authentication** | Django Auth Framework |
| **Media Handling** | Django ImageField with file uploads |
| **Search** | Django ORM Q objects for full-text search |

## ✨ Key Features Explained

### 1. **Item Listing System**
- Users can create items with category, name, description, price, and images
- Items tracked with `is_sold` status to manage active listings
- Related items shown on detail pages for discovery
- Timestamp tracking for item creation

### 2. **Search & Filtering**
- Full-text search across item names and descriptions
- Category-based filtering for browsing
- Combined search + category filtering capabilities
- Clean query parameters for SEO-friendly URLs

### 3. **Seller Approval Workflow**
- Users must be approved as sellers before listing items
- `Seller.get_approval()` checks seller status
- Redirects non-approved users to seller application page
- Security measure to maintain marketplace quality

### 4. **Messaging System**
- Direct communication between buyers and sellers
- Attached to item listings for context
- Support for ongoing conversations
- User relationship tracking

### 5. **User Authorization**
- Login requirements on listing/editing endpoints
- Ownership verification (users can only edit their own items)
- Permission-based access control
- Django's `@login_required` decorator usage

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or poetry
- Virtual environment

### Installation & Setup

```bash
# Clone repository
git clone <repository-url>
cd SAS_Exchange/marketplace

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

### Access Admin Dashboard
Navigate to [http://localhost:8000/admin](http://localhost:8000/admin) and log in with your superuser credentials.

## 📁 Project Structure

```
marketplace/
├── item/                 # Item listings app
│   ├── models.py        # Item, Category models
│   ├── views.py         # Browse, create, edit items
│   ├── forms.py         # Item creation/editing forms
│   ├── urls.py          # Item app routing
│   └── templates/       # Item listing templates
├── conversation/        # Messaging system app
│   ├── models.py        # Message, Conversation models
│   ├── views.py         # Messaging logic
│   └── templates/       # Conversation templates
├── core/                # Core app (Seller model, etc.)
├── marketplace/         # Main project settings
│   ├── settings.py      # Django configuration
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # Production deployment
├── manage.py            # Django CLI
└── db.sqlite3          # Development database
```

## 🔧 Database Models

### Item Model
```python
- category (ForeignKey to Category)
- name (CharField)
- description (TextField)
- price (FloatField)
- image (ImageField)
- is_sold (BooleanField)
- created_by (ForeignKey to User)
- created (DateTimeField)
```

### Category Model
```python
- name (CharField)
- Ordering: alphabetical by name
```

### Seller Model
```python
- Approval status tracking
- get_approval() method for verification
```

## 🔐 Security & Permissions

- User authentication required for listing items
- Item ownership verification prevents unauthorized edits
- Seller approval system maintains marketplace quality
- Django's CSRF protection on all forms
- SQL injection prevention through ORM

## 📤 Deployment

### Production Considerations
- Switch to PostgreSQL for better scalability
- Use environment variables for sensitive settings
- Configure allowed hosts in `settings.py`
- Set `DEBUG = False` for production
- Use whitenoise for static file serving
- Deploy via Heroku, PythonAnywhere, AWS, or similar

### Deployment Checklist
```
- Update ALLOWED_HOSTS with domain
- Configure PostgreSQL database
- Set SECRET_KEY in environment variables
- Enable HTTPS/SSL
- Configure static files serving
- Set up email for password recovery
- Enable secure cookie settings
```

## 📋 What This Project Demonstrates

✅ **Full-Stack Django Development** - Models, views, templates, and routing  
✅ **Database Design** - Relational models with proper relationships  
✅ **User Authentication** - Secure login and permission system  
✅ **Advanced Queries** - Q objects for complex search functionality  
✅ **File Handling** - Image uploads and media management  
✅ **Responsive Forms** - Dynamic form validation and rendering  
✅ **Authorization Logic** - Ownership verification and approval systems  
✅ **Business Logic** - Seller approval workflow and item status tracking  
✅ **SEO Practices** - Clean URLs and querystring parameters  

## 🔄 Future Enhancement Ideas

- Real-time messaging with WebSockets
- Payment integration (Stripe/PayPal)
- User ratings and reviews system
- Advanced search with Elasticsearch
- Email notifications
- Image optimization and CDN delivery
- API (REST/GraphQL) for mobile clients
- Wishlist functionality

## 📞 Questions?

For questions about the architecture, features, or implementation details, feel free to reach out!
