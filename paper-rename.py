#!/usr/bin/env python3
#
# File: paper-rename.py
#
from tika import parser

pdfFile = "d:/ws/masters/research/current/00469437.pdf"

raw = parser.from_file(pdfFile)
print(raw["content"])
pass