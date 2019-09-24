# Decode Attijari bank IBAN

a simple script that decodes a given IBAN from the Attijari bank (Tunisia)

## Requirements

* Python 3

## How to use

```shell
python3 decode_iban.py "[IBAN_number]"
```

* example:

    ```shell
    python3 decode_iban.py "TN59 04 123456789123456789"
    ```


## sample output

```sh
Code pays: TN59
Code banque à la banque centrale: 04
Code agence à la banque centrale: 123
Code agence interne: 123
Numéro de compte: 1234567891
Clé interne: 1
Clé banque centrale: xx
=============ajout beneficaire attijari=========
Agence: 123  N° Compte: 1234567891  Clé: 1
```

## References

The code for checking the validation of the IBAN was taken from REF: [<https://rosettacode.org/wiki/IBAN#Python>]
