import setuptools

'''
with open('README', 'r') as fh:
    long_description= fg.read()
'''

setuptools.setup(
    name = 'pack2534',
    version='0.0.1',
    author_email='hyo156@kitech.re.kr',
    description='Python package for Adserver team in KITECH',
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.20.0',
        'scipy>=1.5.0',
        'matplotlib>=3.0.0',
        ],
    author='JJH2',
    )

print('Package path found here')
print(setuptools.find_packages())