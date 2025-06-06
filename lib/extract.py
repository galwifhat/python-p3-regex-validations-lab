import re
# Extract Username and Domain Separately

email_regex = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*)"


pattern = re.compile(
    r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*)"
)

emails = "Send reports to john.doe@gmail.com and help@support.mail.google.co.uk"

matches = pattern.findall(emails)

for username, domain in matches:
    print("Username:", username)
    print("Domain:", domain)
    print("------")
