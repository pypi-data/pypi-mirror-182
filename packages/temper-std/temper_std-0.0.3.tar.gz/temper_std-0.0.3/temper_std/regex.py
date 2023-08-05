from builtins import isinstance as isinstance0, Exception as Exception5, len as len_1273, list as list_1285
from abc import ABC as ABC3
from temper_core import TemperObject as TemperObject1, cast_by_type as cast_by_type4, Label as Label6, NoResultException as NoResultException7, isinstance_int as isinstance_int8, cast_by_test as cast_by_test9, list_join as list_join_1264, generic_eq as generic_eq_1266, list_builder_add as list_builder_add_1267, string_code_points as string_code_points_1239, bool_not as bool_not_1270, generic_lt as generic_lt_1274, list_get as list_get_1275, int_to_string as int_to_string_1240, str_cat as str_cat_1241, generic_not_eq as generic_not_eq_1281, generic_gt_eq as generic_gt_eq_1284
from temper_core.regex import compiled_regex_compile_formatted as compiled_regex_compile_formatted_1260, compiled_regex_compiled_found_in as compiled_regex_compiled_found_in_1261, compiled_regex_compiled_find as compiled_regex_compiled_find_1262, regex_formatter_push_capture_name as regex_formatter_push_capture_name_1268, regex_formatter_push_code_to as regex_formatter_push_code_to_1269
def Regex(x_1245):
  return isinstance0(x_1245, Regex__8)
def CodePart(x_1247):
  return isinstance0(x_1247, CodePart__13)
def Special(x_1249):
  return isinstance0(x_1249, Special__15)
def SpecialSet(x_1250):
  return isinstance0(x_1250, SpecialSet__20)
class Regex__8(ABC3):
  def compiled(this__9):
    t_1230 = CompiledRegex(this__9)
    return__57 = t_1230
    return return__57
  def foundIn(this__10, text__133):
    t_1227 = this__10.compiled()
    t_1228 = t_1227.foundIn(text__133)
    return__58 = t_1228
    return return__58
  def find(this__11, text__136):
    t_1225 = this__11.compiled()
    t_865 = t_1225.find(text__136)
    return__59 = t_865
    return return__59
def Capture(*args_1246):
  return Capture__12(*args_1246)
class Capture__12(Regex__8, TemperObject1):
  def constructor__140(this__60, name__141, item__142):
    return__61 = None
    this__60.name__138 = name__141
    this__60.item__139 = item__142
    return return__61
  def __init__(this__60, name__141, item__142):
    this__60.constructor__140(name__141, item__142)
  def getname__306(this__307):
    return__308 = this__307.name__138
    return return__308
  def getitem__310(this__311):
    return__312 = this__311.item__139
    return return__312
  name = property(getname__306, None)
  item = property(getitem__310, None)
class CodePart__13(Regex__8, ABC3):
  pass
def CodePoints(*args_1248):
  return CodePoints__14(*args_1248)
class CodePoints__14(CodePart__13, TemperObject1):
  def constructor__144(this__62, value__145):
    return__63 = None
    this__62.value__143 = value__145
    return return__63
  def __init__(this__62, value__145):
    this__62.constructor__144(value__145)
  def getvalue__314(this__315):
    return__316 = this__315.value__143
    return return__316
  value = property(getvalue__314, None)
class Special__15(Regex__8, ABC3):
  pass
class SpecialSet__20(CodePart__13, Special__15, ABC3):
  pass
def CodeRange(*args_1251):
  return CodeRange__24(*args_1251)
class CodeRange__24(CodePart__13, TemperObject1):
  def constructor__162(this__78, min__163, max__164):
    return__79 = None
    this__78.min__160 = min__163
    this__78.max__161 = max__164
    return return__79
  def __init__(this__78, min__163, max__164):
    this__78.constructor__162(min__163, max__164)
  def getmin__318(this__319):
    return__320 = this__319.min__160
    return return__320
  def getmax__322(this__323):
    return__324 = this__323.max__161
    return return__324
  min = property(getmin__318, None)
  max = property(getmax__322, None)
def CodeSet(*args_1252):
  return CodeSet__25(*args_1252)
