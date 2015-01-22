#!/usr/bin/env python

import sys, numpy

if len( sys.argv ) < 3 :
    sys.exit( 'missing args: input-file table-file' )

x = 1
y = 1
xmax = 1
table = numpy.zeros((43,43))

for line in open( sys.argv[1] ) :
    for element in [float(e) for e in line.split() ] :
        table[ y ][ x ] = element
        if x < xmax :
            x += 1
        else :
            x = 1
            y += 1
            xmax += 1

num_to_name = {}
for line in open( sys.argv[2] ) :
    num, name = line.split('.')
    num_to_name[ int( num ) ] = name.strip().replace( ' ', '_' )

print "\
@base <http:// <http://rhizomik.net/ontologies/>example.org/\n\
<http://example.org/data>intelligenceModel#> .\n\
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n\
"

for x in range( 1, 43 ) :       
    for y in range( 1, 43 ) :
        if table[x][y] > 0.0 :
            print ':' + num_to_name[ x ] + ' :similarConcept [ rdf:value :' + num_to_name[ y ] + '; :weight ' + str( table[x][y] ) + ' ].'
    print
