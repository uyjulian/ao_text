from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c020b.bin",                # FileName
        "c020b",                    # MapName
        "c020b",                    # Location
        0x000A,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 3, 0, 4],
    )

    BuildStringList((
        "c020b",                  # 0
        "Ryu",                 # 1
        "Ponce",                 # 2
        "Brick",               # 3
        "car",                     # 4
        "SE control",                 # 5
        "Policeman",                   # 6
        "Central square",               # 7
        "Nishi dori",                 # 8
        "Administrative district",                 # 9
        "Residential area",                 # 10
        "Entertainment district",                 # 11
        "East Street",                 # 12
        "old Town",                 # 13
        "Harbor district",                 # 14
        "IBC",                 # 15
        "Beside the station",               # 16
        "Back street",                 # 17
        "Ursula interchange",           # 18
        "East Crossbell Highway",       # 19
        "West Crossbell Highway",       # 20
        "Mainz Mountain Road",           # 21
        "Orchis Tower",         # 22
    ))

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch30000.itc",                   # 04
    ))

    DeclNpc(4294966296, 0,       610,     90,   257,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(4294952177, 0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   7,   255,  0)
    DeclNpc(6570,    4294967146, 5119,    90,   341,  0x0, 0,   3,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294936837, 0,       7500,    180,  385,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(14500,   4294960796, 4294953796, 1200,    14500,   4294961796, 4294953796, 0x007C, 0,  5,  0x0000)
    DeclActor(33490,   4294963296, 4294950556, 1500,    33490,   4294965296, 4294950556, 0x007C, 0,  10, 0x0000)
    DeclActor(4294932766, 0,       4350,    1500,    4294932766, 1500,    4350,    0x007C, 0,  19, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "Central square")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "Nishi dori")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "Administrative district")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "Residential area")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "Entertainment district")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "East Street")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "old Town")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "IBC")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "Beside the station")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "Back street")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(91.0, 0.0, 213.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ChipFrameInfo(1124, 0)                                       # 0

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_514",          # 01, 1
        "Function_2_575",          # 02, 2
        "Function_3_5D6",          # 03, 3
        "Function_4_5F4",          # 04, 4
        "Function_5_67D",          # 05, 5
        "Function_6_7CE",          # 06, 6
        "Function_7_926",          # 07, 7
        "Function_8_A2B",          # 08, 8
        "Function_9_ABB",          # 09, 9
        "Function_10_C6A",         # 0A, 10
        "Function_11_CB7",         # 0B, 11
        "Function_12_11C4",        # 0C, 12
        "Function_13_1245",        # 0D, 13
        "Function_14_1276",        # 0E, 14
        "Function_15_12A7",        # 0F, 15
        "Function_16_12D8",        # 10, 16
        "Function_17_132E",        # 11, 17
        "Function_18_135F",        # 12, 18
        "Function_19_138D",        # 13, 19
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_49C"),
        (1, "loc_4A8"),
        (2, "loc_4B4"),
        (3, "loc_4C0"),
        (4, "loc_4CC"),
        (5, "loc_4D8"),
        (6, "loc_4E4"),
        (SWITCH_DEFAULT, "loc_4F0"),
    )


    label("loc_49C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4A8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4B4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4C0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4CC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4D8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_4FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_513")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4FC")

    label("loc_513")

    Return()

    # Function_0_464 end

    def Function_1_514(): pass

    label("Function_1_514")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_574")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_514")

    label("loc_574")

    Return()

    # Function_1_514 end

    def Function_2_575(): pass

    label("Function_2_575")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5D5")
    OP_95(0xFE, -10000, 0, 5750, 800, 0x0)
    OP_95(0xFE, -10000, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_575")

    label("loc_5D5")

    Return()

    # Function_2_575 end

    def Function_3_5D6(): pass

    label("Function_3_5D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5E5")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)

    label("loc_5E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5F3")
    ClearChrFlags(0xD, 0x80)

    label("loc_5F3")

    Return()

    # Function_3_5D6 end

    def Function_4_5F4(): pass

    label("Function_4_5F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_607")
    OP_70(0xF, 0x0)
    Jump("loc_60B")

    label("loc_607")

    OP_70(0xF, 0x1E)

    label("loc_60B")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61D")
    Jump("loc_676")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_676")
    ClearChrFlags(0xB, 0x80)
    OP_78(0xE, 0xB)
    SetChrPos(0xB, 34510, -4000, -15670, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xE, 0x2)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_676")

    ClearMapObjFlags(0x7, 0x10)
    Return()

    # Function_4_5F4 end

    def Function_5_67D(): pass

    label("Function_5_67D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77D")
    Sound(14, 0, 100, 0)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＺＷＥＩ２企鹅', 1)"), scpexpr(EXPR_END)), "loc_706")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＺＷＥＩ２企鹅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_778")

    label("loc_706")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＺＷＥＩ２企鹅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＺＷＥＩ２企鹅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_778")

    Jump("loc_7C2")

    label("loc_77D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_67D end

    def Function_6_7CE(): pass

    label("Function_6_7CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C9")

    ChrTalk(
        0xFE,
        (
            "明日は、Orchis Towerで\x01",
            "Two Shawaiigi\x01",
            "There seems to be it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand it somewhat,\x01",
            "Because it's a big deal with Henry\x01",
            "I'm going to see the sights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, surely fun\x01",
            "It's a party or something.\x01",
            "I'm looking forward to tomorrow ~ ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_922")

    label("loc_8C9")


    ChrTalk(
        0xFE,
        (
            "What is Two Shawaiigi?\x01",
            "Perhaps it's a party or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, look forward to tomorrow ~.\x02",
    )

    CloseMessageWindow()

    label("loc_922")

    TalkEnd(0xFE)
    Return()

    # Function_6_7CE end

    def Function_7_926(): pass

    label("Function_7_926")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DD")

    ChrTalk(
        0xFE,
        (
            "Oops ……\x01",
            "Photosensitive quartz\x01",
            "You have run out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the unveiling ceremony in the daytime\x01",
            "It seems like I took too many photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before the oval store closes\x01",
            "I have to go buy a new one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A27")

    label("loc_9DD")


    ChrTalk(
        0xFE,
        (
            "Before the oval store closes\x01",
            "New sensitive quartz\x01",
            "I have to go buy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A27")

    TalkEnd(0xFE)
    Return()

    # Function_7_926 end

    def Function_8_A2B(): pass

    label("Function_8_A2B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "If you read books in a cafe\x01",
            "It has become such a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Buru ……\x01",
            "It will be cold at night as well.\x01",
            "I wonder if I will return home before catching a cold.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_A2B end

    def Function_9_ABB(): pass

    label("Function_9_ABB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_C66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C15")

    ChrTalk(
        0xFE,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "During the trade conference to strengthen security\x01",
            "夜間のcar輌通行を制限しています。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "carで市外に出たい場合は\x01",
            "Please apply for permission on this occasion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00604FSecurity, trouble.\x01",
            "Please give my best regards with that condition.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "This is a Dudley investigator!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Are you on duty?\x01",
            "Thank you very much!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C66")

    label("loc_C15")


    ChrTalk(
        0xFE,
        (
            "今のところ、不審なcar輌は\x01",
            "I do not see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please leave it here.\x02",
    )

    CloseMessageWindow()

    label("loc_C66")

    TalkEnd(0xFE)
    Return()

    # Function_9_ABB end

    def Function_10_C6A(): pass

    label("Function_10_C6A")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FGeoFront is a walkable distance.\x01",
            "carを使う必要はないな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_10_C6A end

    def Function_11_CB7(): pass

    label("Function_11_CB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    SoundLoad(468)
    ClearChrFlags(0xB, 0x80)
    OP_78(0xE, 0xB)
    OP_49()
    SetChrPos(0xB, 40500, 2080, -8000, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    OP_74(0xE, 0x1E)
    OP_71(0xE, 0x79, 0xB4, 0x1, 0x20)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D68")
    EndChrThread(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 12500, 0, -6000, 270)

    def lambda_D58():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D58)

    label("loc_D68")

    FadeToBright(1000, 0)
    BeginChrThread(0xB, 3, 0, 12)
    BeginChrThread(0xC, 1, 0, 18)
    OP_68(15900, 2550, -18000, 0)
    MoveCamera(24, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19500, 0)
    OP_68(19700, -150, -19350, 10000)
    MoveCamera(60, 21, 0, 10000)
    Sleep(8000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xB, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x153, 0x8)
    SetChrPos(0x101, 34500, -4000, -17900, 180)
    SetChrPos(0x102, 34500, -4000, -17900, 180)
    SetChrPos(0x109, 34500, -4000, -17900, 180)
    SetChrPos(0x105, 34500, -4000, -17900, 180)
    SetChrPos(0x153, 34500, -4000, -17900, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xB, 34550, -4000, -15850, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    OP_70(0xE, 0x78)
    OP_68(34650, -3250, -16450, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16650, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(462, 0, 100, 0)
    OP_71(0xE, 0x12D, 0x14A, 0x1, 0x8)
    Sleep(1000)
    Sleep(250)
    OP_68(34650, -3250, -18450, 7000)
    VolumeBGM(0x46, 0x1770)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(1000)
    BeginChrThread(0x153, 3, 0, 17)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 15)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 16)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x153, 3)
    OP_6F(0x79)
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00002F#11PWhew …… Wide city too\x01",
            "carを使えばあっという間か。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FA5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FA5)
    Sleep(100)

    def lambda_FB5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FB5)
    Sleep(100)

    def lambda_FC5():
        TurnDirection(0x153, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 0, lambda_FC5)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x153, 0)

    ChrTalk(
        0x105,
        "#10309F#6PHuh, it's not too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#6PWell, it was fun!\x02\x03",
            "#01110FIt is a distant place.\x01",
            "It looked different!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#6PHuh, it seems so.\x02\x03",
            "#00100FAlright in the city light\x01",
            "I felt like I was swimming.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#11PFrom now on, when you go out\x01",
            "It seems to rely on this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PYeah, durability seems to be high,\x01",
            "I heard that you can go to various places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PWhatching\x01",
            "I must thank my uncle.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(10)
    VolumeBGM(0x64, 0x32)
    Sleep(50)
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_CB7 end

    def Function_12_11C4(): pass

    label("Function_12_11C4")

    SetChrPos(0xFE, 40500, 2080, -8000, 270)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 28850, 300, -8000)
    OP_9F(0x1, 21700, 150, -8000)
    OP_9F(0x1, 19600, 150, -8850)
    OP_9F(0x1, 18650, 150, -11150)
    OP_9F(0x1, 18350, -1850, -19050)
    OP_9F(0x1, 20700, -1850, -20250)
    OP_9F(0x1, 26850, -3850, -20250)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_12_11C4 end

    def Function_13_1245(): pass

    label("Function_13_1245")


    def lambda_124A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_124A)
    OP_95(0xFE, 36480, -4000, -19100, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_1245 end

    def Function_14_1276(): pass

    label("Function_14_1276")


    def lambda_127B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_127B)
    OP_95(0xFE, 33950, -4000, -20400, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_14_1276 end

    def Function_15_12A7(): pass

    label("Function_15_12A7")


    def lambda_12AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12AC)
    OP_95(0xFE, 32850, -4000, -19600, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_15_12A7 end

    def Function_16_12D8(): pass

    label("Function_16_12D8")


    def lambda_12DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12DD)
    OP_95(0xFE, 34450, -4000, -18500, 2000, 0x0)
    Sleep(100)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Sound(461, 0, 100, 0)
    OP_71(0xE, 0x14B, 0x168, 0x0, 0x8)
    Sleep(1000)
    Sleep(200)
    OP_93(0xFE, 0xB4, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_12D8 end

    def Function_17_132E(): pass

    label("Function_17_132E")


    def lambda_1333():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1333)
    OP_95(0xFE, 35050, -4000, -19950, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_132E end

    def Function_18_135F(): pass

    label("Function_18_135F")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 80, 0)
    Sleep(4000)
    Sound(493, 0, 100, 0)
    Sleep(1000)
    Sound(459, 0, 100, 0)
    Sleep(3000)
    Sound(492, 0, 60, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_135F end

    def Function_19_138D(): pass

    label("Function_19_138D")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is tightly closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_19_138D end

    SaveToFile()

Try(main)
