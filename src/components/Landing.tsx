import React from 'react'
import { AuthForm } from './AuthForm'
import { UserRole } from '../lib/supabase'

export const Landing: React.FC = () => {
  const [selectedRole, setSelectedRole] = React.useState<UserRole | null>(null)

  if (selectedRole) {
    return (
      <div className="landing">
        <button 
          onClick={() => setSelectedRole(null)}
          className="back-button"
        >
          ← Back to Role Selection
        </button>
        <AuthForm userType={selectedRole} />
      </div>
    )
  }

  return (
    <div className="landing">
      <div className="landing-header">
        <h1>Welcome to Software CourseWork</h1>
        <p>Choose your account type to get started</p>
      </div>

      <div className="role-selection">
        <div className="role-card">
          <h3>I'm a User</h3>
          <p>Looking for services and products from businesses</p>
          <ul>
            <li>Browse available services</li>
            <li>Connect with businesses</li>
            <li>Track your orders</li>
            <li>Save favorites</li>
          </ul>
          <button 
            onClick={() => setSelectedRole(UserRole.USER)}
            className="role-button user-button"
          >
            Continue as User
          </button>
        </div>

        <div className="role-card">
          <h3>I'm a Business Owner</h3>
          <p>Looking to offer services and manage my business</p>
          <ul>
            <li>Manage products/services</li>
            <li>Customer relationship management</li>
            <li>Business analytics</li>
            <li>Configure business settings</li>
          </ul>
          <button 
            onClick={() => setSelectedRole(UserRole.BUSINESS_OWNER)}
            className="role-button business-button"
          >
            Continue as Business Owner
          </button>
        </div>
      </div>
    </div>
  )
}