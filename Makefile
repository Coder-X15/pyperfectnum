# TODO: Create Makefile for python project

PROJECT_NAME := pyperfectnum
PYTHON := python
VENV_DIR := ./venv
REQUIREMENTS_FILE := requirements.txt
REQUIREMENTS_DEV_FILE := requirements_dev.txt

.PHONY: git-init git-config-user git-config-alias venv install-deps install-dev-deps lint format test clean exit

git-init:
	if not exist .git (
		git init
		curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
	) else (
		echo "Already a git repository"; \
	)

git-config-user:
	git config user.name "Coder-X15"
	git config user.email "samrubenabraham@yahoo.com"

git-config-alias:
	git config --global alias.co checkout
	git config --global alias.ci commit
	git config --global alias.cim "commit -m"
	git config --global alias.cima "commit -am"
	git config --global alias.br branch
	git config --global alias.brs switch
	git config --global alias.bsd "switch dev"
	git config --global alias.bsm "switch main"
	# TODO: log commands
	git config --global alias.logad "log --oneline --graph --all --decorate"
	# TODO: Plumbing commands


venv:
    # $(VENV_DIR)/Scripts/activate
    # $(VENV_DIR)/Scripts/activate: $(REQUIREMENTS_FILE)
	if  not exist $(VENV_DIR) (
		$(PYTHON) -m venv $(VENV_DIR)
		$(VENV_DIR)/Scripts/python -m pip install --upgrade pip setuptools wheel
	)

install-deps: venv
    # $(VENV_DIR)/Scripts/activate
	if exist $(REQUIREMENTS_FILE) (
		$(VENV_DIR)/Scripts/python -m pip install -r $(REQUIREMENTS_FILE)
	)

install-dev-deps: venv
    # $(VENV_DIR)/Scripts/activate
	if exist $(REQUIREMENTS_DEV_FILE) (
		$(VENV_DIR)/Scripts/python -m pip install -r $(REQUIREMENTS_DEV_FILE); \
	)

lint: $(VENV_DIR)/Scripts/activate
	$(VENV_DIR)/Scripts/python -m pylint **/*.py

format:
    # $(VENV_DIR)/Scripts/activate
	$(VENV_DIR)/Scripts/python -m black **/*.py

test: $(VENV_DIR)/Scripts/activate
	$(VENV_DIR)/Scripts/python -m pytest -v

clean:
	rmdir /s /q __pycache__
	del /s /q *.pyc

exit: clean
	rmdir /s /q $(VENV_DIR)

.PHONY: init
init: git-init git-config-user git-config-alias venv install-deps install-dev-deps

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  git-init	  Initialize a new Git repository and download Python gitignore"
	@echo "  git-config-user  Configure Git user name and email"
	@echo "  git-config-alias Configure common Git aliases"
	@echo "  venv		  Create a new virtual environment"
	@echo "  install-deps  Install project dependencies from requirements.txt"
	@echo "  install-dev-deps Install development dependencies from requirements_dev.txt"
	@echo "  lint		  Run code linter (pylint)"
	@echo "  format		Format code with black"
	@echo "  test		  Run tests with pytest"
	@echo "  clean		 Remove temporary files"
	@echo "  exit		  Clean and remove the virtual environment"
	@echo "  help		  Show this help message"