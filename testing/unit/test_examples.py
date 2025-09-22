"""
Unit Testing Examples using pytest

This module demonstrates comprehensive unit testing practices
including fixtures, parameterized tests, mocking, and test organization.
"""

import pytest
import math
from typing import List, Dict, Any
from unittest.mock import Mock, patch, MagicMock
from dataclasses import dataclass
from datetime import datetime, timedelta


# Sample classes to test
@dataclass
class User:
    id: int
    username: str
    email: str
    is_active: bool = True
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()


class Calculator:
    """Simple calculator for testing basic operations"""
    
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        return base ** exponent
    
    def sqrt(self, value: float) -> float:
        if value < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(value)


class UserRepository:
    """Repository for user data operations"""
    
    def __init__(self, database):
        self.database = database
    
    def find_by_id(self, user_id: int) -> User:
        user_data = self.database.get(f"user:{user_id}")
        if not user_data:
            raise ValueError(f"User with id {user_id} not found")
        return User(**user_data)
    
    def find_by_username(self, username: str) -> User:
        users = self.database.query("users", {"username": username})
        if not users:
            raise ValueError(f"User with username {username} not found")
        return User(**users[0])
    
    def save(self, user: User) -> User:
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_active": user.is_active,
            "created_at": user.created_at.isoformat()
        }
        self.database.set(f"user:{user.id}", user_data)
        return user
    
    def get_active_users(self) -> List[User]:
        users_data = self.database.query("users", {"is_active": True})
        return [User(**data) for data in users_data]


class EmailService:
    """Service for sending emails"""
    
    def __init__(self, smtp_client):
        self.smtp_client = smtp_client
    
    def send_welcome_email(self, user: User) -> bool:
        subject = f"Welcome {user.username}!"
        body = f"Hello {user.username}, welcome to our platform!"
        
        try:
            self.smtp_client.send(
                to=user.email,
                subject=subject,
                body=body
            )
            return True
        except Exception:
            return False


# Test fixtures
@pytest.fixture
def calculator():
    """Provide a fresh calculator instance for each test"""
    return Calculator()


@pytest.fixture
def sample_user():
    """Provide a sample user for testing"""
    return User(
        id=1,
        username="john_doe",
        email="john@example.com",
        is_active=True,
        created_at=datetime(2024, 1, 1, 12, 0, 0)
    )


@pytest.fixture
def mock_database():
    """Mock database for testing repository"""
    mock_db = Mock()
    
    # Set up mock data
    mock_db.get.return_value = {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "is_active": True,
        "created_at": "2024-01-01T12:00:00"
    }
    
    mock_db.query.return_value = [{
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com",
        "is_active": True,
        "created_at": "2024-01-01T12:00:00"
    }]
    
    return mock_db


@pytest.fixture
def user_repository(mock_database):
    """Provide user repository with mocked database"""
    return UserRepository(mock_database)


@pytest.fixture
def mock_smtp_client():
    """Mock SMTP client for email testing"""
    return Mock()


@pytest.fixture
def email_service(mock_smtp_client):
    """Provide email service with mocked SMTP client"""
    return EmailService(mock_smtp_client)


# Basic unit tests
class TestCalculator:
    """Test suite for Calculator class"""
    
    def test_add_positive_numbers(self, calculator):
        result = calculator.add(2, 3)
        assert result == 5
    
    def test_add_negative_numbers(self, calculator):
        result = calculator.add(-2, -3)
        assert result == -5
    
    def test_add_mixed_numbers(self, calculator):
        result = calculator.add(-2, 3)
        assert result == 1
    
    def test_subtract_numbers(self, calculator):
        result = calculator.subtract(5, 3)
        assert result == 2
    
    def test_multiply_numbers(self, calculator):
        result = calculator.multiply(4, 5)
        assert result == 20
    
    def test_divide_numbers(self, calculator):
        result = calculator.divide(10, 2)
        assert result == 5
    
    def test_divide_by_zero_raises_error(self, calculator):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)
    
    def test_power_calculation(self, calculator):
        result = calculator.power(2, 3)
        assert result == 8
    
    def test_sqrt_positive_number(self, calculator):
        result = calculator.sqrt(9)
        assert result == 3
    
    def test_sqrt_negative_number_raises_error(self, calculator):
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            calculator.sqrt(-1)


