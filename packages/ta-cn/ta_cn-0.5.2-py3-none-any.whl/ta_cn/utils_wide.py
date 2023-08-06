"""
宽表处理工具
"""
from functools import wraps

import numpy as np

from .imports.long import BY_DATE, BY_ASSET
from .utils import pd_to_np, np_to_pd


def get_uint_type(i):
    """通过数据大小得到合适的类型，用于减少内存"""
    # np.uint8, np.uint128, np.uint256 太小或太大都没什么意义
    int_types = [np.uint16, np.uint32, np.uint64]
    # np.iinfo(it).max
    # 65535
    # 4294967295
    # 18446744073709551615
    if i <= 65535:
        return np.uint16
    if i <= 4294967295:
        return np.uint32
    else:
        return np.uint64


def pushna(arr, direction='down'):
    """将非空数据按方向移动

    Parameters
    ----------
    arr: np.darray
    direction: str
        up, down, left, right

    Returns
    -------
    arr
        重排后的数据
    row
        行索引。将用于还原
    col
        列索引。将用于还原

    References
    ----------
    https://stackoverflow.com/questions/32062157/move-non-empty-cells-to-the-left-in-pandas-dataframe
    https://stackoverflow.com/questions/39361839/move-non-empty-cells-to-left-in-grouped-columns-pandas

    """
    if direction is None:
        return arr, None, None

    if direction == 'down':
        row = (~np.isnan(arr)).argsort(axis=0, kind='stable').astype(get_uint_type(arr.shape[0]))
        col = np.arange(arr.shape[1])[None]
    if direction == 'up':
        row = np.isnan(arr).argsort(axis=0, kind='stable').astype(get_uint_type(arr.shape[0]))
        col = np.arange(arr.shape[1])[None]
    if direction == 'left':
        col = np.isnan(arr).argsort(axis=1, kind='stable').astype(get_uint_type(arr.shape[1]))
        row = np.arange(arr.shape[0])[:, None]
    if direction == 'right':
        col = (~np.isnan(arr)).argsort(axis=1, kind='stable').astype(get_uint_type(arr.shape[1]))
        row = np.arange(arr.shape[0])[:, None]

    return arr[row, col], row, col


def pullna(arr, row, col):
    """pushna的还原

    Parameters
    ----------
    arr: np.array
    row
        行索引
    col
        列索引

    Examples
    --------
    >>> a, row, col = pushna(df)
    >>> print(pullna(a, row, col))

    """
    if row is None:
        return arr

    # col 过于简单，可以通过direction推断出来

    tmp = np.empty_like(arr)
    tmp[row, col] = arr
    return tmp


