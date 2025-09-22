#!/bin/bash

# Project Setup Script
# Initializes a new software project with common structure and configurations

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Project types
PROJECT_TYPES=("web" "api" "desktop" "mobile" "library")

# Print colored output
print_colored() {
    echo -e "${1}${2}${NC}"
}

print_success() {
    print_colored "$GREEN" "✓ $1"
}

print_error() {
    print_colored "$RED" "✗ $1"
}

print_warning() {
    print_colored "$YELLOW" "⚠ $1"
}

print_info() {
    print_colored "$BLUE" "ℹ $1"
}

# Function to display usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -n, --name NAME        Project name (required)"
    echo "  -t, --type TYPE        Project type: web, api, desktop, mobile, library"
    echo "  -l, --language LANG    Primary language: python, javascript, java, cpp"
    echo "  -g, --git             Initialize Git repository"
    echo "  -d, --docker          Add Docker configuration"
    echo "  -v, --verbose         Verbose output"
    echo "  -h, --help            Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 -n my-web-app -t web -l javascript -g -d"
    echo "  $0 --name api-service --type api --language python --git"
}

# Default values
PROJECT_NAME=""
PROJECT_TYPE="web"
LANGUAGE="javascript"
INIT_GIT=false
ADD_DOCKER=false
VERBOSE=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -n|--name)
            PROJECT_NAME="$2"
            shift 2
            ;;
        -t|--type)
            PROJECT_TYPE="$2"
            shift 2
            ;;
        -l|--language)
            LANGUAGE="$2"
            shift 2
            ;;
        -g|--git)
            INIT_GIT=true
            shift
            ;;
        -d|--docker)
            ADD_DOCKER=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# Validate required arguments
if [[ -z "$PROJECT_NAME" ]]; then
    print_error "Project name is required"
    usage
    exit 1
fi

# Validate project type
if [[ ! " ${PROJECT_TYPES[@]} " =~ " ${PROJECT_TYPE} " ]]; then
    print_error "Invalid project type: $PROJECT_TYPE"
    print_info "Available types: ${PROJECT_TYPES[*]}"
    exit 1
fi

# Verbose logging function
log_verbose() {
    if [[ "$VERBOSE" == true ]]; then
        print_info "$1"
    fi
}

print_info "Starting project initialization..."
print_info "Project Name: $PROJECT_NAME"
print_info "Project Type: $PROJECT_TYPE"
print_info "Language: $LANGUAGE"

# Create project directory
if [[ -d "$PROJECT_NAME" ]]; then
    print_error "Directory '$PROJECT_NAME' already exists"
    exit 1
fi

mkdir "$PROJECT_NAME"
cd "$PROJECT_NAME"
print_success "Created project directory: $PROJECT_NAME"

# Create basic directory structure
log_verbose "Creating directory structure..."

case $PROJECT_TYPE in
    "web")
        mkdir -p src/{components,pages,styles,utils,assets}
        mkdir -p public
        mkdir -p tests/{unit,integration,e2e}
        mkdir -p docs
        ;;
    "api")
        mkdir -p src/{controllers,models,services,middleware,utils}
        mkdir -p tests/{unit,integration}
        mkdir -p docs
        mkdir -p config
        ;;
    "desktop")
        mkdir -p src/{ui,core,utils}
        mkdir -p resources
        mkdir -p tests
        mkdir -p docs
        ;;
    "mobile")
        mkdir -p src/{screens,components,services,utils}
        mkdir -p assets/{images,fonts}
        mkdir -p tests
        mkdir -p docs
        ;;
    "library")
        mkdir -p src
        mkdir -p tests
        mkdir -p docs
        mkdir -p examples
        ;;
esac

print_success "Created directory structure for $PROJECT_TYPE project"

# Create language-specific files
log_verbose "Creating language-specific files..."

