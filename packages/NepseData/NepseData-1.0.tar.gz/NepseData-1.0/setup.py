from setuptools import setup
setup(
    name = "NepseData",
    version = "1.0",
    description = "Every information and data in nepse daily trading are available",
    long_description= "  { ticker : Stock Symbol },{ ltp : Last Transaction Price },{ change : Change in Points }, { change_in_percentage : Percentage change of particular stock }, { opens : Opening Price of Stock }, { high : Highest price of stock that day},{ low : Lowest price of stock that day},{ volume = Total transaction volume that day } ",
    author = "Anup Timsina",
    packages = ['NepseData'],
    install_requires = ['requests','bs4']
)
    