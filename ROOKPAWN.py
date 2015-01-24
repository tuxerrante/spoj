# http://www.spoj.com/problems/ROOKPAWN/
from collections import defaultdict  

# Hopcroft-Karp bipartite max-cardinality matching and max independent set
# David Eppstein, UC Irvine, 27 Apr 2002

def bipartiteMatch(graph):
	'''Find maximum cardinality matching of a bipartite graph (U,V,E).
	The input format is a dictionary mapping members of U to a list
	of their neighbors in V.  The output is a triple (M,A,B) where M is a
	dictionary mapping members of V to their matches in U, A is the part
	of the maximum independent set in U, and B is the part of the MIS in V.
	The same object may occur in both U and V, and is treated as two
	distinct vertices if this happens.'''
	
	# initialize greedy matching (redundant, but faster than full search)
	matching = {}
	for u in graph:
		for v in graph[u]:
			if v not in matching:
				matching[v] = u
				break
	
	while 1:
		# structure residual graph into layers
		# pred[u] gives the neighbor in the previous layer for u in U
		# preds[v] gives a list of neighbors in the previous layer for v in V
		# unmatched gives a list of unmatched vertices in final layer of V,
		# and is also used as a flag value for pred[u] when u is in the first layer
		preds = {}
		unmatched = []
		pred = dict([(u,unmatched) for u in graph])
		for v in matching:
			del pred[matching[v]]
		layer = list(pred)
		
		# repeatedly extend layering structure by another pair of layers
		while layer and not unmatched:
			newLayer = {}
			for u in layer:
				for v in graph[u]:
					if v not in preds:
						newLayer.setdefault(v,[]).append(u)
			layer = []
			for v in newLayer:
				preds[v] = newLayer[v]
				if v in matching:
					layer.append(matching[v])
					pred[matching[v]] = v
				else:
					unmatched.append(v)
		
		# did we finish layering without finding any alternating paths?
		if not unmatched:
			unlayered = {}
			for u in graph:
				for v in graph[u]:
					if v not in preds:
						unlayered[v] = None
			return (matching,list(pred),list(unlayered))

		# recursively search backward through layers to find alternating paths
		# recursion returns true if found path, false otherwise
		def recurse(v):
			if v in preds:
				L = preds[v]
				del preds[v]
				for u in L:
					if u in pred:
						pu = pred[u]
						del pred[u]
						if pu is unmatched or recurse(pu):
							matching[v] = u
							return 1
			return 0

		for v in unmatched: recurse(v)
# -------------------------------------------------------------------

left, right = 0, 0
mV = []
m  = []
e = defaultdict(list)


def readRow(s, r, col, i):
   # matrice dei vettori (L,R)
   global m, mV, left
   j = 0;
   A = 0
   for char in s:
      #  --- leggi le sequenze di A per riga
      if char =='A':
         #  aggiorna valore sinistro della coppia = left
         mV[i][j][0] = left
         A += 1   # ho letto almeno una A
                  
      if (char == 'P' or j==col-1) and A>0:
         left += 1   #  crea un nuovo vertice sinistro
         A = 0      
      
      m[i][j] = char    # copio la matrice d'input
      j += 1            # avanza di col nella mV

def redCol(m, row, col):
   global mV, right
   A, i, j = 0, 0, 0
   
   for c in xrange(col):
      A = 0
      for r in xrange(row):
         char = m[r][c]
         if char == 'A':
            mV[r][c][1] = right
            
            mLeft  = mV[r][c][0]
            mRight = mV[r][c][1]         
            if mLeft!=-1 and mRight!=-1:
               e[mLeft].append( mRight )
            
            A += 1
            
         if (char=='P' or r==row-1) and A>0:            
            right += 1
            A = 0
'''
#  ----------  create bipartite graph  ---------         
def createBG(row, col):          
   global e   
   #  uso le tuple in mV per creare archi diretti
   for r in xrange(row):
      for c in xrange(col):
         mLeft  = mV[r][c][0]
         mRight = mV[r][c][1]         
         if mLeft!=-1 and mRight!=-1:
            e[mLeft].append( mRight )  # da fare in readcol ?!
'''   

def start():
   global mV, m, e 
   
   while True:
      num_test = int(raw_input())
      
      for i in range(num_test):
         r, c = [int(i) for i in raw_input().split()]
         
         # --- build intial matrix
         mV =  [[[-1,-1] for col in xrange(c)] for line in xrange(r)]
         m  =  [['' for col in xrange(c)] for line in xrange(r)]
         i = 0
         for row in range(int(r)):
             readRow( raw_input().split(), r, c, i)
             i+=1

         e = defaultdict(list)
         redCol(m, r, c)
         
         #createBG(r, c)
         
         # --- search for paths
         #  ----------  OUTPUT   ----------
         

         #print "\n input m:\t", m,"\n left V:\t", left,"\n right V:\t",right#,"\n graph m:", mV,"\n edges:", e.items()

         match, _, _ =  bipartiteMatch( e )
         #print " Edges matched:\t", match,"\n Match:\t",len( match )
         
         print len( match )

      return

if __name__ == '__main__': 
    start()






