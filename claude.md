# Claude Code Session Guide for Costa

## Working Style Preferences

- **Code in small chunks**: Max 2-3 lines at a time for new concepts
- **Exception for repetitive code**: Can provide all at once (e.g., buttons a-h, 1-8)
- **Explanations**: Provide full, detailed explanations of code elements
- **Line-by-line breakdowns**: Walk through CSS/code line by line when requested
- **Understanding first**: Ensure full understanding before moving to next step
- **Active learning**: Ask questions to verify understanding as we go
- **Test frequently**: Pause to test functionality as features are added

## Session 2026-01-14: Virtual Keyboard UI

### What We Built
- `/session` route for puzzle-solving interface
- `session.html` template with virtual keyboard
- Text input interface (no chess board needed)
- Virtual keyboard with:
  - Chess pieces: K Q R B N
  - Files: a-h
  - Ranks: 1-8
  - Symbols: x + # ? ! = -
  - Controls: Space, Enter, Backspace
- CSS flexbox layout for evenly-sized button rows
- JavaScript functions: `insertText()` and `deleteLastChar()`

### Key Learnings
- CSS class (`.name`) vs ID (`#name`) selectors
- Flexbox `flex: 1` for equal-width buttons
- Descendant selectors (`.parent child`)
- IDs are unique, classes are reusable
- `<div>` (block) vs `<span>` (inline) elements
- `getElementById()` returns the entire element object, not just values

### Next Steps
- Add timer (session + per-puzzle)
- Navigation between puzzles (#1, #2, #3)
- Save solutions to database
- Marking/review functionality

### Environment Notes
- Working on Windows PC (also has Mac setup)
- Using PowerShell (execution policy set to RemoteSigned)
- Flask app runs on port 5001
- Virtual environment: `venv\Scripts\activate`
