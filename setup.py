from setuptools import setup, find_packages
setup(name = "House_Price",
      version = "0.0.1",
      author = "Devke_Govind",
      author_email = "devkegovind2575@gmail.com",
      packages = find_packages(),
      install_requires = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'flask', 'sklearn']
      )