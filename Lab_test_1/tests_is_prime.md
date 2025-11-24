## AI-generated test plan for `is_prime(n)`

I used the AI coding agent (me) to enumerate and justify the following coverage-focused test inputs before touching the implementation:

| Test ID | Input `n` | Expected | Rationale |
| --- | --- | --- | --- |
| T1 | 2 | True | Smallest prime, catches fencepost errors around the lower bound. |
| T2 | 3 | True | First odd prime; also validates skipping even divisors. |
| T3 | 4 | False | Smallest composite, ensures even numbers > 2 return False. |
| T4 | 1 | False | Definition check: 1 is not prime. |
| T5 | 0 | False | Non-positive numbers must be rejected. |
| T6 | -7 | False | Negative input handling. |
| T7 | 25 | False | Perfect square composite to confirm sqrt-based loop boundaries. |
| T8 | 97 | True | Larger prime to test loop coverage. |
| T9 | 221 | False | Composite with non-trivial odd factors (13 × 17) to ensure full divisor search. |
| T10 | 104729 | True | 10000th prime stresses efficiency for moderately large inputs. |

All subsequent implementation and automated checks will be required to satisfy these expectations.

