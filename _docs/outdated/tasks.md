# ChoreCrew MVP Backlog

## 1. Scaffold the empty Django project
Goal: Create an empty ChoreCrew Django project with one passing smoke test.
Description: Initialize the selected Python and Django versions with a minimal project structure and dependency configuration. Add one smoke test that proves Django starts and the test suite passes, without implementing product behavior.

## 2. Configure the local application environment
Goal: Run Django with PostgreSQL and Redis through a documented local setup.
Description: Add the development containers, persistent volumes, environment variables, and Django settings for the database, cache, email, timezone, static files, and local media. Include readiness handling and concise commands for starting the application and its dependencies.

## 3. Build the shared user-interface shell
Goal: Establish the responsive page structure and frontend tools used by every feature.
Description: Create the base Django templates, navigation, messages, Tailwind styling pipeline, HTMX integration, and minimal Alpine.js setup. Include reusable form, button, status, empty-state, and dialog patterns with accessible focus and error behavior.

## 4. Implement user accounts and authentication
Goal: Let users create and recover an account, sign in, sign out, and edit their basic profile.
Description: Create the custom email-based user model and server-rendered authentication and profile flows using Django's security features. Cover duplicate signup, invalid credentials, password reset tokens, authenticated redirects, and user creation with focused tests.

## 5. Implement household creation and settings
Goal: Let a user create and configure a Couple, Family, or Roommates household.
Description: Model Household and HouseholdMember with name, type, expected member count, timezone, reward cost, and Admin, Adult, or Child role. Build the creation and Admin-only settings flows, atomically make the creator an Admin, and protect historical dates when settings change.

## 6. Implement household invitations and joining
Goal: Let an Admin invite another account by expiring link or human-readable code.
Description: Model revocable invitations and build creation, display, and acceptance flows that add the authenticated user to the correct household. Handle invalid, expired, revoked, reused, and already-member invitations without leaking household information.

## 7. Build household member administration
Goal: Let Admins view members, change roles, and remove members safely.
Description: Add the member-management interface and server-side authorization for membership changes. Prevent removal or demotion of the final Admin, reject cross-household operations, and record who performed each change.

## 8. Implement configurable Child permissions
Goal: Give Child members a simplified experience controlled by household settings.
Description: Store switches for viewing, creating, swapping, and refusing chores, then apply them through shared server-side authorization helpers. Adapt the navigation and dashboard to emphasize assigned chores, due dates, points, rewards, and progress for Child members.

## 9. Create and seed chore templates
Goal: Offer the common starter chores from the product plan while allowing household customization.
Description: Model global and household-owned templates with name, description, difficulty, and estimated duration. Seed the MVP template catalog and provide Admin controls for creating, editing, and deactivating household templates without changing global entries.

## 10. Build chore definition management
Goal: Let authorized members create, edit, and deactivate custom chores or chores copied from templates.
Description: Model the reusable Chore definition with household, description, effort, assignment type, proof requirement, and active state. Build validated server-rendered forms and enforce role and household boundaries for every operation.

## 11. Implement fixed and shared chore assignments
Goal: Assign a chore to one member or to several members working together.
Description: Store eligible members and assignment rules for fixed and shared chores, and add them to the chore form. Validate that assignees are active members of the same household and preserve assignment information needed for future occurrence snapshots.

## 12. Implement shared-pool chore claiming
Goal: Let an eligible member atomically claim an available chore occurrence.
Description: Define the shared-pool eligibility rules and add an HTMX claim action for unassigned occurrences. Lock the relevant database record so concurrent requests cannot produce two owners, and return a useful already-claimed result.

## 13. Implement rotating chore assignments
Goal: Choose the next eligible member whenever a rotating chore becomes due.
Description: Store an ordered rotation group and enough state to select members deterministically for each chore. Test advancement, inactive-member skipping, membership changes, retry behavior, and separation between different rotations.

## 14. Model and calculate chore schedules
Goal: Represent every one-time and recurring schedule promised for the MVP.
Description: Model one-time, daily, weekly, monthly, interval, twice-per-week, and custom recurrence rules and provide forms for configuring them. Implement a timezone-aware calculator that returns upcoming due times with tests for calendar boundaries and invalid combinations.

