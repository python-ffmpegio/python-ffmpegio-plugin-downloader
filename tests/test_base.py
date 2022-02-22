from ffmpegio import plugins


def test_hooks():
    hook = plugins.get_hook().finder
    print(hook)
    print(plugins.pm.get_plugins())


if __name__ == "__main__":
    test_hooks()
