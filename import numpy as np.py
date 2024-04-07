#initialisation des rotors

R1 = [[17,4,19,21,7,11,3,-5,7,9,-10,9,17,6,-6,-2,-4,-7,-12,-5,3,4,-21,-16,-2,-21],[10,21,5,-17,21,-4,12,16,6,-3,7,-7,4,2,5,-7,-11,-17,-9,-6,-9,-19,2,-3,-21,-4]]

R2 = [[25,7,17,-3,13,19,12,3,-1,11,5,-5,-7,10,-2,1,-2,4,-17,-8,-16,-18,-9,-1,-22,-16],[3,17,22,18,16,7,5,1,-7,16,-3,8,2,9,2,-5,-1,-13,-12,-17,-11,-4,1,-10,-19,-25]]

R3 = [[12,-1,23,10,2,14,5,-5,9,-2,-13,10,-2,-8,10,-6,6,-16,2,-1,-17,-5,-14,-9,-20,-10],[1,16,5,17,20,8,-2,2,14,6,2,-5,-12,-10,9,10,5,-9,1,-14,-2,-10,-6,13,-10,-23]]

RF = [25, 23, 21, 19, 17, 15 ,13 ,11 ,9 ,7, 5, 3, 1, -1 ,-3, -5 ,-7, -9 ,-11 ,-13 ,-15 ,-17 ,-19 ,-21 ,-23, -25]

#configuration de la clé ((R2,D)(R1,D)(R3,G))

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cue = 0

clefOrdrRotor=[2,1,3]
clefDirctRoto=[-1,-1,1]

rotors = [R1,R2,R3] #liste des rotor
pos_rot = [0,0,0] #position de chaque rotor
rotor_actif = [clefOrdrRotor[cue%3]-1,clefDirctRoto[cue%3]] #[rotor,sens]



#fonction conversion chiffre vers lettre
def chiffre_2_lettre(chiffre):
  return (alpha[chiffre])

#fonction conversion lettre vers chiffre
# "a" => "0"
#def lettre_2_chiffre(lettre):
#  return alpha.index(lettre)

def lettre_2_chiffre(lettre):
  for i in range (len(alpha)):
    if lettre == alpha[i]:
      return (i)

def rot_cir(liste,nb):
  return liste[nb:] + liste[:nb]

def rot_rotor(rotor,nb):
    return [rot_cir(rotor[0],nb),rot_cir(rotor[1],nb)]
     

def main(message):
   
  L= []
  for i in message:
    if i.upper() in alpha:
        L.append(chiffre_2_lettre(encrypt(lettre_2_chiffre(i.upper()))))
        move_rotor()
  return ("".join(L))

def encrypt(chiffre):
  #rotor 1
  chiffre += rotors[0][1][chiffre]
  #rotor 2
  chiffre += rotors[1][1][chiffre%26]
  #rotor 3
  chiffre += rotors[2][1][chiffre%26]
  # reflecteur
  chiffre += RF[chiffre%26]
  #rotor 3
  chiffre += rotors[2][0][chiffre%26]
  #rotor 2
  chiffre += rotors[1][0][chiffre%26]
  #rotor 1
  chiffre += rotors[0][0][chiffre%26]
  return (chiffre%26)

def move_rotor():
    global rotor_actif
    global cue
    pos_rot[rotor_actif[0]]+=rotor_actif[1]    
    rotors[rotor_actif[0]] = rot_rotor(rotors[rotor_actif[0]],rotor_actif[1])
   
    if abs(pos_rot[rotor_actif[0]])==26:
        pos_rot[rotor_actif[0]]=0
       
        cue += 1
        rotor_actif = [clefOrdrRotor[cue%3]-1,clefDirctRoto[cue%3]]

        #pos_rot[rotor_actif[0]]+=rotor_actif[1]  
        #rotors[rotor_actif[0]] = rot_rotor(rotors[rotor_actif[0]],rotor_actif[1])

   
    return None


print(main('OFWEFPGCUWUYQWIVQUXCYOSQBLRE'))