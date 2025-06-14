#!/usr/bin/env python3
"""
🚀 Python Project Structure Generator (Cross‑Platform)
"""

import sys
import platform
from pathlib import Path


def create_directory(path: Path) -> bool:
    """Create Directory"""
    try:
        path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {path}")
        return True
    except Exception as e:
        print(f"✗ Failed to create directory {path}: {e}")
        return False


def create_file(filepath: Path, content: str = "") -> bool:
    """Create File"""

    try:
        filepath.write_text(content, encoding='utf-8')
        print(f"✓ Created file: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Failed to create file {filepath}: {e}")
        return False


def get_vscode_settings() -> str:
    """Get VSCODE Setting"""

    return '''{
    "python.defaultInterpreterPath": "./venv/bin/python"
}'''


def get_github_workflow() -> str:
    """Github WorkFlow"""

    return '''name: Run Unit Tests
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: pytest
'''


def get_gitignore() -> str:
    return '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
.env

# VSCode settings
.vscode/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Build / distribution
build/
dist/

# Logs
*.log

# Data
data/raw/*
data/processed/*
!data/raw/.gitkeep
!data/processed/.gitkeep
'''


def get_requirements() -> str:
    """Return base project dependencies."""
    return '''# Project dependencies
black==24.3.0
flake8==6.1.0
pytest==7.4.0
python-dotenv==1.0.0
'''


def get_pyproject_toml() -> str:
    """ Get Py Project Fucntion """
    return '''[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
'''


def get_makefile() -> str:
    """ Get Mkae file Function 
    """
    return '''.PHONY: venv install test clean

venv:
\tpython3 -m venv venv

install: venv
\tvenv/bin/pip install -r requirements.txt

test:
\tvenv/bin/pytest

clean:
\trm -rf venv __pycache__ build dist *.egg-info
'''


def get_main_readme(proj_name: str) -> str:
    return f"# {proj_name}\n\nProject description goes here.\n"


def get_env_file() -> str:
    return "# Environment variables (example)\nDEBUG=true\n"


def get_docs_readme() -> str:
    return "# Documentation\nAdd project documentation here.\n"


def get_notebooks_readme() -> str:
    return "# Notebooks\nJupyter notebooks for analysis.\n"


def get_scripts_readme() -> str:
    return "# Scripts\nUtility scripts for automation.\n"


def get_data_readme() -> str:
    return "# Data\nRaw and processed data files.\n"


def get_examples_readme() -> str:
    return "# Examples\nExample usage and demos.\n"


def main():
    base = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    proj_name = base.name

    print(f"Creating Python project at: {base}\n")

    dirs = [
        base / ".vscode",
        base / ".github" / "workflows",
        base / "src" / "core",
        base / "src" / "models",
        base / "src" / "utils",
        base / "src" / "services",
        base / "tests" / "unit",
        base / "tests" / "integration",
        base / "notebooks",
        base / "scripts",
        base / "docs",
        base / "data" / "raw",
        base / "data" / "processed",
        base / "config",
        base / "examples",
    ]

    for d in dirs:
        if not create_directory(d):
            return

    init_files = [
        base / "src" / "__init__.py",
        base / "src" / "core" / "__init__.py",
        base / "src" / "models" / "__init__.py",
        base / "src" / "utils" / "__init__.py",
        base / "src" / "services" / "__init__.py",
        base / "tests" / "__init__.py",
        base / "tests" / "unit" / "__init__.py",
        base / "tests" / "integration" / "__init__.py",
        base / "notebooks" / "__init__.py",
        base / "scripts" / "__init__.py",
        base / "config" / "__init__.py",
        base / "examples" / "__init__.py",
    ]
    for fp in init_files:
        create_file(fp, '"""Package initialization."""\n')

    files = {
        base / ".vscode" / "settings.json": get_vscode_settings(),
        Path(base / ".github" / "workflows" / "unittests.yml"): 
        (get_github_workflow()),
        base / ".gitignore": get_gitignore(),
        base / "requirements.txt": get_requirements(),
        base / "pyproject.toml": get_pyproject_toml(),
        base / ".env": get_env_file(),
        base / "Makefile": get_makefile(),
        base / "README.md": get_main_readme(proj_name),
        base / "docs" / "README.md": get_docs_readme(),
        base / "notebooks" / "README.md": get_notebooks_readme(),
        base / "scripts" / "README.md": get_scripts_readme(),
        base / "data" / "README.md": get_data_readme(),
        base / "examples" / "README.md": get_examples_readme(),
    }
    for fp, content in files.items():
        create_file(fp, content)

    print("\n✅ Project structure ready!")
    if platform.system() != "Windows":
        print("Next steps:")
        print(f"  cd {base}")
        print("  python3 -m venv venv")
        print("  source venv/bin/activate")
        print("  pip install -r requirements.txt")
    else:
        print("Next steps:")
        print(f"  cd {base}")
        print("  python -m venv venv")
        print("  venv\\Scripts\\activate")
        print("  pip install -r requirements.txt")


if __name__ == "__main__":
    main()
