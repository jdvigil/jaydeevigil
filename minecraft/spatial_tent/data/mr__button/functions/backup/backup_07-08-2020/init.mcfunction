scoreboard objectives add st_X dummy "X"
scoreboard objectives add st_Y dummy "Y"
scoreboard objectives add st_Z dummy "Z"
scoreboard objectives add st_dim dummy "Dimension"

execute in spatial_tent:spatial_tent run setworldspawn 0 6 0

execute in spatial_tent:spatial_tent run fill 0 248 0 4 248 6 bedrock

execute in spatial_tent:spatial_tent run fill 0 0 0 32 22 32 bedrock
execute in spatial_tent:spatial_tent run fill 1 1 1 29 19 29 red_wool
execute in spatial_tent:spatial_tent run fill 2 2 2 28 18 28 air

execute in spatial_tent:spatial_tent run fill 28 4 2 2 18 28 red_wool
execute in spatial_tent:spatial_tent run fill 28 4 3 2 4 27 air
execute in spatial_tent:spatial_tent run fill 28 5 4 2 5 26 air
execute in spatial_tent:spatial_tent run fill 28 6 5 2 6 25 air
execute in spatial_tent:spatial_tent run fill 28 7 6 2 7 24 air
execute in spatial_tent:spatial_tent run fill 28 8 7 2 8 23 air
execute in spatial_tent:spatial_tent run fill 28 9 8 2 9 22 air
execute in spatial_tent:spatial_tent run fill 28 10 9 2 10 21 air
execute in spatial_tent:spatial_tent run fill 28 11 10 2 11 20 air
execute in spatial_tent:spatial_tent run fill 28 12 11 2 12 19 air
execute in spatial_tent:spatial_tent run fill 28 13 12 2 13 18 air
execute in spatial_tent:spatial_tent run fill 28 14 13 2 14 17 air
execute in spatial_tent:spatial_tent run fill 28 15 14 2 15 16 air
execute in spatial_tent:spatial_tent run fill 28 16 15 2 16 15 air

execute in spatial_tent:spatial_tent run fill 15 12 15 15 16 15 iron_bars
execute in spatial_tent:spatial_tent run setblock 15 11 15 lantern
execute in spatial_tent:spatial_tent run setblock 27 15 15 lantern
execute in spatial_tent:spatial_tent run setblock 3 15 15 lantern

execute in spatial_tent:spatial_tent run fill 28 1 2 2 1 28 glowstone
execute in spatial_tent:spatial_tent run fill 28 2 2 2 2 28 brown_carpet

execute in spatial_tent:spatial_tent run setblock 28 2 15 air
execute in spatial_tent:spatial_tent run setblock 28 1 15 brown_wool
execute in spatial_tent:spatial_tent run setblock 29 1 15 brown_wool
execute in spatial_tent:spatial_tent run setblock 28 2 15 minecraft:spruce_trapdoor[facing=west, half=top, open=true]

execute in spatial_tent:spatial_tent run fill 31 1 14 30 3 16 black_concrete
execute in spatial_tent:spatial_tent run fill 32 1 14 32 3 16 red_wool
execute in spatial_tent:spatial_tent run fill 31 2 15 29 2 15 air
execute in spatial_tent:spatial_tent run setblock 32 1 15 brown_wool

execute in spatial_tent:spatial_tent run setblock 32 2 15 minecraft:spruce_trapdoor[facing=west, half=top, open=true]

execute in spatial_tent:spatial_tent run setblock 33 2 15 campfire

execute in spatial_tent:spatial_tent run setblock 31 0 15 jigsaw