case $LANGUAGE in
    "javascript")
        # Package.json
        cat > package.json << EOF
{
  "name": "$PROJECT_NAME",
  "version": "1.0.0",
  "description": "",
  "main": "src/index.js",
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "test:watch": "jest --watch",
    "lint": "eslint src/",
    "lint:fix": "eslint src/ --fix",
    "build": "webpack --mode production"
  },
  "keywords": [],
  "author": "",
  "license": "MIT",
  "devDependencies": {
    "jest": "^29.0.0",
    "eslint": "^8.0.0",
    "nodemon": "^2.0.0"
  }
}
EOF
        
        # Basic index.js
        cat > src/index.js << EOF
// $PROJECT_NAME
// Main entry point

console.log('Hello from $PROJECT_NAME!');

// Export main functionality
module.exports = {
    // Add your exports here
};
EOF
        
        # Basic test file
        cat > tests/unit/index.test.js << EOF
// Test file for $PROJECT_NAME

describe('$PROJECT_NAME', () => {
    test('should work correctly', () => {
        expect(true).toBe(true);
    });
});
EOF
        
        print_success "Created JavaScript project files"
        ;;
        
    "python")
        # Setup.py
        cat > setup.py << EOF
from setuptools import setup, find_packages

setup(
    name="$PROJECT_NAME",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
    ],
    author="",
    author_email="",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
EOF
        
        # Requirements files
        touch requirements.txt
        cat > requirements-dev.txt << EOF
pytest>=7.0.0
black>=22.0.0
flake8>=4.0.0
mypy>=0.950
pytest-cov>=3.0.0
EOF
        
        # Main Python file
        cat > src/__init__.py << EOF
"""$PROJECT_NAME package."""

__version__ = "1.0.0"
__author__ = ""
__email__ = ""
EOF
        
        cat > src/main.py << EOF
"""Main module for $PROJECT_NAME."""


def main():
    """Main entry point."""
    print("Hello from $PROJECT_NAME!")


if __name__ == "__main__":
    main()
EOF
        
        # Basic test file
        mkdir -p tests
        cat > tests/__init__.py << EOF
"""Tests package."""
EOF
        
        cat > tests/test_main.py << EOF
"""Tests for main module."""

import pytest
from src.main import main


def test_main():
    """Test main function."""
    # Add your tests here
    assert True
EOF
        
        # Pytest configuration
        cat > pytest.ini << EOF
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short
EOF
        
        print_success "Created Python project files"
        ;;
        
    "java")
        # Create Maven structure
        mkdir -p src/{main,test}/java/com/example/$PROJECT_NAME
        mkdir -p src/main/resources
        mkdir -p src/test/resources
        
        # POM.xml
        cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>$PROJECT_NAME</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.version>5.8.2</junit.version>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>\${junit.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M7</version>
            </plugin>
        </plugins>
    </build>
</project>
EOF
        
        # Main Java class
        PROJECT_CLASS=$(echo $PROJECT_NAME | sed 's/[^a-zA-Z0-9]//g' | sed 's/^./\U&/')
        cat > src/main/java/com/example/$PROJECT_NAME/App.java << EOF
package com.example.$PROJECT_NAME;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello from $PROJECT_NAME!");
    }
}
EOF
        
        # Test class
        cat > src/test/java/com/example/$PROJECT_NAME/AppTest.java << EOF
package com.example.$PROJECT_NAME;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    @Test
    void testApp() {
        assertTrue(true);
    }
}
EOF
        
        print_success "Created Java project files"
        ;;
esac

# Create common files
log_verbose "Creating common project files..."

# README.md
cat > README.md << EOF
# $PROJECT_NAME

## Description
Brief description of your $PROJECT_TYPE project.

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation

### Prerequisites
- List prerequisites here

