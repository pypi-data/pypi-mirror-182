import numpy as np


def rank_scale_data(arr: np.ndarray) -> np.ndarray:
    arr = arr.copy()
    raw_ranks = np.zeros(shape=(arr.shape[0]))
    argsort = np.argsort(arr)

    s = (arr[:, np.newaxis] == arr).astype(int)
    raw_ranks[argsort] = np.arange(arr.shape[0]) + 1
    ranks = np.sum(raw_ranks*s, axis=1)/s.sum(axis=0)
    return ranks/ranks.sum()


def protect_norm(x: np.ndarray) -> np.ndarray:
    sum_ = x.sum()
    if sum_ > 0:
        return x/sum_
    else:
        len_ = len(x)
        return np.full(len_, 1/len_)


def scale_data(arr: np.ndarray) -> np.ndarray:
    arr = arr.copy()
    max_ = arr.max()
    min_ = arr.min()
    if max_ == min_:
        arr_n = np.ones_like(arr)
    else:
        arr_n = (arr - min_)/(max_ - min_)
    return arr_n


class SamplingGrid:

    def __init__(self, fit_by: str = 'h') -> None:
        self.fit_by = fit_by
        self.left: np.ndarray
        self.right: np.ndarray
        self.parts: np.ndarray
        self.h: np.ndarray
        self.power_arange: np.ndarray

    @staticmethod
    def culc_h_from_parts(left: np.ndarray, right: np.ndarray,
                          parts: np.ndarray) -> np.ndarray:
        return (right - left)/(2.0**parts - 1)

    @staticmethod
    def culc_parts_from_h(left: np.ndarray, right: np.ndarray,
                          h: np.ndarray) -> np.ndarray:
        return np.ceil(np.log2((right - left)/h + 1)).astype(int)

    def _decoder(self, population_parts, left_i, h_i):
        ipp = population_parts.astype(int)
        arange_ = self.power_arange[:ipp.shape[1]][::-1]
        int_convert = np.sum(ipp*arange_, axis=1)
        return left_i + h_i*int_convert

    def fit(self, left: np.ndarray, right: np.ndarray,
            arg: np.ndarray):
        self.left = left
        self.right = right

        assert self.fit_by in [
            'h', 'parts'], f"incorrect option {self.fit_by} for fit_by. The available ones are 'h' and 'parts'"
        if self.fit_by == 'h':
            min_h = arg
            self.parts = self.culc_parts_from_h(left, right, min_h)
            self.h = self.culc_h_from_parts(left, right, self.parts)
        else:
            self.parts = arg
            self.h = self.culc_h_from_parts(left, right, self.parts)

        self.power_arange = 2**np.arange(self.parts.max(), dtype=np.int64)
        return self

    def transform(self, population: np.ndarray) -> np.ndarray:
        splits = np.add.accumulate(self.parts)
        p_parts = np.split(population, splits[:-1], axis=1)
        fpp = [self._decoder(p_parts_i, left_i, h_i)
               for p_parts_i, left_i, h_i in zip(p_parts,
                                                 self.left,
                                                 self.h)]
        return np.vstack(fpp).T
