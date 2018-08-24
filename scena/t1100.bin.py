from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1100.bin",                # FileName
        "t1100",                    # MapName
        "t1100",                    # Location
        0x0046,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1100",                  # 0
        "Jaeger Sachs",           # 1
        "Jaeger",                 # 2
        "Jaeger",                 # 3
        "Jaeger",                 # 4
        "Jaeger",                 # 5
        "Military Dog",           # 6
        "Military Dog",           # 7
        "SE制御",                 # 8
        "bt1010",                 # 9
        "To Hotel Delphinia",     # 10
    ))

    ATBonus("ATBonus_280", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_340", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_324", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_328", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_32C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_330", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_334", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_338", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_360", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42002.dat", "ms41902.dat", "ms41902.dat", "ms86100.dat", "ms86100.dat", 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_320", "ed7540", "ed7453", "ATBonus_280"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51706.itc",                   # 00
        "chr/ch00000.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   0.0,                   1.5,                   -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -0.5,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 18,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "To Hotel Delphinia")

    ChipFrameInfo(1008, 0)                                       # 0

    ScpFunction((
        "Function_0_3F0",          # 00, 0
        "Function_1_411",          # 01, 1
        "Function_2_4C6",          # 02, 2
        "Function_3_17B6",         # 03, 3
        "Function_4_17C9",         # 04, 4
        "Function_5_17DC",         # 05, 5
        "Function_6_17E6",         # 06, 6
        "Function_7_1801",         # 07, 7
        "Function_8_1822",         # 08, 8
        "Function_9_1843",         # 09, 9
        "Function_10_1EF0",        # 0A, 10
        "Function_11_1F0D",        # 0B, 11
        "Function_12_1F2A",        # 0C, 12
        "Function_13_1F42",        # 0D, 13
        "Function_14_1F5A",        # 0E, 14
        "Function_15_1F83",        # 0F, 15
        "Function_16_1F99",        # 10, 16
        "Function_17_25B7",        # 11, 17
        "Function_18_2651",        # 12, 18
    ))


    def Function_0_3F0(): pass

    label("Function_0_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_401")
    Event(0, 2)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_410")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_410")

    Return()

    # Function_0_3F0 end

    def Function_1_411(): pass

    label("Function_1_411")

    SetMapObjFrame(0xFF, "t1100_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_44D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_476")
    Call(0, 17)

    label("loc_476")

    Sound(126, 1, 80, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A3")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Jump("loc_4C5")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_4C5")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)

    label("loc_4C5")

    Return()

    # Function_1_411 end

    def Function_2_4C6(): pass

    label("Function_2_4C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x52, 0xFF, 0xFF)
    LoadChrToIndex("apl/ch51323.itc", 0x1E)
    SetChrPos(0x101, 0, 0, -32000, 0)
    SetChrPos(0x153, 0, 0, -17000, 0)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, -21500, 6000)
    MoveCamera(0, 20, 0, 6000)
    SetCameraDistance(28000, 6000)
    Sleep(3500)

    def lambda_562():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_562)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xFA0)
    BeginChrThread(0xF, 1, 0, 7)

    ChrTalk(
        0x101,
        (
            "#00001F#6P#N(What is she doing\x01",
            "here...?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -16500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()

    ChrTalk(
        0x153,
        "#01108F#40W#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12P#NKeA. So this is where\x01",
            "you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0xB4, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    ChrTalk(
        0x153,
        "#01102F#5PLloyd...\x02",
    )

    CloseMessageWindow()
    OP_68(0, 1000, -17000, 5000)
    SetCameraDistance(21000, 5000)

    def lambda_6AF():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFBD98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AF)

    def lambda_6C9():

        label("loc_6C9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_6C9")

    QueueWorkItem2(0x153, 2, lambda_6C9)
    Sleep(4000)

    def lambda_6DE():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFBD98, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6DE)
    WaitChrThread(0x153, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x153, 0x2)
    OP_6F(0x79)
    Fade(1000)
    OP_68(3790, 500, 33620, 0)
    MoveCamera(26, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80770, 0)
    PlaceName2(340, 40, "c_plac73", 0x0, 3000)
    MoveCamera(37, 23, 0, 8000)
    OP_6F(0x40)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#12P#NHaha, how nostalgic.\x02\x03",
            "#00000F...Do you remember? We\x01",
            "escaped together from\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x153,
        (
            "#01104F#12P#NEhehe... How could I\x01",
            "forget?\x02\x03",
            "#01121FBecause KeA's memories\x01",
            "all started from here,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00002F#12P#N...I do.\x02\x03",
            "#00008F............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x153,
        (
            "#01103F#12P#NSay, Lloyd.\x02\x03",
            "#01101FKeA was here, but... She\x01",
            "was somewhere else for a\x01",
            "long time, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00003F#12P#NYeah...\x02\x03",
            "#00001F...So you are worried\x01",
            "about it. How you were\x01",
            "born, I mean.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x153,
        (
            "#01106F#12P#N...Yeah.\x02\x03",
            "It's been bothering me\x01",
            "more and more lately,\x01",
            "for some reason...\x02\x03",
            "#01108FI heard from you guys\x01",
            "that I was born a long,\x01",
            "long time ago, but...\x02\x03",
            "#01112FRecently, I feel like I\x01",
            "finally understand what\x01",
            "that means...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#12P#NI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -17000, 0)
    MoveCamera(42, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(19000, 50000)
    OP_0D()
    OP_93(0x153, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x153,
        (
            "#01122F#11PEhehe...\x02\x03",
            "#01121FI have Lloyd, I have\x01",
            "Elie... and Tio, Randy and\x01",
            "everyone...\x02\x03",
            "I'm friends with Shizuku,\x01",
            "Ryｹ and the others and\x01",
            "Sister Marble...\x02\x03",
            "#01108FIt's true that every day\x01",
            "is fun, but...\x02\x03",
            "#01106F#30WOnce in a while... Only\x01",
            "once in a very long while,\x01",
            "I feel all alone...\x02\x03",
            "#30W...Like I was abandoned in\x01",
            "that pitch-black cavern...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x190)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00001F#6P─KeA.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(670, 1000, -16940, 1500)
    Sleep(400)

    def lambda_C1C():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C1C)
    OP_93(0x153, 0x10E, 0x190)
    WaitChrThread(0x101, 1)
    Fade(250)
    Sound(898, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x153, 3, 0, 4)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x153,
        (
            "#01123F#40W#11PSorry... I'm really\x01",
            "sorry.\x02\x03",
            "I didn't really want to\x01",
            "say this, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PDummy, don't hold it in.\x02\x03",
            "#00008FAlso... You couldn't say it,\x01",
            "right?\x02\x03",
            "#00001FAll of us are feeling down,\x01",
            "and you didn't want to worry\x01",
            "us any more than necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        "#01114F#40W#11P............(*nods*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#6PNow look here... You've\x01",
            "got it all wrong, KeA.\x02\x03",
            "#00004FJust knowing that you're\x01",
            "relying on us is enough\x01",
            "to cheer us up.\x02\x03",
            "We'll never lose and\x01",
            "wholeheartedly do our\x01",
            "best.\x02\x03",
            "#00002FSo don't hold it in.\x02\x03",
            "#00009FBecause, at the very\x01",
            "least, I'll always be by\x01",
            "your side, KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01102F#30W#11P...Ah...\x02\x03",
            "#30W#01104F............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Fade(250)
    Sound(812, 0, 70, 0)
    BeginChrThread(0x101, 3, 0, 5)
    BeginChrThread(0x153, 3, 0, 6)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x153,
        "#01109F#11PEhehe, thanks.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A1(0x153, 0x4B0, 0x6, 0x7, 0x8, 0x7, 0x6, 0x7, 0x8)
    Sleep(150)

    ChrTalk(
        0x153,
        (
            "#01101F#11PBut, if you say stuff like\x01",
            "that, you'll never get\x01",
            "yourself a wife, you know?\x02\x03",
            "If you have a kid like me\x01",
            "with you, you might never\x01",
            "meet anyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PNow look here... Just\x01",
            "where did you learn that\x01",
            "stuff?\x02\x03",
            "#00011FWait, could it be from\x01",
            "library books you read?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111F#11PHmm. Maybe, but...\x02\x03",
            "#01100FI guess I got it from\x01",
            "people I talked to in\x01",
            "the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYou're studying too\x01",
            "much...\x02\x03",
            "#00000F─Anyway, my marriage is a\x01",
            "ways away.\x02\x03",
            "Even my older brother was\x01",
            "25 when he thought of\x01",
            "getting married, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01105F#11PYour older brother?\x02\x03",
            "#01106F...I see. He passed\x01",
            "away, didn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah. But that's in the past.\x02\x03",
            "#00000FIt'll be 7 years until I'm as old as he\x01",
            "was... and I can't even think of getting\x01",
            "married until I can stand on my own.\x02\x03",
            "#00012FAnd, I don't even have a partner in the\x01",
            "first place.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x153)
    Sleep(100)
    OP_A1(0x153, 0x5DC, 0x4, 0x7, 0x6, 0x7, 0x8)
    Sleep(200)

    ChrTalk(
        0x153,
        (
            "#01105F#11P7 years from now...\x02\x03",
            "How old will KeA be\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PHmm, you're about 9 now,\x01",
            "so...\x02\x03",
            "#00004FAround 16─ Haha, so even\x01",
            "older than Tio is now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01103F#11PHmm...\x02\x03",
            "#01101FCan KeA marry at that\x01",
            "age?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00011F#6P#4SWhaaat!?\x02\x03",
            "#00006FUm, no matter how you\x01",
            "slice it, isn't 16 way too\x01",
            "young to get married!?\x02\x03",
            "#00008FWell, if your guardian\x01",
            "approves, you can get\x01",
            "married at 16, but...\x02\x03",
            "#00007FB-But no! I'll never\x01",
            "approve, you hear!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01111F#11PHmm? I didn't mean it\x01",
            "like that, though.\x02\x03",
            "#01104FEhehe. So that's how it\x01",
            "is.\x02\x03",
            "#01121FIn that case... I don't\x01",
            "have anything to worry\x01",
            "about, do I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, nothing at all.\x02\x03",
            "#00000F─C'mon. It's about time\x01",
            "we headed to the theme\x01",
            "park.\x02\x03",
            "You've been looking\x01",
            "forward to this forever,\x01",
            "haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x153,
        (
            "#01109F#11PEhehe...\x02\x03",
            "#01110FYou know, Shizuku asked me\x01",
            "to tell her what kind of\x01",
            "place the theme park is.\x02\x03",
            "And, she said she'll go\x01",
            "there with me when her\x01",
            "eyes are healed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00002FIn that case, we've got\x01",
            "to have that much more\x01",
            "fun, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x153, 0x5DC, 0x6, 0x9, 0xA, 0xB, 0xA, 0x9, 0x8)
    Sleep(100)

    ChrTalk(
        0x153,
        "#01109F#11PYeah!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x153, 0x2)
    OP_49()
    OP_D7(0x1E)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    BeginChrThread(0xF, 1, 0, 8)
    SetChrPos(0x0, 0, 0, -12000, 180)
    SetScenarioFlags(0x145, 2)
    OP_29(0xA5, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_2_4C6 end

    def Function_3_17B6(): pass

    label("Function_3_17B6")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x10, 0x11, 0x12)
    Return()

    # Function_3_17B6 end

    def Function_4_17C9(): pass

    label("Function_4_17C9")

    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x1E)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_4_17C9 end

    def Function_5_17DC(): pass

    label("Function_5_17DC")

    OP_A1(0xFE, 0x3E8, 0x3, 0x13, 0x14, 0x15)
    Return()

    # Function_5_17DC end

    def Function_6_17E6(): pass

    label("Function_6_17E6")

    SetChrPos(0xFE, 750, 0, -17000, 270)
    OP_A1(0xFE, 0x3E8, 0x3, 0x3, 0x4, 0x5)
    Return()

    # Function_6_17E6 end

    def Function_7_1801(): pass

    label("Function_7_1801")

    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x1E)
    Return()

    # Function_7_1801 end

    def Function_8_1822(): pass

    label("Function_8_1822")

    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x46)
    Sleep(200)
    OP_25(0x7E, 0x50)
    Return()

    # Function_8_1822 end

    def Function_9_1843(): pass

    label("Function_9_1843")

    EventBegin(0x0)
    FadeToDark(300, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00251.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch00351.itc", 0x23)
    LoadChrToIndex("chr/ch02950.itc", 0x24)
    LoadChrToIndex("chr/ch02951.itc", 0x25)
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)
    LoadChrToIndex("chr/ch41950.itc", 0x2A)
    LoadChrToIndex("chr/ch41951.itc", 0x2B)
    LoadChrToIndex("chr/ch41952.itc", 0x2C)
    LoadChrToIndex("chr/ch42050.itc", 0x2D)
    LoadChrToIndex("chr/ch42051.itc", 0x2E)
    LoadChrToIndex("monster/ch86150.itc", 0x2F)
    LoadChrToIndex("monster/ch86151.itc", 0x30)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 5100, 0)
    OP_90(0x103, 500, 0, 3300, 0)
    OP_90(0x104, -700, 0, 5200, 0)
    OP_90(0x105, -500, 0, 3500, 0)
    OP_90(0x106, 1500, 0, 4350, 0)
    OP_90(0x109, -1500, 0, 4050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x24)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x26)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x28)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xD, 0x2F)
    SetChrChipByIndex(0xE, 0x2F)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 0, 0, 10)
    BeginChrThread(0xE, 0, 0, 10)
    SetChrPos(0x8, 0, 0, 20000, 180)
    SetChrPos(0x9, -2000, 0, 19500, 180)
    SetChrPos(0xC, 2000, 0, 19500, 180)
    SetChrPos(0xD, -1300, 0, 23000, 180)
    SetChrPos(0xE, 1300, 0, 23000, 180)
    OP_68(0, 1000, 17000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(18500, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0xF, 1, 0, 15)

    def lambda_1A99():
        OP_9B(0x0, 0x101, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A99)
    Sleep(50)

    def lambda_1AB1():
        OP_9B(0x0, 0x103, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1AB1)
    Sleep(50)

    def lambda_1AC9():
        OP_9B(0x0, 0x104, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1AC9)
    Sleep(50)

    def lambda_1AE1():
        OP_9B(0x0, 0x109, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1AE1)
    Sleep(50)

    def lambda_1AF9():
        OP_9B(0x0, 0x105, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1AF9)
    Sleep(50)

    def lambda_1B11():
        OP_9B(0x0, 0x106, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1B11)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(0, 1000, 16000, 0)
    OP_68(350, 1000, 17640, 1500)
    MoveCamera(41, 16, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PTch, to think they\x01",
            "assaulted us by sheer\x01",
            "strength...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00312F#12PSachs. The fact that\x01",
            "you're here seems to mean\x01",
            "you're the last ones, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P...Yeah, Captain\x01",
            "Randolph.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHowever, as members of Red\x01",
            "Constellation, we can't\x01",
            "let you pass through!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        (
            "#5P#4SGive this everything\x01",
            "you've got, guys!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#5PIf we can't defend this place\x01",
            "to the end, the vice commander\x01",
            "and missus will waste us!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    ChrTalk(
        0x9,
        "#5PJaー!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0x9C4, 0xFA)

    ChrTalk(
        0xC,
        (
            "#5PWe'll crush them with\x01",
            "all our might!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12PBring it on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10707F#12PI'll make you pay for\x01",
            "Arc-en-Ciel!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(11000, 500)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    BeginChrThread(0x8, 3, 0, 13)
    BeginChrThread(0x9, 3, 0, 12)
    BeginChrThread(0xC, 3, 0, 12)
    BeginChrThread(0xD, 3, 0, 14)
    BeginChrThread(0xE, 3, 0, 14)

    def lambda_1E22():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E22)

    def lambda_1E37():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1E37)

    def lambda_1E4C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E4C)

    def lambda_1E61():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E61)

    def lambda_1E76():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E76)

    def lambda_1E8B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1E8B)
    Sleep(200)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x106, 0x1)
    Battle("BattleInfo_360", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 16)
    Return()

    # Function_9_1843 end

    def Function_10_1EF0(): pass

    label("Function_10_1EF0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F0C")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_10_1EF0")

    label("loc_1F0C")

    Return()

    # Function_10_1EF0 end

    def Function_11_1F0D(): pass

    label("Function_11_1F0D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F29")
    OP_A1(0xFE, 0x960, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_11_1F0D")

    label("loc_1F29")

    Return()

    # Function_11_1F0D end

    def Function_12_1F2A(): pass

    label("Function_12_1F2A")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_12_1F2A end

    def Function_13_1F42(): pass

    label("Function_13_1F42")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_13_1F42 end

    def Function_14_1F5A(): pass

    label("Function_14_1F5A")

    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 11)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
    Return()

    # Function_14_1F5A end

    def Function_15_1F83(): pass

    label("Function_15_1F83")

    Sleep(2200)
    Sound(805, 0, 70, 0)
    Sound(531, 0, 70, 0)
    Sound(540, 0, 20, 0)
    Return()

    # Function_15_1F83 end

    def Function_16_1F99(): pass

    label("Function_16_1F99")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch42053.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00356.itc", 0x26)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 600, 0, 16100, 0)
    OP_90(0x103, 500, 0, 14300, 0)
    OP_90(0x104, -700, 0, 16200, 0)
    OP_90(0x105, -500, 0, 14500, 0)
    OP_90(0x106, 1500, 0, 15350, 0)
    OP_90(0x109, -1500, 0, 15050, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x9, -2500, 0, 21000, 0)
    SetChrPos(0xC, 2000, 0, 22500, 45)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x3)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 200, 0, 19100, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    VolumeBGM(0x32, 0x7D0)
    OP_68(-360, 1000, 18310, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15250, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14250, 2000)
    OP_6F(0x79)
    OP_0D()

    def lambda_215A():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_215A)
    WaitChrThread(0x8, 2)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5P#40W...Tch... Captain\x01",
            "Randolph...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#40WYou're... far stronger\x01",
            "than when you were in\x01",
            "the corps...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, my workplace has\x01",
            "trained me in many ways.\x02\x03",
            "#00300FIt's the experience\x01",
            "that's different, the\x01",
            "experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#40WHah... Greater experience\x01",
            "than we who experience\x01",
            "battlefields every day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#40WWhat kind of workplace\x01",
            "is that...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_22F0():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_22F0)
    WaitChrThread(0x8, 2)
    Sleep(500)
    Fade(500)
    Sound(514, 0, 100, 0)
    OP_68(-230, 1000, 18600, 500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -500, 0, 18250, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        "#60W#5P#2S... Watch... out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#60W#5P#2SInside there.. ...Those\x01",
            "guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#60W#5P#2S............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#12P...Did he faint?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PYeah... He's out cold.\x02\x03",
            "#00311FThose guys'... What the\x01",
            "heck did he mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#12PA trap probably. A\x01",
            "different "enemy",\x01",
            "perhaps...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#12PHmm. I don't know but we\x01",
            "should be on guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#12P...If we need treatment,\x01",
            "we should do it now\x01",
            "while we can.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x7D0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    Call(0, 17)
    SetChrPos(0x0, 0, 0, 11900, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_1F99 end

    def Function_17_25B7(): pass

    label("Function_17_25B7")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 1100, 0, 15000, 0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, -2500, 0, 18000, 0)
    SetChrChipByIndex(0xC, 0x0)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0xC, 2000, 0, 19500, 45)
    Return()

    # Function_17_25B7 end

    def Function_18_2651(): pass

    label("Function_18_2651")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe guest house is this way.\x02\x03",
            "We don't have any particular\x01",
            "business there until\x01",
            "tonight's dinner party.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    OP_68(0, 700, -1700, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37000, 0)
    EventEnd(0x4)
    Return()

    # Function_18_2651 end

    SaveToFile()

Try(main)
