import re
email_address = r"[A-Za-z][A-Za-z0-9]*(\.[A-Za-z0-9]+)*@[A-Za-z0-9]+\.[a-z]{2,}"
email_regex = re.compile(email_address)

# r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*"


#  [a-zA-Z0-9._%+-]+ ->  Username: letters, digits, dot ., underscore _, percent %, plus +, dash -
# [a-zA-Z0-9.-]+ ->  Domain: letters, digits, dots, dashes (e.g., mail.google)
# \.[a-zA-Z]{2,} ->  First top-level domain (e.g., .com, .org)
# (?:\.[a-zA-Z]{2,})* -> Optional second/third domain (e.g., .co.uk, .gov.in)

# example
email_regexx = re.compile(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*"
)

text = """
Valid:
- john.doe@gmail.com
- jane_doe123@support.mail.google.com
- team@university.ac.in
- hello+promo@my-company.co.uk

Invalid:
- justtext
- @no-user.com
- user@.nodomain
"""

matches = email_regexx.findall(text)
print("Valid Emails Found:")
for match in matches:
    print("-", match)
