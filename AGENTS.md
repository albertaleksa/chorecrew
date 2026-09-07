# Commands

- `.venv/bin/python -m pip install --editable .` - install dependencies
- `.venv/bin/python manage.py test` - run the whole test suite
- `.venv/bin/python manage.py test tests.test_smoke` - run one test module

# Rules

- Read `_docs/plan.md` for product and architecture decisions and `_docs/tasks.md` for task scope before making changes.
- Implement only the assigned task. Do not pull features from later backlog tasks into the current task.
- Dependencies are added in `pyproject.toml`. Do not add a dependency without asking first.
- Keep ChoreCrew as a server-rendered Django monolith; use Django templates and HTMX for the main interface.
- Add or update focused tests for behavior changes, then run the relevant tests and the whole suite before finishing.
- Include Django migrations in the same change as any model update.
- Never commit secrets or environment-specific credentials.

Documents

- `_docs/process.md` - how work is organized