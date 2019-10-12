import numpy as np


def save_data(data):
    A= np.random.randn(3,2)
    np.save('2darray.npy', A)
    print('here1')
    print(data['train_images'].shape)
	
    np.save('train_images.npy', data['train_images'])
    np.save('train_labels.npy', data['train_labels'])
    np.save('test_images.npy', data['test_images'])
    np.save('test_labels.npy', data['test_labels'])
    
    