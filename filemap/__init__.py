"""
filemap - Map files and folders to markdown documentation

A tool for collecting files, visualizing folder structures,
and generating comprehensive markdown documentation.
"""

__version__ = '0.1.0'

from .core import (
    collect_files,
    get_folder_structure,
    read_file_content,
    generate_markdown
)