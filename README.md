# Road To 1 Million With EPF

![Static Badge](https://img.shields.io/badge/license-GPL3-blue)
![Static Badge](https://img.shields.io/badge/python-3.11-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jf7sray2rbu8bgclqnvaxu.streamlit.app/)

EPF or KWSP is an institution formed by Malaysia government to safeguard its member retirement saving. Due to the rising cost of living and changing economic landscape, it poses a challenge for people that wishes to retire early. "How much is enough for me to retire early?" has become a common question for many that seek to retire comfortably.

![Alt text](image.png)

## Objective
To provide a framework for projection of the years for a person to achieve 1 million in saving using EPF

## Methodology 
**Goal Seek:**
$$10^6 = 12 \times x \times (r + r^2 + r^3 + ... + r^n) $$
$$\iff n = \frac{1}{ln(r)}\times ln(\frac{10^6 \times (r-1)}{12xr} + 1)$$

where $r = (1 + i)$, the annual dividend rate and $x$ is the monthly contribution rate. In this equation, interest is assumed to be in the form of a yearly payment.

**Contribution Assumption:**

To simplify the computation for contribution, the given yearly bonus is divided as a monthly payment where:

$$x = \frac{bonus}{12} + salary$$

If however, the annual interest is to be given on monthly basis, such an assumption might cause inaccurate projection.

## Data Source
Data | Source
:-- | --:
Income Tax | [Tax Rate](https://www.hasil.gov.my/en/individual/individual-life-cycle/how-to-declare-income/tax-rate/)
EPF Contribution Rate | [Contribution Rate](https://www.kwsp.gov.my/member/overview#:~:text=When%20you%20contribute%2011%25%20of,rate%20exceeding%20the%20statutory%20rates.)
EPF Interest Rate | [Dividend](https://www.kwsp.gov.my/dividend)
SOCSO & EIS | [Perkeso](https://www.perkeso.gov.my/en/rate-of-contribution.html)