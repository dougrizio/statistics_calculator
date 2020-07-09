from Stats.RandomGenerators import n_items_no_seed



def get_sample(data, sample_size):
    sample = n_items_no_seed(data, sample_size )

    return sample