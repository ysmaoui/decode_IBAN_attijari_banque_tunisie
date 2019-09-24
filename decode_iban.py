import re
import sys


class attijari_account:
    IBAN_LENGTH = 24

    def __init__(self, IBAN):
        self.IBAN = IBAN.replace(' ', '').replace('\t', '')
        if self.checkValidity():
            self.decode()
        else:
            print("Invalid IBAN")
            sys.exit(1)

    def decode(self):
        self.countrycode = self.IBAN[:4]
        self.centralBank_bankcode = self.IBAN[4:6]
        self.centralbank_agencycode = self.IBAN[6:9]
        self.internal_agencycode = self.IBAN[9:12]
        self.account_number = self.IBAN[12:22]
        self.internal_key = self.IBAN[21]
        self.centralbank_key = self.IBAN[22:24]

    def checkValidity(self):
        # Reference: https://rosettacode.org/wiki/IBAN#Python
        # Ensure upper alphanumeric input.
        iban = self.IBAN.replace(' ', '').replace('\t', '')
        if not re.match(r'^[\dA-Z]+$', iban):
            print("ERROR: Format is not matching, only country code and digits are allowed")
            return False
        # Validate country code against expected length.
        if len(iban) != attijari_account.IBAN_LENGTH:
            print("ERROR: the length of the given IBAN is not correct")
            return False
        # Shift and convert.
        iban = iban[4:] + iban[:4]
        digits = int(''.join(str(int(ch, 36)) for ch in iban))  # BASE 36: 0..9,A..Z -> 0..35
        if not digits % 97 == 1:
            print("ERROR: validation by IBAN key failed")
            return False
        else:
            return True

if __name__ == '__main__':

    arguments = sys.argv
    if len(arguments) == 1:
        print("Please provide IBAN")
        sys.exit(1)
    else:
        iban = sys.argv[1]
    account = attijari_account(iban)

    print("Code pays: %s" % account.countrycode)
    print("Code banque à la banque centrale: %s" % account.centralBank_bankcode)
    print("Code agence à la banque centrale: %s" % account.centralbank_agencycode)
    print("Code agence interne: %s" % account.internal_agencycode)
    print("Numéro de compte: %s" % account.account_number)
    print("Clé interne: %s" % account.internal_key)
    print("Clé banque centrale: %s" % account.centralbank_key)

    print("=============ajout beneficaire attijari=========")
    print("Agence: %s  N° Compte: %s  Clé: %s" %
          (account.internal_agencycode, account.account_number, account.internal_key))
