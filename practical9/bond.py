def jbond(birth):
    bond_actors={range(1973, 1987):"Roger Moore",range(1987, 1995):"Timothy Dalton",range(1995, 2006):"Pierce Brosnan",range(2006, 2022):"Daniel Craig"}
    #creating a dictionary with a range to match
    birth_year=int(birth)#converting string to a actual number
    for year_range,actor in bond_actors.items():
        if birth_year in year_range:
            return actor
user_input=input("Your birth year:")
favorite=jbond(user_input)
print("Your favorite bond actor is",favorite)