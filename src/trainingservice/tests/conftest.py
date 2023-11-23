import pathlib

import pytest
import torch
import torchvision


@pytest.fixture
def data_dirs(tmp_path):
    paths = [tmp_path / "1", tmp_path / "2"]
    for path in paths:
        path = pathlib.Path(path)
        path.mkdir()
        for subset in ["train", "val"]:
            subset_dir = path / subset
            subset_dir.mkdir()
            n = 10 if subset == "train" else 2
            for i in range(n):
                img = torch.zeros(3, 125, 125, dtype=torch.uint8)
                torchvision.io.write_png(img, str(path / f"{i}.png"))
    return list(map(str, paths))
