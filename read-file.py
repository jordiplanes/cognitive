#!/usr/bin/env python

import sys, numpy

def read_input_file( filename ) :
    x = 1
    y = 1
    xmax = 1
    table = numpy.zeros((43,43))

    for line in open( filename ) :
        for element in [float(e) for e in line.split() ] :
            table[ y ][ x ] = element
            if x < xmax :
                x += 1
            else :
                x = 1
                y += 1
                xmax += 1
    return table

def read_table_file( filename ) :
    num_to_name = {}
    for line in open( filename ) :
        num, name = line.split('.')
        num_to_name[ int( num ) ] = name.strip().replace( ' ', '_' )
    return num_to_name

def print_ttl( filename, table, num_to_name ) :
    ttl_file = open( filename, 'w' )
    print >> ttl_file, "\
    @base <http:// <http://rhizomik.net/ontologies/>example.org/\n\
    <http://example.org/data>intelligenceModel#> .\n\
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n\
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n\
    "

    for x in range( 1, 43 ) :       
        for y in range( 1, 43 ) :
            if table[x][y] > 0.0 :
                print >> ttl_file, ':' + num_to_name[ x ] + ' :similarConcept [ rdf:value :' + num_to_name[ y ] + '; :weight ' + str( table[x][y] ) + ' ].'
        print >> ttl_file

def print_r( filename, table, names ) :
    r_file = open( filename, 'w' )
    for x in range( 1, 43 ) :
        print >> r_file, names[ x ],
    print >> r_file
    for x in range( 1, 43 ) :
        print >> r_file, names[ x ],   
        for y in range( 1, 43 ) :
            if table[x][y] > 0.0 :
                print >> r_file, ' ' + str( table[x][y] ),
        print >> r_file
    
        
if len( sys.argv ) < 4 :
    sys.exit( 'missing args: input-file table-file out-ttl-file out-r-file' )

table_data = read_input_file( sys.argv[1] )
table_names = read_table_file( sys.argv[2] )
print_ttl( sys.argv[3], table_data, table_names )
print_r( sys.argv[4], table_data, table_names )
