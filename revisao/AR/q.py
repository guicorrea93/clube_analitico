import sqlite3, sys
c = sqlite3.connect("file:db/futebol.db?mode=ro", uri=True)
for r in c.execute(sys.argv[1]): print(*r, sep="\t")
