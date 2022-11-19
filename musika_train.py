import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from musika.parse.parse_train import parse_args
from musika.data import Data_functions
from musika.models import Models_functions
from musika.utils import Utils_functions
from musika.train import Train_functions

if __name__ == "__main__":

    # parse args
    args = parse_args()

    # create dataset
    D = Data_functions(args)
    ds = D.create_dataset()

    # initialize networks
    M = Models_functions(args)
    M.download_networks()
    models_ls = M.initialize_networks()

    # test musika in real-time during training
    U = Utils_functions(args)
    U.render_gradio(models_ls)

    # train musika
    T = Train_functions(args)
    T.train(ds, models_ls)
