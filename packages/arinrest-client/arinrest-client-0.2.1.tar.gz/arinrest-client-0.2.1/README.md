# ARINREST LIB

The purpose of this package is to manage and query resources hosted by ARIN.
ARIN has 3 different services that you can query and manage records on. 

- whois, only the RDAP interface is supported by this library
- IRR, This still needs to be implemented 
- RPKI, The reason I start this library os to manage ROA objects hosted in
  ARINs repository.

## Usage
The entry point into this library is the `ArinRest` class. The class only takes
an API Key from ARIN to instantiate.

```python
from arinrest import ArinRest
from arinrest.rpki import ROA

arinclient = ArinRest('your-api-key-here')

# arinclient.rdap() creates a rdap session with ARIN
whois_client = arinclient.rdap()

# You can manage resources in the IRR and RPKI endpoints so currently the classes
# require an API key to instantiate them.

# create an rpki session with signing capabilities, private key required
rpki_client = arin.rpki("/path/to/private/key")

# add a ROA to the queue to be submitted as well as signing it.
rpki_client.add_roa(roa: ROA)

# submit the ROA to ARIN
rpki_clinet.submit_roas()

```
## TODO
Break out the rpki client and the ROA object into 2 separate classes.

 ~~- ROA object will have getters and setters for the attributes with validation~~
  ~~of values.~~

- rpki client will have the connection and url's needed to submit and fetch
  information about ROAs.


## Resources
Manually signed ROA: Implemented in Python
[ARIN Manually signed ROA](https://www.arin.net/resources/manage/rpki/roa_request/#manually-sign)

RSA Signing with cryptography python lib
[RSA](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#signing)
