import setuptools

setuptools.setup(
    name='annaPack1',
    version='0.0.1',
    author_email='anna@kitech.re.kr',
    description='Python package for Adserver team in Kitech',
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.20.0',
        'scipy>=1.5.0',
        'matplotlib>=3.0.0'
    ],
    author='Nahyeon An'
)

print('Package path found here: ')
print(setuptools.find_packages())