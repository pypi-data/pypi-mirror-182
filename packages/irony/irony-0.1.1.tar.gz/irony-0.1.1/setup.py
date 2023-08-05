from setuptools import setup, find_packages

with open("README.md", "r") as f2r:
    lng_desc = f2r.read()

setup(
    name='irony',
    version='0.1.1',
    license='GPL',
    long_description=lng_desc,
    long_description_content_type='text/markdown',
    author="Mohammad S.Niaei",
    author_email='m.shemuni@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/mshemuni/irony',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['IRAF', 'Photometry', 'Python'],
    install_requires=[
        'astroalign',
        'astropy',
        'matplotlib',
        'mpl_point_clicker',
        'numpy',
        'pandas',
        'photutils',
        'pyraf',
        'sep',
    ],
    classifiers=[
        'Natural Language :: English',
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Operating System :: POSIX :: Linux',
    ]

)
