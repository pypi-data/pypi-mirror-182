from abc import ABC as ABC3
from builtins import list as list_1285
from temper_core import temper_print as temper_print_1243, str_cat as str_cat_1241, list_join as list_join_1264, bool_not as bool_not_1270, list_builder_add as list_builder_add_1267
TestFixtureBase = TestFixtureBase__6
class TestFixtureBase__1(ABC3):
  pass
passing__2 = True
t_76 = list_1285()
messages__3 = t_76
def test(name__4, body__5):
  global messages__3, passing__2
  passing__2 = True
  t_68 = list_1285()
  messages__3 = t_68
  body__5()
  if passing__2:
    t_71 = temper_print_1243(str_cat_1241(name__4, ': Passed'))
    t_39 = t_71
  else:
    def fn__65(it__7):
      return__8 = it__7
      return return__8
    t_72 = fn__65
    t_73 = list_join_1264(messages__3, '\n', t_72)
    t_74 = temper_print_1243(str_cat_1241(name__4, ': Failed ', t_73))
    t_39 = t_74
  return__43 = t_39
  return return__43
def assert2(success__9, message__10):
  global messages__3, passing__2
  t_61 = bool_not_1270(success__9)
  if t_61:
    passing__2 = False
    t_63 = message__10()
    list_builder_add_1267(messages__3, t_63)
  return__44 = None
  return return__44
return__42 = None
export = return__42
