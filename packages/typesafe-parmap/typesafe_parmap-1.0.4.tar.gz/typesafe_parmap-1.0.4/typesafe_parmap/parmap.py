import concurrent.futures
from concurrent.futures import Future
from datetime import timedelta
from typing import *

A1 = TypeVar("A1")
A2 = TypeVar("A2")
A3 = TypeVar("A3")
A4 = TypeVar("A4")
A5 = TypeVar("A5")
A6 = TypeVar("A6")
A7 = TypeVar("A7")
A8 = TypeVar("A8")
A9 = TypeVar("A9")
A10 = TypeVar("A10")
A11 = TypeVar("A11")
A12 = TypeVar("A12")
A13 = TypeVar("A13")
A14 = TypeVar("A14")
A15 = TypeVar("A15")
A16 = TypeVar("A16")
A17 = TypeVar("A17")
A18 = TypeVar("A18")
A19 = TypeVar("A19")
A20 = TypeVar("A20")
A21 = TypeVar("A21")
A22 = TypeVar("A22")


def par_map_2(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    return fut1.result(), fut2.result()





def par_map_3(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    return fut1.result(), fut2.result(), fut3.result()


def par_map_4(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    return fut1.result(), fut2.result(), fut3.result(), fut4.result()


def par_map_5(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    return fut1.result(), fut2.result(), fut3.result(), fut4.result(), fut5.result()


def par_map_6(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
    )


def par_map_7(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
    )


def par_map_8(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
    )


def par_map_9(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
    )


def par_map_10(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
    )


def par_map_11(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
    )


def par_map_12(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
    )


def par_map_13(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
    )


def par_map_14(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
    )


def par_map_15(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
    )


def par_map_16(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
        fut16.result(),
    )


def par_map_17(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
        fut16.result(),
        fut17.result(),
    )


def par_map_18(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
        fut16.result(),
        fut17.result(),
        fut18.result(),
    )


def par_map_19(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
        fut16.result(),
        fut17.result(),
        fut18.result(),
        fut19.result(),
    )


def par_map_20(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20,]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    fut20 = executor.submit(func20)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
        fut16.result(),
        fut17.result(),
        fut18.result(),
        fut19.result(),
        fut20.result(),
    )


def par_map_21(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    func21: Callable[[], A21],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21,]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    fut20 = executor.submit(func20)
    fut21 = executor.submit(func21)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
        fut16.result(),
        fut17.result(),
        fut18.result(),
        fut19.result(),
        fut20.result(),
        fut21.result(),
    )


def par_map_22(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    func21: Callable[[], A21],
    func22: Callable[[], A22],
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22,]:
    fut1 = executor.submit(func1)
    fut2 = executor.submit(func2)
    fut3 = executor.submit(func3)
    fut4 = executor.submit(func4)
    fut5 = executor.submit(func5)
    fut6 = executor.submit(func6)
    fut7 = executor.submit(func7)
    fut8 = executor.submit(func8)
    fut9 = executor.submit(func9)
    fut10 = executor.submit(func10)
    fut11 = executor.submit(func11)
    fut12 = executor.submit(func12)
    fut13 = executor.submit(func13)
    fut14 = executor.submit(func14)
    fut15 = executor.submit(func15)
    fut16 = executor.submit(func16)
    fut17 = executor.submit(func17)
    fut18 = executor.submit(func18)
    fut19 = executor.submit(func19)
    fut20 = executor.submit(func20)
    fut21 = executor.submit(func21)
    fut22 = executor.submit(func22)
    return (
        fut1.result(),
        fut2.result(),
        fut3.result(),
        fut4.result(),
        fut5.result(),
        fut6.result(),
        fut7.result(),
        fut8.result(),
        fut9.result(),
        fut10.result(),
        fut11.result(),
        fut12.result(),
        fut13.result(),
        fut14.result(),
        fut15.result(),
        fut16.result(),
        fut17.result(),
        fut18.result(),
        fut19.result(),
        fut20.result(),
        fut21.result(),
        fut22.result(),
    )


@overload
def par_map_n(
    func1: Callable[[], A1], func2: Callable[[], A2], *, executor: concurrent.futures.Executor
) -> Tuple[A1, A2]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1], func2: Callable[[], A2], func3: Callable[[], A3], *, executor: concurrent.futures.Executor
) -> Tuple[A1, A2, A3]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    func21: Callable[[], A21],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21]:
    ...


@overload
def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Callable[[], A3],
    func4: Callable[[], A4],
    func5: Callable[[], A5],
    func6: Callable[[], A6],
    func7: Callable[[], A7],
    func8: Callable[[], A8],
    func9: Callable[[], A9],
    func10: Callable[[], A10],
    func11: Callable[[], A11],
    func12: Callable[[], A12],
    func13: Callable[[], A13],
    func14: Callable[[], A14],
    func15: Callable[[], A15],
    func16: Callable[[], A16],
    func17: Callable[[], A17],
    func18: Callable[[], A18],
    func19: Callable[[], A19],
    func20: Callable[[], A20],
    func21: Callable[[], A21],
    func22: Callable[[], A22],
    *,
    executor: concurrent.futures.Executor,
) -> Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22]:
    ...


