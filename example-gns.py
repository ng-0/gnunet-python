#!/usr/bin/python3

import gnunet.gns

results = gnunet.gns.lookup("www.gnu", "JK55QA8JLAL64MBO8UM209KE93M9JBBO7M2UB8M3M03FKRFSUOMG", "A", True)

for r in results:
  print("Got result from gns")
  print("  record_type     == %s" % repr(r.record_type))
  print("  data            == %s" % repr(r.data))
  print("  expiration_time == %s" % repr(r.expiration_time))
  print("  private         == %s" % repr(r.private))
  print("  pending         == %s" % repr(r.pending))
  print("  shadow          == %s" % repr(r.shadow))

