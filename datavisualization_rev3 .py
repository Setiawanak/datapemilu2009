#Author : Muhamad Fathurahman, M.Kom
#Data Understanding and Visualization
#### Dilanjutkan oleh : Ade Kukuh Setiawan (1402017154)

#Import Library

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
import numpy as np
############################################
sns.set(style="whitegrid")
# Load Dataset :

dir = "C:\Users\SETIAWAN AK\Downloads\Data Mining\Tugas1_1402017154\\pemilu-dki-2009.xls"
dataset = pd.read_excel(dir)

def summaryDataset():
    print(dataset.describe())

def suaraBerdasarkanGender():
    datax = dataset[['Nama Partai','Jenis KeLamin','Suara Sah Caleg', 'Terpilih']]
    datax = datax.loc[datax['Terpilih'] == 'YA']
    ax = sns.countplot(x="Nama Partai", hue="Jenis KeLamin", data=datax)
    ax.set_label("Rekapitulasi Suara Pemilu DKI")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.ylabel("Jumlah Caleg Terpilih")
    plt.xlabel("Nama Partai")
    plt.title("Rekapitulasi Suara Pemilu DKI")
    plt.show()

def suaraPartaiBerdasarkanDapil(dapil = 'Kota Administrasi Jakarta Barat'):
    datax =dataset[['Nama Partai','Jenis KeLamin','Suara Sah Caleg','Kecamatan', 'Terpilih']]
    datax = datax.loc[datax['Terpilih'] == 'YA']
    datax = datax.loc[datax['Kecamatan'] == dapil]
    ax = sns.countplot(x='Nama Partai', hue='Jenis KeLamin', data= datax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.show()

def suarapartai():
    datax = dataset[['Nama Partai','Kecamatan','Terpilih' ]]
    datax = datax.loc[datax['Terpilih']== 'Tidak']
    datax = datax.loc[datax['Nama Partai']== 'Partai Amanat Nasional']
    ax = sns.countplot(x="Nama Partai", hue="Kecamatan", data=datax)
    ax.set_label("Suara Partai Partai Amanat Nasional")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.ylabel("Jumlah Caleg yang Tidak Terpilih")
    plt.show()

def jumlahcalegberdasarkanjk():
    datax = dataset[['Jenis KeLamin', 'Kecamatan' ]]
    datax = datax.loc[datax['Jenis KeLamin'] == 'L']
    ax = sns.countplot(x="Kecamatan", hue="Jenis KeLamin", data=datax)
    ax.set_label("Jumlah caleg berdasarkan jenis kelamin")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.ylabel("Jumlah Laki-Laki")
    plt.show()

def suaradaerahjakartabarat():
    datax = dataset[['Nama Partai', 'Jenis Kelamin ','Suara Sah Caleg' ,'Kecamatan','Terpilih']]
    datax = datax.loc[datax['Terpilih'] == 'TIDAK']
    datax = datax.loc[datax['Kecamatan'] == 'Kota Administrasi Jakarta Barat']
    ax = sns.countplot(x="Nama Partai", hue="Terpilih", data=datax)
    ax.set_label("Suara Di Jakarta Barat")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    plt.ylabel("Jumlah Suara")
    plt.show()

def main():
    #summaryDataset()
    #suaraBerdasarkanGender()
    #suaraPartaiBerdasarkanDapil()
    suarapartai()
    suaradaerahjakartabarat()
    jumlahcalegberdasarkanjk()


###########################################################################################
main()




