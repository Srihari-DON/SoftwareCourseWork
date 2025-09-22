# Database Management

Comprehensive examples and tutorials for database design, management, and integration.

## 🗄️ Database Types

### Relational Databases (SQL)
- **PostgreSQL** - Advanced open-source database
- **MySQL** - Popular web application database
- **SQLite** - Lightweight embedded database
- **Microsoft SQL Server** - Enterprise database system

### NoSQL Databases
- **MongoDB** - Document-based database
- **Redis** - In-memory key-value store
- **Cassandra** - Distributed wide-column database
- **Elasticsearch** - Search and analytics engine

### Specialized Databases
- **Neo4j** - Graph database
- **InfluxDB** - Time-series database
- **Firebase** - Real-time database
- **DynamoDB** - AWS managed NoSQL

## 📊 Database Concepts

### Design Principles
- **Normalization** - Reducing data redundancy
- **ACID Properties** - Atomicity, Consistency, Isolation, Durability
- **CAP Theorem** - Consistency, Availability, Partition tolerance
- **Indexing** - Optimizing query performance

### Query Languages
- **SQL** - Structured Query Language for relational databases
- **NoSQL Queries** - Various query methods for NoSQL databases
- **GraphQL** - Query language for APIs
- **ORM/ODM** - Object-relational mapping tools

## 📁 Structure

```
databases/
├── sql/               # SQL database examples
│   ├── schema/        # Database schemas
│   ├── queries/       # SQL queries
│   ├── migrations/    # Database migrations
│   └── optimization/  # Performance optimization
├── nosql/             # NoSQL database examples
│   ├── mongodb/       # MongoDB examples
│   ├── redis/         # Redis examples
│   └── elasticsearch/ # Elasticsearch examples
├── design/            # Database design patterns
├── integration/       # Application integration examples
└── tools/             # Database tools and utilities
```

## 🚀 Quick Examples

### SQL Basics
```sql
-- Create table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO users (username, email) 
VALUES ('john_doe', 'john@example.com');

-- Query data
SELECT * FROM users WHERE username = 'john_doe';

-- Update data
UPDATE users SET email = 'newemail@example.com' 
WHERE username = 'john_doe';
```

### MongoDB Basics
```javascript
// Insert document
db.users.insertOne({
    username: "john_doe",
    email: "john@example.com",
    profile: {
        firstName: "John",
        lastName: "Doe"
    },
    tags: ["developer", "javascript"]
});

// Query document
db.users.findOne({ username: "john_doe" });

// Update document
db.users.updateOne(
    { username: "john_doe" },
    { $set: { "profile.age": 30 } }
);
```

## 🛠️ Tools & Utilities

### Database Administration
- **pgAdmin** - PostgreSQL administration
- **MySQL Workbench** - MySQL administration
- **MongoDB Compass** - MongoDB GUI
- **Redis CLI** - Redis command line interface

### Development Tools
- **Sequelize** - Node.js ORM for SQL databases
- **Mongoose** - MongoDB object modeling for Node.js
- **SQLAlchemy** - Python SQL toolkit and ORM
- **Prisma** - Modern database toolkit

### Migration Tools
- **Flyway** - Database migration tool
- **Liquibase** - Database schema change management
- **Alembic** - SQLAlchemy database migration tool
- **migrate** - Go database migration library