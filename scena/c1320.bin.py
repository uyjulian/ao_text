from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1320.bin",                # FileName
        "c1320",                    # MapName
        "c1320",                    # Location
        0x001F,                     # MapIndex
        "ed7522",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 31, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1320",                  # 0
        "Researcher Clay",           # 1
        "Researcher David",         # 2
        "doll",                   # 3
    ))

    AddCharChip((
        "chr/ch32800.itc",                   # 00
        "chr/ch29402.itc",                   # 01
    ))

    DeclNpc(4294964197, 4294966817, 22659,   315,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294962597, 4294966917, 22700,   315,  325,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       4294967016, 16660,   1100,    0,       4294967166, 16660,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_236",          # 02, 2
        "Function_3_23D",          # 03, 3
        "Function_4_2BA",          # 04, 4
        "Function_5_448",          # 05, 5
        "Function_6_5D0",          # 06, 6
        "Function_7_955",          # 07, 7
        "Function_8_1DDF",         # 08, 8
        "Function_9_1E2A",         # 09, 9
        "Function_10_1EA0",        # 0A, 10
        "Function_11_1EEB",        # 0B, 11
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_17C"),
        (1, "loc_188"),
        (2, "loc_194"),
        (3, "loc_1A0"),
        (4, "loc_1AC"),
        (5, "loc_1B8"),
        (6, "loc_1C4"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_17C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_188")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_194")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1F3")

    Return()

    # Function_0_144 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215")
    ClearScenarioFlags(0x25, 1)
    Call(0, 2)

    label("loc_215")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_235")
    SetChrFlags(0x8, 0x10)

    label("loc_235")

    Return()

    # Function_1_1F4 end

    def Function_2_236(): pass

    label("Function_2_236")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_236 end

    def Function_3_23D(): pass

    label("Function_3_23D")

    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    SetMapObjFrame(0xFF, "monita3_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita4_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita5_add", 0x0, 0x1)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B9")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)

    label("loc_2B9")

    Return()

    # Function_3_23D end

    def Function_4_2BA(): pass

    label("Function_4_2BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF")
    Call(0, 6)
    Jump("loc_444")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C4")

    ChrTalk(
        0xFE,
        (
            "By the way Roberts'\x01",
            "On the Epstein foundation floor\x01",
            "It seems to be busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, the Orkis Tower\x01",
            "I hackers stealing drawings\x01",
            "She seems to be exploring … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why hackers like that\x01",
            "I guess he stole it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_444")

    label("loc_3C4")


    ChrTalk(
        0xFE,
        (
            "Roberts stole the drawing of the tower\x01",
            "She seems to be searching for a hacker … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why hackers like that\x01",
            "I guess he stole it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444")

    TalkEnd(0xFE)
    Return()

    # Function_4_2BA end

    def Function_5_448(): pass

    label("Function_5_448")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D")
    Call(0, 6)
    Jump("loc_5CC")

    label("loc_45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F")

    ChrTalk(
        0xFE,
        (
            "Marybele lady is\x01",
            "The human use is rough, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "System management\x01",
            "I am given responsible parts.\x01",
            "I have to work hard and put in a lot of effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys,\x01",
            "Stolen lady's dolls\x01",
            "You came to find me, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see that too.\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5CC")

    label("loc_55F")


    ChrTalk(
        0xFE,
        (
            "You guys,\x01",
            "Stolen lady's dolls\x01",
            "You came to find me, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see that too.\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC")

    TalkEnd(0xFE)
    Return()

    # Function_5_448 end

    def Function_6_5D0(): pass

    label("Function_6_5D0")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_66C")
    Jump("loc_6B6")

    label("loc_66C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_68C")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B6")

    label("loc_68C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6AC")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6B6")

    label("loc_6AC")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6B6")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(
        0x8,
        "Well, you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You,\x01",
            "Certainly it was the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, it's been a long time.\x01",
            "Do you remember us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FWith Clay Mr. IBC Engineering Department\x01",
            "You were Mr. David.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLong time no see.\x01",
            "…… Sounds like you are busy, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, the power net\x01",
            "Since it has become popular, management of the system is also\x01",
            "It's getting harder than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I will do it properly.\x01",
            "The lady is also being told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109FHuhu, working under the bell is\x01",
            "It will be hard as ever … but …\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Oh, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Either way, I took the stolen lady doll\x01",
            "You came to find me, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Please do your best.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x1C6, 2)
    Return()

    # Function_6_5D0 end

    def Function_7_955(): pass

    label("Function_7_955")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-820, 900, 14940, 0)
    MoveCamera(32, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13870, 0)
    SetChrPos(0x101, 40, -510, 15350, 0)
    SetChrPos(0x102, -1100, -590, 14550, 0)
    SetChrPos(0x103, -70, -590, 13800, 0)
    SetChrPos(0x104, 1090, -590, 14550, 0)
    SetChrPos(0x109, -1030, -590, 13110, 0)
    SetChrPos(0x105, 970, -590, 13140, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0xB)
    SetChrPos(0xA, 0, -130, 16660, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("chr/ch29400.itc", 0x1F)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#12P#00000FThere it is! The last trunk!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F\"Tower high and skyscraper,\x01",
            "Go down 21 layers from the top of 16 layers\x01",
            "Find numerous windows looking into the different world \"… …\x02\x03",
            "#00200FIBC building on the 16th floor above ground,\x01",
            "It is the 5th floor basement which descended 21 levels from the top floor.\x01",
            "…… It seems it was about this place.\x02\x03",
            "#00200FAnd \"a number of windows looking into different worlds\"\x01",
            "These terminals that can peek at the power net\x01",
            "I mean the monitor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FIf it is said, other than this place\x01",
            "It seems unthinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOk let's check it out\x02",
    )

    CloseMessageWindow()
    Sound(1024, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x5)
    Sleep(1000)

    ChrTalk(
        0x102,
        (
            "#6P#00100FCertainly, this doll is \"Alice\" …\x01",
            "Even in the bell collection\x01",
            "It should have been my favorite.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FKaito B's card … is the last time,\x01",
            "It looks like it is not pasted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHah, what an unexpected place\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FSigh, that was a lot of effort\x02",
    )

    CloseMessageWindow()
    Sound(1026, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FWhat?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 8)
    BeginChrThread(0x9, 1, 0, 9)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x8,
        "#6PWas something here, guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PThe alert where the guidance mail arrived\x01",
            "It seems I heard it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PWhat is there\x01",
            "I wonder if you are a Mary Bell girls doll! Is it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F27():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F27)
    Sleep(50)

    def lambda_F37():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F37)
    Sleep(50)

    def lambda_F47():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F47)
    Sleep(50)

    def lambda_F57():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F57)
    Sleep(50)

    def lambda_F67():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F67)
    Sleep(50)

    def lambda_F77():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F77)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#11P#00005FUm, from here just before\x01",
            "It looks like there was … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FHmm … More than that,\x01",
            "I do not remember mailing at this timing\x01",
            "Somehow it is interesting.\x02\x03",
            "#00200FDo you mind if I access it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 500)

    ChrTalk(
        0x8,
        (
            "#6POh, ah ……\x01",
            "I'm creepy, I beg you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(50, 720, 17660, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13720, 0)
    SetChrPos(0x101, -1060, -280, 17870, 0)
    SetChrPos(0x102, 1060, -280, 17990, 0)
    SetChrPos(0x104, -540, -280, 16850, 0)
    SetChrPos(0x109, 630, -280, 17010, 0)
    SetChrPos(0x105, -50, -280, 16120, 0)
    SetChrPos(0x8, -920, -600, 14160, 0)
    SetChrPos(0x9, 750, -600, 14180, 0)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x103, 0x0)
    SetChrBattleFlags(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -40, -130, 18520, 0)
    Sleep(1500)
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sound(836, 0, 100, 0)

    ChrTalk(
        0x103,
        (
            "#11P#00203F(Type type)\x02\x03",
            "#00205FHuh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FWhat's wrong, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00201F…… In the sender's column,\x01",
            "The name of \"Kaitou B\" ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#00105FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Phantom Thief B… That guy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "F-from where\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F…… Tio.\x01",
            "Can you open it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#00201FWill do\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, 100)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "From: Kaitou B\x01",
            "Subject: Untitled\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dear moral support department ──\x01\x01",
            "First of all, in my recent surprise\x01",
            "To be touched by my heart's content\x01",
            "Let me express our gratitude.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ms. Mariavell, the owner of the doll,\x01",
            "And to the producer Jorg Meister\x01",
            "I apologize for having worked so hard.\x01\x01",
            "However, so that this supreme work of art will not get scratched\x01",
            "Because I had the greatest consideration,\x01",
            "Please be assured about that point.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I will soon\x01",
            "I will leave this place.\x01",
            "Farewell, you guys at the Special Affairs Division.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Serving Serpent\" Enforcer No.嘳,\x01",
            "\"Kaito gentleman\" Bull Blank ──\x01",
            "In the case of\x01",
            "I greatly expect your further growth,\x01",
            "Let 's pray for the goddess to make a good fight.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P. S.\x01",
            "This guidance mail is automatically deleted.\x01",
            "As preservation is impossible, so give up.\x01",
            "── Kaito B\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#6P#00005FUhh…..Uh……\x02",
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#6P#00011F#4SWHAT WAS THAT MAIL!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, it's like this suddenly\x01",
            "There is coming out.\x02\x03",
            "#10304FAn enforcer of \"a serpent snake\"\x01",
            "\"Kaito gentleman\" ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18DD")

    ChrTalk(
        0x102,
        (
            "#00106FWell, certainly before the time,\x01",
            "Relationship with Len-chan\x01",
            "It was a scary but … ….\x02\x03",
            "#00107FThat's right, Tio!\x01",
            "Can I output this mail?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1978")

    label("loc_18DD")


    ChrTalk(
        0x102,
        (
            "#00106FYes, if that's the case\x01",
            "The technique of stealing Kaito B also\x01",
            "Although it may be explained, …\x02\x03",
            "#00107FThat's right, Tio!\x01",
            "Can I output this mail?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1978")


    ChrTalk(
        0x101,
        (
            "#6P#00005FThat's right!\x01",
            "Maybe an important clue …!\x02",
        )
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)

    ChrTalk(
        0x103,
        (
            "#11P#00203F(Type type)\x01",
            "I am doing it already … but it is useless.\x02\x03",
            "#00200FSimultaneously with the opening of the mail,\x01",
            "Self-destruction of data gradually\x01",
            "You seem to have started.\x02\x03",
            "#00206FIt does not affect other terminals,\x01",
            "It is almost impossible to repair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FUgh, this got super annoying\x02\x03",
            "#00301FYesterday at the Geo Front\x01",
            "Also the fellows who got in\x01",
            "I do not understand anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FRight…\x02\x03",
            "#10101FThat hacking is good,\x01",
            "I have ridiculous technology\x01",
            "I think that there is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "W-we didn't know anything about this\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Uh, clay!\x01",
            "Does the data have an influence once\x01",
            "Please check it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That's right.\x01",
            "Even a virus can enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because that's why,\x01",
            "We will rude with this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x8, 1, 0, 10)
    BeginChrThread(0x9, 1, 0, 11)
    Sleep(1200)
    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#6P#00003FAnd anyway … …\x01",
            "Rosenberg doll\x01",
            "I could recover them all.\x02\x03",
            "#00000FAs it is this way to Mary Bell\x01",
            "Let's say you are going to pass.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)

    def lambda_1D30():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D30)
    Sleep(50)

    def lambda_1D40():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D40)
    Sleep(50)

    def lambda_1D50():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D50)
    Sleep(50)

    def lambda_1D60():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D60)
    Sleep(100)

    ChrTalk(
        0x102,
        "#00100FYes, let's\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrBattleFlags(0x103, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x8000)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    OP_64(0x8)
    OP_64(0x9)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_955 end

    def Function_8_1DDF(): pass

    label("Function_8_1DDF")

    OP_93(0xFE, 0xBE, 0x1F4)
    OP_95(0xFE, -3750, -600, 19550, 2000, 0x0)
    OP_95(0xFE, -3600, -600, 15950, 2000, 0x0)
    OP_95(0xFE, -2560, -600, 14690, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_8_1DDF end

    def Function_9_1E2A(): pass

    label("Function_9_1E2A")

    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0xFE, -4560, -480, 21280, 135)
    OP_0D()
    OP_95(0xFE, -3750, -600, 19550, 2000, 0x0)
    OP_95(0xFE, -3600, -600, 15950, 2000, 0x0)
    OP_95(0xFE, -3430, -600, 15650, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_9_1E2A end

    def Function_10_1EA0(): pass

    label("Function_10_1EA0")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -3720, -600, 15980, 2000, 0x0)
    OP_95(0xFE, -3470, -600, 20320, 2000, 0x0)
    OP_95(0xFE, -5210, -480, 21950, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_1EA0 end

    def Function_11_1EEB(): pass

    label("Function_11_1EEB")

    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 3720, -600, 15950, 2000, 0x0)
    OP_95(0xFE, 3610, -600, 20460, 2000, 0x0)
    OP_95(0xFE, 5110, -480, 21860, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_11_1EEB end

    SaveToFile()

Try(main)
