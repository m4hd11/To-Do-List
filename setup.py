from setuptools import setup

setup(name= 'To-Do-List', version= '1.0', py_modules=['to_do_list', 'main'], entry_points={
    "console_scripts": ["todo=main:To_Do_Sys",],
},
author= 'Mahdi_Iranpour', description = 'This is a simple To-Do-List for managing your tasks')
