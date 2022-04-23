execute store result score @s st_X run data get entity @s Pos[0]
execute store result score @s st_Y run data get entity @s Pos[1]
execute store result score @s st_Z run data get entity @s Pos[2]
execute at @s run tp @p[tag=tent_player] ~ ~ ~
kill @s
