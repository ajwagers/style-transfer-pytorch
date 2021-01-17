import setuptools

setuptools.setup(
    name='style-transfer-pytorch',
    version='0.1',
    description='Neural style transfer in PyTorch.',
    # TODO: add long description
    long_description='Neural style transfer in PyTorch.',
    url='https://github.com/crowsonkb/style-transfer-pytorch',
    author='Katherine Crowson',
    author_email='crowsonkb@gmail.com',
    license='MIT',
    packages=['style_transfer'],
        entry_points={
        'console_scripts': ['style_transfer=style_transfer.cli:main'],
    },
    install_requires=['Pillow>=8.0.0',
                      'torch>=1.7.1',
                      'torchvision>=0.8.2',
                      'tqdm>=4.46.0'],
    # TODO: Add classifiers
    classifiers=[],
)
