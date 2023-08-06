import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfremoveduplicatepages",  # Replace with your own username
    version="0.0.3",
    author="Carsten Engelke",
    author_email="carsten.engelke@gmail.com",
    description="A simple tool to remove duplicate or near-duplicate PDF pages by comparing extracted text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carsten-engelke/pdf-remove-duplicate-pages",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pdfremoveduplicatepages = pdfremoveduplicatepages:main',
        ],
    },
    python_requires=">=3.6",
    install_requires=["PyMuPDF>=1.21.1"]
)
