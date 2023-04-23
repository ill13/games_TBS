# DopeWars..for kids

Simple extensible framework where traditional dopwars items are replaced with kid friendly items



bank: piggy bank
drugs: cards/candy/collectibles
locations: N but places like gym class, cafeteria, playground, classroom, hallway
loan shark: none or "school bully"
police: none or "teachers"

- 30 turns [7 maybe?]
- Randomly prices go up.
- Prices fluctuate, within a range  
  - Regionally, one item will always cost more or less
    - Like "playground", chocolate is always n+x and gum is n-y.
    - However, in "gym class", chocolate is always n-x and gum is n+y. Each location has a price modifier



Clicker so no real loss?


game setup:

    Start with $MONEY
    Start at $RANDOM_LOCATION



game loop:

    Generate $RANDOM_PRICES
    Set $RANDOM_PRICES

    Update Display
    - Location
    - Money
    - Inventory
    - Price List / Grid

    Ask for input

    Do input

    Move or stay will end turn
    - Could add an end turn button


    Calculate numbers

