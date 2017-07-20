﻿from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c100b.bin",                # FileName
        "c100b",                    # MapName
        "c100b",                    # Location
        0x0010,                     # MapIndex
        "ed7513",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 1, 0, 2],
    )

    BuildStringList((
        "c100b",                  # 0
        "Keya",                 # 1
        "Zeit",               # 2
        "Suzuku",                 # 3
        "Arios",               # 4
        "Reception Michelle",           # 5
        "car",                     # 6
        "Mob",                   # 7
        "Mob",                   # 8
        "Central square",               # 9
        "Nishi dori",                 # 10
        "Administrative district",                 # 11
        "Residential area",                 # 12
        "Entertainment district",                 # 13
        "East Street",                 # 14
        "old Town",                 # 15
        "Harbor district",                 # 16
        "IBC",                 # 17
        "Beside the station",               # 18
        "Back street",                 # 19
        "Ursula interchange",           # 20
        "East Crossbell Highway",       # 21
        "West Crossbell Highway",       # 22
        "Mainz Mountain Road",           # 23
        "Orchis Tower",         # 24
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294937296, 4294961796, 4000,    1200,    4294937296, 4294962796, 4000,    0x007C, 0,  3,  0x0000)
    DeclActor(4294944286, 4294952396, 4294962466, 1200,    4294944286, 4294953396, 4294962466, 0x007C, 0,  4,  0x0000)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "Central square")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "Nishi dori")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "Administrative district")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "Residential area")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "Entertainment district")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "East Street")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "old Town")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "Harbor district")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "IBC")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "Beside the station")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "Back street")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-88.0, 0.0, 269.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ChipFrameInfo(1084, 0)                                       # 0

    ScpFunction((
        "Function_0_43C",          # 00, 0
        "Function_1_4EC",          # 01, 1
        "Function_2_510",          # 02, 2
        "Function_3_53F",          # 03, 3
        "Function_4_690",          # 04, 4
        "Function_5_7E1",          # 05, 5
        "Function_6_93F",          # 06, 6
        "Function_7_988",          # 07, 7
        "Function_8_9B6",          # 08, 8
        "Function_9_C75",          # 09, 9
    ))


    def Function_0_43C(): pass

    label("Function_0_43C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_474"),
        (1, "loc_480"),
        (2, "loc_48C"),
        (3, "loc_498"),
        (4, "loc_4A4"),
        (5, "loc_4B0"),
        (6, "loc_4BC"),
        (SWITCH_DEFAULT, "loc_4C8"),
    )


    label("loc_474")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_480")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_48C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_498")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4EB")

    Return()

    # Function_0_43C end

    def Function_1_4EC(): pass

    label("Function_1_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_500")
    ClearScenarioFlags(0x22, 0)
    Event(0, 5)
    Jump("loc_50F")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_50F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)

    label("loc_50F")

    Return()

    # Function_1_4EC end

    def Function_2_510(): pass

    label("Function_2_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523")
    OP_70(0xA, 0x0)
    Jump("loc_527")

    label("loc_523")

    OP_70(0xA, 0x1E)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53A")
    OP_70(0xB, 0x0)
    Jump("loc_53E")

    label("loc_53A")

    OP_70(0xB, 0x1E)

    label("loc_53E")

    Return()

    # Function_2_510 end

    def Function_3_53F(): pass

    label("Function_3_53F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63F")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_5C8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_63A")

    label("loc_5C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_63A")

    Jump("loc_684")

    label("loc_63F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_684")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_53F end

    def Function_4_690(): pass

    label("Function_4_690")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_790")
    Sound(14, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('封魔之刃', 1)"), scpexpr(EXPR_END)), "loc_719")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_78B")

    label("loc_719")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xB, 0x1E, 0x0, 0x0, 0x0)

    label("loc_78B")

    Jump("loc_7D5")

    label("loc_790")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_690 end

    def Function_5_7E1(): pass

    label("Function_5_7E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    ClearChrFlags(0xD, 0x80)
    OP_78(0xC, 0xD)
    OP_49()
    SetChrPos(0xD, -21000, -350, 28700, 180)
    OP_D5(0xD, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x79, 0xB4, 0x1, 0x20)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8BE")
    ClearChrFlags(0xE, 0x80)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrPos(0xE, -18150, -3000, 4000, 0)
    BeginChrThread(0xE, 3, 0, 7)
    ClearChrFlags(0xF, 0x80)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -14050, -300, 16200, 180)

    label("loc_8BE")

    FadeToBright(1000, 0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 6)
    OP_68(-24300, 3850, 15000, 0)
    MoveCamera(30, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26850, 0)
    OP_68(-20200, 1850, 15850, 5000)
    MoveCamera(65, 5, 0, 5000)
    Sleep(4500)
    OP_0D()
    StopSound(458, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c020B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_7E1 end

    def Function_6_93F(): pass

    label("Function_6_93F")

    SetChrPos(0xFE, -21000, -300, 28700, 180)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -21000, -300, 19000)
    OP_9F(0x1, -25350, -300, 14100)
    OP_9F(0x1, -40900, -300, 13900)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_6_93F end

    def Function_7_988(): pass

    label("Function_7_988")

    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x5A, 0xBB8, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_7_988 end

    def Function_8_9B6(): pass

    label("Function_8_9B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch08200.itc", 0x1F)
    LoadChrToIndex("chr/ch08700.itc", 0x20)
    LoadChrToIndex("chr/ch02400.itc", 0x21)
    LoadChrToIndex("chr/ch09100.itc", 0x22)
    SetChrPos(0x101, -13750, -300, 13300, 125)
    SetChrPos(0x102, -15150, -300, 12300, 125)
    SetChrPos(0x104, -14900, -300, 13900, 125)
    SetChrPos(0x109, -12050, -300, 14900, 170)
    SetChrPos(0x105, -13400, -300, 15000, 170)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x5)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -15650, -300, 11300, 125)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -13750, -300, 12300, 125)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -11100, -300, 10500, 305)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -11100, -300, 9700, 305)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -9800, -300, 11600, 305)

    def lambda_AF3():

        label("loc_AF3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_AF3")

    QueueWorkItem2(0xA, 2, lambda_AF3)

    def lambda_B05():

        label("loc_B05")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_B05")

    QueueWorkItem2(0xB, 2, lambda_B05)

    def lambda_B17():

        label("loc_B17")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_B17")

    QueueWorkItem2(0xC, 2, lambda_B17)
    SetMapObjFrame(0xFF, "turi00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "turi01", 0x0, 0x1)
    OP_68(-12700, 900, 11600, 0)
    MoveCamera(71, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)
    TurnDirection(0x8, 0x101, 500)

    def lambda_BBE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BBE)
    Sleep(50)

    def lambda_BCE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BCE)
    Sleep(50)

    def lambda_BDE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BDE)
    Sleep(1000)
    OP_93(0x8, 0x131, 0x1F4)
    OP_68(-20000, 900, 11600, 9000)
    MoveCamera(53, 17, 0, 9000)
    SetCameraDistance(23000, 9000)
    BeginChrThread(0x9, 3, 0, 9)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 9)
    Sleep(450)
    BeginChrThread(0x102, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(6000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)
    SetScenarioFlags(0x22, 0)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_9B6 end

    def Function_9_C75(): pass

    label("Function_9_C75")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_C81():
        OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C81)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_C75 end

    SaveToFile()

Try(main)
