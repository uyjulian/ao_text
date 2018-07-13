from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r4050.bin",                # FileName
        "r4050",                    # MapName
        "r4050",                    # Location
        0x00A6,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x26,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 12000, 0, 41000, 0, 0, 1, 166, 0, 1, 0, 2],
    )

    BuildStringList((
        "r4050",                  # 0
        "Military Dog",           # 1
        "State Guard Soldier",    # 2
        "State Guard Soldier",    # 3
        "MapThread",              # 4
        "Army Chameleon",         # 5
        "SE制御",                 # 6
        "br4010",                 # 7
        "br4010",                 # 8
        "br4010",                 # 9
        "br4010",                 # 10
        "br4010",                 # 11
        "br4010",                 # 12
    ))

    ATBonus("ATBonus_3D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3E4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_3C4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2388", 6,   0,   2,   15,  8,   4,   0)
    Sepith("Sepith_2390", 4,   10,  4,   6,   0,   9,   0)
    Sepith("Sepith_2398", 6,   3,   12,  3,   0,   0,   11)
    Sepith("Sepith_23A0", 10,  6,   4,   10,  0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_424", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_488", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_48C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_490", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_494", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_498", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_49C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_404", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 0, 0, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 68, 6, 60, 8, 1, 40, 0, "br4010", "Sepith_2388", 40, 30, 20, 10,
        (
            ("ms78400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms78400.dat", "ms78400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms78400.dat", "ms78400.dat", "ms78400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms78400.dat", "ms78400.dat", "ms78400.dat", "ms78400.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
        )
    )

    BattleInfo(
        "BattleInfo_58C", 0x0000, 68, 6, 60, 8, 1, 20, 0, "br4010", "Sepith_2390", 40, 30, 20, 10,
        (
            ("ms82400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82400.dat", "ms82400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82400.dat", "ms82400.dat", "ms82400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82400.dat", "ms82400.dat", "ms82400.dat", "ms82400.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
        )
    )

    BattleInfo(
        "BattleInfo_654", 0x0000, 68, 6, 60, 8, 1, 30, 0, "br4010", "Sepith_2398", 40, 30, 20, 10,
        (
            ("ms82800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82800.dat", "ms82800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
        )
    )

    BattleInfo(
        "BattleInfo_71C", 0x0000, 68, 6, 60, 8, 1, 30, 0, "br4010", "Sepith_23A0", 50, 30, 20, 0,
        (
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", 0, 0, 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", 0, 0, "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            ("ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "ms86700.dat", "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7450", "ed7453", "ATBonus_3D4"),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_7B8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "ms82800.dat", "MonsterBattlePostion_404", "MonsterBattlePostion_484", "ed7451", "ed7453", "ATBonus_3E4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7FC", 0x004A, 3, 6, 45, 3, 3, 30, 0, "br4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41400.dat", "ms80800.dat", "ms41500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4A4", "MonsterBattlePostion_484", "ed7453", "ed7453", "ATBonus_3C4"),
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
        "monster/ch78450.itc",               # 10
        "monster/ch78450.itc",               # 11
        "monster/ch82450.itc",               # 12
        "monster/ch82450.itc",               # 13
        "monster/ch82850.itc",               # 14
        "monster/ch82851.itc",               # 15
        "monster/ch86750.itc",               # 16
        "monster/ch86750.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(54709,   6750,    4294940876, 0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(7790,    10850,   0,       0x101008C,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(8750,    4294939366, 0,       0x101008C,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294964606, 4294959036, 560,     0x1010032,    "BattleInfo_654", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4294948616, 5210,    4000,    0x101005F,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4294952636, 19180,   4000,    0x1010140,    "BattleInfo_71C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(37200,   30540,   4000,    0x101008C,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(44100,   6010,    4294964296, 0x1010140,    "BattleInfo_71C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(32500,   4294944066, 4294962296, 0x1010032,    "BattleInfo_654", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(44700,   4294963206, 4294965546, 0x101008C,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(41250,   4294930116, 4294961296, 0x101008C,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)

    DeclActor(54710,   6250,    4294940876, 1200,    54710,   7250,    4294940876, 0x007C, 0,  3,  0x0000)
    DeclActor(4294947296, 4000,    23000,   1200,    4294947296, 5000,    23000,   0x007C, 0,  4,  0x0000)
    DeclActor(48300,   4294965546, 4294965356, 1200,    48300,   4294966546, 4294965356, 0x007C, 0,  5,  0x0000)
    DeclActor(10050,   0,       48930,   1200,    10050,   1000,    48930,   0x007C, 0,  6,  0x0000)
    DeclActor(44070,   4000,    23010,   1200,    44070,   4500,    23010,   0x007C, 0,  7,  0x0000)
    DeclActor(42740,   4294964296, 20440,   1200,    42740,   4294965296, 20440,   0x007C, 0,  8,  0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1700, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4])                       # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_8F4",          # 00, 0
        "Function_1_910",          # 01, 1
        "Function_2_934",          # 02, 2
        "Function_3_EAE",          # 03, 3
        "Function_4_10CA",         # 04, 4
        "Function_5_121C",         # 05, 5
        "Function_6_136E",         # 06, 6
        "Function_7_140A",         # 07, 7
        "Function_8_14D8",         # 08, 8
        "Function_9_159C",         # 09, 9
        "Function_10_15F3",        # 0A, 10
        "Function_11_1AAF",        # 0B, 11
        "Function_12_1EC1",        # 0C, 12
        "Function_13_1F8D",        # 0D, 13
        "Function_14_1FC7",        # 0E, 14
        "Function_15_1FE3",        # 0F, 15
        "Function_16_1FFF",        # 10, 16
        "Function_17_2038",        # 11, 17
        "Function_18_2062",        # 12, 18
        "Function_19_208C",        # 13, 19
        "Function_20_20A6",        # 14, 20
    ))


    def Function_0_8F4(): pass

    label("Function_0_8F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_90F")
    OP_A1(0xFE, 0x2BC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_8F4")

    label("loc_90F")

    Return()

    # Function_0_8F4 end

    def Function_1_910(): pass

    label("Function_1_910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_924")
    ClearScenarioFlags(0x22, 0)
    Event(0, 10)
    Jump("loc_933")

    label("loc_924")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_933")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)

    label("loc_933")

    Return()

    # Function_1_910 end

    def Function_2_934(): pass

    label("Function_2_934")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF2D100C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x1, 0x0, 28990, 0, 2680, 4000, 2000, 330000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 19220, 10, 8290, 2000, 2000, 300000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x210, 6)), scpexpr(EXPR_END)), "loc_E45")
    SetMapObjFrame(0xFF, "brake00", 0x2, "stop")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    EndChrThread(0xB, 0x0)
    Jump("loc_E5D")

    label("loc_E45")

    BeginChrThread(0xB, 0, 0, 9)
    SetMapObjFrame(0xFF, "brake00", 0x2, "defolt")

    label("loc_E5D")

    OP_1C(0x0, 0x3, 0x0, 0x0, 0x0, 0x0, 0x1086, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7B")
    OP_70(0x0, 0x0)
    Jump("loc_E7F")

    label("loc_E7B")

    OP_70(0x0, 0x1E)

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E92")
    OP_70(0x1, 0x0)
    Jump("loc_E96")

    label("loc_E92")

    OP_70(0x1, 0x1E)

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EA9")
    OP_70(0x2, 0x0)
    Jump("loc_EAD")

    label("loc_EA9")

    OP_70(0x2, 0x1E)

    label("loc_EAD")

    Return()

    # Function_2_934 end

    def Function_3_EAE(): pass

    label("Function_3_EAE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107F")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB1")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F0B():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F0B)

    def lambda_F25():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F25)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Monsters appeared!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_7B8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F92"),
        (2, "loc_FA1"),
        (1, "loc_FAE"),
        (SWITCH_DEFAULT, "loc_FB1"),
    )


    label("loc_F92")

    SetScenarioFlags(0x217, 2)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_FB1")

    label("loc_FA1")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_FAE")

    OP_B9(0x0)
    Return()

    label("loc_FB1")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x6E, 1)"), scpexpr(EXPR_END)), "loc_100A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_107A")

    label("loc_100A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_107A")

    Jump("loc_10BE")

    label("loc_107F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10BE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_EAE end

    def Function_4_10CA(): pass

    label("Function_4_10CA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C6")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_114F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_11C1")

    label("loc_114F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11C1")

    Jump("loc_1210")

    label("loc_11C6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1210")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_10CA end

    def Function_5_121C(): pass

    label("Function_5_121C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1318")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_12A1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E4, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1313")

    label("loc_12A1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1313")

    Jump("loc_1362")

    label("loc_1318")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1362")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_121C end

    def Function_6_136E(): pass

    label("Function_6_136E")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Climb the Rope to the Woodland Road\x01",      # 0
            "Step Away\x01",                                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13DD"),
        (1, "loc_13FD"),
        (SWITCH_DEFAULT, "loc_1409"),
    )


    label("loc_13DD")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    NewScene("r4000", 102, 0, 0)
    IdleLoop()
    Jump("loc_1409")

    label("loc_13FD")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_1409")

    label("loc_1409")

    Return()

    # Function_6_136E end

    def Function_7_140A(): pass

    label("Function_7_140A")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Use the Rope and Go Down\x01",      # 0
            "Step Away\x01",                     # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_146E"),
        (1, "loc_14CB"),
        (SWITCH_DEFAULT, "loc_14D7"),
    )


    label("loc_146E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 42400, -3000, 18950, 180)
    SetChrPos(0x1, 42400, -3000, 18950, 180)
    SetChrPos(0x2, 42400, -3000, 18950, 180)
    SetChrPos(0x3, 42400, -3000, 18950, 180)
    OP_E2(0x2)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_14D7")

    label("loc_14CB")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_14D7")

    label("loc_14D7")

    Return()

    # Function_7_140A end

    def Function_8_14D8(): pass

    label("Function_8_14D8")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Climb the Rope\x01",      # 0
            "Step Away\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1532"),
        (1, "loc_158F"),
        (SWITCH_DEFAULT, "loc_159B"),
    )


    label("loc_1532")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 44640, 4000, 24150, 0)
    SetChrPos(0x1, 44640, 4000, 24150, 0)
    SetChrPos(0x2, 44640, 4000, 24150, 0)
    SetChrPos(0x3, 44640, 4000, 24150, 0)
    OP_E2(0x2)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_159B")

    label("loc_158F")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_159B")

    label("loc_159B")

    Return()

    # Function_8_14D8 end

    def Function_9_159C(): pass

    label("Function_9_159C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x210, 6)), scpexpr(EXPR_END)), "loc_15EA")
    SetMapObjFrame(0xFF, "brake00", 0x2, "anime")
    Sound(156, 0, 100, 0)
    Sleep(1650)
    OP_82(0x0, 0xC8, 0x7D0, 0x190)
    Sleep(400)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    EndChrThread(0xFE, 0x0)

    label("loc_15EA")

    Sleep(1)
    Jump("Function_9_159C")

    label("loc_15F2")

    Return()

    # Function_9_159C end

    def Function_10_15F3(): pass

    label("Function_10_15F3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SetChrPos(0x101, 10300, 0, 43800, 180)
    SetChrPos(0x102, 9700, 0, 45200, 180)
    SetChrPos(0x103, 10950, 0, 46100, 180)
    SetChrPos(0x104, 11100, 0, 44550, 180)
    SetChrPos(0x109, 10450, 0, 47550, 180)
    SetChrPos(0x105, 9550, 0, 46650, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    Sleep(1000)
    OP_11(0x3C, 0x41, 0x69, 0x32, 0x96, 0x0)
    OP_68(31600, 8700, 2100, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(33000, 0)
    FadeToBright(1000, 0)
    OP_68(45650, 8700, -11950, 8000)
    OP_6F(0x79)
    Fade(500)
    OP_68(35900, 4500, -28100, 0)
    MoveCamera(340, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(42950, 0)
    MoveCamera(300, 16, 0, 8000)
    PlaceName2(340, 200, "c_plac55", 0x0, 2000)
    OP_6F(0x79)
    Fade(1000)
    OP_11(0x3C, 0x41, 0x69, 0x1E, 0x78, 0x0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_68(10300, 4200, 44800, 0)
    MoveCamera(315, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19650, 0)
    OP_68(10300, 1200, 44800, 3500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x102,
        "#00107F#11PT-Those are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10110F#11PA-Azure Flowers...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00307F#11PTsk...until two months ago\x01",
            "there was any of them!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5PIt looks like they began\x01",
            "to bloom recently.\x02\x03",
            "#00008FTio, what about the elements presence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#11P...Confirmed Time, Space and Mirage elements.\x02\x03",
            "#00201FThe strange presence I sensed just\x01",
            "before seems like it was theirs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F#11P...It looks like this place difficulty has\x01",
            "increased even more because of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PYeah, to begin with, this is an intricate\x01",
            "place, easy to get lost into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101F#11PLet's proceed with caution so to\x01",
            "not get ambushed by monsters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00013F#5PYeah...!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 12370, 0, 41660, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x163, 7)
    OP_29(0xA8, 0x1, 0xA)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_15F3 end

    def Function_11_1AAF(): pass

    label("Function_11_1AAF")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41450.itc", 0x1E)
    LoadChrToIndex("chr/ch41451.itc", 0x1F)
    LoadChrToIndex("chr/ch41550.itc", 0x20)
    LoadChrToIndex("chr/ch41551.itc", 0x21)
    LoadChrToIndex("monster/ch80850.itc", 0x22)
    LoadChrToIndex("monster/ch80851.itc", 0x23)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 0, 0)
    SetChrFlags(0x9, 0x8)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x8)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x20)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 15)
    SetChrFlags(0x8, 0x8)
    OP_68(11800, 2000, 18000, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    BeginChrThread(0x101, 3, 0, 12)
    FadeToBright(1000, 0)
    OP_68(14300, 1000, -7000, 8000)
    MoveCamera(315, 26, 0, 8000)
    SetCameraDistance(35000, 8000)
    OP_0D()
    Sleep(6500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 13)
    FadeToBright(1000, 0)
    OP_68(22500, -3000, -3550, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(21500, 3000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00015F#11P(Kh...nothing less expected from former CGF.)\x02\x03",
            "#00013F(What will you do...\x01",
            "...Lloyd Bannings...!)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 26000, -4000, -13200, 0)
    Sound(911, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0xD, 1, 0, 19)
    OP_68(22500, -3000, -4550, 1000)
    OP_6F(0x79)
    EndChrThread(0xD, 0x1)
    WaitChrThread(0x8, 3)
    OP_68(22500, -3000, -3550, 750)
    OP_9B(0x1, 0x101, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00010F#11PKh...!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    SetChrPos(0x9, 24850, -4000, 7900, 180)
    SetChrPos(0xA, 26000, -3750, 8900, 180)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x9,
        "#2SThere he is...!\x02",
    )

    CloseMessageWindow()
    OP_68(22500, -3000, -2850, 2000)
    BeginChrThread(0x9, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 18)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xA,
        "#11PSeize him!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)

    def lambda_1E12():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E12)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)

    def lambda_1E2F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1E2F)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 15)
    BeginChrThread(0xD, 1, 0, 19)

    def lambda_1E67():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E67)
    SetCameraDistance(15500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0xD, 0x1)
    Battle("BattleInfo_7FC", 0x0, 0x1, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 20)
    Return()

    # Function_11_1AAF end

    def Function_12_1EC1(): pass

    label("Function_12_1EC1")

    SetChrPos(0xFE, 9970, 0, 25800, 180)
    OP_95(0xFE, 12070, 0, 17430, 6000, 0x1)
    OP_95(0xFE, 13620, 0, 6960, 6000, 0x1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x35A2, 0x5DC, 0xD02, 0x7D0, 0x1388)
    SetChrFlags(0xFE, 0x1)
    OP_95(0xFE, 13240, 1500, -5870, 6000, 0x1)
    SetChrSubChip(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0x3B4C, 0x0, 0xFFFFD896, 0x3E8, 0x1770)
    SetChrFlags(0xFE, 0x1)
    OP_95(0xFE, 20850, 0, -15300, 6000, 0x1)
    OP_95(0xFE, 20470, 0, -20750, 6000, 0x0)
    Return()

    # Function_12_1EC1 end

    def Function_13_1F8D(): pass

    label("Function_13_1F8D")

    SetChrPos(0xFE, 24950, -4000, 8050, 180)
    OP_95(0xFE, 23350, -4000, 3200, 5000, 0x1)
    OP_95(0xFE, 22500, -4000, -3550, 5000, 0x0)
    Return()

    # Function_13_1F8D end

    def Function_14_1FC7(): pass

    label("Function_14_1FC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FE2")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_14_1FC7")

    label("loc_1FE2")

    Return()

    # Function_14_1FC7 end

    def Function_15_1FE3(): pass

    label("Function_15_1FE3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FFE")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_15_1FE3")

    label("loc_1FFE")

    Return()

    # Function_15_1FE3 end

    def Function_16_1FFF(): pass

    label("Function_16_1FFF")

    OP_96(0xFE, 0x5BCC, 0xFFFFF060, 0xFFFFDE9A, 0x1388, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 14)
    Return()

    # Function_16_1FFF end

    def Function_17_2038(): pass

    label("Function_17_2038")

    OP_95(0xFE, 22250, -4000, 3150, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(531, 0, 100, 0)
    Return()

    # Function_17_2038 end

    def Function_18_2062(): pass

    label("Function_18_2062")

    OP_95(0xFE, 23850, -4000, 2900, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sound(805, 0, 100, 0)
    Return()

    # Function_18_2062 end

    def Function_19_208C(): pass

    label("Function_19_208C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20A5")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_19_208C")

    label("loc_20A5")

    Return()

    # Function_19_208C end

    def Function_20_20A6(): pass

    label("Function_20_20A6")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("apl/ch51611.itc", 0x1F)
    SoundLoad(863)
    SoundLoad(861)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 22500, -4000, -3550, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x3)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x9, 24600, -4000, 350, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xA, 21500, -4000, 1050, 45)
    SetChrFlags(0x8, 0x80)
    OP_68(22500, -3000, -3550, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00008F#6P(Damn, in this case I'll aim for\x01",
            "Crossbell City from the freight line...)\x02",
        )
    )

    CloseMessageWindow()
    Sound(355, 0, 80, 0)
    Sound(863, 2, 100, 0)
    Sound(861, 2, 50, 0)
    Sleep(700)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(355, 0, 80, 0)
    OP_68(22460, -3000, -4220, 1500)
    OP_9B(0x1, 0x101, 0xB4, 0x12C, 0x4B0, 0x0)
    Sleep(500)
    OP_9B(0x1, 0x101, 0xB4, 0x1F4, 0x4B0, 0x0)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00015F#6P(In any case, whatever it takes...)\x02\x03",
            "#00010F(...By hook or by crook,\x01",
            "I'll get away from this place...!)\x02",
        )
    )

    CloseMessageWindow()
    Sound(355, 0, 80, 0)
    OP_93(0x101, 0xB4, 0x28A)
    SetCameraDistance(25000, 1500)

    def lambda_22E6():
        OP_9B(0x0, 0xFE, 0x163, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22E6)
    Sleep(500)
    StopSound(863, 3000, 90)
    StopSound(861, 3000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(355, 0, 40, 0)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x101, 0x1)
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("r4090", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_20A6 end

    SaveToFile()

Try(main)
