# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = CensusData
SOURCEDIR     = rst
BUILDDIR      = ../../censusdata-docs

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	jupyter nbconvert --to rst --output-dir rst/ notebooks/example1.ipynb
	jupyter nbconvert --to rst --output-dir rst/ notebooks/example2.ipynb
	jupyter nbconvert --to rst --output-dir rst/ notebooks/example3.ipynb
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
