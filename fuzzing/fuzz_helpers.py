import contextlib
import datetime
import io
import tempfile
from typing import List, TypeVar

import atheris

T = TypeVar("T")


class EnhancedFuzzedDataProvider(atheris.FuzzedDataProvider):
    def ConsumeRandomBytes(self) -> bytes:
        return self.ConsumeBytes(self.ConsumeIntInRange(0, self.remaining_bytes()))

    def ConsumeRandomString(self) -> str:
        return self.ConsumeUnicodeNoSurrogates(
            self.ConsumeIntInRange(0, self.remaining_bytes())
        )

    def ConsumeRemainingString(self) -> str:
        return self.ConsumeUnicodeNoSurrogates(self.remaining_bytes())

    def ConsumeRemainingBytes(self) -> bytes:
        return self.ConsumeBytes(self.remaining_bytes())

    def ConsumeSublist(self, source: List[T]) -> List[T]:
        """
        Returns a shuffled sub-list of the given list of len [1, len(source)]
        """
        chosen = [elem for elem in source if self.ConsumeBool()]

        # Shuffle
        for i in range(len(chosen) - 1, 1, -1):
            j = self.ConsumeIntInRange(0, i)
            chosen[i], chosen[j] = chosen[j], chosen[i]

        return chosen or [self.PickValueInList(source)]

    def ConsumeDate(self) -> datetime.datetime:
        try:
            return datetime.datetime.fromtimestamp(self.ConsumeFloat())
        except (OverflowError, OSError, ValueError):
            return datetime.datetime(year=1970, month=1, day=1)

    @contextlib.contextmanager
    def ConsumeMemoryFile(
        self, all_data: bool = False, as_bytes: bool = True
    ) -> io.BytesIO:
        if all_data:
            file_data = (
                self.ConsumeRemainingBytes()
                if as_bytes
                else self.ConsumeRemainingString()
            )
        else:
            file_data = (
                self.ConsumeRandomBytes() if as_bytes else self.ConsumeRandomString()
            )

        file = io.BytesIO(file_data) if as_bytes else io.StringIO(file_data)
        yield file
        file.close()

    @contextlib.contextmanager
    def ConsumeTemporaryFile(
        self, suffix: str, all_data: bool = False, as_bytes: bool = True
    ) -> str:
        if all_data:
            file_data = (
                self.ConsumeRemainingBytes()
                if as_bytes
                else self.ConsumeRemainingString()
            )
        else:
            file_data = (
                self.ConsumeRandomBytes() if as_bytes else self.ConsumeRandomString()
            )

        mode = "w+b" if as_bytes else "w+"
        tfile = tempfile.NamedTemporaryFile(mode=mode, suffix=suffix)
        tfile.write(file_data)
        tfile.seek(0)
        tfile.flush()
        yield tfile.name
        tfile.close()
