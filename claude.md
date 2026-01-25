# Claude Code Session Guide for Costa

## Working Style Preferences - UPDATED 2026-01-21

**NEW APPROACH: Learning by Doing**
- **Costa writes the code**: Claude describes what needs to happen, Costa implements it
- **Struggle is learning**: Making mistakes and debugging them is where real learning happens
- **Feedback loop**: Costa shows code → Claude gives feedback → Costa fixes it → Repeat
- **Explanations when needed**: Deep explanations of concepts, but Costa does the implementation
- **No spoon-feeding**: Claude guides and corrects, but doesn't write the code for Costa

**Previous approach (kept for reference):**
- ~~Code in small chunks: Max 2-3 lines at a time~~ → Now Costa writes the chunks
- **Exception for repetitive code**: Can provide all at once (e.g., buttons a-h, 1-8)
- **Explanations**: Provide full, detailed explanations of code elements
- **Line-by-line breakdowns**: Walk through CSS/code line by line when requested
- **Understanding first**: Ensure full understanding before moving to next step
- **Active learning**: Ask questions to verify understanding as we go
- **Test frequently**: Pause to test functionality as features are added

## Session 2026-01-24: Fixing Two-Column Display Logic

### What We Fixed
- Bug: Moves displayed in staircase pattern (one move per row with empty opposite column)
- Root cause: Logic used `onWhiteMove` toggle, filling only one column per iteration
- Fix: Each loop iteration now grabs TWO moves (one for each column)
- Simplified code by removing `onWhiteMove` and `whiteFirst` variables for now
- Added bounds checking (`moveIndex < moves.length`) to handle odd number of moves

### Key Learnings
- **Tracing code execution**: Walking through loop iterations with actual values
- **Bounds checking**: Prevent accessing array elements that don't exist
- **Simplify first**: Started with "white always first" before handling edge cases
- **Two if/else blocks**: Both run each iteration (not either/or like if/else if)

### Next Steps
- Add handling for "black moves first" case
- Add gray work-in-progress text display (currentMove) while typing
- Implement Backspace functionality

---

## Session 2026-01-21: Two-Column Chess Notation Display

### What We Built
- White/Black to move selector buttons (determine starting player)
- Two-column layout for Principal Variation (PV):
  - White moves in left column (200px wide)
  - Black moves in right column (200px wide)
  - Larger font (18px) for main line
  - Flexbox rows for layout
- Move tracking with `moves[]` array and `currentMove` string
- Space bar commits current move to array
- `updateDisplay()` function with two-column HTML generation
- Kept `updateDisplayInline()` for future sideline/variation display

### Key Learnings - JavaScript & Debugging
- **Post-increment (`moveIndex++`)**: Use value first, then increment
- **Pre-increment (`++moveIndex`)**: Increment first, then use value
- **Logical NOT operator (`!`)**: `!onWhiteMove` flips true/false
- **Assignment with NOT**: `onWhiteMove = !onWhiteMove` toggles state
- **String concatenation**: `+` joins string literals and variables
- **Splitting long strings**: Need `+` when breaking across lines for readability
- **innerHTML property**: Replaces content inside an element
- **Browser DevTools**: Using Elements tab and Console for debugging
- **Inline CSS in JavaScript**: Building HTML strings with style attributes
- **Empty divs hold space**: Width is preserved even with no content

### Problem-Solving Approach
- Costa wrote code based on requirements/hints from Claude
- Made mistakes with syntax (missing `<`, `>`, `/`, `;`)
- Debugged logic errors (incrementing moveIndex in wrong places)
- Learned by fixing own errors with feedback
- Much more effective than being given code!

### Next Steps
- Add gray work-in-progress text display (currentMove) while typing
- Implement Backspace functionality
- Add sideline/variation support (smaller font, continuous flow)
- Promotion/demotion of variations
- Timer (session + per-puzzle)
- Navigation between puzzles
- Save solutions to database

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

### Environment Notes
- Working on Windows PC (also has Mac setup)
- Using PowerShell (execution policy set to RemoteSigned)
- Flask app runs on port 5001
- Virtual environment: `venv\Scripts\activate`
