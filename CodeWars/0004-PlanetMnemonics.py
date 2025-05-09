# def is_planet_mnemonic_correct(solar_system, mnemonic):
#     mnemonic = [word[0] for word in mnemonic.split()]
#     planets = list(filter(lambda planet: planet != "Asteroid", solar_system))
    
#     if len(mnemonic) > len(planets) or len(mnemonic) != len(planets):
#         return False
    
#     for idx in range(len(planets)):
#         if planets[idx][0] != mnemonic[idx]:
#             return False
#     return True

# Initial solution above -----------------------------

# convert to a string, the initial letters of each planet, excluding "Asteroids"
# Convert to a string, the initial letters of each word in the mnemonic
# Return the result of comparing the two strings.

def is_planet_mnemonic_correct(solar_system, mnemonic):
    solar_acronym = "".join([x[0] for x in solar_system if x != "Asteroid"])
    mnemonic_acronym = "".join(x[0] for x in mnemonic.split())
    
    return solar_acronym == mnemonic_acronym


testData = [[["Earth", "Jupiter", "Asteroid", "Asteroid", "Mercury", "Asteroid", "Saturn"], "Even Jaguars Make Spaghetti"], [
    [], "Hello"], [[], ""], [["Asteroid", "Asteroid", "Asteroid", "Asteroid", "Asteroid", "Asteroid"], ""], [["Mars", "Jupiter"], "My Shoes"], [["Mercury", "Asteroid", "Saturn"], "My Shoes"]]

for data in testData:
    print(is_planet_mnemonic_correct(data[0], data[1]))