class CodeSet__25(Regex__8, TemperObject1):
  def constructor__167(this__80, items__168, negated = ...):
    negated__169 = negated
    return__82 = None
    if negated__169 is ...:
      negated__169 = False
    this__80.items__165 = items__168
    this__80.negated__166 = negated__169
    return return__82
  def __init__(this__80, items__168, negated = ...):
    negated__169 = negated
    this__80.constructor__167(items__168, negated__169)
  def getitems__326(this__327):
    return__328 = this__327.items__165
    return return__328
  def getnegated__330(this__331):
    return__332 = this__331.negated__166
    return return__332
  items = property(getitems__326, None)
  negated = property(getnegated__330, None)
def Or(*args_1253):
  return Or__26(*args_1253)
class Or__26(Regex__8, TemperObject1):
  def constructor__171(this__83, items__172):
    return__85 = None
    this__83.items__170 = items__172
    return return__85
  def __init__(this__83, items__172):
    this__83.constructor__171(items__172)
  def getitems__334(this__335):
    return__336 = this__335.items__170
    return return__336
  items = property(getitems__334, None)
def Repeat(*args_1254):
  return Repeat__27(*args_1254)
class Repeat__27(Regex__8, TemperObject1):
  def constructor__177(this__86, item__178, min__179, max__180, reluctant = ...):
    reluctant__181 = reluctant
    return__88 = None
    if reluctant__181 is ...:
      reluctant__181 = False
    this__86.item__173 = item__178
    this__86.min__174 = min__179
    this__86.max__175 = max__180
    this__86.reluctant__176 = reluctant__181
    return return__88
  def __init__(this__86, item__178, min__179, max__180, reluctant = ...):
    reluctant__181 = reluctant
    this__86.constructor__177(item__178, min__179, max__180, reluctant__181)
  def getitem__338(this__339):
    return__340 = this__339.item__173
    return return__340
  def getmin__342(this__343):
    return__344 = this__343.min__174
    return return__344
  def getmax__346(this__347):
    return__348 = this__347.max__175
    return return__348
  def getreluctant__350(this__351):
    return__352 = this__351.reluctant__176
    return return__352
  item = property(getitem__338, None)
  min = property(getmin__342, None)
  max = property(getmax__346, None)
  reluctant = property(getreluctant__350, None)
def Sequence(*args_1255):
  return Sequence__28(*args_1255)
class Sequence__28(Regex__8, TemperObject1):
  def constructor__191(this__92, items__192):
    return__94 = None
    this__92.items__190 = items__192
    return return__94
  def __init__(this__92, items__192):
    this__92.constructor__191(items__192)
  def getitems__354(this__355):
    return__356 = this__355.items__190
    return return__356
  items = property(getitems__354, None)
def Match(*args_1256):
  return Match__29(*args_1256)
class Match__29(TemperObject1):
  def constructor__194(this__95, groups__195):
    return__97 = None
    this__95.groups__193 = groups__195
    return return__97
  def __init__(this__95, groups__195):
    this__95.constructor__194(groups__195)
  def getgroups__358(this__359):
    return__360 = this__359.groups__193
    return return__360
  groups = property(getgroups__358, None)
def Group(*args_1257):
  return Group__30(*args_1257)
class Group__30(TemperObject1):
  def constructor__199(this__98, name__200, value__201, codePointsBegin__202):
    return__99 = None
    this__98.name__196 = name__200
    this__98.value__197 = value__201
    this__98.codePointsBegin__198 = codePointsBegin__202
    return return__99
  def __init__(this__98, name__200, value__201, codePointsBegin__202):
    this__98.constructor__199(name__200, value__201, codePointsBegin__202)
  def getname__362(this__363):
    return__364 = this__363.name__196
    return return__364
  def getvalue__366(this__367):
    return__368 = this__367.value__197
    return return__368
  def getcodePointsBegin__370(this__371):
    return__372 = this__371.codePointsBegin__198
    return return__372
  name = property(getname__362, None)
  value = property(getvalue__366, None)
  code_points_begin = property(getcodePointsBegin__370, None)
def RegexRefs__128(*args_1258):
  return RegexRefs__31(*args_1258)
