# IS-105_2016_Gruppe13
Repository for gruppe 13, UiA.

Hvis du skal laste opp f.eks. en fil, last opp til develop-branch først. Master branch er kun til ferdige oppgaver.
Hvis du ønsker å laste opp til develop-branch med cmd/git bash, MÅ du endre på hvilken branch du bruker. Dette gjøres ved å skrive følgende:

```sh
git checkout develop
```

Legg ønsket fil i lokal mappe og skriv følgende i cmd:
```sh
- git add --all
- git commit -m "Kommentar her"
- git push origin develop
```

Hvis noen gjør endringer i develop-branchen må den lokale mappen på din PC synkroniseres på nytt. Skriv:
```sh
git pull
```
