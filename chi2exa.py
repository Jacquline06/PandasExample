import seaborn as sns
import pandas as pd
import numpy as np
from scipy import stats
df=sns.load_dataset("tips")

data=pd.crosstab(index=[df["sex"], df["smoker"], df["day"], df["time"]], columns=df["size"])
#print(data)
#print("-------------------------------------------------------------------------")
observed_value=data.values
print("observed_value:",observed_value)
value=stats.chi2_contingency(data)
print("value:",value)
expected_value=value[3]
print("Expected_value:",expected_value)
#how we are going to do in formula and cross check
chi2=sum([((o-e)**2)/e for o,e in zip(observed_value,expected_value)])
print("chi2:",chi2)
chi2sq=sum(sum([((o-e)**2)/e for o,e in zip(observed_value,expected_value)]))
print("chi2sq:",chi2sq)#statitics value
critical_point=stats.chi2.ppf(q=0.97,df=95)
print("critical_point:",critical_point)
#chi2sq=86.7674870356798
#critical_point=122.56179371396274
if chi2sq>critical_point:
    print("H0 Reject null hypothesis, Ha accepts alternate hypothesis , both columns are dependent")
else:
    print("H0 accept null hypothesis, Ha rejects alternate hypothesis,  both columns are independent")

#we are going to calculate p value
p_value=1-stats.chi2.cdf(x=chi2sq,df=95)
print("p_value :",p_value)

if p_value<0.075:
    print("H0 Reject null hypothesis, Ha accepts alternate hypothesis , both columns are dependent")
else:
    print("H0 accept null hypothesis, Ha rejects alternate hypothesis,  both columns are independent")