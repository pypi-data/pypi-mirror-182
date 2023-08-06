from setuptools import setup

setup(name='dataModul13',
      version='1.2',
      description='Syntax:		function: data("{data}")# save data;		function; read(); read data		function encodeData() encode data		function decodeData() decode data		example:		from dataModul import *;		test=data("ABC");		test.encode();		print(test.read());		test.decode();		print(test.read());				Console:		{0}{1}{2}		abc',
      packages=[''],
      author_email='pyprogrammer13@gmail.com',
      zip_safe=False)
