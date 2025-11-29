import re

def validate_email(email: str, regex = r"\b[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*\.)+(?:com|org|ua|pl|ru)\b") -> bool:
    result = str(re.search(regex, email))
    print(result)
    if len(result) > 0 and "@" in result:
        return True
    else: return False



if __name__ == "__main__":
    print('support@my-site.org' == 'support@my-site.org')
