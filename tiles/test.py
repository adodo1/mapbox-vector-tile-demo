#!/usr/bin/env python
# encoding: utf-8

import os, sys, re, math, json, sqlite3, mapbox_vector_tile
import zlib, gzip, StringIO


if __name__=='__main__':
    print '[==DoDo==]'
    print 'amap labels.'
    print 'Encode: %s' %  sys.getdefaultencoding()

    '''
    f = open('6.pbf', 'rb')
    d = f.read()
    f.close()
    s = mapbox_vector_tile.decode(d)
    f = open('6.json', 'wb')
    f.write(json.dumps(s))
    f.close()
    '''


    f = open('6_.json', 'rb')
    s = f.read()
    f.close()
    d = json.loads(s)
    v = mapbox_vector_tile.encode(d, extents=256)
    

    conn = sqlite3.connect('AMAP.mbtiles', check_same_thread = False)
    cursor = conn.cursor()
    #cursor.execute('insert into TILES(TILE_DATA, ZOOM_LEVEL, TILE_COLUMN, TILE_ROW) values(?,?,?,?)', (sqlite3.Binary(v),3,3,6))
    cursor.execute('update TILES set TILE_DATA=? where ZOOM_LEVEL=3 and TILE_COLUMN=3 and TILE_ROW=6', (sqlite3.Binary(v),))
    conn.commit()

    conn.close()


    
    print 'OK.'
