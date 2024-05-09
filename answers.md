### 1. How many SU-25s’s have been delivered to the Russian Air Force?

no records

### 2. What type of missile is a RVV-MD?

```
match(e:Equipment)-[:ROLE]->(c:Classification)  where e.label="RVV‐MD" return c.label;

```

"Anti-aircraft"
"Combat/offensive"

### 3. What is the Max Fuel Weight of the SU-25s?

no records

### 4. Where are the 22nd Fighter Aviation Regiment of the Russian air force located?


```
match(o:Organization)-[r]->(l:Location)  where o.label="22nd Fighter Aviation Regiment" return l.label

```

"Russian Federation"

### 5. What is a AB-250?


```
match(e:Equipment)-[r]->(c:Classification)  where e.label="AB-250" return c.description;

```

"General bombardment weapons such as unguided rocket systems, not necessarily targeted at destroying specific pieces of equipment."

"Providing offensive capabilities for engaging the enemy and causing damage or disruption. Includes conventional weaponry as well as electronic forms of attack"

"The piece of equipment/system, when operational, operates while airborne"

"Operates from an airborne platform targeting/surveilling sea- (surface) or land-based targets"

"Covering weapons and countermeasures. To include, but not limited to guns, missiles, rockets, bombs torpedoes, mines, as well as munitions and physical countermeasure launchers"

"Air dropped munition, may have guidance and flight control surfaces but no propulsion"

"Government run organisations that fall under the military chain of command"


### 6. What is the role of a SU-35s?


```
match(e:Equipment)-[r:ROLE]->(c:Classification)  where e.label="Su-35S" return c.description;

```

"Aircraft used to deliver large bomb loads for strategic or tactical purposes. Can deploy stand-off weapons (such as cruise missiles) as well as precision guided weapons or conventional bombs. Weapons usually carried in an internal weapons bay. May have defensive aids suites but would have very limited capability in air-to-air combat."

"Providing offensive capabilities for engaging the enemy and causing damage or disruption. Includes conventional weaponry as well as electronic forms of attack"

"Aircraft used for air-to-air combat, the most capable aircraft would be designed to oppose enemy fighters and would range from  air supremacy aircraft (used to totally nullify an opposing force) through to air superiority aircraft (used to seize control of airspace). Multirole fighters are capable of air-to-air combat but are not optimised for it."

### 7. List the events the SU-35S has been involved with in Ukraine?

```
match(e:Event)-[r]->(l:Location) where l.label="Ukraine" return e.description;

```

"A Russian Su-35S appears to have been shot down in the KHERSON OBLAST. Ukrainian officials have claimed responsibility for the shootdown while some pro-Russian sources are reporting the aircraft was downed by Russian air defences. Russian forces deployed an Mi-24 to conduct search and rescue following the shootdown."

"The Ukrainian Ministry of Defence reports that Russian Su-35 were used to conduct strikes against Ukrainian targets in KLYNOVE. The Ukrainians also claim Orlan-10 were used to provide the aircraft with targeting data."

"The Ukrainian Ministry of Defence reports that Russian Su-35 were used to conduct strikes against Ukrainian targets in SOLEDAR. The Ukrainians also claim Orlan-10 were used to provide the aircraft with targeting data."

"The Ukrainian Ministry of Defence reports that Russian Su-35 were used to conduct strikes against Ukrainian targets in BAKHMUT. The Ukrainians also claim Orlan-10 were used to provide the aircraft with targeting data."

"The Ukrainian Ministry of Defence reports that Russian Su-35 were used to conduct strikes against Ukrainian targets in VOVCHOYARIVKA. The Ukrainians also claim Orlan-10 were used to provide the aircraft with targeting data."

"The Ukrainian Ministry of Defence reports that Russian Su-35 were used to conduct strikes against Ukrainian targets in SOLEDAR. The Ukrainians also claim Orlan-10 were used to provide the aircraft with targeting data."


### 8. What are the Synonyms of the SU-35S?

no records

### 9. What is the NATO name for the SU-35S?

Flanker-E

### 10. What two entities operate the SU-35S?

```
match(e:Equipment)-[r:OPERATED_BY]->(o:Organization)  return o.label as entities limit 2;

```

"6th Air Brigade"

"929th State Flight Test Centre "

### 11. How long is the SU-35S?

```
match(e:Equipment)-[r]->(s:Specification) where e.label="Su-35S" and s.label="Length, overall" return s.rendered_output as length;

```

"21.90 m (71 ft 10 1/4 in)"

### 12. Who makes the SU-35S?

```
match(o:Organization)-[r:MANUFACTURES]->(e:Equipment)  return o.label as manufacturer;

```

"JSC Aviation Holding Company Sukhoi"

### 13. What are the navigation systems used by the SU-35S?

no records

### 14. How many different types of missiles can be used by the SU-35S?

```
return count{match(e:Equipment)-[:EQUIPMENT_TYPE]->(s:Classification) where s.label="Missile"} as missiles;

```
14      

### 15. What is the SU-35S?

```
match(e:Equipment)-[:EQUIPMENT_TYPE]->(s:Classification) where e.label="Su-35S" return s.description as su35;

```
"Fixed-wing aircraft that uses jet engines for propulsion (e.g.. turbojet, turbofan)"

"Aircraft which for the majority of its flight achieves lift by being moved through the air generating a pressure differential using the shape of the aircraft's structure, it may hover for short periods using ducted thrust for take off landing and manoeuvring."

"Vehicle or vessel a designed to carry people, and/or cargo, and/or equipment, such as an installed weapon"


### 16. What unit operates the SU-35S in China?

```
match(e:Equipment)-[r]->(o:Organization) where e.label="Su-35S" match(o)-[t]->(l:Location) where l.label="China" return o.label as unit

```

"6th Air Brigade"

### 17. How many exercises has the SU-35S been involved in?

```
return count{ match(e:Event) where e.description contains "Su-35S" and e.description contains "exercise" return e} as times

```

17  

### 18. List the Specifications of the SU-35S.

```
match(e:Equipment)-[r]->(s:Specification) where e.label="Su-35S" return s.label as Specifications;

```

"Rate of climb"

"Wing span"

"Max T-O weight"

"Max payload"

"Max level speed"

"Max level speed"

"Max wing loading"

"Weight empty"

"Range"

"Landing run"

"Max level Mach number"

"Wing aspect ratio"

"T-O run"

"g limits"

"Range"

"Max T-O weight"

"Range"

"Length, overall"

"Height, overall"

"Max fuel weight"

"Max thrust loading"

"Max fuel weight"

"Wing span"

"Service ceiling"

"Gross wing area"

"Max level Mach number"

### 19. In total how many SU-35S’s are in service in the world?

```
match(e:Inventory)-[r]->(t:Equipment) with collect(toInteger(e.total_in_service_inventory_total)) as list return apoc.coll.sum(list);
```

135.0 


### 20. What Russian division is the 23rd Fights Aviation Regiment part of?

```
match(o:Organization)-[:BRANCH]->(c:Classification) where o.label="23rd Fighter Aviation Regiment" return c.label;
```

"Air Force"



"Based on our understanding of the data and application of the database Neo4j, we created corresponding scripts to query for each question and got the answers. Please check the pdf which contains scripts and answers."