import json

PARTIE = ["PO", "PSL", "PiS", "RPL", "SLD", "MN"]

with open("wyniki2011.json", encoding="utf-8") as f:
    data = json.load(f)

print("nr okregu | nazwa ", end="")
for i, partia in enumerate(PARTIE):
  print(" | ", partia, end="")
print(" | Last | Lost | Różnica w procentach")
print("\n")

ostat_wyniki = {}
blisko = []
for okreg in data:
    ilorazy = []
    mandaty = int(okreg["Mandaty"])
    dzielnik = 1

    while len(ilorazy) < mandaty * len(PARTIE):
        for partia in PARTIE:
            wyniki_proc = okreg[partia]
            
            if wyniki_proc > 5.0 or partia == "MN":
                ilorazy += [(partia, wyniki_proc / dzielnik, dzielnik)]
        dzielnik += 1

    czesc_wyniki = sorted(ilorazy, key=lambda el: el[1], reverse=True)
    
    wyniki = czesc_wyniki[:mandaty]
    nazwy = [r[0] for r in wyniki]
    okreg_wyniki = {n: nazwy.count(n) for n in nazwy}

    print(okreg["Okreg"], " | ", okreg["Nazwa"], end="")
    for partia in PARTIE:
        if partia in okreg_wyniki:
         print(" | ", okreg_wyniki[partia], end="")
        else:
            print(" | ", 0, end="")
    last = czesc_wyniki[mandaty-1]
    lost = min(filter( lambda el: el[1]<last[1] and el[0] != last[0],czesc_wyniki),key=lambda el: (last[1] - el[1])*min(last[2],el[2]))        
    roznica = (last[1]-lost[1]) * min(last[2], lost[2])
    blisko+=[(okreg["Nazwa"],last[0],lost[0],roznica)]
    print(" | ", last[0], " | ",lost[0]," | ","{0:.2f}".format(roznica) )


print("Okręg | Last | Lost | Różnica")
for a,b,c,d in sorted(blisko, key=lambda el: el[3]):
    print(a ," | ", b , " | ", c, " | ", "{0:.2f}".format(d))
