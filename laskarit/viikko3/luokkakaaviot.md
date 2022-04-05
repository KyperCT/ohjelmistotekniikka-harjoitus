# viikko 3 luokkakaavioita

## tehtävä 1

```mermaid
classDiagram
Monopoli "1" -- "2" Noppa
Monopoli "1" -- "2..8" Pelaaja
Monopoli "1" -- "1" Pelilauta
Pelilauta "1" -- "40" Ruutu
Ruutu "1" -- "1" Ruutu : Seuraava ruutu
Pelaaja "1" -- "1" Pelinappula
Pelinappula "1" -- "1" Ruutu
```

## tehtävä 2

```mermaid
classDiagram
Monopoli "1" -- "2" Noppa
Monopoli "1" -- "2..8" Pelaaja
Monopoli "1" -- "1" Pelilauta
Pelilauta "1" -- "40" Ruutu
Ruutu "1" -- "1" Ruutu : Seuraava ruutu
Pelaaja "1" -- "1" Pelinappula
Pelinappula "1" -- "1" Ruutu

Aloitusruutu --> Ruutu
Vankila --> Ruutu
SattumaYhteismaa --> Ruutu
AsemaLaitos --> Ruutu
Katu --> Ruutu

class Katu {
nimi
}
class Pelaaja {
raha
}

Monopoli "1" -- "1" Vankila
Monopoli "1" -- "1" Aloitusruutu

Ruutu "1" -- "1" Toiminto
SattumaYhteismaa "1" -- "1" Kortti
Kortti "1" -- "1" Toiminto
Pelaaja "1" -- "0..1" Katu : Omistaa
Katu "1" -- "0..4" Talo
Katu "1" -- "0..1" Hotelli
```

## Tehtävä 3

```mermaid
sequenceDiagram
main ->>+ Machine: Machine()
Machine ->> FuelTank: FuelTank()
Machine ->> FuelTank: fill(40)
Machine ->> Engine: Engine(self._tank)
Machine -->>- main: #160;

main ->>+ Machine: drive()
Machine ->>+ Engine: start()
Engine ->> FuelTank: consume(5)
Engine -->>- Machine: #160;
Machine ->>+ Engine: is_running()
Engine ->>+ FuelTank: fuel_contents
FuelTank -->>- Engine: 35
Engine -->>- Machine: True
Machine ->>+ Engine: use_energy()
Engine ->> FuelTank: consume(10)
Engine -->>- Machine: #160;
Machine -->>- main: #160;


```
