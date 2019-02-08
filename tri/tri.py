#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# import des données
data = pd.read_csv("data.csv",sep=";")

# tri à plat
data["csp"].value_counts()

# tri à plat avec probabilités
data["csp"].value_counts(normalize=True,dropna=False)

# tri croisé version pivot_table()
data.pivot_table(index="csp",columns="ville",aggfunc=len)

# tri croisé version crosstab
pd.crosstab(data["csp"],data["ville"])
