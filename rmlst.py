
import sys 
import requests
import argparse 
import base64
import os
import json

parser = argparse.ArgumentParser()
parser.add_argument(
    "--output", "-o",
    type = str,
    dest = "output",
    default = "rmlst.json",
    help = "Output tsv file path."
)
parser.add_argument(
  '--fasta', '-f',
  type = str,
  default = 'sample.fasta',
  help='assembly contig filename (FASTA format)')

parser.add_argument(
  '--uri', '-u',
  type = str,
  default = 'https://rest.pubmlst.org/db/pubmlst_rmlst_seqdef_kiosk/schemes/1/sequence',
  help='scheme uri')
args = parser.parse_args()


def get_rmlst_json(assembly_file):
  uri = args.uri
  with open(assembly_file, 'r') as x: 
    fasta = x.read()
  payload = '{"base64":true,"details":true,"sequence":"' + base64.b64encode(fasta.encode()).decode() + '"}'
  response = requests.post(uri, data=payload)
  if response.status_code == requests.codes.ok:
    data = response.json()
    try: 
      data['taxon_prediction']
    except KeyError:
      print("No rMLST match")
      sys.exit(0)

  else:
    raise requests.HTTPError(response.text)
  return data

if __name__ == "__main__":
  json_object = get_rmlst_json(args.fasta)
  
  with open(args.output, 'w') as output:
    json.dump(json_object, output)