class WArr(np.ndarray):
    """宽表计算中间体，用于进行输入的堆叠，输出的还原，不可修改"""
    arr = None  # 堆叠后的数据
    row = None
    col = None
    direction = None
    _raw = None

    def raw(self):
        """还原 原始数据。内部还原操作只做一次"""
        if self._raw is None:
            self._raw = pullna(self.arr, self.row, self.col)
        return self._raw

    @classmethod
    def from_args(cls, arr, row, col, direction):
        """直接设置 堆叠后数据 和方向"""
        c = cls(shape=(1,))
        c.arr, c.row, c.col, c.direction = arr, row, col, direction
        return c

    @classmethod
    def from_array(cls, arr, direction):
        """输入 原始数据 和方向，内部自动堆叠"""
        return cls.from_args(*pushna(pd_to_np(arr), direction), direction)

    @classmethod
    def from_obj(cls, obj, direction):
        """输入 WArr对象 和 新方向。自动复制对象"""
        if isinstance(obj, cls):
            # 方向一样就直接返回
            if direction == obj.direction:
                return obj
            # 不一样就还原数据
            return cls.from_array(obj.raw(), direction)
        elif isinstance(obj, (int, float)):
            # 处理某一个参数为纯数字的问题
            return cls.from_args(obj, None, None, None)
        else:
            return cls.from_array(obj, direction)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr * other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() * other.raw(), self.direction)
        else:
            return self.from_array(self.raw() * other, self.direction)

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(other * self.arr, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(other.raw() * self.raw(), self.direction)
        else:
            return self.from_array(other * self.raw(), self.direction)

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr > other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() > other.raw(), self.direction)
        else:
            return self.from_array(self.raw() > other, self.direction)

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr < other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() < other.raw(), self.direction)
        else:
            return self.from_array(self.raw() < other, self.direction)

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr >= other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() >= other.raw(), self.direction)
        else:
            return self.from_array(self.raw() >= other, self.direction)

    def __le__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr <= other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() <= other.raw(), self.direction)
        else:
            return self.from_array(self.raw() <= other, self.direction)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr == other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() == other.raw(), self.direction)
        else:
            return self.from_array(self.raw() == other, self.direction)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr + other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() + other.raw(), self.direction)
        else:
            return self.from_array(self.raw() + other, self.direction)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(other + self.arr, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(other.raw() + self.raw(), self.direction)
        else:
            return self.from_array(other + self.raw(), self.direction)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr - other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() - other.raw(), self.direction)
        else:
            return self.from_array(self.raw() - other, self.direction)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(other - self.arr, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(other.raw() - self.raw(), self.direction)
        else:
            return self.from_array(other - self.raw(), self.direction)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr / other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() / other.raw(), self.direction)
        else:
            return self.from_array(self.raw() / other, self.direction)

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(other / self.arr, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(other.raw() / self.raw(), self.direction)
        else:
            return self.from_array(other / self.raw(), self.direction)

    def __floordiv__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr // other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() // other.raw(), self.direction)
        else:
            return self.from_array(self.raw() // other, self.direction)

    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(self.arr % other, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(self.raw() % other.raw(), self.direction)
        else:
            return self.from_array(self.raw() % other, self.direction)

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            return self.from_args(self.arr ** power, self.row, self.col, self.direction)
        if isinstance(power, WArr):
            return self.from_array(self.raw() ** power.raw(), self.direction)
        else:
            return self.from_array(self.raw() ** power, self.direction)

    def __rpow__(self, other):
        if isinstance(other, (int, float)):
            return self.from_args(other ** self.arr, self.row, self.col, self.direction)
        if isinstance(other, WArr):
            return self.from_array(other.raw() ** self.raw(), self.direction)
        else:
            return self.from_array(other ** self.raw(), self.direction)

    def __neg__(self):
        return self.from_args(-self.arr, self.row, self.col, self.direction)

    def __and__(self, other):
        if isinstance(other, WArr):
            return self.from_array(self.raw() & other.raw(), self.direction)
        else:
            return self.from_array(self.raw() & other, self.direction)

    def __or__(self, other):
        if isinstance(other, WArr):
            return self.from_array(self.raw() | other.raw(), self.direction)
        else:
            return self.from_array(self.raw() | other, self.direction)


def wide_wraps(func, direction='down', input_num=1, to_kwargs={1: 'timeperiod'}, output_num=1):
    """将二维函数包装成堆叠函数

    Parameters
    ----------
    func:
        1. 必须是二维数据处理函数
        2. 由于数据已经堆叠。内部处理时最好能跳过空行或空列
    direction
        数据堆叠方向。时序堆叠到最后。
    input_num: int
        入参数量。二维数据个数
    to_kwargs: dict
        第几个入参转成命名参数
    output_num: int
        输出数量

    """

    @wraps(func)
    def decorated(*args, **kwargs):
        # 将位置参数提取出命名参数。主要为是talib的二维封装
        _kwargs = {k: args[i] for i, k in to_kwargs.items() if i < len(args)}
        _args = [WArr.from_obj(v, direction) for i, v in enumerate(args) if i not in to_kwargs]
        arg0 = _args[0]

        # 输入+计算
        if input_num == 1:
            outputs = func(arg0.arr, **kwargs, **_kwargs)
        else:
            outputs = func(*[v.arr for v in _args], **kwargs, **_kwargs)

        # 输出
        if output_num == 1:
            return WArr.from_args(outputs, arg0.row, arg0.col, direction)
        else:
            return tuple([WArr.from_args(v, arg0.row, arg0.col, direction) for v in outputs])

    return decorated


def long_wraps(func, direction='down'):
    """将长表函数包装成宽表函数

    Parameters
    ----------
    func:
        1. 必须是长表处理函数
    direction
        数据堆叠方向。时序堆叠到最后。

    """

    def _get_raw_arr(arr):
        """取原始数据"""
        if isinstance(arr, WArr):
            return arr.raw()
        return arr

    def _convert(x):
        """宽表转长表，并调整"""
        y = np_to_pd(_get_raw_arr(x)).stack(dropna=False)
        y.index.names = [BY_DATE, BY_ASSET]
        return y

    @wraps(func)
    def decorated(*args, **kwargs):
        args = [_convert(a) for a in args]

        # 输入+计算
        outputs = func(*args, **kwargs)

        # 输出
        return WArr.from_array(outputs.unstack(), direction=direction)

    return decorated
