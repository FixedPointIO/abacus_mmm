"""Parse absl flags for when it is run by github actions by pytest."""

from absl import flags


def pytest_configure(config):
  flags.FLAGS.mark_as_parsed()
