from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Researcher Clay",        # 1
        "Researcher David",       # 2
        "Doll",                   # 3
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
        "Function_5_459",          # 05, 5
        "Function_6_5DF",          # 06, 6
        "Function_7_985",          # 07, 7
        "Function_8_1ECB",         # 08, 8
        "Function_9_1F16",         # 09, 9
        "Function_10_1F8C",        # 0A, 10
        "Function_11_1FD7",        # 0B, 11
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
    Jump("loc_455")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C5")

    ChrTalk(
        0xFE,
        (
            "Incidentally, it seems that Chief\x01",
            "Roberts is currently busy at the\x01",
            "Epstein Foundation building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems he's looking for\x01",
            "a hacker who stole the\x01",
            "Orchis Tower's blueprints...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why would a hacker\x01",
            "stole such a thing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_455")

    label("loc_3C5")


    ChrTalk(
        0xFE,
        (
            "It seems that Chief Roberts is looking for a hacker\x01",
            "who stole the Orchis Tower's blueprints...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why would a hacker\x01",
            "stole such a thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_455")

    TalkEnd(0xFE)
    Return()

    # Function_4_2BA end

    def Function_5_459(): pass

    label("Function_5_459")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46E")
    Call(0, 6)
    Jump("loc_5DB")

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57C")

    ChrTalk(
        0xFE,
        (
            "Milady Mariabell is a\x01",
            "slavedriver, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "She entrusted us with a responsible part\x01",
            "as system management.\x01",
            "We must get fired up and do our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guys, you're looking\x01",
            "for milady's stolen\x01",
            "dolls, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You too, please\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5DB")

    label("loc_57C")


    ChrTalk(
        0xFE,
        (
            "Guys, you're looking\x01",
            "for milady's stolen\x01",
            "dolls, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You too, please\x01",
            "do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB")

    TalkEnd(0xFE)
    Return()

    # Function_5_459 end

    def Function_6_5DF(): pass

    label("Function_6_5DF")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_67B")
    Jump("loc_6C5")

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_69B")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C5")

    label("loc_69B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BB")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C5")

    label("loc_6BB")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C5")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(
        0x8,
        "Oh, you're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Aren't you the...\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ha ha, long time no see.\x01",
            "Do you remember us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYou are Mr. Clay and Mr. David\x01",
            "of the IBC technology department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLong time no see.\x01",
            "...Somehow you look...busy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. Because the orbal net spread,\x01",
            "the system management too has \x01",
            "become tougher than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, it has to be done very strictly.\x01",
            "Milady has given us detailed instructions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F*giggle*, working under Bell\x01",
            "is as tough as always, but...\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yeah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You too, you're looking for\x01",
            "milady's stolen dolls, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Do you best too.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x1C6, 2)
    Return()

    # Function_6_5DF end

    def Function_7_985(): pass

    label("Function_7_985")

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
            "#12P#00203F"At the skyscraper that towers high, descend\x01",
            "to 21F from the 16F summit and search the\x01",
            "many windows peering into another world"...\x02\x03",
            "#00200FFrom the IBC building top floor, 16F,\x01",
            "if you descend to 21F, that makes B5F.\x01",
            "...So it seems he meant this floor.\x02\x03",
            "#00200FAnd the "many windows peering into\x01",
            "another world" are these terminal\x01",
            "monitors looking at the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FNow that you mention it,\x01",
            "I can't think of any other place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlright. Let's check it out.\x02",
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
            "#6P#00100FThis one is definitely\x01",
            ""Alice", Bell's favorite of\x01",
            "those in her collection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FAnd regarding Phantom Thief B's card... \x01",
            "That was the last one, it doesn't look\x01",
            "like there's one affixed to the trunk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FHu hu, request complete, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106F*sigh*, that sure took awhile...\x02",
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
        "#12P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FW-What is it?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 8)
    BeginChrThread(0x9, 1, 0, 9)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    ChrTalk(
        0x8,
        "#6PGuys, did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PIt looks like there was an alert\x01",
            "that an orbal mail arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PHuh? Is that Miss\x01",
            "Mariabell's doll!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FC6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC6)
    Sleep(50)

    def lambda_FD6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FD6)
    Sleep(50)

    def lambda_FE6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FE6)
    Sleep(50)

    def lambda_FF6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FF6)
    Sleep(50)

    def lambda_1006():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1006)
    Sleep(50)

    def lambda_1016():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1016)
    Sleep(100)

    ChrTalk(
        0x101,
        (
            "#11P#00005FUmm, it was actually\x01",
            "here for awhile...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FHmm... More importantly, I am\x01",
            "worried about getting a mail\x01",
            "with this kind of timing.\x02\x03",
            "#00200FDo you mind if I check it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 500)

    ChrTalk(
        0x8,
        (
            "#6PN-No... It's rather\x01",
            "ominous, so please do.\x02",
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
            "#11P#00203F(*klak klak klak klak*...)\x02\x03",
            "#00205F...Huh...?\x02",
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
            "#11P#00201F..."Phantom Thief B"\x01",
            "is in the sender field...\x02",
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
        "#00105FEeh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Phantom Thief B, you say? Was it really him!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "W-Where the heck did he send it from...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...Tio, can\x01",
            "you open it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#11P#00201F...Roger.\x02",
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
            "From: Phantom Thief B\x01",
            "Subject: None\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To my beloved ladies and gentlemen\x01",
            "of the Special Support Section──\x01",
            "Firstly, I must express\x01",
            "my gratitude to you for\x01",
            "entertaining me thus far.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I apologize to both doll owner\x01",
            "Miss Mariabell and their creator,\x01",
            "Meister Jｶrg, for my terribly\x01",
            "impolite conduct. However, I\x01",
            "took the utmost care so as not\x01",
            "to damage these supreme works\x01",
            "of art, so please do not worry.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Then, I must leave this land before long.\x01",
            "Farewell, ladies and gentlemen of the\x01",
            "Special Support Section!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Ouroboros" Enforcer No. X,\x01",
            ""Gentleman Phantom Thief" Bleublanc ──\x01",
            "I look forward to seeing your\x01",
            "continued growth and I pray\x01",
            "the Goddess grants you luck.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "P.S. This orbal mail will\x01",
            "be automatically deleted,\x01",
            "and saving it is not possible.\x01",
            "               ──Phantom Thief B\x02",
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
        "#6P#00005F...Wha... What...\x02",
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#6P#00011F#4S...What's with this mail!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu, who would have thought he\x01",
            "would come out suddenly like that.\x02\x03",
            "#10304FThe "Phantom Thief", an Enforcer\x01",
            "of "Ouroboros", huh...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19D1")

    ChrTalk(
        0x102,
        (
            "#00106FT-That's the group that\x01",
            "Renne was involved with\x01",
            "before, right...?\x02\x03",
            "#00107FT-That's right! Tio, can\x01",
            "you output that mail?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6D")

    label("loc_19D1")


    ChrTalk(
        0x102,
        (
            "#00106FI-Indeed, if that's how it is,\x01",
            "it could explain Phantom\x01",
            "Thief B's stealing skills too...\x02\x03",
            "#00107FT-That's right! Tio, can\x01",
            "you output that mail?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6D")


    ChrTalk(
        0x101,
        (
            "#6P#00005FR-Right! We might be\x01",
            "able to find some clue...!\x02",
        )
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)

    ChrTalk(
        0x103,
        (
            "#11P#00203F(*klak klak klak klak*...) \x01",
            "I've been trying...but it's no good.\x02\x03",
            "#00200FEver since we opened\x01",
            "the mail, it has been\x01",
            "slowly erasing itself.\x02\x03",
            "#00206FThe other terminals weren't affected,\x01",
            "but recovery will be almost impossible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh man. That guy thought of everything.\x02\x03",
            "#00301FWe don't know anything 'bout\x01",
            "the hacker that trapped us in\x01",
            "the Geofront yesterday, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FRight...\x02\x03",
            "#10101FHacking aside, there can't be\x01",
            "any doubt they possess crazily\x01",
            "advanced technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "W-We don't get it at all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Clay! We've got to\x01",
            "check if there was any\x01",
            "impact on our data!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "R-Right. A virus might've\x01",
            "entered the system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyway, we have to\x01",
            "excuse ourselves.\x02",
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
            "#6P#00003FA-Anyway...\x01",
            "We recovered all the\x01",
            "Rosenberg dolls.\x02\x03",
            "#00000FLet's go return them\x01",
            "to Miss Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)

    def lambda_1E28():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1E28)
    Sleep(50)

    def lambda_1E38():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E38)
    Sleep(50)

    def lambda_1E48():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E48)
    Sleep(50)

    def lambda_1E58():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E58)
    Sleep(100)

    ChrTalk(
        0x102,
        "#00100FYes...let's.\x02",
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

    # Function_7_985 end

    def Function_8_1ECB(): pass

    label("Function_8_1ECB")

    OP_93(0xFE, 0xBE, 0x1F4)
    OP_95(0xFE, -3750, -600, 19550, 2000, 0x0)
    OP_95(0xFE, -3600, -600, 15950, 2000, 0x0)
    OP_95(0xFE, -2560, -600, 14690, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_8_1ECB end

    def Function_9_1F16(): pass

    label("Function_9_1F16")

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

    # Function_9_1F16 end

    def Function_10_1F8C(): pass

    label("Function_10_1F8C")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -3720, -600, 15980, 2000, 0x0)
    OP_95(0xFE, -3470, -600, 20320, 2000, 0x0)
    OP_95(0xFE, -5210, -480, 21950, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_1F8C end

    def Function_11_1FD7(): pass

    label("Function_11_1FD7")

    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 3720, -600, 15950, 2000, 0x0)
    OP_95(0xFE, 3610, -600, 20460, 2000, 0x0)
    OP_95(0xFE, 5110, -480, 21860, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_11_1FD7 end

    SaveToFile()

Try(main)
