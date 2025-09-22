import React from 'react'
import { useAuth } from '../contexts/AuthContext'
import { UserRole } from '../lib/supabase'

export const Dashboard: React.FC = () => {
  const { profile, signOut } = useAuth()

  if (!profile) {
    return <div>Loading profile...</div>
  }

  const isBusinessOwner = profile.role === UserRole.BUSINESS_OWNER

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Welcome, {profile.full_name || profile.email}!</h1>
        <button onClick={signOut} className="signout-button">
          Sign Out
        </button>
      </header>

      <div className="dashboard-content">
        <div className="profile-card">
          <h2>Profile Information</h2>
          <div className="profile-info">
            <p><strong>Email:</strong> {profile.email}</p>
            <p><strong>Role:</strong> {isBusinessOwner ? 'Business Owner' : 'User'}</p>
            {profile.full_name && <p><strong>Full Name:</strong> {profile.full_name}</p>}
            {profile.business_name && <p><strong>Business Name:</strong> {profile.business_name}</p>}
            <p><strong>Member since:</strong> {new Date(profile.created_at).toLocaleDateString()}</p>
          </div>
        </div>

        <div className="role-specific-content">
          {isBusinessOwner ? (
            <BusinessOwnerContent />
          ) : (
            <UserContent />
          )}
        </div>
      </div>
    </div>
  )
}

const BusinessOwnerContent: React.FC = () => {
  return (
    <div className="business-owner-content">
      <h3>Business Owner Dashboard</h3>
      <div className="feature-grid">
        <div className="feature-card">
          <h4>Manage Products/Services</h4>
          <p>Add, edit, and manage your business offerings.</p>
          <button className="feature-button">Manage Products</button>
        </div>
        <div className="feature-card">
          <h4>Customer Management</h4>
          <p>View and manage your customer relationships.</p>
          <button className="feature-button">View Customers</button>
        </div>
        <div className="feature-card">
          <h4>Analytics</h4>
          <p>Track your business performance and metrics.</p>
          <button className="feature-button">View Analytics</button>
        </div>
        <div className="feature-card">
          <h4>Settings</h4>
          <p>Configure your business settings and preferences.</p>
          <button className="feature-button">Business Settings</button>
        </div>
      </div>
    </div>
  )
}

const UserContent: React.FC = () => {
  return (
    <div className="user-content">
      <h3>User Dashboard</h3>
      <div className="feature-grid">
        <div className="feature-card">
          <h4>Browse Services</h4>
          <p>Discover services and products from businesses.</p>
          <button className="feature-button">Browse</button>
        </div>
        <div className="feature-card">
          <h4>My Orders</h4>
          <p>View your order history and track current orders.</p>
          <button className="feature-button">View Orders</button>
        </div>
        <div className="feature-card">
          <h4>Favorites</h4>
          <p>Manage your favorite businesses and services.</p>
          <button className="feature-button">View Favorites</button>
        </div>
        <div className="feature-card">
          <h4>Profile Settings</h4>
          <p>Update your profile and account preferences.</p>
          <button className="feature-button">Edit Profile</button>
        </div>
      </div>
    </div>
  )
}