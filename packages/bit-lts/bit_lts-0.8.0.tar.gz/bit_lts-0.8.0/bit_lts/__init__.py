from bit_lts.format import verify_sig
from bit_lts.network.fees import set_fee_cache_time
from bit_lts.network.rates import SUPPORTED_CURRENCIES, set_rate_cache_time
from bit_lts.network.services import set_service_timeout
from bit_lts.wallet import Key, PrivateKey, PrivateKeyTestnet, wif_to_key, MultiSig, MultiSigTestnet

__version__ = '0.8.0'
