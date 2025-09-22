import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://clwausuodzmfrdrpckgj.supabase.co'
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsd2F1c3VvZHptZnJkcnBja2dqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg1NTIzMTQsImV4cCI6MjA3NDEyODMxNH0.Cv6f91ghpm6BcSo3OdllAXIK41ENDknFruoRIczPPPo'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

// User roles enum
export const UserRole = {
  USER: 'user',
  BUSINESS_OWNER: 'business_owner'
} as const

export type UserRole = typeof UserRole[keyof typeof UserRole]

// Database types
export interface UserProfile {
  id: string
  email: string
  role: UserRole
  full_name?: string
  business_name?: string
  created_at: string
  updated_at: string
}