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
        "Function_6_172A",         # 06, 6
        "Function_7_1767",         # 07, 7
        "Function_8_2A35",         # 08, 8
        "Function_9_2A72",         # 09, 9
        "Function_10_2A9B",        # 0A, 10
        "Function_11_2AD8",        # 0B, 11
        "Function_12_2B15",        # 0C, 12
        "Function_13_2B3E",        # 0D, 13
        "Function_14_2B7B",        # 0E, 14
        "Function_15_2FF5",        # 0F, 15
        "Function_16_308C",        # 10, 16
        "Function_17_30EB",        # 11, 17
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
            "#6P#00608FThis is... No doubt\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#01403FYeah, the united front\x01",
            "was here.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1000, 900, -14600, 4000)
    SetCameraDistance(16500, 4000)

    def lambda_8EC():
        OP_97(0x101, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8EC)
    Sleep(100)

    def lambda_909():
        OP_97(0x102, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_909)
    Sleep(100)

    def lambda_926():
        OP_97(0x103, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_926)
    Sleep(100)

    def lambda_943():
        OP_97(0x104, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_943)
    Sleep(100)

    def lambda_960():
        OP_97(0x109, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_960)
    Sleep(100)

    def lambda_97D():
        OP_97(0x105, 0x1F4, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_97D)
    WaitChrThread(0x109, 0)

    def lambda_99B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_99B)
    WaitChrThread(0x105, 0)

    def lambda_9AC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9AC)

    ChrTalk(
        0x101,
        "#00001F#5PDudley, Arios...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5PUmm, is something wrong?\x02",
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
            "#12P#00606F...Things just got\x01",
            "harder.\x02\x03",
            "#00601FIt seems the terrorists\x01",
            "split into two groups\x01",
            "here.\x02",
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
            "#5P#00301FThe groups after the\x01",
            "chancellor and President\x01",
            "split here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#12P#01403FYeah, I'm sure of it.\x02",
    )

    CloseMessageWindow()
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(100)

    def lambda_BDB():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BDB)
    Sleep(50)

    def lambda_BEB():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BEB)
    Sleep(50)

    def lambda_BFB():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BFB)
    Sleep(50)

    def lambda_C0B():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C0B)
    Sleep(50)

    def lambda_C1B():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C1B)
    Sleep(50)

    def lambda_C2B():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C2B)
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
            "#01400FIt appears the Republican\x01",
            "terrorists went to\x01",
            "Geofront C-Division─\x02",
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

    def lambda_D0A():
        OP_93(0x101, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D0A)
    Sleep(50)

    def lambda_D1A():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D1A)
    Sleep(50)

    def lambda_D2A():
        OP_93(0x103, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D2A)
    Sleep(50)

    def lambda_D3A():
        OP_93(0x104, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D3A)
    Sleep(50)

    def lambda_D4A():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D4A)
    Sleep(50)

    def lambda_D5A():
        OP_93(0x105, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D5A)
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
            "#01401FWhile the Imperial\x01",
            "terrorists escaped to\x01",
            "D-Division there.\x02",
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

    def lambda_E0B():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E0B)
    Sleep(50)

    def lambda_E1B():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E1B)
    Sleep(50)

    def lambda_E2B():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E2B)
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
        (
            "#5P#10302FI see, so footprints\x01",
            "were the deciding\x01",
            "factor?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#12P#01404FYeah. In a situation like\x01",
            "this, it appears they didn't\x01",
            "have time to conceal them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PIf that's the case... We\x01",
            "should split into two\x01",
            "groups too.\x02\x03",
            "#00001FAt this rate, they'll\x01",
            "get away if we don't\x01",
            "hurry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#00603FYeah, that's the best\x01",
            "course of action.\x02\x03",
            "#00600F...MacLaine and I will\x01",
            "handle C-Division to the\x01",
            "right.\x02\x03",
            "You guys chase after the\x01",
            "Imperial terrorists who\x01",
            "fled to D-Division.\x02",
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
        "#00005F#5PHuh? Not evenly?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#5PWon't it be dangerous\x01",
            "with just the two of\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#01403FC-Division has a heat treatment\x01",
            "plant and the like. It's a\x01",
            "slightly troublesome place.\x02\x03",
            "#01400FConversely, D-Division is large\x01",
            "and searching it will be\x01",
            "difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00304FThis might be a good way\x01",
            "to divide, then.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#5P#00301FLloyd, there's no time.\x01",
            "Let's go with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PUnderstood.\x02\x03",
            "#00001FDudley, Arios. Please,\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12C7():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12C7)
    Sleep(100)

    ChrTalk(
        0x9,
        "#12P#01404FHmph, you too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12P#00603FThe enemies are terrorists\x01",
            "who don't even care about\x01",
            "their own lives.\x02\x03",
            "#00601FBe extremely careful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#5PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FRoger that!\x02",
    )

    CloseMessageWindow()

    def lambda_1398():

        label("loc_1398")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1398")

    QueueWorkItem2(0x101, 2, lambda_1398)

    def lambda_13AA():

        label("loc_13AA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_13AA")

    QueueWorkItem2(0x103, 2, lambda_13AA)

    def lambda_13BC():

        label("loc_13BC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_13BC")

    QueueWorkItem2(0x105, 2, lambda_13BC)

    def lambda_13CE():

        label("loc_13CE")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_13CE")

    QueueWorkItem2(0x102, 2, lambda_13CE)

    def lambda_13E0():

        label("loc_13E0")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_13E0")

    QueueWorkItem2(0x104, 2, lambda_13E0)

    def lambda_13F2():

        label("loc_13F2")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_13F2")

    QueueWorkItem2(0x109, 2, lambda_13F2)

    def lambda_1404():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1404)
    Sleep(100)

    def lambda_1414():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1414)
    WaitChrThread(0x9, 2)
    OP_68(22500, 4900, -19000, 3000)
    MoveCamera(53, 23, 0, 3000)
    SetCameraDistance(24000, 3000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)

    def lambda_1457():
        OP_95(0xFE, 26000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1457)
    WaitChrThread(0x8, 2)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)

    def lambda_1482():
        OP_95(0xFE, 25600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1482)
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

    def lambda_14D1():
        OP_95(0xFE, 31000, 4000, -19000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14D1)
    Sleep(200)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)

    def lambda_14F6():
        OP_95(0xFE, 30600, 4000, -18000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14F6)
    Sleep(300)

    def lambda_1513():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1513)
    Sleep(200)

    def lambda_1527():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1527)
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
            "We're catching the\x01",
            "terrorists before they\x01",
            "escape the Geofront!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1629():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1629)
    Sleep(50)

    def lambda_1639():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1639)
    Sleep(50)

    def lambda_1649():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1649)
    Sleep(50)

    def lambda_1659():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1659)
    Sleep(50)

    def lambda_1669():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1669)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00101F#11PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#5PWe'll make 'em pay for\x01",
            "what they've done!\x02",
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

    def Function_6_172A(): pass

    label("Function_6_172A")


    def lambda_172F():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_172F)
    Sleep(50)

    def lambda_173F():
        TurnDirection(0x104, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_173F)
    Sleep(50)

    def lambda_174F():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_174F)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Return()

    # Function_6_172A end

    def Function_7_1767(): pass

    label("Function_7_1767")

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
            "#1KAfter that...\x02",
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

    def lambda_1C6D():
        OP_97(0x12, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1C6D)
    Sleep(50)

    def lambda_1C8A():
        OP_97(0x13, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1C8A)
    Sleep(50)

    def lambda_1CA7():
        OP_97(0x11, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1CA7)
    Sleep(50)

    def lambda_1CC4():
        OP_97(0x14, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1CC4)
    Sleep(50)

    def lambda_1CE1():
        OP_97(0x15, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1CE1)
    Sleep(50)

    def lambda_1CFE():
        OP_97(0x16, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1CFE)
    Sleep(50)

    def lambda_1D1B():
        OP_97(0x17, 0x0, 0x0, 0x2EE0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1D1B)
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
        "#12P#03210FOhh...\x02",
    )

    CloseMessageWindow()
    OP_68(200000, 900, 17500, 3000)
    MoveCamera(30, 17, 0, 3000)

    def lambda_1DCB():
        OP_97(0xA, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1DCB)
    Sleep(100)

    def lambda_1DE8():
        OP_97(0xB, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1DE8)
    Sleep(100)

    def lambda_1E05():
        OP_97(0xC, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1E05)
    Sleep(100)

    def lambda_1E22():
        OP_97(0xD, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1E22)
    Sleep(100)

    def lambda_1E3F():
        OP_97(0xE, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1E3F)
    Sleep(100)

    def lambda_1E5C():
        OP_97(0xF, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1E5C)
    Sleep(100)

    def lambda_1E79():
        OP_97(0x10, 0x0, 0x0, 0xFFFFD8F0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1E79)
    WaitChrThread(0xA, 0)
    OP_6F(0x79)

    ChrTalk(
        0xA,
        (
            "#5P#04500F─Well look who we have\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#04612F#5PAhaha, what a\x01",
            "coincidence!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EF0():
        OP_97(0xA, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1EF0)
    Sleep(100)

    def lambda_1F0D():
        OP_97(0xB, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1F0D)
    Sleep(100)

    def lambda_1F2A():
        OP_97(0xC, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1F2A)
    Sleep(100)

    def lambda_1F47():
        OP_97(0xD, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1F47)
    Sleep(100)

    def lambda_1F64():
        OP_97(0xE, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1F64)
    Sleep(100)

    def lambda_1F81():
        OP_97(0xF, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1F81)
    Sleep(100)

    def lambda_1F9E():
        OP_97(0x10, 0x0, 0x0, 0xFFFFC950, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F9E)
    Sleep(1000)
    Fade(500)
    OP_68(200600, 900, -400, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(17000, 2500)
    OP_11(0x12, 0x13, 0x16, 0x19, 0x55, 0x0)

    def lambda_2007():
        OP_97(0x12, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2007)
    Sleep(100)

    def lambda_2024():
        OP_97(0x13, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2024)
    Sleep(100)

    def lambda_2041():
        OP_97(0x11, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2041)
    Sleep(100)

    def lambda_205E():
        OP_97(0x14, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_205E)
    Sleep(100)

    def lambda_207B():
        OP_97(0x15, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_207B)
    Sleep(100)

    def lambda_2098():
        OP_97(0x16, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2098)
    Sleep(100)

    def lambda_20B5():
        OP_97(0x17, 0x0, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_20B5)
    WaitChrThread(0x17, 0)
    OP_6F(0x79)

    ChrTalk(
        0x13,
        "Red Constellation's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12PThe Battle Ogre and his\x01",
            "daughter, huh...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10, 0)

    ChrTalk(
        0xC,
        (
            "#5PMaster Sigmund... We're\x01",
            "ready anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#04504FHehe, relax.\x02\x03",
            "#04500FIt'll be after we're\x01",
            "through with our respective\x01",
            "clients' orders.\x02\x03",
            "It'd be unprofessional to\x01",
            "have any more fun than\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#03209FHaha, I agree.\x02\x03",
            "#03205FBy the way...\x01",
            "Congratulations on the\x01",
            "opening of Neue-Blanc.\x02\x03",
            "#03204FI apologize for not\x01",
            "coming to visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#04504FI must apologize too.\x02\x03",
            "#04500FSorry for not coming to\x01",
            "your office, even though\x01",
            "we know each other.\x02\x03",
            "#04502FBy the way... How are\x01",
            "those guys who escaped\x01",
            "death doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#03204FThe lot them are doing\x01",
            "so well, you'd be\x01",
            "disgusted by it.\x02\x03",
            "#03210FWell, due to you guys,\x01",
            "it seems the elder is\x01",
            "still having bad dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#04609FAhaha, well we did attack\x01",
            "your elder's meeting and\x01",
            "took a few hostages!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700FHmph. It seems doing the\x01",
            "mission without my help\x01",
            "was the right answer.\x02",
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
            "#5P#04605FAah! Could you be Yin!?\x02\x03",
            "#04602FThe legendary assassin\x01",
            "said to be the Eastern\x01",
            "Quarter's strongest!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702FThen that makes you Bloody\x01",
            "Shirley.\x02\x03",
            "Said to be the strongest\x01",
            "jaeger battalion commander,\x01",
            "at the tender age of 16.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#04606FHmm... Acting alone's\x01",
            "easier, though.\x02\x03",
            "#04611F─But hey, listen up.\x02\x03",
            "That disguise of yours is\x01",
            "super cool, but wouldn't\x01",
            "you be stronger without it?\x02",
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
            "#5P#04606FThe way you use your\x01",
            "muscles is unnatural.\x02\x03",
            "#04600FIf you used them normally,\x01",
            "you'd be stronger. Isn't\x01",
            "that such a waste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00700F............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x11, 500)

    ChrTalk(
        0x12,
        "#11P#03205FOhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#04504FHaha, I may be a doting\x01",
            "father, but her sharp\x01",
            "eye is the real deal.\x02\x03",
            "#04500FWell, if she hurt your\x01",
            "feelings, I'll apologize\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#12P#00702F...Not at all.\x02\x03",
            "#00700FCao, if you're going to\x01",
            "continue with these pointless\x01",
            "greetings, I'll go on ahead.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11P#03204FHaha, sorry.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#12P#03202F...Then, until next we\x01",
            "meet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P#04502FYeah─ See you next time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5P#04612FHaha, bye!\x02",
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

    # Function_7_1767 end

    def Function_8_2A35(): pass

    label("Function_8_2A35")

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

    # Function_8_2A35 end

    def Function_9_2A72(): pass

    label("Function_9_2A72")

    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_9_2A72 end

    def Function_10_2A9B(): pass

    label("Function_10_2A9B")

    OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_97(0xFE, 0x1388, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_10_2A9B end

    def Function_11_2AD8(): pass

    label("Function_11_2AD8")

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

    # Function_11_2AD8 end

    def Function_12_2B15(): pass

    label("Function_12_2B15")

    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_12_2B15 end

    def Function_13_2B3E(): pass

    label("Function_13_2B3E")

    OP_97(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFFF34E, 0x0, 0xFFFFF5D8, 0x7D0, 0x1)
    OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_2B3E end

    def Function_14_2B7B(): pass

    label("Function_14_2B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F62")
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
            "#00005FIf I remember correctly, this\x01",
            "is... This door connects to\x01",
            "the base of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThis is the division we came\x01",
            "through while chasing the\x01",
            "trade conference terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWell, it looks like it's\x01",
            "completely sealed off,\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FWe split with Dudley and\x01",
            "Arios right around here.\x02\x03",
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
            "#10106FI-I'm sorry. That's not\x01",
            "a very pleasant memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F...Haha, don't worry\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#4PAnyway, there's no lift over\x01",
            "here that exits above\x01",
            "ground.\x02\x03",
            "#00100FD-Division seems to be\x01",
            "sealed off too. Let's return\x01",
            "to C-Division for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's.\x02",
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
    Jump("loc_2FF4")

    label("loc_2F62")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis door connects to the\x01",
            "base of Orchis Tower.\x02\x03",
            "It looks like it's sealed\x01",
            "off, so let's return to\x01",
            "C-Division and use the lift.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_2FF4")

    Return()

    # Function_14_2B7B end

    def Function_15_2FF5(): pass

    label("Function_15_2FF5")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FThis door connects to\x01",
            "D-Division.\x02\x03",
            "...For now, let's return to\x01",
            "C-Division and use the lift\x01",
            "that exits above ground.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -24210, -8000, 3000, 180)
    EventEnd(0x4)
    Return()

    # Function_15_2FF5 end

    def Function_16_308C(): pass

    label("Function_16_308C")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00003FWe don't have time to\x01",
            "retrace our steps. Let's\x01",
            "hurry ahead!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -390, 0, 6230, 180)
    EventEnd(0x4)
    Return()

    # Function_16_308C end

    def Function_17_30EB(): pass

    label("Function_17_30EB")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FLet's leave C-Division\x01",
            "to Dudley and Arios.\x02\x03",
            "Let's chase the Imperial\x01",
            "terrorists who ran into\x01",
            "D-Division!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 19030, 4000, -19240, 270)
    EventEnd(0x4)
    Return()

    # Function_17_30EB end

    SaveToFile()

Try(main)
