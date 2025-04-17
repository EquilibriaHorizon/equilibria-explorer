from observer import app, config
import oxenmq
config.oxend_rpc = oxenmq.Address('ipc:///home/sstar/.equilibria/testnet/equilibria.sock')
 