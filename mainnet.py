from observer import app, config
import oxenmq

config.oxend_rpc = oxenmq.Address('tcp://127.0.0.1:9231')
