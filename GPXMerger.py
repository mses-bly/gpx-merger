from argparse import ArgumentParser

import gpxpy
import os

parser = ArgumentParser()

parser.add_argument("-d", "--directory", dest="directory",
                    required=True, help="path to directory containing gpx files")

parser.add_argument("-o", "--output", dest="output",
                    required=True, help="path to output")


args = parser.parse_args()

######### PARAMETERS #############
directoy = args.directory
output = args.output

merged = gpxpy.gpx.GPX()
for root, _, files in os.walk(directoy):
    for file in files:
        if file.endswith(".gpx"):
            gpx_file = open("/".join([root,file]), 'r', encoding="utf-8")
            gpx = gpxpy.parse(gpx_file)
            for track in gpx.tracks:
                track.name = file
                merged.tracks.append(track)
            for route in gpx.routes:
                route.name = file
                merged.routes.append(route)
            for wp in gpx.waypoints:
                merged.waypoints.append(wp)

# Write to the output file
with open(output, 'w') as o:
    o.write(merged.to_xml())