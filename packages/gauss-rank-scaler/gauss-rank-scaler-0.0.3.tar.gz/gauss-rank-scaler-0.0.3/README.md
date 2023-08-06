# Gauss Rank Scaler
  
A scikit-learn style transformer that scales numeric variables to normal distributions. 

Input normalization for neural networks is very important. Gauss Rank is an effective algorithm for converting numeric variable distributions to normals. It is based on rank transformation. The first step is to assign a spacing between -1 and 1 to the sorted features, then apply the inverse of error function `erfinv` to make it look like a Gaussian. 
  
![](https://aldente0630.github.io/assets/gauss_rank_scaler3.png)
  
This generally works much better than Standard or Min Max Scaler.
  
## Important Links
  
* [Interview of the Kaggle competition winner (Michael Jahrer)](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction/discussion/44629#250927)  
* [Blog post introducing Gauss Rank's concept and simple implementation (Zygmunt Zając)](http://fastml.com/preparing-continuous-features-for-neural-networks-with-rankgauss)
  
## Usage

Gauss Rank Scaler is a fully compatible sklearn transformer that can be used in pipelines or existing scripts. Supported input formats include numpy arrays and pandas dataframes. All columns passed to the transformer are properly scaled.

## Example

```python
from gauss_rank_scaler import GaussRankScaler
import pandas as pd
from sklearn.datasets import load_boston
%matplotlib inline

# prepare some data
bunch = load_boston()
df_X_train = pd.DataFrame(bunch.data[:250], columns=bunch.feature_names)
df_X_test = pd.DataFrame(bunch.data[250:], columns=bunch.feature_names)

# plot histograms of two numeric variables
_ = df_X_train[['CRIM', 'DIS']].hist()
```
![](https://aldente0630.github.io/assets/gauss_rank_scaler1.png)
```python
# scale the numeric variables with Gauss Rank Scaler
scaler = GaussRankScaler()
df_X_new_train = scaler.fit_transform(df_X_train[['CRIM', 'DIS']])

# plot histograms of the scaled variables
_ = pd.DataFrame(df_X_new_train, columns=['CRIM', 'DIS']).hist()
```
![](https://aldente0630.github.io/assets/gauss_rank_scaler2.png)
```python
# scale test dataset with the fitted scaler
df_X_new_test = scaler.transform(df_X_test[['CRIM', 'DIS']])
```
## This is a direct copy of the repositopry by Aldente06030 packaged for pip
(https://github.com/aldente0630/gauss-rank-scaler)
