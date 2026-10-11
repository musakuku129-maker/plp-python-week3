# Week 3 Assignment: Conditions and Loops

- grade_reporter.py — checks each score, assigns a grade, counts passes and failures, and prints the average.
- bug_hunt.py — fixes the broken loop so it sums the numbers from 1 to 5 and prints the correct result.

The hardest bug to find in Part B was the loop condition. It ran without crashing and still produced a value, but it stopped before reaching 5, so the result was wrong even though the code looked close to correct. I knew something was wrong because the output did not match the expected total of 15, and a quick check of the loop logic showed it was excluding the final number.