class RegexRefs__31(TemperObject1):
  def constructor__206(this__100, code_points = ..., match__208 = ..., or_object = ...):
    codePoints__207 = code_points
    match__208 = match__208
    orObject__209 = or_object
    return__101 = None
    if codePoints__207 is ...:
      t_1174 = CodePoints('')
      codePoints__207 = t_1174
    if match__208 is ...:
      t_1176 = Group('', '', 0)
      t_1178 = Match((t_1176,))
      match__208 = t_1178
    if orObject__209 is ...:
      t_1179 = Or(())
      orObject__209 = t_1179
    this__100.codePoints__203 = codePoints__207
    this__100.match__204 = match__208
    this__100.orObject__205 = orObject__209
    return return__101
  def __init__(this__100, code_points = ..., match__208 = ..., or_object = ...):
    codePoints__207 = code_points
    match__208 = match__208
    orObject__209 = or_object
    this__100.constructor__206(codePoints__207, match__208, orObject__209)
  def getcodePoints__374(this__375):
    return__376 = this__375.codePoints__203
    return return__376
  def getmatch__378(this__379):
    return__380 = this__379.match__204
    return return__380
  def getorObject__382(this__383):
    return__384 = this__383.orObject__205
    return return__384
  code_points = property(getcodePoints__374, None)
  match = property(getmatch__378, None)
  or_object = property(getorObject__382, None)
def CompiledRegex(*args_1259):
  return CompiledRegex__32(*args_1259)
class CompiledRegex__32(TemperObject1):
  def constructor__212(this__33, data__213):
    return__102 = None
    this__33.data__211 = data__213
    t_1168 = this__33.format()
    t_1169 = compiled_regex_compile_formatted_1260(this__33, t_1168)
    this__33.compiled__221 = t_1169
    return return__102
  def __init__(this__33, data__213):
    this__33.constructor__212(data__213)
  def foundIn(this__34, text__216):
    t_1167 = compiled_regex_compiled_found_in_1261(this__34, this__34.compiled__221, text__216)
    return__103 = t_1167
    return return__103
  def find(this__35, text__219):
    t_824 = compiled_regex_compiled_find_1262(this__35, this__35.compiled__221, text__219, regexRefs__210)
    return__104 = t_824
    return return__104
  def format(this__39):
    t_1160 = RegexFormatter__129()
    t_1161 = t_1160.format(this__39.data__211)
    return__108 = t_1161
    return return__108
  def getdata__386(this__387):
    return__388 = this__387.data__211
    return return__388
  data = property(getdata__386, None)
  compiled = property(None, None)
def RegexFormatter__129(*args_1263):
  return RegexFormatter__40(*args_1263)