# Parameterized tests
class TestCalculatorParameterized:
    """Parameterized tests for Calculator class"""
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (3.5, 2.5, 6.0)
    ])
    def test_add_various_inputs(self, calculator, a, b, expected):
        result = calculator.add(a, b)
        assert result == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (10, 2, 5),
        (100, 10, 10),
        (1, 1, 1),
        (0, 5, 0),
        (-10, 2, -5)
    ])
    def test_divide_various_inputs(self, calculator, a, b, expected):
        result = calculator.divide(a, b)
        assert result == expected
    
    @pytest.mark.parametrize("base,exponent,expected", [
        (2, 3, 8),
        (3, 2, 9),
        (5, 0, 1),
        (10, 1, 10),
        (2, -1, 0.5)
    ])
    def test_power_various_inputs(self, calculator, base, exponent, expected):
        result = calculator.power(base, exponent)
        assert result == expected


# Testing with mocks
class TestUserRepository:
    """Test suite for UserRepository with mocked dependencies"""
    
    def test_find_by_id_existing_user(self, user_repository, mock_database):
        user = user_repository.find_by_id(1)
        
        assert user.id == 1
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        mock_database.get.assert_called_once_with("user:1")
    
    def test_find_by_id_non_existing_user(self, user_repository, mock_database):
        mock_database.get.return_value = None
        
        with pytest.raises(ValueError, match="User with id 999 not found"):
            user_repository.find_by_id(999)
    
    def test_find_by_username(self, user_repository, mock_database):
        user = user_repository.find_by_username("john_doe")
        
        assert user.username == "john_doe"
        mock_database.query.assert_called_once_with("users", {"username": "john_doe"})
    
    def test_save_user(self, user_repository, mock_database, sample_user):
        saved_user = user_repository.save(sample_user)
        
        assert saved_user == sample_user
        mock_database.set.assert_called_once()
        
        # Verify the call arguments
        call_args = mock_database.set.call_args
        assert call_args[0][0] == "user:1"
        user_data = call_args[0][1]
        assert user_data["username"] == "john_doe"
        assert user_data["email"] == "john@example.com"
    
    def test_get_active_users(self, user_repository, mock_database):
        users = user_repository.get_active_users()
        
        assert len(users) == 1
        assert users[0].username == "john_doe"
        assert users[0].is_active is True
        mock_database.query.assert_called_once_with("users", {"is_active": True})


class TestEmailService:
    """Test suite for EmailService with mocked SMTP client"""
    
    def test_send_welcome_email_success(self, email_service, mock_smtp_client, sample_user):
        mock_smtp_client.send.return_value = True
        
        result = email_service.send_welcome_email(sample_user)
        
        assert result is True
        mock_smtp_client.send.assert_called_once()
        
        # Verify call arguments
        call_args = mock_smtp_client.send.call_args
        assert call_args[1]["to"] == "john@example.com"
        assert "Welcome john_doe!" in call_args[1]["subject"]
        assert "Hello john_doe" in call_args[1]["body"]
    
    def test_send_welcome_email_failure(self, email_service, mock_smtp_client, sample_user):
        mock_smtp_client.send.side_effect = Exception("SMTP Error")
        
        result = email_service.send_welcome_email(sample_user)
        
        assert result is False
        mock_smtp_client.send.assert_called_once()


