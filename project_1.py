######################
# Import libraries
######################
import numpy as np
import pandas as pd
import streamlit as st
import pickle
import io
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import gridspec
from math import pi
# rdkit library
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import PandasTools
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import Fragments
#for similarity
from rdkit import Chem, DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols

#What we'll need for analysis, clustering, etc.

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.cluster import KMeans
from sklearn import datasets, decomposition
from sklearn.manifold import TSNE
#All we need for clustering
from scipy.cluster.hierarchy import dendrogram, linkage
#from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


original_title = '<p style="font-family:URW Chancery L; color:cyan ; text-align: center; font-size: 40px;">AaDya:A Chemical Sapce Navigator for Dual–Target-Directed-Inhibitor design</p>'
st.markdown(original_title, unsafe_allow_html=True)


st.markdown("<h2 style='text-align: center; color: gold;font-size: 20px'>''Chemical space is a concept in cheminformatics referring to the property space spanned by all possible molecules and chemical compounds adhering to a given set of construction principles and boundary conditions'' </h2>", unsafe_allow_html=True)


# detail and use of app
st.markdown("<h2 style='text-align: center; color: pink;font-size: 18px'>'Chemical space is extremely large and screening of entire libraries is impractical and time consuming. Further, most of the molecules are inactive for particular drug targets. Thus, our focus in this work was to calculate the physicochemical descriptors of known inhibitor molecules to know the physicochemical descriptor distribution among inhibitors. The goal of the present study was to characterize the chemical space of BACE-1 and GSK3 to guide focused library design and reduce the time and computational cost. </h2>", unsafe_allow_html=True)


st.markdown("<h2 style='text-align: center; color: pink;font-size: 18px'>'Physicochemical descriptors have been successfully used in earlier studies to design molecules with drug-like oral drug-like properties, and also used to optimize the solubility, permeability and other properties of a molecules (Ajay et al., 1998; Lipinski, 2000; Lajiness et al., 2004; Muegge, 2003). The most accepted and popular implementation of physicochemical descriptors study is Lipinski’s rule of five (Lipinski et al., 2001) and similar kind of implementation were performed for non-oral routes of drug delivery system (Choy and Prausnitz, 2011). These physicochemical descriptors like molecular weight, number of hydrogen bond donor acceptor, logP, polar surface area, number of rotatable bond etc. are extensively used in different studies. These descriptors are used to differentiate between various molecules like human metabolites, toxins, lead like molecules and also used to filter/reduce the size of database for screening </h2>", unsafe_allow_html=True)