def par_map_n(
    func1: Callable[[], A1],
    func2: Callable[[], A2],
    func3: Optional[Callable[[], A3]] = None,
    func4: Optional[Callable[[], A4]] = None,
    func5: Optional[Callable[[], A5]] = None,
    func6: Optional[Callable[[], A6]] = None,
    func7: Optional[Callable[[], A7]] = None,
    func8: Optional[Callable[[], A8]] = None,
    func9: Optional[Callable[[], A9]] = None,
    func10: Optional[Callable[[], A10]] = None,
    func11: Optional[Callable[[], A11]] = None,
    func12: Optional[Callable[[], A12]] = None,
    func13: Optional[Callable[[], A13]] = None,
    func14: Optional[Callable[[], A14]] = None,
    func15: Optional[Callable[[], A15]] = None,
    func16: Optional[Callable[[], A16]] = None,
    func17: Optional[Callable[[], A17]] = None,
    func18: Optional[Callable[[], A18]] = None,
    func19: Optional[Callable[[], A19]] = None,
    func20: Optional[Callable[[], A20]] = None,
    func21: Optional[Callable[[], A21]] = None,
    func22: Optional[Callable[[], A22]] = None,
    *,  # Makes executor keyword only
    executor: concurrent.futures.Executor,
) -> Union[
    Tuple[A1, A2],
    Tuple[A1, A2, A3],
    Tuple[A1, A2, A3, A4],
    Tuple[A1, A2, A3, A4, A5],
    Tuple[A1, A2, A3, A4, A5, A6],
    Tuple[A1, A2, A3, A4, A5, A6, A7],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21],
    Tuple[A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17, A18, A19, A20, A21, A22],
]:
    """Executes 2 to 22 functions in parallel"""
    if (
        func22 is not None
        and func21 is not None
        and func20 is not None
        and func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_22(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            func20=func20,
            func21=func21,
            func22=func22,
            executor=executor,
        )
    if (
        func21 is not None
        and func20 is not None
        and func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_21(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            func20=func20,
            func21=func21,
            executor=executor,
        )
    if (
        func20 is not None
        and func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_20(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            func20=func20,
            executor=executor,
        )
    if (
        func19 is not None
        and func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_19(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            func19=func19,
            executor=executor,
        )
    if (
        func18 is not None
        and func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_18(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            func18=func18,
            executor=executor,
        )
    if (
        func17 is not None
        and func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_17(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            func17=func17,
            executor=executor,
        )
    if (
        func16 is not None
        and func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_16(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            func16=func16,
            executor=executor,
        )
    if (
        func15 is not None
        and func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_15(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            func15=func15,
            executor=executor,
        )
    if (
        func14 is not None
        and func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_14(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            func14=func14,
            executor=executor,
        )
    if (
        func13 is not None
        and func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_13(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            func13=func13,
            executor=executor,
        )
    if (
        func12 is not None
        and func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_12(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            func12=func12,
            executor=executor,
        )
    if (
        func11 is not None
        and func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_11(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            func11=func11,
            executor=executor,
        )
    if (
        func10 is not None
        and func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_10(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            func10=func10,
            executor=executor,
        )
    if (
        func9 is not None
        and func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_9(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            func9=func9,
            executor=executor,
        )
    if (
        func8 is not None
        and func7 is not None
        and func6 is not None
        and func5 is not None
        and func4 is not None
        and func3 is not None
    ):
        return par_map_8(
            func1=func1,
            func2=func2,
            func3=func3,
            func4=func4,
            func5=func5,
            func6=func6,
            func7=func7,
            func8=func8,
            executor=executor,
        )
    if func7 is not None and func6 is not None and func5 is not None and func4 is not None and func3 is not None:
        return par_map_7(
            func1=func1, func2=func2, func3=func3, func4=func4, func5=func5, func6=func6, func7=func7, executor=executor
        )
    if func6 is not None and func5 is not None and func4 is not None and func3 is not None:
        return par_map_6(
            func1=func1, func2=func2, func3=func3, func4=func4, func5=func5, func6=func6, executor=executor
        )
    if func5 is not None and func4 is not None and func3 is not None:
        return par_map_5(func1=func1, func2=func2, func3=func3, func4=func4, func5=func5, executor=executor)
    if func4 is not None and func3 is not None:
        return par_map_4(func1=func1, func2=func2, func3=func3, func4=func4, executor=executor)
    if func3 is not None:
        return par_map_3(func1=func1, func2=func2, func3=func3, executor=executor)
    else:
        return par_map_2(func1=func1, func2=func2, executor=executor)