class RegexFormatter__40(TemperObject1):
  def format(this__41, regex__238):
    this__41.pushRegex(regex__238)
    t_1156 = this__41.out__236
    def fn__1152(x__240):
      return__895 = x__240
      return return__895
    t_1155 = fn__1152
    t_1157 = list_join_1264(t_1156, '', t_1155)
    return__112 = t_1157
    return return__112
  def pushRegex(this__42, regex__242):
    return__113 = None
    try:
      cast_by_type4(regex__242, Capture__12)
      t_785 = True
    except Exception5:
      t_785 = False
    with Label6() as s_1265:
      if t_785:
        try:
          t_786 = cast_by_type4(regex__242, Capture__12)
        except Exception5:
          s_1265.break_()
        this__42.pushCapture(t_786)
      else:
        try:
          cast_by_type4(regex__242, CodePoints__14)
          t_789 = True
        except Exception5:
          t_789 = False
        if t_789:
          try:
            t_790 = cast_by_type4(regex__242, CodePoints__14)
          except Exception5:
            s_1265.break_()
          this__42.pushCodePoints(t_790, False)
        else:
          try:
            cast_by_type4(regex__242, CodeRange__24)
            t_793 = True
          except Exception5:
            t_793 = False
          if t_793:
            try:
              t_794 = cast_by_type4(regex__242, CodeRange__24)
            except Exception5:
              s_1265.break_()
            this__42.pushCodeRange(t_794)
          else:
            try:
              cast_by_type4(regex__242, CodeSet__25)
              t_797 = True
            except Exception5:
              t_797 = False
            if t_797:
              try:
                t_798 = cast_by_type4(regex__242, CodeSet__25)
              except Exception5:
                s_1265.break_()
              this__42.pushCodeSet(t_798)
            else:
              try:
                cast_by_type4(regex__242, Or__26)
                t_801 = True
              except Exception5:
                t_801 = False
              if t_801:
                try:
                  t_802 = cast_by_type4(regex__242, Or__26)
                except Exception5:
                  s_1265.break_()
                this__42.pushOr(t_802)
              else:
                try:
                  cast_by_type4(regex__242, Repeat__27)
                  t_805 = True
                except Exception5:
                  t_805 = False
                if t_805:
                  try:
                    t_806 = cast_by_type4(regex__242, Repeat__27)
                  except Exception5:
                    s_1265.break_()
                  this__42.pushRepeat(t_806)
                else:
                  try:
                    cast_by_type4(regex__242, Sequence__28)
                    t_809 = True
                  except Exception5:
                    t_809 = False
                  if t_809:
                    try:
                      t_810 = cast_by_type4(regex__242, Sequence__28)
                    except Exception5:
                      s_1265.break_()
                    this__42.pushSequence(t_810)
                  elif generic_eq_1266(regex__242, Begin):
                    try:
                      list_builder_add_1267(this__42.out__236, '^')
                    except Exception5:
                      s_1265.break_()
                  elif generic_eq_1266(regex__242, Dot):
                    try:
                      list_builder_add_1267(this__42.out__236, '.')
                    except Exception5:
                      s_1265.break_()
                  elif generic_eq_1266(regex__242, End):
                    try:
                      list_builder_add_1267(this__42.out__236, '$')
                    except Exception5:
                      s_1265.break_()
                  elif generic_eq_1266(regex__242, WordBoundary):
                    try:
                      list_builder_add_1267(this__42.out__236, '\\b')
                    except Exception5:
                      s_1265.break_()
                  elif generic_eq_1266(regex__242, Digit):
                    try:
                      list_builder_add_1267(this__42.out__236, '\\d')
                    except Exception5:
                      s_1265.break_()
                  elif generic_eq_1266(regex__242, Space):
                    try:
                      list_builder_add_1267(this__42.out__236, '\\s')
                    except Exception5:
                      s_1265.break_()
                  elif generic_eq_1266(regex__242, Word):
                    try:
                      list_builder_add_1267(this__42.out__236, '\\w')
                    except Exception5:
                      s_1265.break_()
      return return__113
    raise NoResultException7()
  def pushCapture(this__43, capture__245):
    return__114 = None
    list_builder_add_1267(this__43.out__236, '(')
    t_780 = this__43.out__236
    t_1138 = capture__245.name
    regex_formatter_push_capture_name_1268(this__43, t_780, t_1138)
    t_1140 = capture__245.item
    this__43.pushRegex(t_1140)
    list_builder_add_1267(this__43.out__236, ')')
    return return__114
  def pushCode(this__45, code__252, insideCodeSet__253):
    return__116 = None
    regex_formatter_push_code_to_1269(this__45, this__45.out__236, code__252, insideCodeSet__253)
    return return__116
  def pushCodePoints(this__47, codePoints__261, insideCodeSet__262):
    return__118 = None
    t_1126 = codePoints__261.value
    t_1132 = string_code_points_1239(t_1126)
    slice__264 = t_1132
    while True:
      t_1127 = slice__264.is_empty
      t_1131 = bool_not_1270(t_1127)
      if t_1131:
        t_1128 = slice__264.read()
        this__47.pushCode(t_1128, insideCodeSet__262)
        t_1129 = slice__264.advance(1)
        slice__264 = t_1129
      else:
        break
    return return__118
  def pushCodeRange(this__48, codeRange__266):
    return__119 = None
    list_builder_add_1267(this__48.out__236, '[')
    this__48.pushCodeRangeUnwrapped(codeRange__266)
    list_builder_add_1267(this__48.out__236, ']')
    return return__119
  def pushCodeRangeUnwrapped(this__49, codeRange__269):
    return__120 = None
    t_1119 = codeRange__269.min
    this__49.pushCode(t_1119, True)
    list_builder_add_1267(this__49.out__236, '-')
    t_1121 = codeRange__269.max
    this__49.pushCode(t_1121, True)
    return return__120
  def pushCodeSet(this__50, codeSet__272):
    return__121 = None
    t_1111 = this__50.adjustCodeSet(codeSet__272, regexRefs__210)
    adjusted__274 = t_1111
    try:
      cast_by_type4(adjusted__274, CodeSet__25)
      t_747 = True
    except Exception5:
      t_747 = False
    with Label6() as s_1271:
      if t_747:
        with Label6() as s_1272:
          try:
            t_748 = cast_by_type4(adjusted__274, CodeSet__25)
            list_builder_add_1267(this__50.out__236, '[')
          except Exception5:
            s_1272.break_()
          t_1117 = t_748.negated
          if t_1117:
            try:
              list_builder_add_1267(this__50.out__236, '^')
            except Exception5:
              s_1272.break_()
          i__275 = 0
          while True:
            t_1113 = t_748.items
            t_1116 = len_1273(t_1113)
            try:
              t_753 = generic_lt_1274(i__275, t_1116)
            except Exception5:
              break
            if t_753:
              t_1114 = t_748.items
              try:
                t_756 = list_get_1275(t_1114, i__275)
              except Exception5:
                break
              this__50.pushCodeSetItem(t_756)
              t_754 = i__275 + 1
              i__275 = t_754
            else:
              try:
                list_builder_add_1267(this__50.out__236, ']')
              except Exception5:
                s_1272.break_()
              s_1271.break_()
        raise NoResultException7()
      this__50.pushRegex(adjusted__274)
    return return__121
  def adjustCodeSet(this__51, codeSet__277, regexRefs__278):
    return__122 = codeSet__277
    return return__122
  def pushCodeSetItem(this__52, codePart__281):
    return__123 = None
    try:
      cast_by_type4(codePart__281, CodePoints__14)
      t_734 = True
    except Exception5:
      t_734 = False
    with Label6() as s_1276:
      if t_734:
        try:
          t_735 = cast_by_type4(codePart__281, CodePoints__14)
        except Exception5:
          s_1276.break_()
        this__52.pushCodePoints(t_735, True)
      else:
        try:
          cast_by_type4(codePart__281, CodeRange__24)
          t_738 = True
        except Exception5:
          t_738 = False
        if t_738:
          try:
            t_739 = cast_by_type4(codePart__281, CodeRange__24)
          except Exception5:
            s_1276.break_()
          this__52.pushCodeRangeUnwrapped(t_739)
        else:
          try:
            cast_by_type4(codePart__281, SpecialSet__20)
            t_742 = True
          except Exception5:
            t_742 = False
          if t_742:
            try:
              t_743 = cast_by_type4(codePart__281, SpecialSet__20)
            except Exception5:
              s_1276.break_()
            this__52.pushRegex(t_743)
      return return__123
    raise NoResultException7()
  def pushOr(this__53, or__284):
    return__124 = None
    t_1096 = or__284.items
    t_1104 = not t_1096
    t_1103 = bool_not_1270(t_1104)
    with Label6() as s_1278:
      if t_1103:
        with Label6() as s_1279:
          try:
            list_builder_add_1267(this__53.out__236, '(?:')
            t_1101 = or__284.items
            t_722 = list_get_1275(t_1101, 0)
          except Exception5:
            s_1279.break_()
          this__53.pushRegex(t_722)
          i__286 = 1
          while True:
            t_1097 = or__284.items
            t_1100 = len_1273(t_1097)
            try:
              t_726 = generic_lt_1274(i__286, t_1100)
            except Exception5:
              break
            if t_726:
              try:
                list_builder_add_1267(this__53.out__236, '|')
                t_1098 = or__284.items
                t_729 = list_get_1275(t_1098, i__286)
              except Exception5:
                break
              this__53.pushRegex(t_729)
              t_727 = i__286 + 1
              i__286 = t_727
            else:
              try:
                list_builder_add_1267(this__53.out__236, ')')
              except Exception5:
                s_1279.break_()
              s_1278.break_()
        raise NoResultException7()
    return return__124
  def pushRepeat(this__54, repeat__288):
    return__125 = None
    with Label6() as s_1280:
      try:
        list_builder_add_1267(this__54.out__236, '(?:')
        t_1089 = repeat__288.item
        this__54.pushRegex(t_1089)
        list_builder_add_1267(this__54.out__236, ')')
        t_1091 = repeat__288.min
        min__290 = t_1091
        t_700 = repeat__288.max
      except Exception5:
        s_1280.break_()
      max__291 = t_700
      if generic_eq_1266(min__290, 0):
        t_701 = generic_eq_1266(max__291, 1)
      else:
        t_701 = False
      if t_701:
        try:
          list_builder_add_1267(this__54.out__236, '?')
        except Exception5:
          s_1280.break_()
      else:
        if generic_eq_1266(min__290, 0):
          t_703 = generic_eq_1266(max__291, None)
        else:
          t_703 = False
        if t_703:
          try:
            list_builder_add_1267(this__54.out__236, '*')
          except Exception5:
            s_1280.break_()
        else:
          if generic_eq_1266(min__290, 1):
            t_705 = generic_eq_1266(max__291, None)
          else:
            t_705 = False
          if t_705:
            try:
              list_builder_add_1267(this__54.out__236, '+')
            except Exception5:
              s_1280.break_()
          else:
            t_708 = this__54.out__236
            t_1092 = int_to_string_1240(min__290)
            try:
              list_builder_add_1267(t_708, str_cat_1241('{', t_1092))
            except Exception5:
              s_1280.break_()
            if generic_not_eq_1281(min__290, max__291):
              try:
                list_builder_add_1267(this__54.out__236, ',')
              except Exception5:
                s_1280.break_()
              if generic_not_eq_1281(max__291, None):
                t_711 = this__54.out__236
                try:
                  t_709 = cast_by_test9(max__291, isinstance_int8)
                  t_1093 = int_to_string_1240(t_709)
                  list_builder_add_1267(t_711, t_1093)
                except Exception5:
                  s_1280.break_()
            try:
              list_builder_add_1267(this__54.out__236, '}')
            except Exception5:
              s_1280.break_()
      t_1094 = repeat__288.reluctant
      if t_1094:
        try:
          list_builder_add_1267(this__54.out__236, '?')
        except Exception5:
          s_1280.break_()
      return return__125
    raise NoResultException7()
  def pushSequence(this__55, sequence__293):
    return__126 = None
    i__295 = 0
    with Label6() as s_1282:
      while True:
        t_1084 = sequence__293.items
        t_1087 = len_1273(t_1084)
        try:
          t_691 = generic_lt_1274(i__295, t_1087)
        except Exception5:
          break
        if t_691:
          t_1085 = sequence__293.items
          try:
            t_694 = list_get_1275(t_1085, i__295)
          except Exception5:
            break
          this__55.pushRegex(t_694)
          t_692 = i__295 + 1
          i__295 = t_692
        else:
          s_1282.break_()
      raise NoResultException7()
    return return__126
  def maxCode(this__56, codePart__297):
    try:
      cast_by_type4(codePart__297, CodePoints__14)
      t_663 = True
    except Exception5:
      t_663 = False
    with Label6() as s_1283:
      if t_663:
        try:
          t_664 = cast_by_type4(codePart__297, CodePoints__14)
        except Exception5:
          s_1283.break_()
        t_1073 = t_664.value
        value__299 = t_1073
        t_1074 = not value__299
        if t_1074:
          t_674 = None
        else:
          max__300 = 0
          t_1075 = string_code_points_1239(value__299)
          slice__301 = t_1075
          while True:
            t_1076 = slice__301.is_empty
            t_1079 = bool_not_1270(t_1076)
            if t_1079:
              t_1077 = slice__301.read()
              next__302 = t_1077
              try:
                t_672 = generic_gt_eq_1284(next__302, max__300)
              except Exception5:
                s_1283.break_()
              if t_672:
                max__300 = next__302
              t_1078 = slice__301.advance(1)
              slice__301 = t_1078
            else:
              break
          t_673 = max__300
          t_674 = t_673
        t_688 = t_674
      else:
        try:
          cast_by_type4(codePart__297, CodeRange__24)
          t_678 = True
        except Exception5:
          t_678 = False
        if t_678:
          try:
            t_679 = cast_by_type4(codePart__297, CodeRange__24)
          except Exception5:
            s_1283.break_()
          t_1080 = t_679.max
          t_688 = t_1080
        elif generic_eq_1266(codePart__297, Digit):
          t_1070 = string_code_points_1239('9')
          t_1081 = t_1070.read()
          t_688 = t_1081
        elif generic_eq_1266(codePart__297, Space):
          t_1071 = string_code_points_1239(' ')
          t_1082 = t_1071.read()
          t_688 = t_1082
        elif generic_eq_1266(codePart__297, Word):
          t_1072 = string_code_points_1239('z')
          t_1083 = t_1072.read()
          t_688 = t_1083
        else:
          t_688 = None
      try:
        return__127 = t_688
        return return__127
      except Exception5:
        pass
    raise NoResultException7()
  def constructor__303(this__109, out = ...):
    out__304 = out
    return__111 = None
    if out__304 is ...:
      t_1066 = list_1285()
      out__304 = t_1066
    this__109.out__236 = out__304
    return return__111
  def __init__(this__109, out = ...):
    out__304 = out
    this__109.constructor__303(out__304)
  out = property(None, None)
