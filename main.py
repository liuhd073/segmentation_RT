import os

from dl.dataloader.dataloader import DatasetPatch, DatasetSingle
from dl.model.model import Model
# from mask2rs.rtstruct import RTStruct
from rs2mask.dcm2mask import Dataset

if __name__ == '__main__':

    # dataset
    structures = ["Parotide D", "Parotide G",
                  "Trachee", "Mandibule", "Tronc cerebral", "Encephale",
                  "Oesophage", "Larynx", 'Levres', 'Cavite buccale']

    # dataset = Dataset('data/ORL', 'data/ORL_dataset', structures)
    # dataset.make()

    # training
    root_training = 'data/ORL_dataset/'
    checkpoints_dir = 'checkpoints/'
    name = 'ORL_3D'
    expr_dir = os.path.join(checkpoints_dir, name)

    dataset = DatasetPatch(root_training, structures, 0.9, batch_size=1, num_worker=0)
    training_loader_patches, validation_loader_patches = dataset.get_loaders()

    model = Model(expr_dir, structures, n_blocks=18, niter=100, niter_decay=100)
    model.train(training_loader_patches, validation_loader_patches)

    # testing
    # expr_dir = os.path.join(checkpoints_dir, name)
    # model = Model(expr_dir, structures,  n_blocks=9)
    # root_prediction = 'prediction/'
    # pred_data_loader = DatasetSingle(root_prediction, structures)
    # model.test(pred_data_loader)

    # rtstruct
    # data = os.path.join('prediction')
    # struct = RTStruct(data)
    # struct.create()
    # struct.save()
