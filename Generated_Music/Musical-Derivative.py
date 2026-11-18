import math
from ntpath import join

"""
By using the Sieve of Eratosthenes, this algorithm generates
a list of prime numbers up to a given limit corresponding to a multiple of 4 (Carrure).
We start by 5 since 3 = 0 (mod 3) and 2 = -1 (mod 3).
The primes are coded in (modulo 3 - 1) this gives a binary sequence.
"""

def Eratosthenes(N):
	#Filling numbres from 2 to N
	L=[]
	for k in range(2,N+1):
		L.append(k)
	#Removing compound numbersup to N
	counter = 0
	while (counter < len(L)):
		i = L[counter]
		j=i
		while (i*j <= N):
			if (i*j in L):
				L.remove(i*j)
			j=j+1
		counter = counter + 1
	return(L)

def PrimeList_5(N):
	# We need numbers starting from 5 for musical reasons exmplained above
	L=[]
	n=N
	while(len(L)<N):
		L=[]
		L=Eratosthenes(n)
		#Remove 2,3 to start from 5
		L.remove(2)
		L.remove(3)
		n=n+1
	return(L)

Carrure = 16
L=PrimeList_5(4*Carrure)
#print(L)

L_Mod=[]
for x in L:
    L_Mod.append(x%3-1)
#print(L_Mod)

L4=[]

# Organise by package of 4 elements
for i in range(0, len(L_Mod), 4):
    L4.append(L_Mod[i:i+4])

#print(L4)

#Generate musical notes
"""
Let's us now consider 0 as silence and 1 as a note.
We now count the numbers of 1 (notes) and generate
again la list of primes of this number of 1s and code
them in mod 12 (chromatic scale)
"""

n1=0
for x in L_Mod:
	if not(x==0): 
		n1=n1+1

#print(n1)

Notes=PrimeList_5(n1)

Notes12=[]

for n in Notes:
	Notes12.append(n%12)

"""
For the same reasons as for rhythm, 
we omit 2 and 3 because we remark a 
'dance' of an arpeggio of G7^-5 chord

5, 7, 11, 1, 
5, 7, 11, 5, 
7, 1, 5, 7, 
11, 5, 11, 1, 
7, 11, 1, 7, 
11, 5, 1, 5, 
7, 11, 1, 5, 
7, 11, 5, 7, 
5, 7]
"""

# We now 'inject' notes over the rhythms


counter=0
while counter < len(Notes12):
    for x in L4:
        for y in range(4):
            if x[y] == 1:
                x[y] = Notes12[counter]
                counter += 1
            else:
                x[y] = 'r'

# Now we generate a musical code for Lilypond
NoteNames=[[0,'c'],[1,'des'],[2,'d'],[3,'es'],[4,'e'],[5,'f'],[6,'ges'],[7,'g'],[8,'as'],[9,'a'],[10,'bes'],[11,'b']]

"""
Now we generate a musical code for Lilypond
[5, 'r', 7, 'r'] will transform into a list of strings 
This list will be writtent under the name of the musical piece in a Lilypond file (prime_music.ly).
"""

L4_to_file=[]
for L4a in L4:
	L4_mus=[]
	for x in L4a:
		if x == 'r':
			L4_mus.append(x)
		else:
			for y in NoteNames:
				if x == y[0]:
					L4_mus.append(y[1])
	
	s=' '.join(L4_mus)
	# we need to instert \8 after the first element
	s = s.replace(' ', '8 ', 1)
	L4_to_file.append(s)

"""
We now generate a musical code for Lilypond
[5, 'r', 7, 'r'] will be printed to a file
"""

#The file starts with the caracter { and ends with the caracter }
with open("Score/prime_music.ly", "w") as f:
    f.write("{\n")

for c in L4_to_file:
    with open("Score/prime_music.ly", "a") as f:
        f.write(c + "\n")

with open("Score/prime_music.ly", "a") as f:
    f.write("}\n")