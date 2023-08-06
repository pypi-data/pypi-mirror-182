import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='hw_wisecloud_analytics_1',
    version="7.0.1",
    author='Huawei HMS Core',
    author_email='hms@huawei.com',
    description='Analytics Kit is a one-stop user behavior analysis platform for products such as mobile apps, web apps, quick apps, quick games, and mini-programs. It offers scenario-specific data collection, management, analysis, and usage, helping enterprises achieve effective user acquisition, product optimization, precise operations, and business growth.',
    keywords='example, pypi, package',
    long_description='Analytics Kit is a one-stop user behavior analysis platform for products such as mobile apps, web apps, quick apps, quick games, and mini-programs. It offers scenario-specific data collection, management, analysis, and usage, helping enterprises achieve effective user acquisition, product optimization, precise operations, and business growth.',
    long_description_content_type='text/markdown',
    url='https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/introduction-0000001050745149',
    project_urls={
        'Documentation': 'https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/introduction-0000001050745149',
        'Bug Reports':
        'https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/introduction-0000001050745149/issues',
        'Source Code': 'https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/introduction-0000001050745149',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    extras_require={
    },
)
