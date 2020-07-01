from Stats.RandomGenerators import n_items_no_seed


def get_sample(data, sample_size = 5):
    sample = n_items_no_seed(data, choices = sample_size )
    print(sample)
    return sample
