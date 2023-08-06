import argparse as arg
import os

# import .util as util 
from . import util

def bmcompiler_parser():
    parser = arg.ArgumentParser(description     = "handle nas with command line",
                                formatter_class = arg.ArgumentDefaultsHelpFormatter,
                                prog            = "python -m dtools")

    
    parser.add_argument("--method", type=str,help="method: upload or list", required=True, choices=['upload', 'list'])
    parser.add_argument("--local_dir", type=str,help="local dir")
    parser.add_argument("--temporary-token", type=str,help="nas dir. Attention : \n \
        1. temporary-token is a token given by Sophon official people for delivering files with time limition. \n ")
    return parser

def main():
    parser = bmcompiler_parser()
    a = parser.parse_args()
    
    if a.method == 'upload':
        util.upload_with_token(a.temporary_token, a.local_dir)
        
    if a.method == 'list': 
        util.list_file_with_token(a.temporary_token)

if __name__ == "__main__":
    parser = bmcompiler_parser()
    a = parser.parse_args()
    
    if a.method == 'upload':
        util.upload_with_token(a.temporary_token, a.local_dir)
        
    if a.method == 'list': 
        util.list_file_with_token(a.temporary_token)
    