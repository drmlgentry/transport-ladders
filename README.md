\# transport-ladders



Shared code + reproducible scans for the \*\*transport ladder\*\* program and two companion papers:



\- \*\*Paper IIIa\*\*: completeness / recurrence structure for selected ladder families

\- \*\*Paper IIIb\*\*: certified exclusion results using algebraic certification



This repo is intentionally built to be:

\- \*\*deterministic\*\* (fixed scan domains, manifest + tables),

\- \*\*auditable\*\* (explicit conventions, explicit certificates),

\- \*\*paper-aligned\*\* (LaTeX entrypoints + shared technical appendix).



---



\## Mathematical object (the “ladder”)



We work in a fixed hyperbolic Coxeter transport model with two distinguished elements:



\- a “shift” element `τ`

\- a “transport” element `ρ`



and study the \*\*two-parameter ladder family\*\*

\\\[

W(m,n) \\;=\\; \\tau^{m}\\,\\rho\\,\\tau^{n}\\,\\rho^{-1},

\\qquad (m,n)\\in\\mathbb{Z}^2.

\\]



A scan evaluates \\(W(m,n)\\) on a bounded integer box and records:

1\) \*\*numeric observables\*\* from a chosen real representation (e.g. a spectral radius surrogate),

2\) \*\*exact certificates\*\* derived from an algebraic model (degree-8 norm polynomials over \\(\\mathbb{Q}\\)).



---



\## What the scan produces



The scan writes:



\- `output/scan/manifest.json` (run metadata + summary counts)

\- `output/scan/table.csv` (rowwise data)



Each row corresponds to one \\((m,n)\\) hit and includes numeric invariants plus the exact certificate polynomial over \\(\\mathbb{Q}\\):

\\\[

\\mathrm{cert\\\_poly\\\_Q}(t)

\\;=\\;

\\mathrm{Norm}\_{\\mathbb{Q}(\\sqrt5)/\\mathbb{Q}}\\big(\\chi\_{W}(t)\\big),

\\]

where \\(\\chi\_W\\) is the characteristic polynomial of the exact algebraic realization of \\(W(m,n)\\).



\### Certificate statuses



\- `cert\_ok`: a Perron root \\(>1\\) is extracted with \*\*positive root separation margin\*\*

\- `cert\_degenerate`: the certificate polynomial is intrinsically non-informative (e.g. repeated-root unipotent forms such as \\((t-1)^d\\) or \\((t^2-1)^k\\)), hence separation margin is zero

\- `cert\_fail`: true computational failure (should be 0 for a healthy toolchain)



Default scan (current small box) yields:

\- `cert\_ok = 30`

\- `cert\_degenerate = 60`

\- `cert\_fail = 0`



---



\## Reproducibility



Run these commands in PowerShell:



```powershell

cd C:\\dev\\transport-ladders

.\\scripts\\setup-python.ps1

.\\scripts\\run-tests.ps1

.\\scripts\\build-iiia.ps1

.\\scripts\\build-iiib.ps1

python -m transport\_ladders.run\_scan

Get-Content .\\output\\scan\\manifest.json



