# Shared Household Chores Tool — MVP Project Scope

## 1. Project Overview

The Shared Household Chores Tool is an application for organizing, assigning, tracking, and balancing household chores among people who live together.

The tool should support different household types:

- Couples
- Families
- Roommates

During setup, users choose the household type and specify the number of household members.

The main goal is to make household chore management clear, fair, flexible, and more engaging through scheduling, workload tracking, points, rewards, and light gamification.

---

## 2. MVP Goals

The MVP should allow a household to:

1. Create a household.
2. Add and manage household members.
3. Define member roles.
4. Create chores manually or from templates.
5. Assign chores in different ways.
6. Share chores between multiple people.
7. Schedule one-time and recurring chores.
8. Group chores into routines.
9. Track completed, unfinished, upcoming, and overdue chores.
10. Allow chore swaps.
11. Allow users to spend rewards to refuse and reassign chores.
12. Track effort, fairness, and completion history.
13. Award and deduct points.
14. Unlock funny titles/rewards.
15. Show chores in task-list and calendar views.
16. Support optional proof of completion.
17. Allow simple comments on chores.
18. Send configurable notifications.

---

## 3. Target Users

The application should work for any shared household.

### 3.1 Couples

Two people sharing household responsibilities.

Examples:

- Cooking
- Washing dishes
- Laundry
- Cleaning
- Grocery shopping

### 3.2 Families

Households containing adults and children.

The application should support different permissions and a configurable child mode.

### 3.3 Roommates

Independent adults sharing common household responsibilities.

Examples:

- Taking out trash
- Cleaning common areas
- Buying shared supplies
- Cleaning the kitchen

---

## 4. Household Setup

### 4.1 Create Household

One person creates the household and becomes the initial Admin.

The creator selects:

- Household name
- Household type:
  - Couple
  - Family
  - Roommates
- Number of household members

### 4.2 Invite Members

Members can join through:

- Invite link
- Invite code

Each household member should have an individual profile/account so the system can track:

- Assignments
- Completion history
- Points
- Rewards
- Workload
- Permissions

---

## 5. Household Roles

The MVP supports three roles.

### Admin

Can:

- Manage household settings
- Invite/remove members
- Create/edit/delete chores
- Configure child mode
- Manage templates and routines
- Configure household reward rules

### Adult

Can:

- Create chores
- Complete assigned chores
- Request swaps
- Use rewards
- Comment on chores
- View household workload and schedule

### Child

Permissions are configurable by the Admin.

Child mode may simplify the interface and show primarily:

- Assigned chores
- Due dates
- Points
- Rewards
- Progress

---

## 6. Chore Creation

Users can create chores in two ways.

### 6.1 Chore Templates

The application includes common chore templates, for example:

- Wash dishes
- Take out trash
- Vacuum
- Mop floors
- Clean bathroom
- Do laundry
- Fold laundry
- Grocery shopping
- Clean kitchen
- Feed pet
- Walk dog
- Change bed sheets

Users can modify a template after selecting it.

### 6.2 Custom Chores

Users can create their own chores.

A chore can contain:

- Name
- Description
- Assignment type
- Assigned member(s)
- Difficulty
- Estimated time
- Due date
- Recurrence
- Reminder settings
- Optional proof requirement
- Comments

---

## 7. Chore Assignment Types

Each chore can use one of four assignment models.

### 7.1 Fixed Assignment

The chore is assigned to one specific person.

Example:

> Alex always takes out the trash.

### 7.2 Rotation

The application automatically rotates the chore between selected household members.

Example:

> Bathroom cleaning rotates weekly between three roommates.

### 7.3 Shared Pool

The chore is available for eligible household members to take.

Example:

> Someone needs to pick up groceries.

### 7.4 Shared Chore

A chore can be assigned to multiple people.

Example:

> Two people clean the garage together.

---

## 8. Scheduling

The MVP supports flexible recurring schedules.

Examples:

- Daily
- Weekly
- Monthly
- Every 3 days
- Twice per week
- Custom recurrence

A chore may also have a single due date.

---

## 9. Chore Difficulty and Estimated Effort

Each chore contains:

### Difficulty

- Easy
- Medium
- Hard

### Estimated Time

Example:

- 10 minutes
- 30 minutes
- 60 minutes

These values are used to calculate:

- Points
- Workload
- Household fairness

This prevents the application from treating a five-minute task as equivalent to a one-hour chore.

---

## 10. Chore Completion

A user can mark an assigned chore as complete.

No approval is required by default.

When completed, the system records:

- Chore
- Person who completed it
- Completion time
- Points earned
- Optional photo
- Optional note

---

## 11. Optional Proof of Completion

Proof is optional.

Users may attach:

- A photo
- A short note

The MVP does not require another household member to approve the proof.

---

## 12. Unfinished and Overdue Chores

If a chore is not completed by its deadline:

1. It is marked **Unfinished**.
2. The assigned person's points are reduced.
3. It remains visible in the unfinished/overdue list.

For recurring chores:

- The unfinished occurrence remains in history.
- The next scheduled occurrence is still created.