### Setup
\`\`\`bash
# Clone the repository
git clone <repository-url>
cd $PROJECT_NAME

# Install dependencies
# Add installation commands here
\`\`\`

## Usage
\`\`\`bash
# Add usage examples here
\`\`\`

## Development

### Running Tests
\`\`\`bash
# Add test commands here
\`\`\`

### Building
\`\`\`bash
# Add build commands here
\`\`\`

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for your changes
5. Submit a pull request

## License
MIT License - see LICENSE file for details
EOF

# .gitignore
case $LANGUAGE in
    "javascript")
        cat > .gitignore << EOF
# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Production builds
dist/
build/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
logs/
*.log

# Coverage reports
coverage/
.nyc_output/
EOF
        ;;
    "python")
        cat > .gitignore << EOF
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Testing
.pytest_cache/
.coverage
htmlcov/

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Environment variables
.env
EOF
        ;;
    "java")
        cat > .gitignore << EOF
# Compiled class files
*.class

# Log files
*.log

# Package files
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties

# IDEs
.idea/
.vscode/
*.iws
*.iml
*.ipr

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db
EOF
        ;;
esac

# MIT License
cat > LICENSE << EOF
MIT License

Copyright (c) $(date +%Y)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

print_success "Created common project files"

# Initialize Git repository
if [[ "$INIT_GIT" == true ]]; then
    log_verbose "Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Project setup for $PROJECT_NAME"
    print_success "Initialized Git repository"
fi

# Add Docker configuration
if [[ "$ADD_DOCKER" == true ]]; then
    log_verbose "Adding Docker configuration..."
    
    case $LANGUAGE in
        "javascript")
            cat > Dockerfile << EOF
FROM node:16-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY src/ ./src/

# Expose port
EXPOSE 3000

# Start application
CMD ["npm", "start"]
EOF
            ;;
        "python")
            cat > Dockerfile << EOF
FROM python:3.9-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Start application
CMD ["python", "src/main.py"]
EOF
            ;;
        "java")
            cat > Dockerfile << EOF
FROM openjdk:11-jre-slim

WORKDIR /app

# Copy JAR file
COPY target/$PROJECT_NAME-1.0.0.jar app.jar

# Expose port
EXPOSE 8080

# Start application
CMD ["java", "-jar", "app.jar"]
EOF
            ;;
    esac
    
    # Docker Compose
    cat > docker-compose.yml << EOF
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
    volumes:
      - .:/app
      - /app/node_modules
    
  # Add other services as needed
  # database:
  #   image: postgres:13
  #   environment:
  #     POSTGRES_DB: $PROJECT_NAME
  #     POSTGRES_USER: user
  #     POSTGRES_PASSWORD: password
  #   ports:
  #     - "5432:5432"
EOF
    
    print_success "Added Docker configuration"
fi

# Create development scripts
mkdir -p scripts
cat > scripts/setup.sh << 'EOF'
#!/bin/bash
# Development setup script

echo "Setting up development environment..."

# Add setup commands here based on your project needs
# Example: npm install, pip install, etc.

echo "Setup complete!"
EOF

cat > scripts/test.sh << 'EOF'
#!/bin/bash
# Run all tests

echo "Running tests..."

# Add test commands here based on your project type
# Example: npm test, pytest, mvn test, etc.

echo "Tests complete!"
EOF

chmod +x scripts/*.sh

print_success "Created development scripts"

# Final summary
echo ""
print_info "Project initialization complete!"
echo ""
print_success "Project: $PROJECT_NAME"
print_success "Type: $PROJECT_TYPE"
print_success "Language: $LANGUAGE"
print_success "Location: $(pwd)"

if [[ "$INIT_GIT" == true ]]; then
    print_success "Git repository initialized"
fi

if [[ "$ADD_DOCKER" == true ]]; then
    print_success "Docker configuration added"
fi

echo ""
print_info "Next steps:"
echo "  1. cd $PROJECT_NAME"
echo "  2. Review and customize the generated files"
echo "  3. Install dependencies for your language"
echo "  4. Start developing!"

if [[ "$INIT_GIT" == true ]]; then
    echo "  5. Set up remote repository: git remote add origin <url>"
fi

echo ""
print_info "Happy coding! 🚀"