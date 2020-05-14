DataDictionary

The physical data model is having star schema

fact_temp(start_time) -> time table(start_time)
fact_temp(City) -> city table(City)

Time table
1. start_time - DateType notnull primary key - date on which the temperature was measured
2. month - integer  notnull - month on which the temperature was measured
3. year - integer  notnull - year on which the temperature was measured

City Table
1. City - string notnull primary key - avg temperature of the City
2. State - string notnull - State in which the City is locate
3. Country - string not null - Country in which the State is located

fact_temp
1. start_time - string notnull primary_key - date on which the temperature was measured
2. City - string notnull - City in which the temperature was measured 
3. avg_temp_fahrenheit - integer notnull - avg temperature in fahrenheit
4. avg_temp_celcius - integer notnull - avg temperature in celcius