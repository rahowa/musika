import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from musika.parse.parse_encode import parse_args
from musika.models import Models_functions
from musika.utils_encode import UtilsEncode_functions

if __name__ == "__main__":

    # parse args
    args = parse_args()

    # initialize networks
    M = Models_functions(args)
    if args.download_networks:
        M.download_networks()
    models_ls = M.get_networks()

    # encode samples
    U = UtilsEncode_functions(args)
    if args.whole:
        U.compress_whole_files(models_ls)
    else:
        U.compress_files(models_ls)