# Test class for User model
class TestUser:
    """Test suite for User dataclass"""
    
    def test_user_creation_with_defaults(self):
        user = User(1, "testuser", "test@example.com")
        
        assert user.id == 1
        assert user.username == "testuser"
        assert user.email == "test@example.com"
        assert user.is_active is True
        assert isinstance(user.created_at, datetime)
    
    def test_user_creation_with_all_fields(self):
        created_time = datetime(2024, 1, 1, 10, 0, 0)
        user = User(
            id=2,
            username="testuser2",
            email="test2@example.com",
            is_active=False,
            created_at=created_time
        )
        
        assert user.id == 2
        assert user.username == "testuser2"
        assert user.email == "test2@example.com"
        assert user.is_active is False
        assert user.created_at == created_time


# Integration-style tests
class TestUserWorkflow:
    """Integration tests for user-related workflows"""
    
    @pytest.fixture
    def user_workflow_setup(self, mock_database, mock_smtp_client):
        """Set up complete user workflow dependencies"""
        repository = UserRepository(mock_database)
        email_service = EmailService(mock_smtp_client)
        return repository, email_service
    
    def test_create_and_welcome_user_workflow(self, user_workflow_setup, mock_database, mock_smtp_client):
        repository, email_service = user_workflow_setup
        
        # Create new user
        new_user = User(
            id=2,
            username="newuser",
            email="newuser@example.com"
        )
        
        # Save user
        saved_user = repository.save(new_user)
        
        # Send welcome email
        email_sent = email_service.send_welcome_email(saved_user)
        
        # Assertions
        assert saved_user.username == "newuser"
        assert email_sent is True
        
        # Verify interactions
        mock_database.set.assert_called_once()
        mock_smtp_client.send.assert_called_once()


# Performance and property-based tests
class TestCalculatorProperties:
    """Property-based and performance tests"""
    
    def test_add_commutative_property(self, calculator):
        """Test that addition is commutative: a + b = b + a"""
        a, b = 3, 5
        assert calculator.add(a, b) == calculator.add(b, a)
    
    def test_multiply_identity_property(self, calculator):
        """Test that multiplying by 1 returns the original number"""
        number = 42
        assert calculator.multiply(number, 1) == number
    
    def test_divide_and_multiply_inverse_operations(self, calculator):
        """Test that division and multiplication are inverse operations"""
        number = 10
        divisor = 3
        
        result = calculator.divide(number, divisor)
        back_to_original = calculator.multiply(result, divisor)
        
        # Use pytest.approx for floating point comparison
        assert back_to_original == pytest.approx(number, rel=1e-9)


# Markers and test organization
@pytest.mark.slow
class TestExpensiveOperations:
    """Tests marked as slow for selective execution"""
    
    def test_large_number_calculation(self, calculator):
        """Test calculation with very large numbers"""
        large_num = 10**10
        result = calculator.multiply(large_num, large_num)
        assert result == 10**20


@pytest.mark.integration
class TestDatabaseIntegration:
    """Tests marked for integration testing"""
    
    def test_database_connection(self, mock_database):
        """Test database connection (mocked for unit tests)"""
        result = mock_database.get("test_key")
        assert result is not None


# Custom test utilities
def assert_user_valid(user: User):
    """Custom assertion for user validation"""
    assert user.id > 0, "User ID must be positive"
    assert len(user.username) >= 3, "Username must be at least 3 characters"
    assert "@" in user.email, "Email must contain @ symbol"
    assert isinstance(user.created_at, datetime), "Created at must be datetime"


class TestCustomAssertions:
    """Tests using custom assertions"""
    
    def test_user_validation(self, sample_user):
        assert_user_valid(sample_user)
    
    def test_invalid_user_fails_validation(self):
        invalid_user = User(0, "ab", "invalid-email")
        
        with pytest.raises(AssertionError, match="User ID must be positive"):
            assert_user_valid(invalid_user)


# Example usage and test execution
if __name__ == "__main__":
    print("=== Unit Testing Examples ===")
    print("Run tests with: pytest test_examples.py")
    print("Run with coverage: pytest --cov=test_examples")
    print("Run specific test: pytest test_examples.py::TestCalculator::test_add_positive_numbers")
    print("Run with markers: pytest -m slow")
    print("Run verbose: pytest -v")
    print("Run and show output: pytest -s")