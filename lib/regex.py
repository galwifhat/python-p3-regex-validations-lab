import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John Cena, Anya Taylor-Joy, D'Angelo"
name_regex = re.compile(r"[A-Z][']*([A-Za-z][ \-']?)+")

# [A-Z][a-z]+(?:['\-][A-Z][a-z]+)?
# r"^[\w\.-]+@[\w\.-]+\.\w+$"


phone_number = r"\(?\d{3}\)?[- ]?\d{3}-?\d{4}"
phone_regex = re.compile(phone_number)

# phone_number = r"\({0,1}[\d]{3}\){0,1}[- ]{0,1}[\d]{3}-{0,1}[\d]{4}"

email_address = r"[A-Za-z][A-Za-z0-9]*(\.[A-Za-z0-9]+)*@[A-Za-z0-9]+\.[a-z]{2,}"
email_regex = re.compile(email_address)

# r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*"


#  [a-zA-Z0-9._%+-]+ ->  Username: letters, digits, dot ., underscore _, percent %, plus +, dash -
# [a-zA-Z0-9.-]+ ->  Domain: letters, digits, dots, dashes (e.g., mail.google)
# \.[a-zA-Z]{2,} ->  First top-level domain (e.g., .com, .org)
# (?:\.[a-zA-Z]{2,})* -> Optional second/third domain (e.g., .co.uk, .gov.in)
