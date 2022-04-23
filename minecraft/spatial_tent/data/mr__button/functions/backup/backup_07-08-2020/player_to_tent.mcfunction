tag @s add tent_player

execute unless entity @e[tag=tent_pos] run summon minecraft:armor_stand ~ ~ ~ {Tags:["tent_pos"],Invisible:1b,Marker:1b}

execute as @e[tag=tent_pos,limit=1] run function copy_coords
execute at @s if score @s st_dim matches 0 in minecraft:overworld run tp @s ~0.5 ~ ~0.5
execute at @s if score @s st_dim matches 1 in minecraft:the_end run tp @s ~0.5 ~ ~0.5
execute at @s if score @s st_dim matches -1 in minecraft:the_nether run tp @s ~0.5 ~ ~0.5
tag @s remove tent_player

execute in spatial_tent:spatial_tent run tp @s 30 2 15 facing ~-600 ~ ~


