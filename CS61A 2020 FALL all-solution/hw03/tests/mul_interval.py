test = {
  'name': 'mul_interval',
  'points': 1,
  'suites': [
    {
      'type': 'doctest',
      'setup': """
      >>> import hw03
      >>> from hw03 import *
      """,
      'cases': [
        {
          'code': """
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          '-8 to 16'
          """
        }
      ]
    },
    {
      'type': 'doctest',
      'setup': """
      >>> import hw03
      >>> old_abstraction = hw03.interval, hw03.lower_bound, hw03.upper_bound
      >>> hw03.interval = lambda a, b: lambda x: a if x == 0 else b
      >>> hw03.lower_bound = lambda s: s(0)
      >>> hw03.upper_bound = lambda s: s(1)
      >>> from hw03 import *
      """,
      'cases': [
        {
          'locked': False,
          'code': """
          >>> # Testing for abstraction violations
          >>> # Your code should not check for which implementation is used
          >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
          '-8 to 16'
          """
        },
      ],
      'teardown': """
      >>> hw03.interval, hw03.lower_bound, hw03.upper_bound = old_abstraction
      """
    },
  ]
}
