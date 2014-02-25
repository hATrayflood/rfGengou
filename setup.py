from distutils.core import setup;
setup(
	name="rfGengou",
	version="0.3",
	description="Translate A.D. to Regnal year, and other in Japanese.",
	url="https://github.com/hATrayflood/rfGengou",
	author="hATrayflood",
	author_email="h.rayflood@gmail.com",
	license="The MIT License (MIT)",
	long_description="Detail is needed to written in Japanese. visit github. https://github.com/hATrayflood/rfGengou",
	classifiers=(
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: Japanese",
		"Programming Language :: Python :: 2 :: Only",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Text Processing :: Filters",
	),
	py_modules=["rfGengou"],
	scripts=['rfgengou', 'rfgengou.bat', 'rfGengouCmd.py'],
)
