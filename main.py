#!/usr/bin/python

import audiotools
import audiotools.cdio
import os
import sys
from subprocess import call

def main(argv):
    #if len(sys.argv) < 2:
        #sys.exit('Missing arguments')

    cd = audiotools.cdio.CDDAReader("/dev/cdrom", True)
    cd_infos = audiotools.cddareader_metadata_lookup(cd)

    track_offsets = cd.track_offsets
    tracks_to_rip = list(sorted(track_offsets.keys()))
    input_filenames=[
        audiotools.Filename("track%2.2d.cdda.wav" % (i))
        for i in tracks_to_rip]
    #list of filename objects e.g.['track02.cdda.wav', 'track03.cdda.wav']
    print input_filenames
    #print "extracting track infos"
    #for result in cd_infos[0]:
        #print result
        #print "\n\n\n"
    # use first element to get album_name
    album = cd_infos[0][0].album_name.replace(" ", "_")
    artist = cd_infos[0][0].artist_name.lower().replace(" ", "_")

    print "album name is %s" % album
    print "album author is %s" % artist

    #sys.exit("aaa")

    crea_cartelle(artist, album)

    fstr = "%(track_name)s.%(suffix)s"
    AudioType = audiotools.TYPE_MAP["flac"] #flac is hardcoded

    # rippa le tracce del CD dentro quella cartella
    #rip_cmd = ['cd2track', '-t', 'flac', '-d', flac_fpath, '--format="%(track_name)s.%(suffix)s"']
    #call(rip_cmd)
    output_tracks=[]
    for i, val in enumerate(input_filenames):
        output_tracks.append([AudioType,
            val,
            8, #default quality for flac
            cd_infos[0][i]] #metadata choice
            )

    track_offset = track_offsets

    for o in output_tracks:
        print "elemento"
        print o


    sys.exit('aa')

def crea_cartelle(artist, album):
    basefolder = os.path.join(os.path.expanduser("~"), "test")
    artist_fpath = os.path.join(basefolder, artist)
    if not os.path.exists(artist_fpath):
        print "Artist folder does not exist, will be created"
        os.makedirs(artist_fpath)
    album_fpath = os.path.join(artist_fpath, album)
    if not os.path.exists(album_fpath):
        print "Album folder does not exist, will be created"
        os.makedirs(album_fpath)
    flac_fpath = os.path.join(album_fpath, "flac")
    if not os.path.exists(flac_fpath):
        print "Flac sub-folder does not exist, will be created"
        os.makedirs(flac_fpath)
    mp3_fpath = os.path.join(album_fpath, "mp3")
    if not os.path.exists(mp3_fpath):
        print "Mp3 sub-folder does not exist, will be created"
        os.makedirs(mp3_fpath)



if __name__ == "__main__":
    main(sys.argv)
