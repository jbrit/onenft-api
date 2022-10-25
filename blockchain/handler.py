from web3 import Web3

from blockchain.abis import NFT_MARKET_ABI, OWNABLE_NFT_ABI
from utils import get_json_from_ipfs

w3 = Web3(Web3.HTTPProvider("https://api.s0.b.hmny.io"))



nft_market_contract = w3.eth.contract(address="0xEEF20045d1CC0A94D6D4Ee02dbB677FfFE45D9B9", abi=NFT_MARKET_ABI)

def get_nft_contract(address):
  address = Web3.toChecksumAddress(address)
  return w3.eth.contract(address=address, abi=OWNABLE_NFT_ABI)

class OwnableNFT:
  def __init__(self, address):
    self.address = Web3.toChecksumAddress(address)
    self.contract = get_nft_contract(address)

  def get_owner(self, token_id):
    return self.contract.functions.ownerOf(token_id).call()

  def get_token_uri(self, token_id):
    return self.contract.functions.tokenURI(token_id).call()

  def get_token_count(self):
    tokens = None

    # check if the contract starts at 0
    try:
      self.get_owner(0)
      tokens = [0, 0]
    except:
      # check if the contract starts at 1
      try:
        self.get_owner(1)
        tokens = [1, 1]
      except:
        return tokens

    # check the contract address till we find an exception for the end
    try:
      while True:
        self.get_owner(tokens[1] + 1)
        tokens[1] += 1

        # maximum of 100 tokens
        if tokens[1] == 100:
          return tokens

    except:
      return tokens
      
  def get_tokens(self):
    tokens = self.get_token_count()
    return [] if tokens is None else [ self.get_token(i) for i in range(tokens[0], tokens[1] + 1)]

  def get_token(self, token_id):
    return {"id": token_id, "data": get_json_from_ipfs(self.get_token_uri(token_id))}
