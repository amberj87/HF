def no_of_e(element):
  symbol = [
            'H','He',
            'Li','Be','B','C','N','O','F','Ne',
            'Na','Mg','Al','Si','P','S','Cl','Ar',
            'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe',
            'Co', 'Ni', 'Cu', 'Zn',
            'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru',
            'Rh', 'Pd', 'Ag', 'Cd',
            'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm',  'Eu',
            'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
            'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
            'Tl','Pb','Bi','Po','At','Rn']
  return(symbol.index(element)+1)

#electron_num=no_of_e('He')
#print('no of electrons '+str(electron_num))
