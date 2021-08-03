import re, pyperclip as pc


def main():
    # get data from clipboard
    data = pc.paste()

    # regex the phone
    phoneRegex = re.compile(
        r"""
        # area code
        ((\(\d{3}\)|    # w/ parens
        \d{3}-)         # w/o parens

        \d{3}-          # middle three digits
        \d{4})          # last 4 digits
    """,
        re.VERBOSE,
    )
    phoneRegexOutput = phoneRegex.findall(data)
    phoneNumbers = list()
    for i in phoneRegexOutput:
        phoneNumbers.append(i[0])

    # regex the email
    emailRegex = re.compile(r"\S+@\w+\.\w+")
    emailRegexOutput = emailRegex.findall(data)
    emails = list()
    for i in emailRegexOutput:
        emails.append(i)

    # save numbers and clipboard to clipboard
    pc.copy("\n".join(phoneNumbers) + "\n".join(emails))


if __name__ == "__main__":
    main()
