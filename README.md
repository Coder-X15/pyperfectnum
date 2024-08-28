# pyperfectnum
A module to check for perfect numbers, just for the sake of learning TDD (test-driven development) of Python projects

## How-tos
1. Initialising:

   i. Setup the virtual environment (not necessary unless for remote testing/debugging purposes):`python3 -m venv ./venv` after `cd`ing into the main directory (parent of `src`), and then run `activate` in `./venv/bin/activate` for Linux (or `./venv/Scripts/Activate.ps1` in Windows) after allowing scripts to run (like using `chmod` in Linux)
   
   ii. Initialising with required modules and stuff: `make init`
2. Testing: `make test`
3. Linting/testing code quality:`make lint` (well, I got a score of 6.96/10)
4. Formatting:`make format`