def Begin__146(*args_1286):
  return Begin__16(*args_1286)
class Begin__16(Special__15, TemperObject1):
  def constructor__147(this__64):
    return__65 = None
    return return__65
  def __init__(this__64):
    this__64.constructor__147()
t_1231 = Begin__146()
Begin = t_1231
def Dot__148(*args_1287):
  return Dot__17(*args_1287)
class Dot__17(Special__15, TemperObject1):
  def constructor__149(this__66):
    return__67 = None
    return return__67
  def __init__(this__66):
    this__66.constructor__149()
t_1232 = Dot__148()
Dot = t_1232
def End__150(*args_1288):
  return End__18(*args_1288)
class End__18(Special__15, TemperObject1):
  def constructor__151(this__68):
    return__69 = None
    return return__69
  def __init__(this__68):
    this__68.constructor__151()
t_1233 = End__150()
End = t_1233
def WordBoundary__152(*args_1289):
  return WordBoundary__19(*args_1289)
class WordBoundary__19(Special__15, TemperObject1):
  def constructor__153(this__70):
    return__71 = None
    return return__71
  def __init__(this__70):
    this__70.constructor__153()
t_1234 = WordBoundary__152()
WordBoundary = t_1234
def Digit__154(*args_1290):
  return Digit__21(*args_1290)
