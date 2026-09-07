# Commands

- `.venv/bin/python -m pip install --editable .` - install dependencies
- `.venv/bin/python manage.py test` - run the whole test suite
- `.venv/bin/python manage.py test tests.test_smoke` - run one test module

# Rules

- Read `_docs/process.md` before starting work.
- Use the assigned GitHub issue as the source of truth for task scope and acceptance criteria.
- Follow the relevant role guide in `_docs/team/`.
- Use `_docs/outdated/plan.md` and `_docs/outdated/tasks.md` only as historical context; they do not override the assigned issue.
- Implement only the assigned task. Do not pull features from later backlog tasks into the current task.
- Dependencies are added in `pyproject.toml`. Do not add a dependency without asking first.
- Keep ChoreCrew as a server-rendered Django monolith; use Django templates and HTMX for the main interface.
- Add or update focused tests for behavior changes, then run the relevant tests and the whole suite before finishing.
- Include Django migrations in the same change as any model update.
- Never commit secrets or environment-specific credentials.

Documents

- `_docs/process.md` - how work is organized
- `_docs/task-template.md` - required format for groomed issues
- `_docs/team/pm.md` - instructions for grooming an issue
- `_docs/team/software-engineer.md` - instructions for implementing an issue
- `_docs/outdated/` - historical planning documents
