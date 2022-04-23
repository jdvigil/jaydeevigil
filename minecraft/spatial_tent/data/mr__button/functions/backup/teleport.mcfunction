execute store result score @s st_X run data get entity @s Pos[0]
execute store result score @s st_Y run data get entity @s Pos[1]
execute store result score @s st_Z run data get entity @s Pos[2]
execute store result score @s st_dim run data get entity @s Dimension

execute if score st_dim matches 0 run 

summon minecraft:armor_stand ~ ~ ~ {CustomName:"\"Bob\"",Invisible:1}

execute as @a at @s if block ~ ~-2 ~ minecraft:structure_block if entity @s facing entity @e[name=Bob] eyes run teleport @s 30 2 15 facing ~-600 ~ ~

execute if entity @s facing entity @e[name=Bob] eyes if block ~ ~-2 ~ minecraft:structure_block run tp @s st_X st_Y st_Z

execute at @e[name=Bob] run tp @s ~ ~ ~ 180 0
