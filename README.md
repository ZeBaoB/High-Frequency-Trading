# High Frequency Trading: Analysis and Optimal Strategy Simulation

This project explores the dynamics of high-frequency trading by:
- Analyzing Limit Order Book (LOB) data,
- Modeling arrival processes (Poisson, Hawkes processes),
- Calibrating market models based on real or simulated data,
- Simulating and analyzing optimal trading strategies.

The work is structured into several HTML files (exported Jupyter Notebooks), with further extension into optimal control models inspired by academic research.

## Contents

- **Limit Order Book (LOB) analysis**
- **Modeling with Poisson processes**
- **Modeling with Hawkes processes**
- **Calibration of market models**
- **Simulation of optimal strategies (Limit/Market Orders)**

## How to Use

1. **Download or clone the repository.**
2. **Open the HTML files** with any web browser to view the full analysis.
   - No need to run Jupyter locally.
3. (Optional) If you wish to modify or re-run the analysis:
   - Convert the HTML back to `.ipynb` (e.g., using `jupyter nbconvert`) or use the original notebooks.

## Data

> 📂 **Important**:  
> The datasets used in this project (Limit Order Book data) are **not published** in the repository due to confidentiality/licensing reasons.  
> However, the code is written to be **easily adaptable** to any local dataset.  
> You can replace the data-loading parts with your own files (CSV, database, etc.) with minimal changes.

## Future Work

- **Model calibration** and **optimal strategy simulations** will be based on:
  > *Fabien Guilbaud and Huyên Pham (2013)*,  
  > *Optimal high-frequency trading with limit and market orders*,  
  > Quantitative Finance, 13(1), 79–94.  
  > [Link to the article](https://doi.org/10.1080/14697688.2012.708779)

The framework will involve:
- Estimation of order execution intensities,
- Simulation of agent strategies balancing execution and inventory risk,
- Use of mixed regular/impulse control techniques.

## Topics Covered

- Structure and behavior of Limit Order Books
- Arrival processes for orders (Poisson and Hawkes modeling)
- Calibration of spread models and execution processes
- Optimal trading strategies under market and limit orders

## Requirements (if using Jupyter)

- Python 3.x
- Jupyter Notebook / Jupyter Lab
- `numpy`
- `scipy`
- `pandas`
- `matplotlib`
- `statsmodels`
- `hawkes` (for Hawkes process modeling)

## References

- Bacry, E., Mastromatteo, I., Muzy, J.-F. (2015). *Hawkes processes in finance*.
- Cont, R. (2011). *Statistical modeling of high-frequency financial data*.
- Abergel, F., Chakrabarti, B. K., Chakraborti, A., Muni Toke, I., and Patriarca, M. (2011). *Limit Order Books*.
- Guilbaud, F., Pham, H. (2013). *Optimal high-frequency trading with limit and market orders*, Quantitative Finance.