## 15. Create immutable chore occurrences
Goal: Store each due chore instance independently from its editable definition.
Description: Model ChoreOccurrence with its scheduled time, lifecycle status, assignment snapshot, effort snapshot, point-value snapshot, and originating chore or routine. Add uniqueness and state constraints so editing a definition cannot rewrite history.

## 16. Generate upcoming chore occurrences
Goal: Materialize a bounded window of one-time and recurring occurrences without duplicates.
Description: Implement an idempotent service that queries active schedules and creates missing occurrences through a configurable future horizon. Apply fixed, shared, pool, and rotation rules while respecting the household timezone and repeated execution.

## 17. Configure background and periodic processing
Goal: Run occurrence generation and other deferred work through Celery and Redis.
Description: Integrate Celery workers and Celery Beat with Django and define a small periodic schedule rather than one schedule entry per chore. Provide testable task boundaries and document how to run the worker and scheduler in the local environment.

## 18. Implement the points ledger and formula
Goal: Calculate chore points and record every balance change as an immutable transaction.
Description: Define the initial difficulty-and-duration formula and model PointTransaction with member, occurrence, signed amount, reason, actor, and timestamp. Provide a reliable nonnegative balance calculation and uniqueness rules that prevent retried jobs from awarding or deducting points twice.

## 19. Implement chore completion
Goal: Let an authorized assignee complete an occurrence and receive its snapshotted points.
Description: Build an atomic completion service and HTMX form that records the completer, completion time, optional note, and point transaction. Reject unauthorized or duplicate completion while making repeated submissions return the completed state safely.

## 20. Add optional completion proof photos
Goal: Accept a validated local photo when an occurrence requires proof.
Description: Store proof through Django's filesystem storage in the persistent media directory and validate its type and size. Require the file only for configured chores and enforce household authorization whenever the photo is retrieved.

## 21. Process missed and overdue occurrences
Goal: Mark past-due work and apply the configured point loss exactly once.
Description: Implement an idempotent periodic service that finds open occurrences after their deadline, updates their status, and creates the ledger deduction without taking a balance below zero. Keep missed occurrences in history and leave later recurring occurrences eligible for normal generation.

## 22. Build chore and occurrence detail pages with comments
Goal: Give members one place to inspect a chore, its current occurrence, history, and simple discussion.
Description: Create permission-scoped detail pages and a Comment model with author, text, and timestamp. Add an HTMX comment form with length validation and consistent ordering, without mentions, reactions, threads, or household chat.

## 23. Implement normal chore swaps
Goal: Let one member request a swap and let the recipient accept or decline it.
Description: Model the full pending, accepted, declined, and stale request lifecycle with requester, recipient, relevant occurrences, and timestamps. Perform acceptance atomically with locked assignments, and test eligibility, duplicate requests, concurrent responses, and household isolation.

## 24. Implement paid chore refusal and reassignment chains
Goal: Let the current assignee spend points to transfer an occurrence to another eligible member.
Description: Build an atomic refusal service that verifies ownership and balance, deducts the configured cost, changes the assignee, and records an immutable reassignment event. Support repeated transfers without a fixed limit while rejecting concurrent attempts, former assignees, inactive recipients, and insufficient balances.

## 25. Implement funny titles and unlocks
Goal: Unlock the initial title catalog from completed chore activity and let a member select an active title.
Description: Model title definitions, criteria, member unlocks, and the selected title, then seed the names from the product plan. Evaluate unlocks idempotently after relevant completions and display earned titles on member profiles.

## 26. Build routine management
Goal: Let authorized members group ordered chores into a reusable scheduled routine.
Description: Model Routine and its ordered items with household ownership, schedule, assignment type, eligible members, and active state. Provide create, edit, reorder, and deactivate flows without adding dependencies between component chores.

## 27. Generate chore occurrences from routines
Goal: Materialize every component chore when a scheduled routine becomes due.
Description: Extend occurrence generation with an idempotent routine service that applies the routine's fixed, shared, or rotation policy. Preserve item order and the originating routine snapshot so generated work remains understandable in lists and history.

