# Grade Reporter & Bug Hunt

## Files Included
- `grade_reporter.py`: Iterates through test scores to display grades, count passes/fails, and calculate the overall average.
- `bug_hunt.py`: Solves syntax, loop boundary, and type errors to correctly sum numbers 1 through 5.

## Reflection
The off-by-one error (`count < 5` instead of `count <= 5`) was the hardest bug to spot because Python ran the script without throwing any error messages. I knew something was wrong because the printed sum was `10` instead of the expected `15`, indicating the loop stopped before adding 5.