# Software CourseWork - Supabase Authentication App

A React application with Supabase integration featuring role-based authentication for Users and Business Owners.

## Features

- 🔐 **Dual Authentication System**: Separate login flows for Users and Business Owners
- 👤 **Role-Based Access Control**: Different dashboards and features based on user roles
- 🔒 **Secure Database**: Row-level security with Supabase
- 🎨 **Modern UI**: Responsive design with gradient backgrounds and glassmorphism effects
- ⚡ **Fast Development**: Built with Vite and TypeScript

## Setup Instructions

### 1. Database Setup

The application uses Supabase as the backend. Run the SQL commands in `database/schema.sql` in your Supabase project to set up the necessary tables and functions.

**Important SQL Commands to run in Supabase SQL Editor:**

```sql
-- Run the entire content of database/schema.sql in your Supabase project
-- This will create:
-- - user_profiles table with role-based access
-- - RLS (Row Level Security) policies
-- - Automatic profile creation triggers
-- - User role management functions
```

### 2. Environment Setup

The Supabase configuration is already set up in `src/lib/supabase.ts` with the provided credentials:
- **URL**: `https://clwausuodzmfrdrpckgj.supabase.co`
- **Anon Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`

### 3. Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Build for Production

```bash
# Build the application
npm run build

# Preview the production build
npm run preview
```

## User Roles

### Regular Users
- Browse services and products
- View order history
- Manage favorites
- Update profile settings

### Business Owners
- Manage products/services
- Customer relationship management
- View business analytics
- Configure business settings

## Project Structure

```
src/
├── components/          # React components
│   ├── AuthForm.tsx    # Authentication forms
│   ├── Dashboard.tsx   # Role-based dashboards
│   └── Landing.tsx     # Landing page with role selection
├── contexts/           # React contexts
│   └── AuthContext.tsx # Authentication state management
├── lib/               # Utilities and configurations
│   └── supabase.ts    # Supabase client and types
└── App.tsx           # Main application component

database/
└── schema.sql        # Database schema and setup
```

## Authentication Flow

1. **Role Selection**: Users choose between "User" or "Business Owner"
2. **Sign Up/Sign In**: Role-specific authentication forms
3. **Profile Creation**: Automatic profile creation with selected role
4. **Dashboard Access**: Role-based dashboard with appropriate features

## Database Schema

### user_profiles table
- `id` (uuid): References auth.users.id
- `email` (text): User's email address
- `role` (text): Either 'user' or 'business_owner'
- `full_name` (text): User's full name (optional)
- `business_name` (text): Business name for business owners (optional)
- `created_at` (timestamp): Account creation time
- `updated_at` (timestamp): Last profile update time

## Security Features

- Row Level Security (RLS) enabled
- Users can only access their own profiles
- Role-based access control
- Secure authentication with Supabase Auth
- Automatic profile creation on user signup

## Technologies Used

- **Frontend**: React 18, TypeScript, Vite
- **Backend**: Supabase (PostgreSQL, Auth, Real-time)
- **Styling**: CSS3 with modern features (Grid, Flexbox, Backdrop-filter)
- **State Management**: React Context API
- **Build Tool**: Vite
- **Package Manager**: npm

## Development Notes

- The application uses TypeScript for type safety
- Modern CSS features like backdrop-filter for glassmorphism effects
- Responsive design that works on mobile and desktop
- Error handling for authentication flows
- Loading states for better user experience
