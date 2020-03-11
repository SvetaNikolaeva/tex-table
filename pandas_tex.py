import pandas as pd
import numpy as np


df_tex = pd.DataFrame()
df_1 = pd.read_csv('fit_results.dat', delimiter = ' ')
params = ['nh', 'PI', 'norm', '1', '2', '3'] # list of parameters
fact = [1, 1, 10**5, 1, 1, 1] # list of factors for each parameter

# write first 3 columns unchanged (obsIds, exposure, chi_r etc)
for i in np.arange(0, 5):
    df_tex[df_1.columns[i]] = df_1[df_1.columns[i]].apply(lambda x:x)

# write parameters with errors    
def errs(par, Min, Max, funct = lambda x:fac*x, k = 2):
    #low = f'{par - Min}'
    low = f'%.{k}f' %funct(par - Min)
    hi  = f'%.{k}f' %funct(Max - par)
    parr = f'%.{k}f' %funct(par)
    par_tex = '$' + parr + '^{+' + hi + '}_{-' + low + '}$'
    return par_tex

for par, fac in zip(params, fact):
    def latex_error(row,par):
        err= errs(row[par],row['min_' + par],row['max_' + par], k = 2)
        return err  
    df_tex[par] = df_1.apply(lambda x: latex_error(x,  par), axis = 1)
    
print(df_tex.to_latex(escape = False, index = False)) 