Example:

If "Clean Kitchen" is scheduled every Monday and this Monday's chore is missed:

- Monday's chore remains marked Unfinished.
- A new chore is still created for the following Monday.

---

## 13. Chore Swaps

Users can request to swap chores with another household member.

Flow:

1. Person A requests a swap.
2. Person B receives the request.
3. Person B can accept or decline.
4. If accepted, assignments are updated.

Normal swaps require agreement.

This is different from the reward-based refusal system described below.

---

## 14. Points System

Points provide lightweight gamification and help measure contribution.

### Points Earned

Users earn points when completing chores.

Points should be calculated automatically based on:

- Difficulty
- Estimated time

Example logic:

- Easy + short chore = fewer points
- Hard + long chore = more points

Exact point formulas can be tuned during implementation.

### Points Lost

Users lose points when assigned chores become unfinished.

A user's point balance cannot fall below zero.

---

## 15. Rewards

Rewards are available to all household members, not only children.

The MVP focuses on fun, non-monetary rewards.

### 15.1 Funny Titles

Users can unlock titles such as:

- Dish Destroyer
- Laundry Legend
- Vacuum Viking
- Trash Titan
- Mop Master
- Kitchen Commander
- Bathroom Boss
- Chore Champion

Titles can be displayed on the user's profile.

### 15.2 Skip/Reassign Reward

A user can spend a reward to refuse an assigned chore.

When using this reward:

1. The person spends the required reward/points.
2. They choose another household member.
3. The chore is reassigned to that person.

The newly assigned person can also refuse the chore, but only if they have enough rewards to do so.

The reassignment chain can continue without a fixed limit as long as each person spends a reward.

This turns chore refusal into a game mechanic rather than a free action.

### Initial MVP Rule

Use a simple fixed reward cost, such as:

> 50 points to refuse/reassign one chore.

The exact cost can be adjusted after testing.

---

## 16. Household Fairness

The system should help users understand whether chores are distributed fairly.

Fairness should not be measured only by the number of chores.

Instead, workload should consider:

- Difficulty
- Estimated time
- Completed chores
- Unfinished chores

Example:

Person A:
- 5 easy chores
- 50 minutes total

Person B:
- 2 hard chores
- 120 minutes total

The application should recognize that Person B may have contributed more effort despite completing fewer chores.

---

## 17. Routines

Users can create reusable routines containing several chores.

Example:

### Sunday Reset

- Vacuum
- Clean bathroom
- Do laundry
- Take out trash
- Clean kitchen

A routine can be:

- Assigned to one person
- Assigned to multiple people
- Rotated between household members

For the MVP, routines are groups of chores.

Complex dependencies such as:

> Chore B cannot start until Chore A is complete

are not included.

---

## 18. Dashboard

The home dashboard should focus on information users need every day.

Suggested sections:

### Today

Chores due today.

### Upcoming

Chores coming soon.

### Unfinished / Overdue

Missed chores that still require attention.

### Household Workload

Simple comparison of expected/completed effort among members.

### Points

Current points for each member.

### Rewards / Titles

Unlocked rewards and current title.

---

## 19. Calendar

The MVP includes:

- Weekly view
- Monthly view

Users should be able to see:

- Scheduled chores
- Recurring chores
- Upcoming chores
- Unfinished chores

This is an internal application calendar.

External Google Calendar or Apple Calendar synchronization is not part of the MVP.

---

## 20. Chore History

The system keeps a history of important chore activity.

History should include:

- Completed chores
- Completion date
- Person who completed the chore
- Points earned
- Unfinished chores
- Points deducted
- Chore swaps
- Reward-based refusals/reassignments

This history supports fairness calculations and household statistics.

---

## 21. Comments

Each chore can contain simple text comments.

Examples:

> "Please use the new cleaning spray."

> "Trash bags are under the sink."

The MVP does not include:

- @mentions
- Reactions
- Threaded conversations
- Full household chat

---

## 22. Notifications

Notifications should be configurable per user.

Possible notification types:

- Chore due soon
- Chore overdue
- New chore assigned
- Swap request
- Swap accepted/declined
- Chore reassigned through a reward

Each user can choose which notification types they want.

---

## 23. Search and Filtering

Users should be able to filter chores by:

- Household member
- Status
- Date

Statuses may include:

- Upcoming
- Due Today
- Completed
- Unfinished
- Overdue

Advanced search and complex tagging are not required for the MVP.

---

## 24. Suggested Main User Flows

### Flow 1: Create a Household

1. User signs up.
2. Selects Create Household.
3. Chooses Couple, Family, or Roommates.
4. Sets number of people.
5. Invites members.
6. Assigns roles.

### Flow 2: Create a Chore

1. Select Add Chore.
2. Choose a template or custom chore.
3. Set difficulty.
4. Set estimated time.
5. Choose assignment type.
6. Choose person/people.
7. Set schedule.
8. Set reminders.
9. Save.

### Flow 3: Complete a Chore

1. User opens assigned chore.
2. Optionally attaches photo/note.
3. Marks it complete.
4. System records completion.
5. Points are added.

