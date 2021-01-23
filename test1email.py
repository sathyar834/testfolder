from dns import resolver

records = dns.resolver.query('scottbrady91.com', 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)