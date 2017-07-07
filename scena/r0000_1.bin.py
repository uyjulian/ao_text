from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r0000_1.bin",                # FileName
        "r0000",                    # MapName
        "r0000",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [100, 0, 0, 0, 83952996, 83952897, 5, 1, 1380, 1281, 1281, 1281, 84215045, 5, 83887460, 1280, 512, 5, 0, 2, 0, 0, 0],
    )

    BuildStringList((
        "r0000_1",                # 0
    ))

    ChipFrameInfo(356, 0)                                        # 0

    ScpFunction((
        "Function_0_164",          # 00, 0
        "Function_1_1FA",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_D36",          # 03, 3
        "Function_4_14D3",         # 04, 4
        "Function_5_18D4",         # 05, 5
        "Function_6_1C2D",         # 06, 6
        "Function_7_1C6E",         # 07, 7
    ))


    def Function_0_164(): pass

    label("Function_0_164")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I found something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF")
    Call(1, 5)
    Jump("loc_1F9")

    label("loc_1AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7")
    Call(1, 4)
    Jump("loc_1F9")

    label("loc_1D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 5)), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F6")
    Call(1, 3)
    Jump("loc_1F9")

    label("loc_1F6")

    Call(1, 2)

    label("loc_1F9")

    Return()

    # Function_0_164 end

    def Function_1_1FA(): pass

    label("Function_1_1FA")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224")
    Call(1, 5)
    Jump("loc_24B")

    label("loc_224")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_248")
    Call(1, 4)
    Jump("loc_24B")

    label("loc_248")

    Call(1, 3)

    label("loc_24B")

    Return()

    # Function_1_1FA end

    def Function_2_24C(): pass

    label("Function_2_24C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2AB"),
        (1, "loc_2F9"),
        (2, "loc_347"),
        (3, "loc_395"),
        (4, "loc_3E3"),
        (5, "loc_431"),
        (6, "loc_47F"),
        (7, "loc_4CD"),
        (8, "loc_51B"),
        (9, "loc_569"),
        (SWITCH_DEFAULT, "loc_5B7"),
    )


    label("loc_2AB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '解毒药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('解毒药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_2F9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '软化膏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('软化膏', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_347")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '绝缘胶带'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('绝缘胶带', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_395")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '解冻暖炉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('解冻暖炉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_3E3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '舒缓凝胶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('舒缓凝胶', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_431")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '冷却喷雾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('冷却喷雾', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_47F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '眼药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('眼药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_4CD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '提神薄荷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('提神薄荷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_51B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '苏醒药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('苏醒药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_569")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '镇静剂'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('镇静剂', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_5B7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_605")

    Jump("loc_D35")

    label("loc_60A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6DA"),
        (18, "loc_6DA"),
        (25, "loc_6DA"),
        (1, "loc_738"),
        (19, "loc_738"),
        (26, "loc_738"),
        (2, "loc_796"),
        (20, "loc_796"),
        (27, "loc_796"),
        (3, "loc_7F4"),
        (21, "loc_7F4"),
        (28, "loc_7F4"),
        (4, "loc_852"),
        (22, "loc_852"),
        (29, "loc_852"),
        (5, "loc_8B0"),
        (23, "loc_8B0"),
        (30, "loc_8B0"),
        (6, "loc_90E"),
        (24, "loc_90E"),
        (31, "loc_90E"),
        (7, "loc_96C"),
        (8, "loc_9BD"),
        (9, "loc_A0E"),
        (10, "loc_A5F"),
        (11, "loc_AB0"),
        (12, "loc_B01"),
        (13, "loc_B52"),
        (14, "loc_BA3"),
        (15, "loc_BF4"),
        (16, "loc_C45"),
        (17, "loc_C96"),
        (SWITCH_DEFAULT, "loc_CE7"),
    )


    label("loc_6DA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56ISepis of the earth\x07\x00",
            "I picked 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_738")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57IWater sepis\x07\x00",
            "I picked 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x1, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_796")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58IFire Sepis\x07\x00",
            "I picked 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x2, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_7F4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59IWind sepice\x07\x00",
            "I picked 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x3, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_852")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60ITime sepis\x07\x00",
            "I picked 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x4, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_8B0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61IEmpty sepis\x07\x00",
            "I picked 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x5, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_90E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62IPhantom Sepis\x07\x00",
            "I picked 10 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x6, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_96C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '鲑鱼卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鲑鱼卵', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_9BD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('熬炼丸子', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_A0E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '红虫'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('红虫', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_A5F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '蚯蚓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蚯蚓', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_AB0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽兽肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽兽肉', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_B01")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽鱼肉', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_B52")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之壳'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之壳', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_BA3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之卵', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_BF4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽羽翼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽羽翼', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_C45")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之种'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之种', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_C96")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽明胶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽明胶', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_CE7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回复药', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_D35")

    Return()

    # Function_2_24C end

    def Function_3_D36(): pass

    label("Function_3_D36")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_DD0"),
        (1, "loc_E1E"),
        (2, "loc_E6C"),
        (3, "loc_EBA"),
        (4, "loc_F08"),
        (5, "loc_F56"),
        (6, "loc_FA4"),
        (7, "loc_FF2"),
        (8, "loc_1040"),
        (9, "loc_108E"),
        (10, "loc_10DC"),
        (11, "loc_112A"),
        (12, "loc_1178"),
        (13, "loc_11C6"),
        (14, "loc_1214"),
        (15, "loc_1262"),
        (16, "loc_12B0"),
        (17, "loc_12FE"),
        (18, "loc_134C"),
        (19, "loc_139A"),
        (20, "loc_13E8"),
        (21, "loc_1436"),
        (22, "loc_1484"),
        (SWITCH_DEFAULT, "loc_14D2"),
    )


    label("loc_DD0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＨＰ１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_E1E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_E6C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('攻击１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_EBA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('防御１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_F08")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_F56")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔防１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_FA4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('命中１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_FF2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回避１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1040")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('移动１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_108E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('行动力１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_10DC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('妨害１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_112A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ１'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('省ＥＰ１', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1178")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '银胸针'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('银胸针', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_11C6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('珊瑚戒指', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1214")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '英雄戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('英雄戒指', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1262")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '夜光眼镜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('夜光眼镜', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_12B0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '凉爽项链'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('凉爽项链', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_12FE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '打火机'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('打火机', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_134C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('幻彩围巾', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_139A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '叮当耳环'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('叮当耳环', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_13E8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '钢手镯'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('钢手镯', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1436")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '花之瓶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('花之瓶', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1484")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣之链'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('神圣之链', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_14D2")

    Return()

    # Function_3_D36 end

    def Function_4_14D3(): pass

    label("Function_4_14D3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_152B"),
        (1, "loc_1579"),
        (2, "loc_15C7"),
        (3, "loc_1615"),
        (4, "loc_1663"),
        (5, "loc_16B1"),
        (6, "loc_16FF"),
        (7, "loc_174D"),
        (8, "loc_179B"),
        (9, "loc_17E9"),
        (10, "loc_1837"),
        (11, "loc_1885"),
        (SWITCH_DEFAULT, "loc_18D3"),
    )


    label("loc_152B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＨＰ２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1579")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_15C7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('攻击２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1615")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('防御２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1663")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_16B1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔防２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_16FF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('命中２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_174D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回避２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_179B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '移动２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('移动２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_17E9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('行动力２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1837")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '妨害２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('妨害２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1885")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('省ＥＰ２', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_18D3")

    Return()

    # Function_4_14D3 end

    def Function_5_18D4(): pass

    label("Function_5_18D4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1920"),
        (1, "loc_196E"),
        (2, "loc_19BC"),
        (3, "loc_1A0A"),
        (4, "loc_1A58"),
        (5, "loc_1AA6"),
        (6, "loc_1AF4"),
        (7, "loc_1B42"),
        (8, "loc_1B90"),
        (9, "loc_1BDE"),
        (SWITCH_DEFAULT, "loc_1C2C"),
    )


    label("loc_1920")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＨＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＨＰ３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_196E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('ＥＰ３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_19BC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '攻击３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('攻击３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1A0A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '防御３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('防御３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1A58")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '精神３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('精神３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1AA6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔防３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔防３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1AF4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('命中３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1B42")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('回避３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1B90")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '行动力３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('行动力３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1BDE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '省ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('省ＥＰ３', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1C2C")

    Return()

    # Function_5_18D4 end

    def Function_6_1C2D(): pass

    label("Function_6_1C2D")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I found something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 7)
    TalkEnd(0xFF)
    ClearMapFlags(0x80)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C2D end

    def Function_7_1C6E(): pass

    label("Function_7_1C6E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E3")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1CD9"),
        (1, "loc_1D2A"),
        (2, "loc_1D7B"),
        (3, "loc_1DCC"),
        (4, "loc_1E1D"),
        (5, "loc_1E6E"),
        (6, "loc_1EBC"),
        (7, "loc_1F0A"),
        (8, "loc_1F58"),
        (9, "loc_1FA6"),
        (10, "loc_1FF4"),
        (11, "loc_2042"),
        (SWITCH_DEFAULT, "loc_2090"),
    )


    label("loc_1CD9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '鲑鱼卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鲑鱼卵', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1D2A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('熬炼丸子', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1D7B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '红虫'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('红虫', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1DCC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '蚯蚓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蚯蚓', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1E1D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子ＤＸ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('熬炼丸子ＤＸ', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1E6E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽兽肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽兽肉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1EBC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽鱼肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽鱼肉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1F0A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之壳'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之壳', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1F58")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之卵'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之卵', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1FA6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽羽翼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽羽翼', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1FF4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽之种'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽之种', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_2042")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽明胶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽明胶', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_2090")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '魔兽兽肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('魔兽兽肉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_20DE")

    Jump("loc_2915")

    label("loc_20E3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_217D"),
        (1, "loc_21CE"),
        (2, "loc_221F"),
        (3, "loc_2270"),
        (4, "loc_22C1"),
        (5, "loc_2312"),
        (6, "loc_2363"),
        (7, "loc_23B4"),
        (8, "loc_2405"),
        (9, "loc_2456"),
        (10, "loc_24A7"),
        (11, "loc_24F8"),
        (12, "loc_2549"),
        (13, "loc_259A"),
        (14, "loc_25EB"),
        (15, "loc_263C"),
        (16, "loc_268D"),
        (17, "loc_26DE"),
        (18, "loc_272F"),
        (19, "loc_2780"),
        (20, "loc_27D1"),
        (21, "loc_2822"),
        (22, "loc_2873"),
        (SWITCH_DEFAULT, "loc_28C4"),
    )


    label("loc_217D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '发芽糙米'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('发芽糙米', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_21CE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '五谷味噌'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('五谷味噌', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_221F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '百药精酒'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('百药精酒', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2270")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '朝摘香叶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked five pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('朝摘香叶', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_22C1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '清绿香草'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked five pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('清绿香草', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2312")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '胡椒粒'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked 8 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('胡椒粒', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2363")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '热辣椒'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked 8 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('热辣椒', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_23B4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '香油'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked 8 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('香油', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2405")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '蜂蜜糖浆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked 8 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蜂蜜糖浆', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2456")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '粗碎岩盐'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked 8 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('粗碎岩盐', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_24A7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新磨小麦粉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked 8 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新磨小麦粉', 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_24F8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜牛奶'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up 4 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜牛奶', 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2549")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜奶酪'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up 4 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜奶酪', 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_259A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜鸡蛋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up 4 pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜鸡蛋', 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_25EB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '铃铛草莓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up three.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('铃铛草莓', 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_263C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑暗菇'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up three.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('黑暗菇', 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_268D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '七彩豆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up three.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('七彩豆', 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_26DE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '国王马铃薯'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked five pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('国王马铃薯', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_272F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '万能青葱'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked five pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('万能青葱', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2780")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '迷你胡萝卜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked five pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('迷你胡萝卜', 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_27D1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('苦西红柿', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2822")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '雪花里脊肉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('雪花里脊肉', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2873")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜白肉鱼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜白肉鱼', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_28C4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '新鲜白肉鱼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I picked up two.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('新鲜白肉鱼', 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2915")

    Return()

    # Function_7_1C6E end

    SaveToFile()

Try(main)