### Flow 4: Miss a Chore

1. Deadline passes.
2. Chore is marked Unfinished.
3. Points are deducted.
4. Chore remains visible.
5. If recurring, the next occurrence is still created.

### Flow 5: Swap a Chore

1. User chooses Request Swap.
2. Selects another member/chore.
3. Other member accepts or declines.
4. System updates assignments if accepted.

### Flow 6: Refuse a Chore Using a Reward

1. User opens assigned chore.
2. Selects Use Reward to Refuse.
3. Required reward/points are deducted.
4. User selects another household member.
5. Chore is reassigned.
6. New assignee may repeat the process only if they can pay the reward cost.

### Flow 7: Create a Routine

1. User creates a routine.
2. Gives it a name.
3. Adds several chores.
4. Chooses assignment/rotation rules.
5. Sets the routine schedule.

---

## 25. Core MVP Data Entities

A simple implementation will likely require the following major entities.

### User

- User ID
- Name
- Account details

### Household

- Household ID
- Name
- Household type
- Settings

### Household Member

- Household
- User
- Role
- Points
- Active title/reward

### Chore

- Chore ID
- Name
- Description
- Difficulty
- Estimated time
- Assignment type
- Schedule
- Status

### Chore Assignment

- Chore
- Assigned member(s)
- Assignment date

### Chore Occurrence

Represents a specific scheduled occurrence of a recurring chore.

- Scheduled date
- Status
- Completed by
- Completion time

### Routine

- Routine ID
- Name
- Included chores
- Assignment rules
- Schedule

### Reward

- Reward type
- Cost
- User eligibility

### Point Transaction

- User
- Points added/deducted
- Reason
- Date

### Swap Request

- Requester
- Recipient
- Chore(s)
- Status

### Comment

- Chore
- Author
- Text
- Date

---

## 26. MVP Permissions Summary

| Action | Admin | Adult | Child |
|---|---|---|---|
| View household chores | Yes | Yes | Configurable |
| Complete assigned chore | Yes | Yes | Yes |
| Create chores | Yes | Yes | Configurable |
| Edit/delete household chores | Yes | Limited | No |
| Request swaps | Yes | Yes | Configurable |
| Use rewards | Yes | Yes | Configurable |
| Manage members | Yes | No | No |
| Manage household settings | Yes | No | No |
| Configure child mode | Yes | No | No |

---

## 27. Explicitly Out of Scope for MVP

The following features should not be built in the first version.

### AI Chore Suggestions

Templates are sufficient for initial setup.

AI-generated chore plans can be considered later.

### External Calendar Integrations

No Google Calendar, Apple Calendar, or Outlook Calendar sync in MVP.

### Payments / Allowances

The application should not process real money or automate allowances.

### Advanced Gamification

Not included:

- Competitive leaderboards
- Complex streak systems
- Seasons
- Tournaments
- Marketplace rewards

### Real-Time Household Chat

Simple chore comments are enough.

### Complex Chore Dependencies

No task dependency graph or workflow engine.

### Custom Permission Builder

Use Admin / Adult / Child rather than fully customizable permissions.

### Advanced Analytics

The MVP needs basic workload/fairness information, not a full analytics platform.

---

## 28. Future / Nice-to-Have Features

Possible later improvements:

- AI-generated chore plans
- AI workload balancing suggestions
- Google/Apple/Outlook Calendar synchronization
- Push notifications
- Household leaderboards
- Streaks
- More badges and achievements
- Custom reward marketplace
- Real allowance/money integration
- Smart-home integrations
- Voice assistants
- Automatic assignment based on workload
- Vacation mode
- Household supply tracking
- Grocery lists
- Advanced statistics
- Custom household roles
- Chore dependencies
- Location-based reminders

---

## 29. MVP Success Criteria

The MVP is successful if a household can reliably:

1. Set up its members.
2. Create chores.
3. Assign and rotate chores.
4. Schedule recurring chores.
5. Complete or miss chores.
6. Track points.
7. Swap chores.
8. Spend rewards to refuse/reassign chores.
9. Track household workload.
10. View current and future responsibilities clearly.

The application should make it easier to answer:

- What do I need to do today?
- Who is responsible for this chore?
- What chores are overdue?
- Is the workload reasonably fair?
- How many points do I have?
- Can I use a reward to avoid this chore?
- What is coming up this week?

---

## 30. Final MVP Definition

The MVP is a shared household chore-management application for couples, families, and roommates.

Users create a household, invite members, assign roles, create chores from templates or manually, schedule and rotate chores, group chores into routines, mark chores complete or unfinished, earn and lose points, request swaps, spend rewards to refuse and reassign chores, unlock funny titles, and monitor workload fairness.

The application provides:

- Task views
- Calendar views
- Chore history
- Configurable notifications
- Simple comments
- Optional completion proof
- Points and rewards
- Basic household fairness statistics

The focus of the MVP is **shared responsibility, fairness, flexibility, and lightweight fun** without adding unnecessary complexity such as payments, AI features, advanced analytics, or external integrations.
