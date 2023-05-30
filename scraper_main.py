import pandas as pd

# HTML text processing
from bs4 import beautifulsoup

# NLP package used to aid in text manipulation
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Machine Learning modules used to prepare and measure text
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch

# Helper modules
import matplotlib.pyplot as plt
from tqdm.notebook import trange  # Progress bar

# Refinitiv packages to extract filings data and retrieve price data
import refinitiv.dataplatform as rd
from refinitiv.dataplatform.content import filings

# Convenient modules to simplify API access to Filings
%run ./FilingsQuery.ipynb
%run ./SymbolLookup.ipynb
pd.set_option('display.max_colwidth', 60)