## 28. Build the household dashboard
Goal: Show due-today, upcoming, and unfinished work for the active household.
Description: Create a mobile-friendly dashboard with sections for the current member's assignments, shared work, claimable pool chores, upcoming due dates, and overdue items. Use the household timezone, clear empty states, efficient queries, and direct controls for permitted actions.

## 29. Build task lists and filtering
Goal: Let members browse chores and occurrences by member, status, and date.
Description: Create server-side list views with shareable filter parameters, pagination where needed, and HTMX result updates. Validate all selected members against the household and test combined filters and empty results.

## 30. Build weekly and monthly calendar views
Goal: Display scheduled, recurring, upcoming, and unfinished occurrences on an internal calendar.
Description: Add a permission-scoped Django JSON feed and configure FullCalendar weekly and monthly views against it. Restrict queries to the requested date range, handle timezone boundaries and status styling, and link events to occurrence details.

## 31. Build household workload and fairness summaries
Goal: Compare contribution using time, difficulty, completion, and missed work rather than chore counts alone.
Description: Define and document the MVP fairness calculations from occurrence snapshots and point history. Display a simple member comparison for a selected date range and test it against the workload examples in the product plan.

## 32. Build the chore activity history
Goal: Present an auditable timeline of important household chore events.
Description: Combine completions, missed occurrences, point changes, swaps, and paid reassignments in one read-only chronological view. Add member, event-type, and date filters while keeping all records scoped to the current household.

## 33. Implement notification preferences and in-app notifications
Goal: Let each member configure and receive durable notifications inside ChoreCrew.
Description: Store preferences for due-soon, overdue, assignment, swap, and paid reassignment events, and create in-app records only when enabled. Add an unread indicator, list, mark-read action, and deduplication keys for retried domain events.

## 34. Implement email notifications and reminders
Goal: Deliver enabled MVP notifications by email from background jobs.
Description: Render and queue email for new assignments, due-soon and overdue chores, swap outcomes, and paid reassignments. Respect member preferences and household timezone, deduplicate retries, and expose sent messages through the development email backend for testing.

## 35. Polish responsive and accessible core flows
Goal: Make the daily ChoreCrew experience usable on phones, keyboards, and assistive technology.
Description: Review signup, household setup, chore creation, dashboard, calendar, completion, swap, refusal, and notification flows at supported viewport sizes. Correct focus movement, labels, validation announcements, contrast, touch targets, loading states, and HTMX failure feedback.

## 36. Audit household authorization and file access
Goal: Prove that data and actions cannot cross household or role boundaries.
Description: Inventory every page, mutation, JSON endpoint, and proof-photo response and test Admin, Adult, configurable Child, nonmember, and member-of-another-household access. Route inconsistent checks through shared authorization helpers and verify denied requests do not reveal protected data.

## 37. Test the primary household lifecycle
Goal: Cover the critical first-release journey with an end-to-end browser test.
Description: Automate account creation, household setup, invitation acceptance, chore creation, assignment, completion, and point award through the real user interface. Keep edge cases in lower-level tests so this scenario remains focused and dependable.

## 38. Test recurring and overdue processing
Goal: Prove recurring schedules remain correct across completion, missed deadlines, and job retries.
Description: Generate consecutive occurrences, complete one, process one as missed, and create the next scheduled instance in an integration test. Assert stable history, correct rotation, exactly-once point transactions, and no duplicate occurrences after repeated task runs.

## 39. Test swaps and paid reassignment chains
Goal: Prove both reassignment mechanisms preserve ownership, balances, and history.
Description: Cover an accepted normal swap and a multi-member paid refusal chain through service and browser-level integration tests. Assert permissions, final assignments, ledger entries, ordered audit events, and safe repeated submissions.

## 40. Prepare the MVP deployment
Goal: Make the complete first version deployable and verifiable without choosing a hosting vendor.
Description: Define production container commands, migrations, static collection, persistent media, web, worker, scheduler, PostgreSQL, Redis, health checks, and required configuration. Document backup and restore expectations and provide a smoke-test procedure for a freshly deployed environment.
