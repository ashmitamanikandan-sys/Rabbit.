-- =========================================================================
-- RABBIT 2.0 — Supabase / PostgreSQL Schema (rabbit_sky_v2.sql)
-- Identity: "Every chapter is a star."
-- 
-- Note: The frontend is engineered with complete local-first offline fallback.
-- If Supabase tables are absent or network is disconnected, the app runs 100%
-- smoothly via LocalStorage without console errors.
-- =========================================================================

-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- 1. User Profiles & Night Sky State
create table if not exists public.rabbit_profiles (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references auth.users(id) on delete cascade,
  username text unique not null,
  display_name text default 'Curious Reader',
  avatar_url text default '✦',
  total_stars integer default 0,
  nights_streak integer default 1,
  last_active_date date default current_date,
  is_demo boolean default false,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 2. Stars Collected (Chapters finished)
create table if not exists public.rabbit_stars (
  id uuid primary key default uuid_generate_v4(),
  profile_id uuid references public.rabbit_profiles(id) on delete cascade not null,
  book_id text not null,
  chapter_n integer not null,
  genre text not null,
  lit_at timestamp with time zone default timezone('utc'::text, now()) not null,
  unique (profile_id, book_id, chapter_n)
);

-- 3. Constellations (Books in progress or completed)
create table if not exists public.rabbit_constellations (
  id uuid primary key default uuid_generate_v4(),
  profile_id uuid references public.rabbit_profiles(id) on delete cascade not null,
  book_id text not null,
  stars_count integer default 1,
  total_chapters integer not null,
  completed boolean default false,
  completed_at timestamp with time zone,
  unique (profile_id, book_id)
);

-- 4. The Warren: Chapter & Line Community Posts
create table if not exists public.rabbit_warren_posts (
  id uuid primary key default uuid_generate_v4(),
  profile_id uuid references public.rabbit_profiles(id) on delete cascade not null,
  book_id text not null,
  chapter_n integer not null,
  card_type text default 'spark', -- 'spark' | 'key_ideas' | 'line' | 'in_your_life' | 'rabbit_hole'
  line_quote text,
  reflection text not null,
  reactions_count integer default 0,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 5. Clubs: Groups that light up constellations together
create table if not exists public.rabbit_clubs (
  id uuid primary key default uuid_generate_v4(),
  name text not null,
  description text,
  target_book_id text not null,
  created_by uuid references public.rabbit_profiles(id) on delete set null,
  member_count integer default 1,
  stars_lit integer default 0,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

create table if not exists public.rabbit_club_members (
  id uuid primary key default uuid_generate_v4(),
  club_id uuid references public.rabbit_clubs(id) on delete cascade not null,
  profile_id uuid references public.rabbit_profiles(id) on delete cascade not null,
  role text default 'member', -- 'creator' | 'member'
  joined_at timestamp with time zone default timezone('utc'::text, now()) not null,
  unique (club_id, profile_id)
);

-- 6. Metrics: "Find this book" clicks & engagement
create table if not exists public.rabbit_metrics (
  id uuid primary key default uuid_generate_v4(),
  profile_id uuid references public.rabbit_profiles(id) on delete set null,
  action text not null,
  book_id text,
  metadata jsonb default '{}'::jsonb,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- Row Level Security (RLS)
alter table public.rabbit_profiles enable row level security;
alter table public.rabbit_stars enable row level security;
alter table public.rabbit_constellations enable row level security;
alter table public.rabbit_warren_posts enable row level security;
alter table public.rabbit_clubs enable row level security;
alter table public.rabbit_club_members enable row level security;
alter table public.rabbit_metrics enable row level security;

-- Public read access for community features
create policy "Allow public read of profiles" on public.rabbit_profiles for select using (true);
create policy "Allow public read of stars" on public.rabbit_stars for select using (true);
create policy "Allow public read of constellations" on public.rabbit_constellations for select using (true);
create policy "Allow public read of warren posts" on public.rabbit_warren_posts for select using (true);
create policy "Allow public read of clubs" on public.rabbit_clubs for select using (true);

-- Authenticated user self-management
create policy "Users can insert own stars" on public.rabbit_stars for insert with check (auth.uid() is not null);
create policy "Users can insert warren posts" on public.rabbit_warren_posts for insert with check (auth.uid() is not null);
