import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from musika.parse.parse_test import parse_args
from musika.models import Models_functions
from musika.utils import Utils_functions

if __name__ == "__main__":

    # parse args
    args = parse_args()

    # initialize networks
    M = Models_functions(args)
    M.download_networks()
    models_ls = M.get_networks()

    # test musika
    U = Utils_functions(args)
    U.render_gradio(models_ls, train=False)
