# tex-table
Here you can find python script for LaTex code of tables creation through pandas python library. It also helps you to write values with errors (upper and lower) with latex style features. You can find python code, example data (fit_results) and log file with code for building tables in latex.

Log file contains LaTex code. Assuming you have table in CSV or text format with columns named like: "par", "par_min", "par_max" and others, e.g., "statistics", "exposure", "obsIds" etc. Some of columns you can keep unchanged without any formating (e.g. last few ones in previous sentence), but for estimated parameters it will look like: " $par^{+err1}_{-err2} ", where err1 = par_max - par, err2 = par - par_min
