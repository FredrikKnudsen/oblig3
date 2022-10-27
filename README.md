# oblig3

Jeg la til GitHub brukeren min til PyCharm, og lagde et repository gjennom PyCharm.
Deretter commitet jeg, og pushet oblig 2 filene mine til repositoriet. 
Jeg gikk så til GitHub siden min, og fant det nye repositoriet. Trykket på "Actions", scrolla ned til "Continuous integration" og trykket configure på Python package.
Dette lagde en fil for meg, som jeg commita til repositoriet. 
Nå har jeg filene fra oblig 2 og den nye .github mappa i repositoriet mitt. 

Jeg prøvde å se om testene mine funket, det gjorde de ikke.
Så jeg gjorde noen endringer til mappe strukturen i PyCharm. 
Commita på nytt og sjekka om testene funka, funket fortsatt ikke. 
Deretter prøvde jeg å gå inn i .github mappa, og en endring, fra python-version: ["3.8", "3.9", "3.10"] til python-version: ["3.9"], fordi det er den versjonen som jeg bruker.
Funket fortsatt ikke. 
Jeg fikk Error, med exit code 5.
Så med noen forsøk til, og litt feilsøking, så jeg at fila med testene mine het: test.py, og endret navnet på den til test_test.py, og commita. Og alt funket. 
