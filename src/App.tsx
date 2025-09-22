import { AuthProvider, useAuth } from './contexts/AuthContext'
import { Landing } from './components/Landing'
import { Dashboard } from './components/Dashboard'
import './App.css'

function App() {
  return (
    <AuthProvider>
      <div className="app">
        <AppContent />
      </div>
    </AuthProvider>
  )
}

function AppContent() {
  const { user, loading } = useAuth()

  if (loading) {
    return (
      <div className="loading">
        <div className="loading-spinner"></div>
        <p>Loading...</p>
      </div>
    )
  }

  return user ? <Dashboard /> : <Landing />
}

export default App
