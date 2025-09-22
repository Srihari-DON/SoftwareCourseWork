-- Enable RLS (Row Level Security)
alter table auth.users enable row level security;

-- Create user_profiles table
create table public.user_profiles (
  id uuid references auth.users on delete cascade primary key,
  email text unique not null,
  role text not null check (role in ('user', 'business_owner')),
  full_name text,
  business_name text,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Enable RLS on user_profiles
alter table public.user_profiles enable row level security;

-- Create policy for users to read their own profile
create policy "Users can view own profile" on public.user_profiles
  for select using (auth.uid() = id);

-- Create policy for users to update their own profile
create policy "Users can update own profile" on public.user_profiles
  for update using (auth.uid() = id);

-- Create policy for users to insert their own profile
create policy "Users can insert own profile" on public.user_profiles
  for insert with check (auth.uid() = id);

-- Create function to handle new user creation
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.user_profiles (id, email, role, full_name)
  values (new.id, new.email, 'user', new.raw_user_meta_data->>'full_name');
  return new;
end;
$$ language plpgsql security definer;

-- Create trigger to automatically create profile on signup
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();

-- Create function to update updated_at timestamp
create or replace function public.handle_updated_at()
returns trigger as $$
begin
  new.updated_at = timezone('utc'::text, now());
  return new;
end;
$$ language plpgsql;

-- Create trigger to update updated_at on profile changes
create trigger handle_updated_at before update on public.user_profiles
  for each row execute procedure public.handle_updated_at();