class Digit__21(SpecialSet__20, TemperObject1):
  def constructor__155(this__72):
    return__73 = None
    return return__73
  def __init__(this__72):
    this__72.constructor__155()
t_1235 = Digit__154()
Digit = t_1235
def Space__156(*args_1291):
  return Space__22(*args_1291)
class Space__22(SpecialSet__20, TemperObject1):
  def constructor__157(this__74):
    return__75 = None
    return return__75
  def __init__(this__74):
    this__74.constructor__157()
t_1236 = Space__156()
Space = t_1236
def Word__158(*args_1292):
  return Word__23(*args_1292)
class Word__23(SpecialSet__20, TemperObject1):
  def constructor__159(this__76):
    return__77 = None
    return return__77
  def __init__(this__76):
    this__76.constructor__159()
t_1237 = Word__158()
Word = t_1237
def entire(item__182):
  global Begin, End, Sequence
  t_1197 = Sequence((Begin, item__182, End))
  return__89 = t_1197
  return return__89
def one_or_more(item__184, reluctant = ...):
  reluctant__185 = reluctant
  global Repeat
  if reluctant__185 is ...:
    reluctant__185 = False
  t_1195 = Repeat(item__184, 1, None, reluctant__185)
  return__90 = t_1195
  return return__90
def optional(item__187, reluctant = ...):
  reluctant__188 = reluctant
  global Repeat
  if reluctant__188 is ...:
    reluctant__188 = False
  t_1192 = Repeat(item__187, 0, 1, reluctant__188)
  return__91 = t_1192
  return return__91
t_1238 = RegexRefs__128()
regexRefs__210 = t_1238
return__894 = RegexFormatter__129
export = return__894
