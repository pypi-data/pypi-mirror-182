# import setuptools

# setuptools.setup(
#     name='uc-sgsim',
#     version='1.1.0',
#     author='Zncl2222',
#     author_email='3002shinning@gmail.com',
#     description='Geo-Statistic alogrithm (Sequential Gaussian Simulation)',
#     url='https://github.com/Zncl2222/Stochastic_UC_SGSIM',
#     packages=setuptools.find_packages(),
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Topic :: Scientific/Engineering :: Mathematics',
#     ],
#     python_requires='>=3.7',
# )

from setuptools import setup, find_packages

setup(
    name='uc_sgsim',
    version='1.1.1',
    description='Random Field Generation',
    url='https://github.com/Zncl2222/Stochastic_UC_SGSIM',
    author='Zncl2222',
    author_email='3002shinning@gmail.com',
    license='MIT',
    zip_safe=False,
    include_package_data=True,
    packages=['uc_sgsim','uc_sgsim/Cov_Model','uc_sgsim/Krige','uc_sgsim/Plot', 'uc_sgsim/c_core'],
    package_data={'': ['*.dll', '*.so']},
    install_requires=['numpy', 'scipy', 'matplotlib'],
    keywords=["RandomField","Sequential Gaussian Simulation","geostatistic"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

    ]
)