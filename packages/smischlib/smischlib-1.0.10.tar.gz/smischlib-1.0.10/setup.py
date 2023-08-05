from setuptools import setup, find_packages

setup(
    name='smischlib', 
    version='1.0.10', 
    packages=find_packages(),
    py_modules=['smischlib',
    'src.utilities.running_os',
    'src.console.clear_console',
    'src.input.anim_input',
    'src.utilities.running_os',
    'src.print.anim_print',
    'src.input.ask_input',
    'src.string.palindrom',
    'src.numbersys.text_to_bin',
    'src.numbersys.bin_to_text'],  
    install_requires=[],
    author='Smisch', 
    author_email='smisch@smisch.sk',
    description='Library with addon functions for python.',
    license='MIT',
    keywords='print input',
)