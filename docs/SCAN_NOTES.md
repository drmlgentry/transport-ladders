\# Scan notes



Baseline scan results (see `output/scan/manifest.json`):



\- cert\_ok = 30

\- cert\_degenerate = 60

\- cert\_fail = 0



Interpretation:

\- `cert\_degenerate` means the normed characteristic polynomial collapses to repeated-root forms

&nbsp; such as `(t-1)^d` or `(t^2-1)^k`, yielding zero root separation margin; these cases are

&nbsp; mathematically non-certifying (fail-closed by design), not computational failures.

\- `cert\_ok` indicates a Perron root > 1 with positive numeric separation margin.

\- `cert\_fail` indicates true extraction failure (should remain 0).



