# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on toimia velkakirjana. Sovelluksella on useampi käyttäjä, jotka voivat merkitä velkojaan toisilleen, ja sovellus näyttää käyttäjille, kuinka paljon he ovat velkaa ja kenelle ja toisinpäin.

## Käyttäjät

Sovelluksella on aluksi vain yhdenlaisia käyttäjiä, mutta jatkokehityksenä olisi lisätä käyttäjähallinta-käyttäjä. Käyttäjähallinta-käyttäjän oikeudet olisi lisätä ja poistaa käyttäjiä, ja muuten käyttäjiä ei voisi lisätä. Ajatuksena olisi siis, että tämä korkeampien oikeuksien käyttäjä silloin verifioisi, että jokainen käyttäjä vastaa oikeaa ihmistä. Ennen tätä käyttäjien luonti toimii jollain tavanomaisemmalla tavalla.

## Perus toiminnallisuudet

 - Ennen kirjautumista
   - Käyttäjä voi kirjautua sisään tunnuksillaan
   - Käyttäjä voi luoda uuden tunnuksen (väliaikainen)

 - Kirjautumisen jälkeen
   - Käyttäjälle näytetään hänen nykyiset velat
   - Käyttäjä voi lisätä uuden velan
   - Käyttäjä voi vähentää toisen ihmisen velkaa hänelleen
   - Käyttäjä voi kirjautua ulos

## Jatkokehitysideoita

 - Käyttäjille salasanat, voivat muuttaa omaa salasanaansa
 - Käyttäjien luonti siirtyy erityiselle käyttäjänhallinta-käyttäjälle (khk)
   - Pohja khk määritetään konfiguraatiossa
   - khk voi lisätä käyttäjän, poistaa käyttäjän tai muuttaa omaa salasanaansa
     - Lisätty voi olla normi tai kh käyttäjä
 - Voi asettaa, että toinen on velkaa itselle (vähän kuin laskutus)
   - toinen hyväksyy tämän jotenkin
