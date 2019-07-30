from client import get_pokemon
import pickle

# charmander = get_pokemon("charmander")
#
# arq = open('charmander.dat', 'wb')
# pickle.dump(charmander, arq)
# arq.close()

arq = open('charmander.dat', 'rb')
pokemon = pickle.load(arq)
arq.close()

print(pokemon)