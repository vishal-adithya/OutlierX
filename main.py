#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 16:05:40 2025

@author: vishaladithya
"""

import pandas as pd
from datasets import load_dataset

nab = load_dataset("numenta/NAB",split="train")
df = pd.Dataframe(nab)
