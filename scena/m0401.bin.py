from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0401.bin",                # FileName
        "m0401",                    # MapName
        "m0401",                    # Location
        0x00A9,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 169, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0401",                  # 0
        "Detective Dudley",       # 1
        "Arios",                  # 2
        "Ogre Sigmund",           # 3
        "Shirley",                # 4
        "Jaeger Gareth",          # 5
        "Red Constellation Jaeger",# 6
        "Red Constellation Jaeger",# 7
        "Red Constellation Jaeger",# 8
        "Red Constellation Jaeger",# 9
        "Yin",                    # 10
        "Cao",                    # 11
        "Lau",                    # 12
        "Heiyue Member",          # 13
        "Heiyue Member",          # 14
        "Heiyue Member",          # 15
        "Heiyue Member",          # 16
    ))

    AddCharChip((
        "chr/ch00953.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       4294950796, 180,  453,  0x0, 3,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(1500,    0,       4294951196, 225,  453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 5,   0.0,                   -8.0,                  -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.6666667461395264,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 2,   0.0,                   9.5,                   -1.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -3.1666667461395264,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 3,   -24.0,                 9.0,                   -9.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.0,                   -3.0,                  1.8000000715255737,    1.0])
    DeclEvent(0x0000, 0, 4,   28.5,                  -19.0,                 3.0,                   81.0,                  [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1666666716337204,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -9.5,                  3.1666667461395264,    -0.6000000238418579,   1.0])
    DeclEvent(0x0000, 0, 15,  -24.0,                 6.0,                   -8.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.6000001430511475,    -2.0,                  1.600000023841858,     1.0])
    DeclEvent(0x0000, 0, 17,  22.0,                  -19.0,                 3.0,                   144.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -7.333333492279053,    2.375,                 -0.6000000238418579,   1.0])

    DeclActor(0,       0,       8220,    1500,    0,       2000,    8500,    0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1400, 0)                                       # 0

    ScpFunction((
        "Function_0_578",          # 00, 0
        "Function_1_5A3",          # 01, 1
        "Function_2_6C2",          # 02, 2
        "Function_3_6F0",          # 03, 3
        "Function_4_71E",          # 04, 4
        "Function_5_74C",          # 05, 5
        "Function_6_17CF",         # 06, 6
        "Function_7_180C",         # 07, 7
        "Function_8_2B03",         # 08, 8
        "Function_9_2B40",         # 09, 9
        "Function_10_2B69",        # 0A, 10
        "Function_11_2BA6",        # 0B, 11
        "Function_12_2BE3",        # 0C, 12
        "Function_13_2C0C",        # 0D, 13
        "Function_14_2C49",        # 0E, 14
        "Function_15_30F2",        # 0F, 15
        "Function_16_3197",        # 10, 16
        "Function_17_31F9",        # 11, 17
    ))


    def Function_0_578(): pass

    label("Function_0_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_58A")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 3)
    Event(0, 7)

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A2")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)

    label("loc_5A2")

    Return()

    # Function_0_578 end

    def Function_1_5A3(): pass

    label("Function_1_5A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5BD")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)
    Jump("loc_5D2")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_5D2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)

    label("loc_5D2")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EA")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_62E")
    ModifyEventFlags(1, 1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_62E")
    OP_70(0x0, 0x28)
    ClearMapObjFlags(0x0, 0x2)
    SetScenarioFlags(0x0, 0)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64D")
    OP_70(0x1, 0x28)
    ClearMapObjFlags(0x1, 0x2)
    SetScenarioFlags(0x0, 1)

    label("loc_64D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66C")
    OP_70(0x2, 0x28)
    ClearMapObjFlags(0x2, 0x2)
    SetScenarioFlags(0x0, 2)

    label("loc_66C")

    ModifyEventFlags(0, 5, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    OP_1B(0x0, 0x0, 0x10)
    OP_70(0x0, 0x28)
    ClearMapObjFlags(0x0, 0x2)
    ModifyEventFlags(1, 5, 0x80)

    label("loc_693")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    OP_66(0x0, 0x1)

    label("loc_6A9")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C1")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_6C1")

    Return()

    # Function_1_5A3 end

    def Function_2_6C2(): pass

    label("Function_2_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF")
    TalkBegin(0xFF)
    Sound(147, 0, 100, 0)
    OP_71(0x0, 0x0, 0x28, 0x0, 0x8)
    ClearMapObjFlags(0x0, 0x2)
    SetScenarioFlags(0x0, 0)
    OP_79(0x0)
    EventEnd(0x3)

    label("loc_6EF")

    Return()

    # Function_2_6C2 end

    def Function_3_6F0(): pass

    label("Function_3_6F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D")
    TalkBegin(0xFF)
    Sound(147, 0, 100, 0)
    OP_71(0x1, 0x0, 0x28, 0x0, 0x8)
    ClearMapObjFlags(0x1, 0x2)
    SetScenarioFlags(0x0, 1)
    OP_79(0x1)
    EventEnd(0x3)

    label("loc_71D")

    Return()

    # Function_3_6F0 end

    def Function_4_71E(): pass

    label("Function_4_71E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74B")
    TalkBegin(0xFF)
    Sound(147, 0, 100, 0)
    OP_71(0x2, 0x0, 0x28, 0x0, 0x8)
    ClearMapObjFlags(0x2, 0x2)
    SetScenarioFlags(0x0, 2)
    OP_79(0x2)
    EventEnd(0x3)

    label("loc_74B")

    Return()

    # Function_4_71E end

    def Function_5_74C(): pass

    label("Function_5_74C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02401.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch00901.itc", 0x20)
    SoundLoad(147)
    OP_68(0, 900, -7900, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, -8200, 180)
    SetChrPos(0x102, 600, 0, -7900, 180)
    SetChrPos(0x103, -600, 0, -7000, 180)
    SetChrPos(0x104, 800, 0, -6700, 180)
    SetChrPos(0x109, -1800, 0, -7300, 180)
    SetChrPos(0x105, 1800, 0, -7300, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 1100, -16500, 2000)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#00608FThis is...\x01",
            "No doubt about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01403FYeah, it looks like the united\x01",
            "front was up to here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1000, 900, -14600, 4000)
    SetCameraDistance(16500, 4000)

    def lambda_900():
        OP_97(0x101, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_900)
    Sleep(100)

    def lambda_91D():
        OP_97(0x102, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_91D)
    Sleep(100)

    def lambda_93A():
        OP_97(0x103, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_93A)
    Sleep(100)

    def lambda_957():
        OP_97(0x104, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_957)
    Sleep(100)

    def lambda_974():
        OP_97(0x109, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_974)
    Sleep(100)

    def lambda_991():
        OP_97(0x105, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_991)
    WaitChrThread(0x109, 0)

    def lambda_9AF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9AF)
    WaitChrThread(0x105, 0)

    def lambda_9C0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9C0)

    ChrTalk(
        0x101,
        "#00001F#5PMr. Dudley, Mr. Arios.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5PUhhm, is something wrong?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#12P#00606F...Things got troublesome.\x02\x03",
            "#00601FIt looks like the terrorists\x01",
            "split in two groups here.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#5P#00101FThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00301FYou mean the bunch that aimed at the \x01",
            "Chancellor's life and those who aimed\x01",
            "at the President's split in this place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01403FYeah, there should be no doubt about it.\x02",
    )

    CloseMessageWindow()
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(100)

    def lambda_C46():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C46)
    Sleep(50)

    def lambda_C56():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C56)
    Sleep(50)

    def lambda_C66():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C66)
    Sleep(50)

    def lambda_C76():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C76)
    Sleep(50)

    def lambda_C86():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C86)
    Sleep(50)

    def lambda_C96():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C96)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#01400FIt appears the Republican terrorists \x01",
            "went to the Geofront C-Division──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1000, 900, -14600, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_68(-24000, -7100, 4500, 3500)
    MoveCamera(37, 23, 0, 3500)
    SetCameraDistance(24000, 3500)
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(100)

    def lambda_D7C():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D7C)
    Sleep(50)

    def lambda_D8C():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D8C)
    Sleep(50)

    def lambda_D9C():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D9C)
    Sleep(50)

    def lambda_DAC():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DAC)
    Sleep(50)

    def lambda_DBC():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DBC)
    Sleep(50)

    def lambda_DCC():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DCC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#01401FWhile the Imperial terrorists\x01",
            "escaped to the D-Division there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1000, 900, -14600, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    BeginChrThread(0x9, 3, 0, 6)
    Sleep(50)

    def lambda_E81():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E81)
    Sleep(50)

    def lambda_E91():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E91)
    Sleep(50)

    def lambda_EA1():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EA1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#5P#00105FY-You can really tell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10302FI see, are the footprints the deciding factor?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#12P#01404FYeah, you can see that they really\x01",
            "had no time to camouflage them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PThen...\x01",
            "Let's split in two groups here.\x02\x03",
            "#00001FIf we don't hurry, they could\x01",
            "end up getting away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#00603FYeah, that's the best thing to do.\x02\x03",
            "#00600F──MacLaine and I will follow them\x01",
            "into the C-Division to the right.\x02\x03",
            "You chase after the Imperial terrorists\x01",
            "who fled into the D-Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PHuh...\x01",
            "We aren't splitting our numbers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#5PDon't you think it is dangerous\x01",
            "being only you two alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01403FIn the C-Division over here there's a\x01",
            "heat treatment plant and other things.\x01",
            "It's a slightly troublesome place.\x02\x03",
            "#01400FConversely, the D-Division over there\x01",
            "is large and the search should be hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00304FIt could be a good allotment.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#5P#00301FLloyd, we have no time.\x01",
            "Let's go with that plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5P...Got it.\x02\x03",
            "#00001FMr. Dudley, Mr. Arios.\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_136A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_136A)
    Sleep(100)

    ChrTalk(
        0x9,
        "#12P#01404FHmph, you too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#00603FThe enemy are dangerous terrorists\x01",
            "who won't spare their lives.\x02\x03",
            "#00601FPay the utmost care!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5PSir...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FRoger!\x02",
    )

    CloseMessageWindow()

    def lambda_1430():

        label("loc_1430")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1430")

    QueueWorkItem2(0x101, 2, lambda_1430)

    def lambda_1442():

        label("loc_1442")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1442")

    QueueWorkItem2(0x103, 2, lambda_1442)

    def lambda_1454():

        label("loc_1454")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1454")

    QueueWorkItem2(0x105, 2, lambda_1454)

    def lambda_1466():

        label("loc_1466")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1466")

    QueueWorkItem2(0x102, 2, lambda_1466)

    def lambda_1478():

        label("loc_1478")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1478")

    QueueWorkItem2(0x104, 2, lambda_1478)

    def lambda_148A():

        label("loc_148A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_148A")

    QueueWorkItem2(0x109, 2, lambda_148A)

    def lambda_149C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_149C)
    Sleep(100)

    def lambda_14AC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_14AC)
    WaitChrThread(0x9, 2)
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)

    def lambda_14EF():
        OP_95(0xFE, 26000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14EF)
    WaitChrThread(0x8, 2)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_151A():
        OP_95(0xFE, 25600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_151A)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    Sound(147, 0, 100, 0)
    OP_71(0x2, 0x0, 0x28, 0x0, 0x0)
    WaitChrThread(0x8, 1)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)

    def lambda_1569():
        OP_95(0xFE, 31000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1569)
    Sleep(200)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)

    def lambda_158E():
        OP_95(0xFE, 30600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_158E)
    Sleep(300)

    def lambda_15AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15AB)
    Sleep(200)

    def lambda_15BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15BF)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    Sound(147, 2, 100, 0)
    OP_71(0x2, 0x28, 0x0, 0x0, 0x0)
    Sleep(500)
    StopSound(147, 1000, 100)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Fade(500)
    OP_68(700, 900, -13100, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#6P#00013FAlright, let's go too!\x02\x03",
            "We must catch the terrorists\x01",
            "before they flee from the Geofront.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16C3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_16C3)
    Sleep(50)

    def lambda_16D3():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_16D3)
    Sleep(50)

    def lambda_16E3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_16E3)
    Sleep(50)

    def lambda_16F3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16F3)
    Sleep(50)

    def lambda_1703():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1703)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00101F#11PYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PWe must make 'em pay soundly\x01",
            "for what they've done!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_79(0x2)
    OP_70(0x2, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_37()
    SetChrPos(0x0, 0, 0, -14500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0xA4, 0x1, 0x7)
    OP_24(0x93)
    EventEnd(0x5)
    Return()

    # Function_5_74C end

    def Function_6_17CF(): pass

    label("Function_6_17CF")


    def lambda_17D4():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_17D4)
    Sleep(50)

    def lambda_17E4():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_17E4)
    Sleep(50)

    def lambda_17F4():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17F4)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Return()

    # Function_6_17CF end

    def Function_7_180C(): pass

    label("Function_7_180C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03300.itc", 0x1E)
    LoadChrToIndex("chr/ch03400.itc", 0x1F)
    LoadChrToIndex("chr/ch41900.itc", 0x20)
    LoadChrToIndex("chr/ch00500.itc", 0x21)
    LoadChrToIndex("chr/ch06300.itc", 0x22)
    LoadChrToIndex("chr/ch31400.itc", 0x23)
    LoadChrToIndex("chr/ch31500.itc", 0x24)
    LoadChrToIndex("chr/ch12500.itc", 0x25)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis405.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, 200600, 0, 26200, 180)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, 199100, 0, 26500, 180)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, 200400, 0, 28300, 180)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrPos(0xD, 198400, 0, 28700, 180)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrPos(0xE, 202000, 0, 30300, 180)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    SetChrPos(0xF, 199700, 0, 29500, 180)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, 198000, 0, 30100, 180)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, 198500, 0, -21500, 0)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, 199900, 0, -20900, 0)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x13, 200400, 0, -21700, 0)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    OP_90(0x14, 198500, 0, -23300, 0)
    SetChrChipByIndex(0x15, 0x25)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    OP_90(0x15, 199400, 0, -24200, 0)
    SetChrChipByIndex(0x16, 0x24)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    OP_90(0x16, 200700, 0, -22800, 0)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    OP_90(0x17, 201600, 0, -23700, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1KAfterwards...\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(200000, 0, 0, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25000, 0)
    OP_11(0x12, 0x13, 0x16, 0x19, 0x9B, 0x0)
    OP_68(200000, -1000, 0, 9000)
    MoveCamera(30, 30, 0, 9000)
    SetCameraDistance(50000, 9000)
    PlayBGM("ed7571", 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3500)
    PlaceName2(340, 200, "c_plac71", 0x0, 0)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(200000, -3000, -17000, 0)
    MoveCamera(30, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(200000, 900, -9500, 5000)
    SetCameraDistance(15000, 5000)

    def lambda_1D12():
        OP_97(0x12, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1D12)
    Sleep(50)

    def lambda_1D2F():
        OP_97(0x13, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1D2F)
    Sleep(50)

    def lambda_1D4C():
        OP_97(0x11, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1D4C)
    Sleep(50)

    def lambda_1D69():
        OP_97(0x14, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1D69)
    Sleep(50)

    def lambda_1D86():
        OP_97(0x15, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1D86)
    Sleep(50)

    def lambda_1DA3():
        OP_97(0x16, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1DA3)
    Sleep(50)

    def lambda_1DC0():
        OP_97(0x17, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1DC0)
    WaitChrThread(0x11, 0)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x79)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700FHmm......\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#12P#03210FOoh...\x02",
    )

    CloseMessageWindow()
    OP_68(200000, 900, 17500, 3000)
    MoveCamera(30, 17, 0, 3000)

    def lambda_1E70():
        OP_97(0xA, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1E70)
    Sleep(100)

    def lambda_1E8D():
        OP_97(0xB, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1E8D)
    Sleep(100)

    def lambda_1EAA():
        OP_97(0xC, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1EAA)
    Sleep(100)

    def lambda_1EC7():
        OP_97(0xD, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1EC7)
    Sleep(100)

    def lambda_1EE4():
        OP_97(0xE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1EE4)
    Sleep(100)

    def lambda_1F01():
        OP_97(0xF, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1F01)
    Sleep(100)

    def lambda_1F1E():
        OP_97(0x10, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F1E)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        "#5P#04500F──Well, well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#04612F#5PAhaha, what a coincidence!\x02",
    )

    CloseMessageWindow()

    def lambda_1F87():
        OP_97(0xA, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1F87)
    Sleep(100)

    def lambda_1FA4():
        OP_97(0xB, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1FA4)
    Sleep(100)

    def lambda_1FC1():
        OP_97(0xC, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1FC1)
    Sleep(100)

    def lambda_1FDE():
        OP_97(0xD, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1FDE)
    Sleep(100)

    def lambda_1FFB():
        OP_97(0xE, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1FFB)
    Sleep(100)

    def lambda_2018():
        OP_97(0xF, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_2018)
    Sleep(100)

    def lambda_2035():
        OP_97(0x10, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2035)
    Sleep(1000)
    Fade(500)
    OP_68(200600, 900, -400, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(17000, 2500)
    OP_11(0x12, 0x13, 0x16, 0x19, 0x55, 0x0)

    def lambda_209E():
        OP_97(0x12, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_209E)
    Sleep(100)

    def lambda_20BB():
        OP_97(0x13, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_20BB)
    Sleep(100)

    def lambda_20D8():
        OP_97(0x11, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_20D8)
    Sleep(100)

    def lambda_20F5():
        OP_97(0x14, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_20F5)
    Sleep(100)

    def lambda_2112():
        OP_97(0x15, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_2112)
    Sleep(100)

    def lambda_212F():
        OP_97(0x16, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_212F)
    Sleep(100)

    def lambda_214C():
        OP_97(0x17, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_214C)
    WaitChrThread(0x17, 0)
    OP_6F(0x79)

    ChrTalk(
        0x13,
        "The "Red Constellation"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#12PThe "Ogre" and his daughter...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0)

    ChrTalk(
        0xC,
        (
            "#5PMaster Sigmund...\x01",
            "We are ready any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#04504FEh eh, relax.\x02\x03",
            "#04500FIt'll be after we each have\x01",
            "finished our clients' orders.\x02\x03",
            "It would be really boorish\x01",
            "to have more fun than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#03209FUh uh, I agree.\x02\x03",
            "#03205FBy the way──\x01",
            "Congratulations on the\x01",
            ""Neue-Blanc" renewal opening.\x02\x03",
            "#03204FI am very sorry to not\x01",
            "have come to greet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#04504FNo, it's likewise.\x02\x03",
            "#04500FAlthough we aren't strangers,\x01",
            "it's my bad I didn't come to greet.\x02\x03",
            "#04502FBy the way...\x01",
            "Are those who escaped death well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#03204FHa ha, they're all doing well,\x01",
            "you'd be disgusted by it.\x02\x03",
            "#03210FWell, thanks to you all, it\x01",
            "appears that even the elders\x01",
            "are still visited by bad dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#04609FAhaha, after all we assaulted the\x01",
            "elders council and took them hostage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700F...Hmph, it seems you did well\x01",
            "in my absence due to a mission.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xB,
        (
            "#5P#04605FAah!\x01",
            "Could you be "Yin"!?\x02\x03",
            "#04602FThe legendary assassin said to \x01",
            "be the Eastern District strongest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702F...And you're\x01",
            ""Bloody Shirley"?\x02\x03",
            "The one working as the strongest jaeger\x01",
            "battalion commander at the mere age of 16?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#04606FYeees, although for me it's easier\x01",
            "to move when I'm alone.\x02\x03",
            "#04611F──More importantly, listen.\x02\x03",
            "You're wearing a cool disguise, but\x01",
            "wouldn't you be stronger without it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00705F#30WWhat...\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#04606FIt makes you use your muscles in an unnatural way.\x02\x03",
            "#04600FYou'd be stronger using them normally.\x01",
            "Isn't it a waste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700F......\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)

    ChrTalk(
        0x12,
        "#11P#03205FOh ooh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#04504FUh uh, this can be coming from a doting parent,\x01",
            "but her discerning eye is the real deal.\x02\x03",
            "#04500FWell, if she hurt your feelings,\x01",
            "I'm going to apologize too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702F...Not at all.\x02\x03",
            "#00700FCao, if you're continuing with the \x01",
            "pointless greetings, I'll go on ahead.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11P#03204FHa ha, I am sorry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x12,
        "#12P#03202F──Then, until next time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#04502FYeah── 'til next time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#04612FUh uh, see youuu!\x02",
    )

    CloseMessageWindow()
    OP_68(200600, 1000, -400, 9000)
    MoveCamera(55, 23, 0, 9000)
    SetCameraDistance(35500, 9000)
    BeginChrThread(0xA, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x12, 0, 0, 8)
    Sleep(7000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_29(0xA4, 0x1, 0xA)
    OP_29(0xA3, 0x4, 0x10)
    OP_29(0xA4, 0x4, 0x10)
    OP_E5(0xA)
    SubItemNumber(0x324, 1)
    SubItemNumber(0x335, 1)
    SubItemNumber(0x336, 1)
    SubItemNumber(0x337, 1)
    SubItemNumber(0x338, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x1E, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e3000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_180C end

    def Function_8_2B03(): pass

    label("Function_8_2B03")

    BeginChrThread(0x12, 3, 0, 9)
    Sleep(800)
    BeginChrThread(0x13, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 9)
    Sleep(800)
    BeginChrThread(0x14, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x15, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x16, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x17, 3, 0, 10)
    Return()

    # Function_8_2B03 end

    def Function_9_2B40(): pass

    label("Function_9_2B40")

    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_9_2B40 end

    def Function_10_2B69(): pass

    label("Function_10_2B69")

    OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_10_2B69 end

    def Function_11_2BA6(): pass

    label("Function_11_2BA6")

    BeginChrThread(0xA, 3, 0, 12)
    Sleep(200)
    BeginChrThread(0xB, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0xC, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0xD, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0xE, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0xF, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0x10, 3, 0, 13)
    Return()

    # Function_11_2BA6 end

    def Function_12_2BE3(): pass

    label("Function_12_2BE3")

    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_12_2BE3 end

    def Function_13_2C0C(): pass

    label("Function_13_2C0C")

    OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_2C0C end

    def Function_14_2C49(): pass

    label("Function_14_2C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3052")
    EventBegin(0x0)
    Fade(500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 40, 0, 4910, 0)
    SetChrPos(0x102, -1370, 0, 4110, 0)
    SetChrPos(0x103, 1370, 0, 4510, 0)
    SetChrPos(0x104, -2440, 0, 4920, 44)
    SetChrPos(0x105, 2740, 0, 5280, 315)
    SetChrPos(0x109, -3320, 0, 6000, 390)
    OP_68(1470, 0, 8070, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20900, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FIf I remember correctly, this is...\x01",
            "The gate connected to the\x01",
            "Orchis Tower base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FIt is the Division we went through when we\x01",
            "were chasing the Trade Conference terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, it looks like now it's\x01",
            "been completely sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FJust around here we split\x01",
            "into two groups with Mr. \x01",
            "Dudley and Mr. Arios.\x02\x03",
            "#10108FAnd after that...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x105)

    ChrTalk(
        0x109,
        (
            "#10106FI-I'm sorry.\x01",
            "It wasn't quite the\x01",
            "pleasant memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304F...Ha ha, don't mind it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#4PAnyway, over here there's no\x01",
            "lift that exits on the surface.\x02\x03",
            "#00100FThe D-Division seems to be sealed too.\x01",
            "Let's return to the C-Division for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's do it.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 0, 0, 4910, 0)
    SetScenarioFlags(0x190, 3)
    EventEnd(0x5)
    Jump("loc_30F1")

    label("loc_3052")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis is the gate that connects\x01",
            "to the Orchis Tower base.\x02\x03",
            "It looks like it's sealed now, so let's\x01",
            "return to the C-Division and use the lift.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_30F1")

    Return()

    # Function_14_2C49 end

    def Function_15_30F2(): pass

    label("Function_15_30F2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FThis is the gate connecting to the D-Division.\x02\x03",
            "...Let's now return to the C-Division\x01",
            "and use the lift that exits on the surface.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24210, -8000, 3000, 180)
    EventEnd(0x4)
    Return()

    # Function_15_30F2 end

    def Function_16_3197(): pass

    label("Function_16_3197")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FWe don't have time to retrace our steps.\x01",
            "Let's hurry on ahead!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -390, 0, 6230, 180)
    EventEnd(0x4)
    Return()

    # Function_16_3197 end

    def Function_17_31F9(): pass

    label("Function_17_31F9")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FLet's leave the C-Division to\x01",
            "Mr. Dudley and Mr. Arios.\x02\x03",
            "Let's chase the Imperial terrorists\x01",
            "who ran into the D-Division!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19030, 4000, -19240, 270)
    EventEnd(0x4)
    Return()

    # Function_17_31F9 end

    SaveToFile()

Try(main)
