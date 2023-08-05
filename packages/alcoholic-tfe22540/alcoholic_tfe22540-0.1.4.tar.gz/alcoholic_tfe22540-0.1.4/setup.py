# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:19:19 2022

@author: manou
"""

from setuptools import setup

setup(
    name='alcoholic_tfe22540',
    version='0.1.4',    
    description='Framework of my master thesis on the effect of withdrawal on the white matter of alcoholic patients using dMRI data.',
    url='https://github.com/mdausort/TFE22-540',
    author='Manon Dausort',
    author_email='manon.dausort@uclouvain.be',
    license='BSD 2-clause',
    packages=['tfe22540'],
    install_requires=['numpy',
                      'nibabel',     
                      'xlsxwriter',
                      'pandas',
                      'matplotlib',
                      'sklearn',
                      'seaborn',
                      'dipy',
                      'scikit-image',
                      'scipy',
                      'openpyxl'
                      ],

    classifiers=[
        'Intended Audience :: Science/Research',    
        'Programming Language :: Python',
    ],
)