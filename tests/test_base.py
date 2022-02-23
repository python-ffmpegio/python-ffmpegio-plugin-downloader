import ffmpegio_plugin_downloader
import ffmpeg_downloader as ffdl
import pytest
from ffmpegio import plugins, path


@pytest.fixture(scope="module", autouse=True)
def ffmpeg():
    install = ffdl.ffmpeg_path is None
    try:
        if install:
            ffdl.update(True)
        print('loaded')
        yield
        print('done')
    finally:
        if install:
            ffdl.remove()


def test_plugin():
    assert ffmpegio_plugin_downloader in plugins.pm.get_plugins()


def test_operation(ffmpeg):
    path.find()
    assert path.get_ffmpeg() == ffdl.ffmpeg_path
    assert path.get_ffmpeg(True) == ffdl.ffprobe_path


if __name__ == "__main__":
    test_operation()
