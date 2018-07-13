from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1520.bin",                # FileName
        "c1520",                    # MapName
        "c1520",                    # Location
        0x00AA,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 170, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1520",                  # 0
        "Mayor Dieter",           # 1
        "Arios",                  # 2
        "Detective Dudley",       # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3200,    0,       100000,  2000,    3300,    900,     100000,  0x007C, 0,  3,  0x0000)
    DeclActor(70000,   0,       103200,  2000,    70000,   900,     103300,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(352, 0)                                        # 0

    ScpFunction((
        "Function_0_160",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_2AF",          # 02, 2
        "Function_3_11E5",         # 03, 3
        "Function_4_16DE",         # 04, 4
        "Function_5_258C",         # 05, 5
        "Function_6_2D0D",         # 06, 6
        "Function_7_2ED1",         # 07, 7
        "Function_8_3495",         # 08, 8
        "Function_9_3C36",         # 09, 9
        "Function_10_4125",        # 0A, 10
        "Function_11_4A54",        # 0B, 11
    ))


    def Function_0_160(): pass

    label("Function_0_160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_174")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)
    Jump("loc_1B9")

    label("loc_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_188")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)
    Jump("loc_1B9")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E")
    Event(0, 6)
    Jump("loc_1B9")

    label("loc_19E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9")
    Event(0, 2)

    label("loc_1B9")

    Return()

    # Function_0_160 end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3")
    VolumeBGM(0x46, 0xC8)
    Jump("loc_21C")

    label("loc_1D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21C")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_27B")

    label("loc_235")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E")
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_27B")

    label("loc_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)
    Jump("loc_27B")

    label("loc_267")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)

    label("loc_27B")

    OP_70(0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AE")
    Sound(927, 1, 100, 0)

    label("loc_2AE")

    Return()

    # Function_1_1BA end

    def Function_2_2AF(): pass

    label("Function_2_2AF")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E3")
    SetScenarioFlags(0x0, 0)
    OP_68(0, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 0, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E")
    SetChrPos(0x1, 800, 0, 600, 0)

    label("loc_34E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D")
    SetChrPos(0x2, -800, 0, 600, 0)

    label("loc_36D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C")
    SetChrPos(0x3, 0, 0, -500, 0)

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x4, 800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE")
    SetChrPos(0x5, -800, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_3DE")

    Jump("loc_5F8")

    label("loc_3E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F0")
    SetScenarioFlags(0x0, 1)
    OP_68(70000, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 70000, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45B")
    SetChrPos(0x1, 70800, 0, 600, 0)

    label("loc_45B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A")
    SetChrPos(0x2, 69200, 0, 600, 0)

    label("loc_47A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0x3, 70000, 0, -500, 0)

    label("loc_499")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C2")
    SetChrPos(0x4, 70800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EB")
    SetChrPos(0x5, 69200, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_4EB")

    Jump("loc_5F8")

    label("loc_4F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F8")
    SetScenarioFlags(0x0, 2)
    OP_68(140000, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 140000, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_568")
    SetChrPos(0x1, 140800, 0, 600, 0)

    label("loc_568")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_587")
    SetChrPos(0x2, 139200, 0, 600, 0)

    label("loc_587")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A6")
    SetChrPos(0x3, 140000, 0, -500, 0)

    label("loc_5A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF")
    SetChrPos(0x4, 140800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F8")
    SetChrPos(0x5, 139200, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_5F8")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_63E")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_65B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65B")

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_77B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_690")
    MenuCmd(1, 0, "★[40F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69B")

    label("loc_690")

    MenuCmd(1, 0, "  [40F]")

    label("loc_69B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C4")
    MenuCmd(1, 0, "★[36F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CF")

    label("loc_6C4")

    MenuCmd(1, 0, "  [36F]")

    label("loc_6CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F7")
    MenuCmd(1, 0, "★[21F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_702")

    label("loc_6F7")

    MenuCmd(1, 0, "  [21F]")

    label("loc_702")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72A")
    MenuCmd(1, 0, "★[1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_734")

    label("loc_72A")

    MenuCmd(1, 0, "  [1F]")

    label("loc_734")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75C")
    MenuCmd(1, 0, "★[B8F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_767")

    label("loc_75C")

    MenuCmd(1, 0, "  [B8F]")

    label("loc_767")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A15")

    label("loc_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_865")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD")
    MenuCmd(1, 0, "★[40F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B8")

    label("loc_7AD")

    MenuCmd(1, 0, "  [40F]")

    label("loc_7B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E1")
    MenuCmd(1, 0, "★[36F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7EC")

    label("loc_7E1")

    MenuCmd(1, 0, "  [36F]")

    label("loc_7EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_814")
    MenuCmd(1, 0, "★[21F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81F")

    label("loc_814")

    MenuCmd(1, 0, "  [21F]")

    label("loc_81F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_847")
    MenuCmd(1, 0, "★[1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_851")

    label("loc_847")

    MenuCmd(1, 0, "  [1F]")

    label("loc_851")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A15")

    label("loc_865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_8E7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_896")
    MenuCmd(1, 0, "★[21F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A1")

    label("loc_896")

    MenuCmd(1, 0, "  [21F]")

    label("loc_8A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9")
    MenuCmd(1, 0, "★[1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D3")

    label("loc_8C9")

    MenuCmd(1, 0, "  [1F]")

    label("loc_8D3")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A15")

    label("loc_8E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_96A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919")
    MenuCmd(1, 0, "★[40F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_924")

    label("loc_919")

    MenuCmd(1, 0, "  [40F]")

    label("loc_924")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94C")
    MenuCmd(1, 0, "★[1F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_956")

    label("loc_94C")

    MenuCmd(1, 0, "  [1F]")

    label("loc_956")

    MenuCmd(1, 0, "  [Get Off]")
    Jump("loc_A15")

    label("loc_96A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    MenuCmd(1, 0, "★[36F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99E")

    label("loc_993")

    MenuCmd(1, 0, "  [36F]")

    label("loc_99E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C7")
    MenuCmd(1, 0, "★[35F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D2")

    label("loc_9C7")

    MenuCmd(1, 0, "  [35F]")

    label("loc_9D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FB")
    MenuCmd(1, 0, "★[34F]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A06")

    label("loc_9FB")

    MenuCmd(1, 0, "  [34F]")

    label("loc_A06")

    MenuCmd(1, 0, "  [Get Off]")

    label("loc_A15")

    MenuCmd(2, 0, 10, 10, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_AE2")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADD")

    label("loc_A4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADD")

    label("loc_A6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A88")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADD")

    label("loc_A88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADD")

    label("loc_AA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADD")

    label("loc_AC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADD")

    Jump("loc_CBA")

    label("loc_AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_B81")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B09")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B7C")

    label("loc_B09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B27")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B7C")

    label("loc_B27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B45")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B7C")

    label("loc_B45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B63")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B7C")

    label("loc_B63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B7C")

    Jump("loc_CBA")

    label("loc_B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_BE4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF")

    label("loc_BA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BDF")

    label("loc_BC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDF")

    Jump("loc_CBA")

    label("loc_BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_C47")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C0B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C42")

    label("loc_C0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C29")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C42")

    label("loc_C29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C42")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C42")

    Jump("loc_CBA")

    label("loc_C47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C65")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CBA")

    label("loc_C65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C83")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CBA")

    label("loc_C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CBA")

    label("loc_CA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD9")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_E1A")

    label("loc_CD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D74")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x64, 0x87, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x87, 0x9A, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D30")
    OP_68(0, 4000, 1000, 2000)
    Jump("loc_D69")

    label("loc_D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D4F")
    OP_68(70000, 4000, 1000, 2000)
    Jump("loc_D69")

    label("loc_D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D69")
    OP_68(140000, 4000, 1000, 2000)

    label("loc_D69")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_E1A")

    label("loc_D74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E0F")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x0, 0x23, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DCB")
    OP_68(0, -3500, 1000, 2000)
    Jump("loc_E04")

    label("loc_DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DEA")
    OP_68(70000, -3500, 1000, 2000)
    Jump("loc_E04")

    label("loc_DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E04")
    OP_68(140000, -3500, 1000, 2000)

    label("loc_E04")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_E1A")

    label("loc_E0F")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_E1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE5")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_E5D"),
        (1, "loc_EA4"),
        (2, "loc_EEB"),
        (3, "loc_F32"),
        (4, "loc_F79"),
        (5, "loc_F89"),
        (6, "loc_FD0"),
        (SWITCH_DEFAULT, "loc_FE0"),
    )


    label("loc_E5D")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E76")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_E9F")

    label("loc_E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E8D")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_E9F")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E9F")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_E9F")

    Jump("loc_FE0")

    label("loc_EA4")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EBD")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_EE6")

    label("loc_EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_ED4")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_EE6")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EE6")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_EE6")

    Jump("loc_FE0")

    label("loc_EEB")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F04")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_F2D")

    label("loc_F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F1B")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_F2D")

    label("loc_F1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F2D")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_F2D")

    Jump("loc_FE0")

    label("loc_F32")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F4B")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_F74")

    label("loc_F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F62")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_F74")

    label("loc_F62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F74")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_F74")

    Jump("loc_FE0")

    label("loc_F79")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()
    Jump("loc_FE0")

    label("loc_F89")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FA2")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_FCB")

    label("loc_FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FB9")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_FCB")

    label("loc_FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FCB")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_FCB")

    Jump("loc_FE0")

    label("loc_FD0")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_FE0")

    label("loc_FE0")

    Jump("loc_11E4")

    label("loc_FE5")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_101F"),
        (1, "loc_1092"),
        (2, "loc_10D9"),
        (3, "loc_1120"),
        (4, "loc_1167"),
        (5, "loc_118D"),
        (6, "loc_11D4"),
        (SWITCH_DEFAULT, "loc_11E4"),
    )


    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1035")
    Call(0, 7)
    Jump("loc_108D")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104B")
    Call(0, 10)
    Jump("loc_108D")

    label("loc_104B")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1064")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_108D")

    label("loc_1064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_107B")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_108D")

    label("loc_107B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_108D")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_108D")

    Jump("loc_11E4")

    label("loc_1092")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10AB")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_10D4")

    label("loc_10AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10C2")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_10D4")

    label("loc_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10D4")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_10D4")

    Jump("loc_11E4")

    label("loc_10D9")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10F2")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_111B")

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1109")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_111B")

    label("loc_1109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_111B")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_111B")

    Jump("loc_11E4")

    label("loc_1120")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1139")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_1162")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1150")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_1162")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1162")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_1162")

    Jump("loc_11E4")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_117D")
    Call(0, 8)
    Jump("loc_1188")

    label("loc_117D")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()

    label("loc_1188")

    Jump("loc_11E4")

    label("loc_118D")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11A6")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_11CF")

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11BD")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_11CF")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11CF")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_11CF")

    Jump("loc_11E4")

    label("loc_11D4")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_11E4")

    label("loc_11E4")

    Return()

    # Function_2_2AF end

    def Function_3_11E5(): pass

    label("Function_3_11E5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is an elevator control panel.\x01",
            "Operate it?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D6")
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_135C")
    SetChrPos(0x0, 1800, 0, 100000, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1299")
    SetChrPos(0x1, 600, 0, 100800, 90)

    label("loc_1299")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B8")
    SetChrPos(0x2, 600, 0, 99200, 90)

    label("loc_12B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12D7")
    SetChrPos(0x3, -500, 0, 100000, 90)

    label("loc_12D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1300")
    SetChrPos(0x4, -1600, 0, 100800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1300")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1329")
    SetChrPos(0x5, -1600, 0, 99200, 90)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1329")

    OP_68(1000, 1000, 100000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_1461")

    label("loc_135C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1461")
    SetChrPos(0x0, 70000, 0, 101800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A3")
    SetChrPos(0x1, 70800, 0, 100600, 0)

    label("loc_13A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C2")
    SetChrPos(0x2, 69200, 0, 100600, 0)

    label("loc_13C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E1")
    SetChrPos(0x3, 70000, 0, 99500, 0)

    label("loc_13E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140A")
    SetChrPos(0x4, 70800, 0, 98400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_140A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1433")
    SetChrPos(0x5, 69200, 0, 98400, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1433")

    OP_68(70000, 1000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)

    label("loc_1461")

    OP_0D()
    Sleep(500)
    Sound(159, 0, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148F")
    OP_68(1000, -9000, 100000, 3000)
    Jump("loc_14F6")

    label("loc_148F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B3")
    OP_68(1000, 9000, 100000, 3000)
    Jump("loc_14F6")

    label("loc_14B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D7")
    OP_68(70000, -9000, 101000, 3000)
    Jump("loc_14F6")

    label("loc_14D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F6")
    OP_68(70000, 9000, 101000, 3000)

    label("loc_14F6")

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1521")
    Call(0, 9)
    Return()

    label("loc_1521")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155C")
    Sound(832, 2, 100, 0)
    OP_68(1000, 9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_1608")

    label("loc_155C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1597")
    Sound(832, 2, 100, 0)
    OP_68(1000, -9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_1608")

    label("loc_1597")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D2")
    Sound(832, 2, 100, 0)
    OP_68(70000, 9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)
    Jump("loc_1608")

    label("loc_15D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1608")
    Sound(832, 2, 100, 0)
    OP_68(70000, -9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)

    label("loc_1608")

    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    StopSound(832, 1000, 100)
    Sound(160, 0, 100, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1645")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_16A6")

    label("loc_1645")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1667")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_16A6")

    label("loc_1667")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1689")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)
    Jump("loc_16A6")

    label("loc_1689")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A6")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)

    label("loc_16A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BE")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_16BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D6")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_16D6")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_11E5 end

    def Function_4_16DE(): pass

    label("Function_4_16DE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SoundLoad(832)
    OP_68(70000, 2100, 1000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 70000, 0, 0, 0)
    SetChrPos(0x102, 68700, 0, -600, 0)
    SetChrPos(0x103, 69300, 0, -1600, 0)
    SetChrPos(0x104, 70600, 0, -1000, 315)
    SetChrPos(0x109, 67400, 0, -600, 45)
    SetChrPos(0x105, 71600, 0, -1600, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 70000, 0, 1800, 180)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    VolumeBGM(0x50, 0x3E8)
    Sound(832, 2, 100, 0)
    Sleep(1000)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        "──I see.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            "I heard that from Dudley too.\x01",
            "The situation is indeed quite dangerous.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(70000, 1100, 1000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00006FYes...\x02\x03",
            "#00001FThere's the actions of the jaeger corps and the \x01",
            "crime syndicate, and on top of that, the motives \x01",
            "of the Imperial and Republican governments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F...There's the threat of terrorists\x01",
            "aiming for the heads of state, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FThere is also that mysterious hacker, right?\x02\x03",
            "#00200FHe was able to steal the tower blueprints\x01",
            "using one of your terminals?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02806F#5PYeah. It seems the Orchis\x01",
            "Tower sub-terminal was\x01",
            "hacked into.\x02\x03",
            "#02801FAfter the incident at IBC, I had our\x01",
            "systems division strengthen anti-\x01",
            "hacking countermeasures, but...\x02\x03",
            "It seems it wasn't enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm. There's still very\x01",
            "few hackers, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FIt's likely to be someone connected\x01",
            "to the Epstein Foundation, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FChief Roberts is looking into\x01",
            "that possibility as we speak.\x02\x03",
            "#00208FI feel like the hacking this time wasn't by\x01",
            "someone connected to the Foundation, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PWell, we'll just have to wait for\x01",
            "the results of that investigation.\x02\x03",
            "#02801FJaeger corps, a crime syndicate and\x01",
            "terrorists... All of them worry me...\x02\x03",
            "But what worries me even more is their\x01",
            "motive for targeting the heads of state.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00001FTheir motive for targeting the heads of state...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FIn other words, do you think it's someone\x01",
            "connected to the Trade Conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02803F#5PI'm not suspecting Princess\x01",
            "Klaudia and Prince Olivert,\x01",
            "who you guys met.\x02\x03",
            "And I trust the Archduke\x01",
            "of Remiferia as well.\x02\x03",
            "#02801F...The problem is Chancellor\x01",
            "Osborne and President Rocksmith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FThe leaders of the two major powers...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FThose two certainly have the most to gain\x01",
            "from getting their hands on Crossbell's fate.\x02\x03",
            "#10301FAny specific actions they've taken in that regard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02806F#5PNo, the opposite.\x02\x03",
            "#02801F──We sent several proposals\x01",
            "for treaties and accords\x01",
            "for the conference and...\x02\x03",
            "The replies from both sides have\x01",
            "been nothing but favorable.\x02\x03",
            "As if they're really hoping for peace \x01",
            "and growth in West Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00011FT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F...That's definitely strange.\x02\x03",
            "#00101FNormally, those countries clash\x01",
            "over the smallest things...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02803F#5PYeah. I honestly have no idea how\x01",
            "this conference is going to go.\x02\x03",
            "#02801FIt seems I'll need to be prepared\x01",
            "in case things go south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FIndeed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FS-So it's a difficult\x01",
            "situation politically, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PHa ha, well I think I'll ask Chairman\x01",
            "MacDowell for his help as well.\x02\x03",
            "#02800FIf it goes well, Liberl, Remiferia\x01",
            "and others might join me as\x01",
            "allies in this negotiation.\x02\x03",
            "#02809FAnyway, aside from preparing for the worst,\x01",
            "all I can do is pray to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108F"Uncle"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI'm sorry for making you\x01",
            "give us this tour during\x01",
            "such a difficult time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#02804F#5PHa ha, perish the thought.\x02\x03",
            "#02800FOn the contrary, it's just because of the\x01",
            "situation that I wanted a change of pace.\x02\x03",
            "I volunteered specifically\x01",
            "to escort you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FIs that right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10101FWe're honored, Mr. Mayor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FThen, we\x01",
            "gladly accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#02809F#5PYes, leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)

    ChrTalk(
        0x8,
        "#11P#02800FOh, we've arrived.\x02",
    )

    CloseMessageWindow()
    StopSound(832, 1000, 100)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x37, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    Sound(160, 0, 100, 0)
    VolumeBGM(0x64, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(107, 0, 100, 0)
    Sleep(500)
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_16DE end

    def Function_5_258C(): pass

    label("Function_5_258C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("apl/ch51255.itc", 0x20)
    SoundLoad(832)
    OP_68(0, -10000, 0, 0)
    MoveCamera(45, 11, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -600, 0, 0, 225)
    SetChrPos(0x102, 500, 0, 0, 225)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    SetChrPos(0x103, -1500, 0, -1500, 270)
    SetChrPos(0x104, 1600, 0, -1000, 270)
    SetChrPos(0x109, 400, 0, -1300, 270)
    SetChrPos(0x105, 900, 0, -2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -700, 0, 1500, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1900, 0, 1300, 180)
    OP_71(0x0, 0x87, 0x9A, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    BlurSwitch(0x1B58, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 20000, 0, 7000)
    MoveCamera(45, 33, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, -900, 0, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    CancelBlur(0)
    OP_68(0, 1100, 0, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#11P#00203FYes... Yes.\x02\x03",
            "#00202F...Understood. \x01",
            "At least we know that much.\x02\x03",
            "#00204FNice work, Jona.\x01",
            "See you later──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sleep(400)

    ChrTalk(
        0x101,
        "#5P#00001FWhat did Jona say...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    OP_0D()
    OP_93(0x103, 0x2D, 0x1F4)

    ChrTalk(
        0x103,
        (
            "#6P#00203FHe computed the\x01",
            "terrorists' escape route.\x02\x03",
            "#00201FIt seems they escaped to\x01",
            "the Geofront from Orchis\x01",
            "Tower's foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PThe foundation... That's part\x01",
            "of the tower's basement.\x02\x03",
            "#00101FI'm sure it's connected to\x01",
            "several Geofront divisions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00603F#5PAlright, we'll certainly capture them.\x02\x03",
            "#00610FIf they get away after such conduct, it'll be\x01",
            "a stain on the name of the Crossbell Police!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01403F#5P──I feel the same.\x02\x03",
            "#01401FThe Guild has officially witnessed their reckless\x01",
            "actions at this international conference.\x02\x03",
            "It would set a bad precedent\x01",
            "if we were to ignore it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107F#11PYes, let's get them for sure!\x02\x03",
            "#10106FI'm a bit worried about the\x01",
            "orbal bombs on the roof, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B02():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2B02)
    Sleep(50)

    def lambda_2B12():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2B12)
    Sleep(50)

    def lambda_2B22():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2B22)
    Sleep(50)

    def lambda_2B32():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2B32)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#00003F#5PIf Miss Kilika and Mr. Lechter are \x01",
            "handling them, it'll probably be all right.\x02\x03",
            "#00002FCaptain Julia and Major Mueller \x01",
            "are with them, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PHa ha, with those guys there,\x01",
            "things will go well for sure.\x02\x03",
            "#00305F...But it sure is\x01",
            "a long way down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FWe're going from\x01",
            "35F to B8F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#11PIt's taking us to the\x01",
            "depths of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 3100, 0, 2000)
    FadeToDark(2000, 0, -1)
    StopSound(832, 2000, 100)
    OP_0D()
    OP_6F(0x1)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("m0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_258C end

    def Function_6_2D0D(): pass

    label("Function_6_2D0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22250, 0)
    SetChrPos(0x101, 0, 0, 1300, 0)
    SetChrPos(0x102, 800, 0, 0, 0)
    SetChrPos(0x103, -800, 0, 0, 0)
    SetChrPos(0x104, 0, 0, -1600, 0)
    SetChrPos(0x109, 1200, 0, -1000, 0)
    SetChrPos(0x105, -1200, 0, -1000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(21500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#11P#00011FUmm... Is this\x01",
            "where it goes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYes. Please insert the access\x01",
            "card we just got there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, 1000, 800)

    def lambda_2E63():
        OP_96(0xFE, 0x0, 0x0, 0x960, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E63)
    WaitChrThread(0x101, 1)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Inserted the access card into the panel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(72, 0, 100, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x164, 5)
    Call(0, 2)
    Return()

    # Function_6_2D0D end

    def Function_7_2ED1(): pass

    label("Function_7_2ED1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0x109, -1100, 0, 600, 135)
    SetChrPos(0x105, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    Sleep(500)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#6P#10305FBy the way, about that panel...\x02\x03",
            "It doesn't look like there're\x01",
            "buttons for 21F through 30F.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00102FOh, they must all be\x01",
            "maintenance floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PMaintenance floors?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11PI am told those floors are mostly\x01",
            "empty. It is necessary to maintain\x01",
            "this huge tower's weight balance.\x02\x03",
            "#00200FApart from that, it seems there is equipment there\x01",
            "to absorb the shock of potential earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PThat's pretty amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10102FIt seems like the latest building\x01",
            "technologies are all here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FSeriously though. Was it really\x01",
            "necessary to make it this big?\x02\x03",
            "#00301FYou could make it 30 stories and\x01",
            "still have the same number of floors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FWell, I'm sure many changes were\x01",
            "made from the initial design...\x02\x03",
            "#00100F"Uncle", who took over the design,\x01",
            "also likes flashy things...\x02\x03",
            "#00104FIn the end, the Croises made up for the\x01",
            "construction budget shortfall personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FWow, how magnanimous of him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PWell, thanks to him, the tower's\x01",
            "had a huge impact as Crossbell\x01",
            "City's newest landmark, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00002F#5POh, looks like we've arrived.\x02",
    )

    CloseMessageWindow()
    MoveCamera(35, 30, 0, 4000)
    SetCameraDistance(19000, 4000)
    Sleep(3000)
    StopSound(832, 2000, 100)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x37, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x164, 6)
    OP_24(0x340)
    EventEnd(0x5)
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2ED1 end

    def Function_8_3495(): pass

    label("Function_8_3495")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0xF4, -1100, 0, 600, 135)
    SetChrPos(0xF5, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00008F#5P──In the end, we could only\x01",
            "disable security up to 21F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FAccording to Chief Roberts,\x01",
            "there's a physically\x01",
            "isolated terminal on 30F.\x02\x03",
            "#00201FHe says control from the\x01",
            "orbal net is impossible\x01",
            "until it's breached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FThen that means we need to go\x01",
            "from 21F to 30F ourselves.\x02\x03",
            "#00301FBut, I think I remember\x01",
            "something about them bein'\x01",
            "empty maintenance floors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106F...It seems they lied in\x01",
            "the official announcement.\x02\x03",
            "#00108FThe outstanding Crois clan\x01",
            "is somehow mysterious...\x02\x03",
            "#00101FIt seems they had an important\x01",
            "role to play in KeA's ritual too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00307FR-Really?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38AC")

    ChrTalk(
        0x10A,
        (
            "#6P#00606F...I thought it was strange during the\x01",
            "Trade Conference security detail, but...\x02\x03",
            "#00610FI can't believe they created a place\x01",
            "like that inside a public building.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3970")

    ChrTalk(
        0x105,
        (
            "#6P#10403FThey're probably full of the \x01",
            "quintessence of heretic science.\x02\x03",
            "#10408FIf possible, I would've liked a preliminary \x01",
            "inspection before things turned out like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3970")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39C4")

    ChrTalk(
        0x109,
        (
            "#6P#10103FAt any rate...\x01",
            "It seems we need to be prepared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F7")

    label("loc_39C4")


    ChrTalk(
        0x103,
        (
            "#00203F...In any case,\x01",
            "we better be prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A5F")

    ChrTalk(
        0x106,
        (
            "#6P#10701F...Right. \x01",
            "The "Red Constellation" personnel\x01",
            "may be waiting for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC2")

    label("loc_3A5F")


    ChrTalk(
        0x102,
        (
            "#11P#00106FYou're right...\x01",
            "It's possible Mr. Arios and the\x01",
            ""Red Constellation" are there too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC2")


    ChrTalk(
        0x101,
        (
            "#00008F#5PYeah... And KeA.\x02\x03",
            "#00003F...No matter what's waiting for us, \x01",
            "we have to break through it.\x02\x03",
            "#00000FWe have to answer the expectations of\x01",
            "Chief and the others who got us this far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00102F*giggle*... No pressure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00304FLet's get\x01",
            "this thing done!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, -1700, 0, 3000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    OP_6F(0x79)
    WaitBGM()
    ReplaceBGM("ed7352", "ed7000")
    SetScenarioFlags(0x1A6, 1)
    OP_29(0xB1, 0x1, 0xA)
    OP_24(0x340)
    SetScenarioFlags(0x25, 1)
    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3495 end

    def Function_9_3C36(): pass

    label("Function_9_3C36")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 100000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 1500, 0, 100000, 270)
    SetChrPos(0x102, 600, 0, 101100, 225)
    SetChrPos(0x103, -1000, 0, 101100, 135)
    SetChrPos(0x104, -1500, 0, 100000, 90)
    SetChrPos(0xF4, 600, 0, 98900, 315)
    SetChrPos(0xF5, -1000, 0, 98900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    BeginChrThread(0x101, 3, 0, 11)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 100000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00003F#11PCome to think of it...\x02\x03",
            "#00001FYou said there was a control\x01",
            "terminal isolated from the\x01",
            "orbal net, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#5PYes. Because of it,\x01",
            "hacking the tower's upper\x01",
            "floors is impossible.\x02\x03",
            "#00201FIf we unlock it, I think Chief Roberts\x01",
            "will be able to grab detailed info\x01",
            "regarding the upper floors...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FSuch as the location of KeA and what\x01",
            "Bell and the others are planning, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EFF")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FWe've got to gain\x01",
            "control of it somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9A")

    label("loc_3EFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F4D")

    ChrTalk(
        0x109,
        (
            "#12P#10103FWe need to gain\x01",
            "control of it somehow...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F9A")

    label("loc_3F4D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F9A")

    ChrTalk(
        0x106,
        (
            "#12P#10703FWe need to gain\x01",
            "control of it in some way...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FCC")

    ChrTalk(
        0x105,
        "#12P#10401F30F, was it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4039")

    label("loc_3FCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4005")

    ChrTalk(
        0x106,
        "#12P#10701FIt's on 30F, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4039")

    label("loc_4005")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4039")

    ChrTalk(
        0x109,
        "#12P#10101FIt was 30F, was it?\x02",
    )

    CloseMessageWindow()

    label("loc_4039")


    ChrTalk(
        0x103,
        (
            "#00203F#5PYes. The top floor of this\x01",
            "Mystic Core, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FIn that case, let's set\x01",
            "our sights for the top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#11PYeah... Let's do this!\x02",
    )

    CloseMessageWindow()
    OP_68(0, -8700, 100000, 2000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x1A6, 3)
    Sound(160, 0, 100, 0)
    Sleep(500)
    OP_24(0x340)
    EventEnd(0x5)
    ClearMapFlags(0x8000000)
    NewScene("c1582", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_9_3C36 end

    def Function_10_4125(): pass

    label("Function_10_4125")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(832)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0xF4, -1100, 0, 600, 135)
    SetChrPos(0xF5, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4269():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4269)
    Sleep(50)

    def lambda_4279():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_4279)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2085, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013FHello?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "T-Thank goodness...\x01",
            "You're all ok!\x02\x03",
            "This is Merkabah No. 9 speaking!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43A3")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10102FFran...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_43CB")

    label("loc_43A3")

    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00102FMiss Fran...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_43CB")

    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Abbas' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It seems you've infiltrated\x01",
            "the tower. How is it going?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44BC")
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FWe're actually just about finished already.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10400FI'll give you a brief explanation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_451A")

    label("loc_44BC")

    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FWell, we're just about finished.\x01",
            "I'll give you a brief explanation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_451A")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Informed the Merkabah bridge\x01",
            "crew of the current situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Abbas' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I see... It really does seem\x01",
            "like you're almost done.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Jona's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like that white doll\x01",
            "on the roof has deployed a\x01",
            "100-arge radius "barrier".\x02\x03",
            "We can't get any closer so don't\x01",
            "expect cover fire or anything, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013FAlright... I understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4719")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10406FWell, seems we'll have to do\x01",
            "something about it ourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4773")

    label("loc_4719")

    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00306FWell, we'll just have to do\x01",
            "something about it ourselves, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4773")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Fran's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "By the way, the other two Aions...\x01",
            "It seems they have been silenced.\x02\x03",
            "It seems Father Kevin, Miss Estelle and\x01",
            "friends have been doing a great job for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FIs that so...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00204F...That is good news.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300FYeah... Those were\x01",
            "some nice wins.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Grace's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Anyway! Don't do\x01",
            "anything reckless!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("Chairman MacDowell's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "May Aidios protect you...\x01",
            "And please, be very careful out there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00100FWe will...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FRoger that...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_68(0, -1700, 0, 3000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x323)
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("e4201", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_4125 end

    def Function_11_4A54(): pass

    label("Function_11_4A54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A8C")
    OP_82(0x0, 0x5, 0xBB8, 0x1F4)
    Sleep(2000)
    OP_82(0x0, 0xA, 0x3E8, 0x1F4)
    Sleep(1000)
    Jump("Function_11_4A54")

    label("loc_4A8C")

    Return()

    # Function_11_4A54 end

    SaveToFile()

Try(main)
