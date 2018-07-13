from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1140.bin",                # FileName
        "m1140",                    # MapName
        "m1140",                    # Location
        0x006E,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 110, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1140",                  # 0
        "Aines the Stout",        # 1
        "Vanguard",               # 2
        "Vanguard",               # 3
        "Vanguard",               # 4
        "Vanguard",               # 5
        "SE制御",                 # 6
        "bm1040",                 # 7
        "bm1040",                 # 8
        "bm1040",                 # 9
        "bm1040",                 # 10
    ))

    ATBonus("ATBonus_3FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_40C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_362C", 8,   8,   21,  13,  0,   0,   0)
    Sepith("Sepith_3634", 6,   6,   0,   0,   13,  13,  13)

    MonsterBattlePostion("MonsterBattlePostion_44C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_508", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_50C", 0x0000, 90, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_362C", 60, 25, 10, 5,
        (
            ("ms65000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms65000.dat", "ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
        )
    )

    BattleInfo(
        "BattleInfo_5D4", 0x0000, 90, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_3634", 60, 25, 10, 5,
        (
            ("ms62700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms62700.dat", "ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_69C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms43200.dat", "ms80000.dat", "ms80000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4CC", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_40C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6E0", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80000.dat", "ms80000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4EC", "MonsterBattlePostion_4AC", "ed7451", "ed7453", "ATBonus_40C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
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
        "monster/ch65050.itc",               # 10
        "monster/ch65050.itc",               # 11
        "monster/ch62750.itc",               # 12
        "monster/ch62750.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(20770,   2670,    4294939296, 0x1010000,    "BattleInfo_50C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(7940,    18540,   4294938106, 0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294966036, 21090,   4294938096, 0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294954776, 16300,   4294938106, 0x1010000,    "BattleInfo_50C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294946086, 4294966746, 4294939296, 0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4300,    4670,    4294940096, 0x1010000,    "BattleInfo_50C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294959716, 4170,    4294940096, 0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(320,     4294960326, 4294940096, 0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 7,   0.0,                   -21.0,                 -29.0,                 784.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.25,                  5.800000190734863,     1.0])
    DeclEvent(0x0000, 0, 16,  0.03999999910593033,   -27.989999771118164,   -28.0,                 784.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0028571428265422583, 6.997499942779541,     5.599999904632568,     1.0])

    DeclActor(489750,  900,     10650,   1500,    489750,  2400,    10650,   0x007C, 0,  2,  0x0000)
    DeclActor(518900,  4294966396, 4294967286, 1500,    518900,  600,     4294967286, 0x007C, 0,  3,  0x0000)
    DeclActor(4294963766, 4294940096, 4294966446, 1800,    4294963766, 4294942096, 4294966446, 0x007C, 0,  5,  0x0000)
    DeclActor(3040,    4294940096, 4294967176, 1800,    3040,    4294942096, 4294967176, 0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_79C",          # 00, 0
        "Function_1_808",          # 01, 1
        "Function_2_93B",          # 02, 2
        "Function_3_AE2",          # 03, 3
        "Function_4_C89",          # 04, 4
        "Function_5_D28",          # 05, 5
        "Function_6_F4A",          # 06, 6
        "Function_7_115E",         # 07, 7
        "Function_8_1EA4",         # 08, 8
        "Function_9_1EC0",         # 09, 9
        "Function_10_1EDB",        # 0A, 10
        "Function_11_1F21",        # 0B, 11
        "Function_12_1F40",        # 0C, 12
        "Function_13_1F66",        # 0D, 13
        "Function_14_1F79",        # 0E, 14
        "Function_15_2897",        # 0F, 15
        "Function_16_28A1",        # 10, 16
        "Function_17_3105",        # 11, 17
    ))


    def Function_0_79C(): pass

    label("Function_0_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_7F1")
    ClearScenarioFlags(0x22, 0)
    SetChrPos(0x0, -930, -27200, -2910, 0)
    SetChrPos(0x1, -930, -27200, -2910, 0)
    SetChrPos(0x2, -930, -27200, -2910, 0)
    SetChrPos(0x3, -930, -27200, -2910, 0)
    Jump("loc_807")

    label("loc_7F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    Event(0, 17)

    label("loc_807")

    Return()

    # Function_0_79C end

    def Function_1_808(): pass

    label("Function_1_808")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_855")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_855")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 0, -29200, 27500, 10000, 3000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 7)), scpexpr(EXPR_END)), "loc_893")
    SetMapObjFrame(0xFF, "Null_books", 0x2, "open_")
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 7)), scpexpr(EXPR_END)), "loc_8B1")
    SetMapObjFrame(0x1, "Null_color00", 0x2, "off_")

    label("loc_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 0)), scpexpr(EXPR_END)), "loc_8CF")
    SetMapObjFrame(0x2, "Null_color00", 0x2, "off_")

    label("loc_8CF")

    Call(0, 4)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_8EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_919")

    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_808 end

    def Function_2_93B(): pass

    label("Function_2_93B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 7)), scpexpr(EXPR_END)), "loc_979")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pedestal is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_AE1")

    label("loc_979")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a glittering light orb.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Take the Light Orb\x01",      # 0
            "Quit\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADA")
    Fade(500)
    SetChrPos(0x0, 492000, 900, 11930, 253)
    SetChrPos(0x1, 491780, 900, 12980, 253)
    SetChrPos(0x2, 493000, 900, 11740, 253)
    SetChrPos(0x3, 493140, 900, 13270, 253)
    OP_68(489540, 2400, 10310, 0)
    MoveCamera(28, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17020, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(173, 0, 100, 0)
    SetMapObjFrame(0x1, "Null_color00", 0x2, "off")
    Sleep(500)
    SetMapObjFrame(0x1, "Null_color00", 0x2, "off_")
    SetScenarioFlags(0x1B7, 7)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_ADA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_AE1")

    Return()

    # Function_2_93B end

    def Function_3_AE2(): pass

    label("Function_3_AE2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 0)), scpexpr(EXPR_END)), "loc_B20")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A pedestal is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_C88")

    label("loc_B20")

    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a glittering light orb.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Take the Light Orb\x01",      # 0
            "Quit\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C81")
    Fade(500)
    SetChrPos(0x0, 516049, -900, -10, 101)
    SetChrPos(0x1, 514760, -900, -1470, 101)
    SetChrPos(0x2, 515049, -900, 970, 101)
    SetChrPos(0x3, 513850, -900, -490, 101)
    OP_68(516740, 600, -1300, 0)
    MoveCamera(56, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17020, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(173, 0, 100, 0)
    SetMapObjFrame(0x2, "Null_color00", 0x2, "off")
    Sleep(500)
    SetMapObjFrame(0x2, "Null_color00", 0x2, "off_")
    SetScenarioFlags(0x1B8, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_C81")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_C88")

    Return()

    # Function_3_AE2 end

    def Function_4_C89(): pass

    label("Function_4_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA7")
    OP_71(0x3, 0xCD, 0xD2, 0x0, 0x20)
    Jump("loc_D27")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_CD1")
    OP_71(0x3, 0x9B, 0xA0, 0x0, 0x20)
    SetMapObjFrame(0x3, "ten_li02", 0x0, 0x1)
    Jump("loc_D27")

    label("loc_CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_CFB")
    OP_71(0x3, 0x37, 0x3C, 0x0, 0x20)
    SetMapObjFrame(0x3, "ten_li01", 0x0, 0x1)
    Jump("loc_D27")

    label("loc_CFB")

    OP_71(0x3, 0x0, 0xA, 0x0, 0x20)
    SetMapObjFrame(0x3, "ten_li01", 0x0, 0x1)
    SetMapObjFrame(0x3, "ten_li02", 0x0, 0x1)

    label("loc_D27")

    Return()

    # Function_4_C89 end

    def Function_5_D28(): pass

    label("Function_5_D28")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_D71")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Light Orb is on the plate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_F49")

    label("loc_D71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F18")
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a scales' plate.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Place the Light Orb\x01",      # 0
            "Quit\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0C")
    Fade(500)
    SetChrPos(0x0, -5190, -27200, 1010, 89)
    SetChrPos(0x1, -5940, -27200, 2040, 89)
    SetChrPos(0x2, -6660, -27200, -170, 89)
    SetChrPos(0x3, -7420, -27200, 630, 89)
    OP_68(-560, -25700, -850, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(22500, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(632, 0, 100, 0)
    SetMapObjFrame(0x3, "ten_li01", 0x1, 0x1)
    Sleep(500)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_EAA")
    Sound(879, 0, 70, 0)
    OP_71(0x3, 0x3C, 0x69, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x69, 0x6E, 0x0, 0x0)
    Jump("loc_ECB")

    label("loc_EAA")

    Sound(879, 0, 70, 0)
    OP_71(0x3, 0x6E, 0x9B, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x9B, 0xA0, 0x0, 0x0)

    label("loc_ECB")

    SetScenarioFlags(0x1B8, 5)
    SubItemNumber(0x33F, 1)
    Sleep(1000)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_F0C")
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23500, 2000)
    OP_0D()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m1150", 0, 0, 0)
    IdleLoop()

    label("loc_F0C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_F49")

    label("loc_F18")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a scales' plate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_F49")

    Return()

    # Function_5_D28 end

    def Function_6_F4A(): pass

    label("Function_6_F4A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_F93")
    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Light Orb is on the plate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_115D")

    label("loc_F93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_112C")
    EventBegin(0x1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a scales' plate.\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Place the Light Orb\x01",      # 0
            "Quit\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1120")
    Fade(500)
    SetChrPos(0x0, 5060, -27200, -1860, 270)
    SetChrPos(0x1, 6460, -27200, -60, 270)
    SetChrPos(0x2, 5990, -27200, -2950, 270)
    SetChrPos(0x3, 7190, -27200, -1530, 270)
    OP_68(260, -25700, 520, 0)
    MoveCamera(41, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(22500, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sound(632, 0, 100, 0)
    SetMapObjFrame(0x3, "ten_li02", 0x1, 0x1)
    Sleep(500)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_10C9")
    Sound(879, 0, 70, 0)
    OP_71(0x3, 0xA0, 0xCD, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0xCD, 0xD2, 0x0, 0x0)
    Jump("loc_10EA")

    label("loc_10C9")

    Sound(879, 0, 70, 0)
    OP_71(0x3, 0xA, 0x37, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x37, 0x3C, 0x0, 0x0)

    label("loc_10EA")

    SetScenarioFlags(0x1B8, 6)
    SubItemNumber(0x33F, 1)
    Sleep(1000)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_1120")
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23500, 2000)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m1150", 0, 0, 0)
    IdleLoop()

    label("loc_1120")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_115D")

    label("loc_112C")

    TalkBegin(0xFF)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a scales' plate.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_115D")

    Return()

    # Function_6_F4A end

    def Function_7_115E(): pass

    label("Function_7_115E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    SetChrFlags(0x15, 0x80)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11D3")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)

    label("loc_11D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11F1")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)

    label("loc_11F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_120F")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch03251.itc", 0x27)

    label("loc_120F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_122D")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch02951.itc", 0x29)

    label("loc_122D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_124B")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch03151.itc", 0x29)

    label("loc_124B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1269")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)

    label("loc_1269")

    LoadChrToIndex("chr/ch43200.itc", 0x2A)
    LoadChrToIndex("chr/ch43250.itc", 0x2B)
    LoadChrToIndex("chr/ch43251.itc", 0x2C)
    LoadChrToIndex("monster/ch80050.itc", 0x2E)
    LoadChrToIndex("monster/ch80051.itc", 0x2F)
    LoadChrToIndex("chr/ch43254.itc", 0x30)
    LoadEffect(0x1, "event/ev10007.eff")
    SoundLoad(825)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, -28000, -22000, 0)
    SetChrPos(0x102, 1030, -28000, -22690, 0)
    SetChrPos(0x103, -500, -28000, -23240, 0)
    SetChrPos(0x104, 450, -28000, -23850, 0)
    SetChrPos(0xF4, -950, -28000, -24340, 0)
    SetChrPos(0xF5, -1390, -28000, -22780, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -27200, -3000, 180)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 8)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3000, -27200, -4000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2E)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 8)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -3000, -27200, -4000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, -27000, -18000, 0)
    MoveCamera(48, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 3000)

    def lambda_141F():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141F)
    Sleep(30)

    def lambda_1437():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1437)
    Sleep(30)

    def lambda_144F():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_144F)
    Sleep(30)

    def lambda_1467():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1467)
    Sleep(30)

    def lambda_147F():
        OP_9B(0x0, 0xF4, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_147F)
    Sleep(30)

    def lambda_1497():
        OP_9B(0x0, 0xF5, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1497)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    NpcTalk(
        0x8,
        "Knight Dressed Girl",
        (
            "#4P──Uh uh.\x01",
            "I have been waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    OP_68(0, -26500, -3500, 3000)
    MoveCamera(30, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15000, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00307F#1PThere she is...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    Fade(500)
    OP_68(0, -25200, -6500, 0)
    OP_68(0, -26100, -6500, 3000)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    BeginChrThread(0xD, 1, 0, 12)

    def lambda_166F():
        OP_9B(0x0, 0x101, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_166F)
    Sleep(50)

    def lambda_1687():
        OP_9B(0x0, 0x102, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1687)
    Sleep(50)

    def lambda_169F():
        OP_9B(0x0, 0x103, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_169F)
    Sleep(50)

    def lambda_16B7():
        OP_9B(0x0, 0x104, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_16B7)
    Sleep(50)

    def lambda_16CF():
        OP_9B(0x0, 0xF4, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_16CF)
    Sleep(50)

    def lambda_16E7():
        OP_9B(0x0, 0xF5, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_16E7)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()

    NpcTalk(
        0x8,
        "Knight Dressed Girl",
        (
            "#5PI am a soldier of the Stahlritter,\x01",
            "Aines the "Stout".\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Knight Dressed Girl",
        (
            "#5PBy orders of my Lord, Arianrhod,\x01",
            "I will be your first opponent.\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    Sound(805, 0, 80, 0)
    Sound(531, 0, 80, 0)
    SetCameraDistance(16800, 500)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()

    NpcTalk(
        0x8,
        "Knight Dressed Girl",
        "#5PCan I ask for your names?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P──Special Support Section,\x01",
            "Lloyd Bannings.\x02\x03",
            "#00013FIt appears there's no room\x01",
            "for discussions, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUh uh, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBack at the Marshlands\x01",
            "I felt you were inexperienced, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAs you're now, you're\x01",
            "acceptable as opponents\x01",
            "for us "Stahlritter".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    SetChrChipByIndex(0x8, 0x30)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_68(0, -26400, -3000, 4000)
    MoveCamera(0, 25, 0, 4000)
    OP_6E(550, 4000)
    SetCameraDistance(18700, 4000)
    OP_82(0x64, 0x64, 0x1770, 0xBB8)
    Sound(825, 2, 50, 0)
    Sleep(400)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    Fade(150)
    Sound(817, 0, 100, 0)
    StopSound(825, 2000, 50)
    BeginChrThread(0xD, 1, 0, 13)
    BeginChrThread(0x9, 3, 0, 10)
    BeginChrThread(0xA, 3, 0, 10)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    Sleep(500)
    Fade(250)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    Sound(805, 0, 80, 0)
    Sound(531, 0, 80, 0)
    SetCameraDistance(16500, 500)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CancelBlur(500)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5PBut, are you qualified to appear\x01",
            "before my Lord, Arianrhod...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PLet me test you with my halberd!!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -26400, -7000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16800, 0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00007F#12PBring it on...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BB8")
    OP_FC(0xC)
    Jump("loc_1BCD")

    label("loc_1BB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BCD")
    OP_FC(0xC)

    label("loc_1BCD")


    ChrTalk(
        0x105,
        (
            "#10407F#13P#NIf you're a "Stahlritter" soldier, then you're\x01",
            "an acceptable opponent for us too...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1C37")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CB3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C61")
    OP_FC(0xC)
    Jump("loc_1C76")

    label("loc_1C61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C76")
    OP_FC(0xC)

    label("loc_1C76")


    ChrTalk(
        0x106,
        (
            "#10701F#13P#NI will fully show you...\x01",
            ""Yin"'s power!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D2A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CDD")
    OP_FC(0xC)
    Jump("loc_1CF2")

    label("loc_1CDD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CF2")
    OP_FC(0x6)

    label("loc_1CF2")


    ChrTalk(
        0x109,
        "#10107F#13P#NCome now, let's have a fair fight!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1D2A")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, -26400, -6000, 500)
    SetCameraDistance(10500, 500)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 11)

    def lambda_1D68():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D68)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 9)

    def lambda_1D90():
        OP_9B(0x1, 0xFE, 0xF, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D90)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x2F)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 0, 0, 9)

    def lambda_1DB8():
        OP_9B(0x1, 0xFE, 0xFFF1, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1DB8)

    def lambda_1DCD():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DCD)

    def lambda_1DE2():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DE2)

    def lambda_1DF7():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DF7)

    def lambda_1E0C():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E0C)

    def lambda_1E21():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1E21)

    def lambda_1E36():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1E36)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xF4, 0x1)
    EndChrThread(0xF5, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_24(0x339)
    Battle("BattleInfo_69C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Call(0, 14)
    Return()

    # Function_7_115E end

    def Function_8_1EA4(): pass

    label("Function_8_1EA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EBF")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_8_1EA4")

    label("loc_1EBF")

    Return()

    # Function_8_1EA4 end

    def Function_9_1EC0(): pass

    label("Function_9_1EC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EDA")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_9_1EC0")

    label("loc_1EDA")

    Return()

    # Function_9_1EC0 end

    def Function_10_1EDB(): pass

    label("Function_10_1EDB")

    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 100, 0, 0, 0, 0, 1650, 1650, 1650, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
    Return()

    # Function_10_1EDB end

    def Function_11_1F21(): pass

    label("Function_11_1F21")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3F")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_11_1F21")

    label("loc_1F3F")

    Return()

    # Function_11_1F21 end

    def Function_12_1F40(): pass

    label("Function_12_1F40")

    Sleep(2200)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F65")
    Sound(540, 0, 50, 0)

    label("loc_1F65")

    Return()

    # Function_12_1F40 end

    def Function_13_1F66(): pass

    label("Function_13_1F66")

    Sleep(900)
    Sound(223, 0, 100, 0)
    Sleep(600)
    Sound(936, 0, 70, 0)
    Return()

    # Function_13_1F66 end

    def Function_14_1F79(): pass

    label("Function_14_1F79")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FB7")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_1FB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FCF")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_1FCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FE7")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_1FE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FFF")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_1FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2017")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_2017")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_202F")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_202F")

    LoadChrToIndex("chr/ch43250.itc", 0x24)
    LoadChrToIndex("chr/ch43253.itc", 0x25)
    LoadChrToIndex("chr/ch43254.itc", 0x26)
    LoadChrToIndex("chr/ch43200.itc", 0x27)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, -27200, -8000, 0)
    SetChrPos(0x102, 1030, -27200, -8690, 0)
    SetChrPos(0x103, -500, -27200, -9240, 0)
    SetChrPos(0x104, 450, -27300, -9850, 0)
    SetChrPos(0xF4, -950, -27470, -10340, 0)
    SetChrPos(0xF5, -1390, -27210, -8780, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -27200, -3000, 180)
    OP_68(0, -26400, -5500, 0)
    OP_68(0, -26400, -4000, 3000)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18700, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#5P──Splendid.\x01",
            "You have endured my halberd well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PAs promised, I will open the path.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(400)
    SetCameraDistance(18200, 800)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(100)
    Sound(805, 0, 70, 0)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x8, 0x26)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Fade(500)
    SetCameraDistance(17800, 0)
    Sound(832, 2, 100, 0)
    Sound(357, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5PHowever, the other two\x01",
            "are veteran masters too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYou will have to face them without self-conceitedness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#12PAh...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16800, 2000)
    BeginChrThread(0xD, 1, 0, 15)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Fade(500)
    SetCameraDistance(18700, 1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(936, 0, 100, 0)
    StopSound(832, 500, 100)

    def lambda_2429():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2429)
    WaitChrThread(0x8, 2)
    CancelBlur(1000)
    OP_6F(0x79)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    Sleep(700)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2470")
    Sound(540, 0, 50, 0)

    label("loc_2470")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_68(0, -26400, -3500, 1500)

    def lambda_24B7():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_24B7)
    Sleep(50)

    def lambda_24CF():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_24CF)
    Sleep(50)

    def lambda_24E7():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_24E7)
    Sleep(50)

    def lambda_24FF():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_24FF)
    Sleep(50)

    def lambda_2517():
        OP_9B(0x0, 0xF4, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2517)
    Sleep(50)

    def lambda_252F():
        OP_9B(0x0, 0xF5, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_252F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#00101F#30W#12P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#12P#N...I lost her presence.\x01",
            "It appears she dislocated and vanished.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12P*sigh*...\x01",
            "She was a terrific girl.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2688")

    ChrTalk(
        0x105,
        (
            "#10406F#12P#NYeah...\x01",
            "I had heard rumors about them, however\x01",
            "I'd never thought they'd be so much skilled.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_26E6")

    label("loc_2688")


    ChrTalk(
        0x106,
        (
            "#10706F#12P#NYes...\x01",
            "I had heard rumors about them,\x01",
            "but to think they're such masters.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_26E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2754")

    ChrTalk(
        0x109,
        (
            "#10101F#12P#NStill, if we use all our might, they\x01",
            "aren't opponents we can't win!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_27A6")

    label("loc_2754")


    ChrTalk(
        0x106,
        (
            "#10701F#12P#NStill, if we use all our might,\x01",
            "it seems we can oppose them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_27A6")

    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00013F#5PYeah...\x01",
            "Let's proceed like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#12P(As I thought, there's something\x01",
            "that's bothering me...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_37()
    SetChrPos(0x0, 400, -27200, -7930, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 7)
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFrame(0xFF, "Null_books", 0x2, "open_")
    SetBarrier(0x2, 0x0, 0x1)
    OP_24(0x340)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_14_1F79 end

    def Function_15_2897(): pass

    label("Function_15_2897")

    Sleep(1100)
    Sound(222, 0, 80, 0)
    Return()

    # Function_15_2897 end

    def Function_16_28A1(): pass

    label("Function_16_28A1")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-170, -26500, -25960, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(21320, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2965")
    SetChrPos(0x101, 120, -28010, -26300, 0)
    SetChrPos(0x102, -1480, -28010, -26550, 0)
    SetChrPos(0x103, 1470, -28010, -26550, 0)
    SetChrPos(0x104, -1480, -28010, -27930, 0)
    SetChrPos(0x109, -120, -28010, -27930, 0)
    SetChrPos(0x105, 1470, -28010, -27930, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_29C4")

    label("loc_2965")

    SetChrPos(0x101, -930, -28010, -26550, 0)
    SetChrPos(0x102, 590, -28010, -26550, 0)
    SetChrPos(0x104, -1480, -28010, -27930, 0)
    SetChrPos(0x109, -120, -28010, -27930, 0)
    SetChrPos(0x105, 1470, -28010, -27930, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_29C4")

    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A26")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_2A26")

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
        "#00005F...Ah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FA-Aren't those...\x02",
    )

    CloseMessageWindow()
    OP_68(-3050, -25900, 21430, 4000)
    MoveCamera(31, 20, 0, 4000)
    OP_6E(590, 4000)
    SetCameraDistance(22500, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B57")
    SetChrPos(0x101, -120, -28010, 10000, 0)
    SetChrPos(0x102, -1480, -28010, 10000, 0)
    SetChrPos(0x103, 1470, -28010, 10000, 0)
    SetChrPos(0x104, -1480, -28010, 8620, 0)
    SetChrPos(0x109, -120, -28010, 8620, 0)
    SetChrPos(0x105, 1470, -28010, 8620, 0)
    Jump("loc_2BAC")

    label("loc_2B57")

    SetChrPos(0x101, -930, -28010, 10000, 0)
    SetChrPos(0x102, 590, -28010, 10000, 0)
    SetChrPos(0x104, -1480, -28010, 8620, 0)
    SetChrPos(0x109, -120, -28010, 8620, 0)
    SetChrPos(0x105, 1470, -28010, 8620, 0)

    label("loc_2BAC")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C6D")

    def lambda_2BC2():
        OP_95(0xFE, 120, -28010, 22100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BC2)
    Sleep(50)

    def lambda_2BDF():
        OP_95(0xFE, -1480, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BDF)
    Sleep(50)

    def lambda_2BFC():
        OP_95(0xFE, 1470, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BFC)
    Sleep(50)

    def lambda_2C19():
        OP_95(0xFE, -1480, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C19)
    Sleep(50)

    def lambda_2C36():
        OP_95(0xFE, -120, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C36)
    Sleep(50)

    def lambda_2C53():
        OP_95(0xFE, 1470, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2C53)
    Jump("loc_2CFB")

    label("loc_2C6D")


    def lambda_2C72():
        OP_95(0xFE, -930, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C72)
    Sleep(50)

    def lambda_2C8F():
        OP_95(0xFE, 590, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C8F)
    Sleep(50)

    def lambda_2CAC():
        OP_95(0xFE, -1480, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CAC)
    Sleep(50)

    def lambda_2CC9():
        OP_95(0xFE, -120, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2CC9)
    Sleep(50)

    def lambda_2CE6():
        OP_95(0xFE, 1470, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CE6)

    label("loc_2CFB")

    Sleep(3000)
    OP_68(-3340, -25900, 19680, 5000)
    MoveCamera(31, 20, 0, 5000)
    OP_6E(590, 5000)
    SetCameraDistance(13470, 5000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    ChrTalk(
        0x105,
        (
            "#10305FAre these the bookshelves?\x02\x03",
            "#10301FThere's nothing on them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FW-Well...\x01",
            "I'm sure that when we looked\x01",
            "earlier there were books here.\x02\x03",
            "#00001FEven according to the report\x01",
            "there's no doubt they were\x01",
            "here until just recently...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EC1")

    ChrTalk(
        0x103,
        (
            "#00203FSomeone took the books away...\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FB-But there's no way the\x01",
            "CGF would not notice...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F32")

    label("loc_2EC1")


    ChrTalk(
        0x109,
        (
            "#10105FSomeone took the books away...\x01",
            "Is that it!?\x02\x03",
            "#10103FB-But there's no way the\x01",
            "CGF would not notice...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F32")


    ChrTalk(
        0x104,
        (
            "#00301FYeah...\x01",
            "Also, for what purpose\x01",
            "the books were taken?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FB9")
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2FB9")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_300B")
    OP_64(0x103)

    label("loc_300B")

    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x101,
        (
            "#00003F...At any rate, we can't do anything\x01",
            "even if we think about it.\x02\x03",
            "#00001FThere were bookshelves on the top floor too.\x01",
            "Let's go there to have a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FYes...let's do like that.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -2680, -29200, 20900, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x71, 0x1, 0x4)
    SetScenarioFlags(0x153, 3)
    ModifyEventFlags(0, 1, 0x80)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_16_28A1 end

    def Function_17_3105(): pass

    label("Function_17_3105")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("monster/ch80050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_312F")
    LoadChrToIndex("chr/ch00050.itc", 0x1F)

    label("loc_312F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3147")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)

    label("loc_3147")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_315F")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)

    label("loc_315F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3177")
    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_3177")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_318F")
    LoadChrToIndex("chr/ch02950.itc", 0x1F)

    label("loc_318F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A7")
    LoadChrToIndex("chr/ch03150.itc", 0x1F)

    label("loc_31A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31BF")
    LoadChrToIndex("chr/ch03250.itc", 0x1F)

    label("loc_31BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31D7")
    LoadChrToIndex("chr/ch00950.itc", 0x1F)

    label("loc_31D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31EF")
    LoadChrToIndex("chr/ch00050.itc", 0x20)

    label("loc_31EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3207")
    LoadChrToIndex("chr/ch00150.itc", 0x20)

    label("loc_3207")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_321F")
    LoadChrToIndex("chr/ch00250.itc", 0x20)

    label("loc_321F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3237")
    LoadChrToIndex("chr/ch00350.itc", 0x20)

    label("loc_3237")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_324F")
    LoadChrToIndex("chr/ch02950.itc", 0x20)

    label("loc_324F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3267")
    LoadChrToIndex("chr/ch03150.itc", 0x20)

    label("loc_3267")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_327F")
    LoadChrToIndex("chr/ch03250.itc", 0x20)

    label("loc_327F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3297")
    LoadChrToIndex("chr/ch00950.itc", 0x20)

    label("loc_3297")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32AF")
    LoadChrToIndex("chr/ch00050.itc", 0x21)

    label("loc_32AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32C7")
    LoadChrToIndex("chr/ch00150.itc", 0x21)

    label("loc_32C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32DF")
    LoadChrToIndex("chr/ch00250.itc", 0x21)

    label("loc_32DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32F7")
    LoadChrToIndex("chr/ch00350.itc", 0x21)

    label("loc_32F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_330F")
    LoadChrToIndex("chr/ch02950.itc", 0x21)

    label("loc_330F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3327")
    LoadChrToIndex("chr/ch03150.itc", 0x21)

    label("loc_3327")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_333F")
    LoadChrToIndex("chr/ch03250.itc", 0x21)

    label("loc_333F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3357")
    LoadChrToIndex("chr/ch00950.itc", 0x21)

    label("loc_3357")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_336F")
    LoadChrToIndex("chr/ch00050.itc", 0x22)

    label("loc_336F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3387")
    LoadChrToIndex("chr/ch00150.itc", 0x22)

    label("loc_3387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_339F")
    LoadChrToIndex("chr/ch00250.itc", 0x22)

    label("loc_339F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33B7")
    LoadChrToIndex("chr/ch00350.itc", 0x22)

    label("loc_33B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33CF")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_33CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33E7")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_33E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33FF")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_33FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3417")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_3417")

    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 499000, 0, -4900, 180)
    BeginChrThread(0xB, 0, 0, 8)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 501000, 0, -4900, 180)
    BeginChrThread(0xC, 0, 0, 8)
    SetChrPos(0x0, 499000, 0, -10500, 0)
    SetChrPos(0x1, 501000, 0, -10500, 0)
    SetChrPos(0x2, 498000, 0, -12500, 0)
    SetChrPos(0x3, 502000, 0, -12500, 0)
    OP_68(499000, 1500, -10280, 0)
    MoveCamera(46, 28, 1, 0)
    OP_6E(500, 0)
    SetCameraDistance(23620, 0)
    OP_68(499000, 1500, -6910, 1500)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3581")
    Sound(540, 0, 50, 0)

    label("loc_3581")

    SetChrChipByIndex(0x0, 0x1F)
    SetChrChipByIndex(0x1, 0x20)
    SetChrChipByIndex(0x2, 0x21)
    SetChrChipByIndex(0x3, 0x22)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    OP_0D()
    Sleep(1000)
    Battle("BattleInfo_6E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrChipByIndex(0x1, 0xFF)
    SetChrChipByIndex(0x2, 0xFF)
    SetChrChipByIndex(0x3, 0xFF)
    Sleep(100)
    SetScenarioFlags(0x1B8, 7)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_17_3105 end

    SaveToFile()

Try(main)
