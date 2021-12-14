# Az alábbi README fájl a Mikroelektro--GKLB_INTM020-_Beadando feladat alapinformációit adja meg

## Alapinformációk
1. A választott téma: Ébresztőóra készítése.
2. Felhasznált vezérlő: Raspberry Pi Model 3 B+
3. Felhasznált eszközök: 
   * Hangszóró
   * Breadboard
   * Fizikai gomb
   * Szükséges kábelek
   * Rezisztor

## Célkitűzés
A projekt célja egy olyan ébresztőóra elkészítése amely az ébresztés- és a leállítás időpontja között eltelt időtartamot adatbázisban tárolja el. Bizonyos időközönként e-mail küldése egy megadot címre a reakcióidőkkel. Az ébresztés leállítása fizikai gombbal történjen. Az ébresztőóra rendelkezzen szundi funkcióval.

## A megvalósítás során az alábbi pontok kidolgozása történt meg
1. Raspberry beüzemelése
2. Zenelejátszás tesztelése
3. Zenelejátszás Python segítségével
4. Loop létrehozás
5. Script lejátszása Bash környezetben
6. Időzítés beállítása
7. Fizikai gomb beüzemelése
   *  Python kód a leállításhoz
   *  Szundi funkció beállítása
8. Reakcióidő megjelenítése
9. A leállítás időpontjának adatbázisba mentése
10. Az adatbázis kiküldése gmail-re meghatározott időpontban
