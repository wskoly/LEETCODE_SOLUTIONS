class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_dict = {}
        for mail in emails:
            local, domain = mail.split('@')
            local = local.split('+')[0].replace('.','')
            origin = f'{local}@{domain}'
            if origin not in email_dict:
                email_dict[origin] = 0
            email_dict[origin] += 1
        return len(email_dict)