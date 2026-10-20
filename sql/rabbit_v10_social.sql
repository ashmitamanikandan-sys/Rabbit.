-- RABBIT V10 social schema. Review and apply in Supabase SQL Editor before enabling shared feeds.
-- This file is not automatically executed by GitHub Pages.
create table if not exists public.rabbit_profiles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  username text unique not null check (char_length(username) between 3 and 30),
  display_name text not null default 'Curious Reader',
  bio text not null default '',
  avatar_url text,
  created_at timestamptz not null default now()
);
create table if not exists public.rabbit_clubs (
  id uuid primary key default gen_random_uuid(),
  owner_id uuid not null references auth.users(id) on delete cascade,
  name text not null check (char_length(name) between 3 and 90),
  description text not null default '',
  cover_url text,
  created_at timestamptz not null default now()
);
create table if not exists public.rabbit_memberships (
  club_id uuid not null references public.rabbit_clubs(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  joined_at timestamptz not null default now(),
  primary key (club_id,user_id)
);
create table if not exists public.rabbit_posts (
  id uuid primary key default gen_random_uuid(),
  author_id uuid not null references auth.users(id) on delete cascade,
  club_id uuid references public.rabbit_clubs(id) on delete cascade,
  body text not null check (char_length(body) between 1 and 3000),
  images text[] not null default '{}',
  created_at timestamptz not null default now()
);
create table if not exists public.rabbit_comments (
  id uuid primary key default gen_random_uuid(),
  post_id uuid not null references public.rabbit_posts(id) on delete cascade,
  author_id uuid not null references auth.users(id) on delete cascade,
  body text not null check (char_length(body) between 1 and 1000),
  created_at timestamptz not null default now()
);
create table if not exists public.rabbit_messages (
  id uuid primary key default gen_random_uuid(),
  club_id uuid not null references public.rabbit_clubs(id) on delete cascade,
  author_id uuid not null references auth.users(id) on delete cascade,
  channel text not null check (channel in ('general','book-talk','spoilers')),
  body text not null check (char_length(body) between 1 and 1500),
  created_at timestamptz not null default now()
);
alter table public.rabbit_profiles enable row level security;
alter table public.rabbit_clubs enable row level security;
alter table public.rabbit_memberships enable row level security;
alter table public.rabbit_posts enable row level security;
alter table public.rabbit_comments enable row level security;
alter table public.rabbit_messages enable row level security;
create policy "Profiles visible to users" on public.rabbit_profiles for select to authenticated using (true);
create policy "Edit own profile" on public.rabbit_profiles for all to authenticated using (user_id=auth.uid()) with check (user_id=auth.uid());
create policy "Read clubs" on public.rabbit_clubs for select to authenticated using (true);
create policy "Create owned clubs" on public.rabbit_clubs for insert to authenticated with check (owner_id=auth.uid());
create policy "Edit owned clubs" on public.rabbit_clubs for update to authenticated using (owner_id=auth.uid()) with check (owner_id=auth.uid());
create policy "Read memberships" on public.rabbit_memberships for select to authenticated using (true);
create policy "Join own membership" on public.rabbit_memberships for insert to authenticated with check (user_id=auth.uid());
create policy "Leave own membership" on public.rabbit_memberships for delete to authenticated using (user_id=auth.uid());
create policy "Read Warren and member club posts" on public.rabbit_posts for select to authenticated using (club_id is null or exists(select 1 from public.rabbit_memberships m where m.club_id=rabbit_posts.club_id and m.user_id=auth.uid()));
create policy "Create own eligible posts" on public.rabbit_posts for insert to authenticated with check (author_id=auth.uid() and (club_id is null or exists(select 1 from public.rabbit_memberships m where m.club_id=rabbit_posts.club_id and m.user_id=auth.uid())));
create policy "Delete own posts" on public.rabbit_posts for delete to authenticated using (author_id=auth.uid());
create policy "Read comments on visible posts" on public.rabbit_comments for select to authenticated using (exists(select 1 from public.rabbit_posts p where p.id=rabbit_comments.post_id and (p.club_id is null or exists(select 1 from public.rabbit_memberships m where m.club_id=p.club_id and m.user_id=auth.uid()))));
create policy "Write own comments on visible posts" on public.rabbit_comments for insert to authenticated with check (author_id=auth.uid() and exists(select 1 from public.rabbit_posts p where p.id=rabbit_comments.post_id and (p.club_id is null or exists(select 1 from public.rabbit_memberships m where m.club_id=p.club_id and m.user_id=auth.uid()))));
create policy "Delete own comments" on public.rabbit_comments for delete to authenticated using (author_id=auth.uid());
create policy "Read club messages if member" on public.rabbit_messages for select to authenticated using (exists(select 1 from public.rabbit_memberships m where m.club_id=rabbit_messages.club_id and m.user_id=auth.uid()));
create policy "Send club messages if member" on public.rabbit_messages for insert to authenticated with check (author_id=auth.uid() and exists(select 1 from public.rabbit_memberships m where m.club_id=rabbit_messages.club_id and m.user_id=auth.uid()));
create policy "Delete own messages" on public.rabbit_messages for delete to authenticated using (author_id=auth.uid());
-- Before production: add moderation/reporting, rate limits, image storage rules, and anti-spam.
