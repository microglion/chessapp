# Claude Code Session Guide for Costa

## Working Style Preferences - UPDATED 2026-01-21

**NEW APPROACH: Learning by Doing**
- **Costa writes the code**: Claude describes what needs to happen, Costa implements it
- **Struggle is learning**: Making mistakes and debugging them is where real learning happens
- **Feedback loop**: Costa shows code → Claude gives feedback → Costa fixes it → Repeat
- **Explanations when needed**: Deep explanations of concepts, but Costa does the implementation
- **No spoon-feeding**: Claude guides and corrects, but doesn't write the code for Costa
- **No hints until asked**: Don't give hints, pseudocode, or implementation details until Costa is stuck and explicitly asks for help

**Previous approach (kept for reference):**
- ~~Code in small chunks: Max 2-3 lines at a time~~ → Now Costa writes the chunks
- **Exception for repetitive code**: Can provide all at once (e.g., buttons a-h, 1-8)
- **Explanations**: Provide full, detailed explanations of code elements
- **Line-by-line breakdowns**: Walk through CSS/code line by line when requested
- **Understanding first**: Ensure full understanding before moving to next step
- **Active learning**: Ask questions to verify understanding as we go
- **Test frequently**: Pause to test functionality as features are added

## Session 2026-01-26: Grey Text, Backspace & Brace Debugging

### What We Built
- **Enter button functional**: Now works same as Space for submitting moves
- **Grey work-in-progress text**: Shows `currentMove` while typing, before submission
- Grey text appears in correct column based on whose turn it is
- **Backspace functionality**: `deleteLastChar()` removes last character from `currentMove`

### Key Learnings - JavaScript & Logic
- **OR operator (`||`)**: `char === ' ' || char === '\n'` - true if either condition is true
- **`innerHTML` rebuilds completely**: Every `updateDisplay()` call replaces entire content, not appending
- **Modulo for turn detection**: `moves.length % 2` determines whose turn based on move count
- **`iswhitesTurn` calculation**: `(whiteFirst && moves.length % 2 === 0) || (!whiteFirst && moves.length % 2 === 1)`
- **Brace matching**: Hardest part of session - mismatched braces caused "html is not defined" errors
- **Combining conditions**: Move variable definition before `if` to use in condition (`if (iswhitesTurn && currentMove.length > 0)`)
- **`slice()` returns new value**: `slice()` doesn't modify the original string - must assign result back (`currentMove = currentMove.slice(0,-1)`)
- **Strings are immutable**: Unlike arrays, string methods return new strings rather than modifying in place

### The Two-Part Grey Text Solution
1. **Inside while loop** (lines 155-157): Handles black's grey text - appears in same row as white's committed move
2. **Post-loop section** (lines 165-172): Handles white's grey text - creates new row when no moves exist yet or after black's move

### Problem-Solving Process
- Started by understanding the flow: `insertText()` → `updateDisplay()` → rebuilds entire HTML
- First attempt put grey text after while loop - appeared in wrong position
- **Approach A**: Grey text on new row for black's turn (jumpy)
- **Approach B**: Grey text inside while loop for black's turn (cleaner - keeps it in same row)
- Multiple brace debugging sessions - learned to trace closing braces carefully
- Final cleanup: moved `iswhitesTurn` before if statement to combine with `currentMove.length > 0`

### Next Steps
- Extend backspace to confirmed moves: when `currentMove` is empty, pop last move from `moves` array into `currentMove` for editing
- Add sideline/variation support (smaller font, continuous flow)
- Promotion/demotion of variations
- Timer (session + per-puzzle)
- Navigation between puzzles
- Save solutions to database

### Completed
- Virtual keyboard UI with chess pieces, files, ranks, symbols, controls
- `/session` route and template
- White/Black to move selector buttons
- Two-column PV display (white left, black right)
- Fixed staircase bug - loop now grabs two moves per iteration
- Enter button functional (same as Space)
- Grey work-in-progress text for `currentMove` while typing
- Backspace functionality for `currentMove`

---

## Session 2026-01-25: Fixing Two-Column Display Logic

### What We Fixed
- **Bug:** Moves displayed in staircase pattern (one move per row with empty opposite column)
- **Root cause:** Logic used `onWhiteMove` toggle, filling only one column per iteration
- **Solution:** Rewrote loop to grab TWO moves per iteration (one for each column)
- Removed `onWhiteMove` variable - no longer needed
- Added special handling for "black moves first" case (first row has empty white column)
- Added proper bounds checking for odd number of moves

### Key Learnings - JavaScript & Logic
- **Ternary operator (`? :`)**: Shorthand for if/else - `condition ? valueIfTrue : valueIfFalse`
- **Array indexing strategy**: Access `moves[moveIndex]` and `moves[moveIndex + 1]`, then increment by 2
- **Post-increment timing**: Why `moves[moveIndex++]` wouldn't work when grabbing two values
- **HTML structure in loops**: Each iteration must create complete row structure (both columns)
- **State vs calculation**: `whiteFirst` never changes; used to determine column assignment
- **Bounds checking edge cases**: `moveIndex + 1 < moves.length` protects against accessing non-existent moves
- **Special case handling**: First row when black moves first needs different logic

### The Fixed Logic
**White moves first:**
- Row 1: `moves[0]` | `moves[1]` → moveIndex += 2
- Row 2: `moves[2]` | `moves[3]` → moveIndex += 2

**Black moves first:**
- Row 1: empty | `moves[0]` → moveIndex += 1
- Row 2: `moves[1]` | `moves[2]` → moveIndex += 2
- Row 3: `moves[3]` | `moves[4]` → moveIndex += 2

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
- Uses both Windows PC and Mac (Mac more on weekends)
- Windows: PowerShell, `venv\Scripts\activate`
- Mac: Terminal, `source venv/bin/activate`
- Flask app runs on port 5001
