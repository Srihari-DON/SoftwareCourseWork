import React, { useState } from 'react'
import { useAuth } from '../contexts/AuthContext'
import { UserRole } from '../lib/supabase'

interface AuthFormProps {
  userType: UserRole
}

export const AuthForm: React.FC<AuthFormProps> = ({ userType }) => {
  const [isSignUp, setIsSignUp] = useState(false)
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [fullName, setFullName] = useState('')
  const [businessName, setBusinessName] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const { signIn, signUp } = useAuth()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    try {
      if (isSignUp) {
        const metadata = {
          full_name: fullName,
          ...(userType === UserRole.BUSINESS_OWNER && { business_name: businessName })
        }
        const { error } = await signUp(email, password, userType, metadata)
        if (error) throw error
      } else {
        const { error } = await signIn(email, password)
        if (error) throw error
      }
    } catch (error: any) {
      setError(error.message)
    } finally {
      setLoading(false)
    }
  }

  const isBusinessOwner = userType === UserRole.BUSINESS_OWNER

  return (
    <div className="auth-form">
      <div className="auth-header">
        <h2>
          {isSignUp ? 'Sign Up' : 'Sign In'} as {isBusinessOwner ? 'Business Owner' : 'User'}
        </h2>
      </div>

      <form onSubmit={handleSubmit} className="form">
        {isSignUp && (
          <div className="form-group">
            <label htmlFor="fullName">Full Name</label>
            <input
              id="fullName"
              type="text"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              required
              className="form-input"
            />
          </div>
        )}

        {isSignUp && isBusinessOwner && (
          <div className="form-group">
            <label htmlFor="businessName">Business Name</label>
            <input
              id="businessName"
              type="text"
              value={businessName}
              onChange={(e) => setBusinessName(e.target.value)}
              required
              className="form-input"
            />
          </div>
        )}

        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className="form-input"
          />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className="form-input"
            minLength={6}
          />
        </div>

        {error && <div className="error-message">{error}</div>}

        <button
          type="submit"
          disabled={loading}
          className="submit-button"
        >
          {loading ? 'Loading...' : (isSignUp ? 'Sign Up' : 'Sign In')}
        </button>

        <button
          type="button"
          onClick={() => setIsSignUp(!isSignUp)}
          className="toggle-button"
        >
          {isSignUp ? 'Already have an account? Sign In' : 'Need an account? Sign Up'}
        </button>
      </form>
    </div>
  )
}